"""Test package mechanics with temporary synthetic assets, not brand image QA."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('local_skill_packager', ROOT / 'tools/package_skill.py')
pack = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pack)


class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / 'pea-newsletter-infographic'
        for name in pack.REQUIRED:
            p = self.skill / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(b'synthetic fixture, not a brand asset')
        (self.skill / 'SKILL.md').write_text('---\nname: pea-newsletter-infographic\ndescription: Packaging test fixture\n---\n# Test\n')
        self.output = self.root / 'dist/skill.zip'

    def test_archive_contains_complete_required_paths_and_original_bytes(self):
        pack.package_skill(self.skill, self.output)
        with zipfile.ZipFile(self.output) as z:
            self.assertIsNone(z.testzip())
            self.assertEqual(len(z.namelist()), len(pack.REQUIRED))
            for relative in pack.REQUIRED:
                self.assertEqual(z.read('pea-newsletter-infographic/' + relative), (self.skill / relative).read_bytes())

    def test_missing_current_logo_stops_instead_of_substituting(self):
        (self.skill / 'assets/pea-logo-exact-original.png').unlink()
        with self.assertRaisesRegex(ValueError, 'Missing required files'):
            pack.package_skill(self.skill, self.output)
        self.assertFalse(self.output.exists())

    def test_font_files_are_rejected(self):
        for suffix in ('.ttf', '.otf', '.woff', '.woff2'):
            with self.subTest(suffix=suffix):
                p = self.skill / ('assets/forbidden' + suffix)
                p.write_bytes(b'not a font')
                with self.assertRaisesRegex(ValueError, 'Font files'):
                    pack.package_skill(self.skill, self.output)
                p.unlink()

    def test_symlink_is_rejected(self):
        outside = self.root / 'outside.md'
        outside.write_text('not for distribution')
        (self.skill / 'assets/linked.md').symlink_to(outside)
        with self.assertRaisesRegex(ValueError, 'Symbolic link'):
            pack.package_skill(self.skill, self.output)

    def test_output_cannot_be_inside_skill_or_have_wrong_name(self):
        with self.assertRaisesRegex(ValueError, 'outside'):
            pack.package_skill(self.skill, self.skill / 'skill.zip')
        with self.assertRaisesRegex(ValueError, 'filename'):
            pack.package_skill(self.skill, self.root / 'other.zip')

    def test_existing_archive_needs_explicit_overwrite(self):
        pack.package_skill(self.skill, self.output)
        with self.assertRaises(FileExistsError):
            pack.package_skill(self.skill, self.output)
        pack.package_skill(self.skill, self.output, overwrite=True)

    def test_wrong_frontmatter_folder_name_is_rejected(self):
        (self.skill / 'SKILL.md').write_text('---\nname: other\ndescription: fixture\n---\n')
        with self.assertRaisesRegex(ValueError, 'name must match'):
            pack.package_skill(self.skill, self.output)


if __name__ == '__main__':
    unittest.main()
