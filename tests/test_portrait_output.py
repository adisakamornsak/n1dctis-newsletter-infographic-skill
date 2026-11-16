"""Executable geometry checks with synthetic fixtures, not real newsletter QA."""
from contextlib import redirect_stdout
import hashlib
import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'pea-newsletter-infographic'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validator = load('portrait_validator', SKILL / 'scripts/validate_output.py')
logo = load('portrait_logo', SKILL / 'scripts/lock_logo.py')


class PortraitOutputTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def jpeg(self, size=(1440, 2560), name='output.jpg'):
        path = self.root / name
        Image.new('RGB', size, 'white').save(path)
        return path

    def test_exact_portrait_passes_without_modifying_bytes(self):
        path = self.jpeg()
        before = hashlib.sha256(path.read_bytes()).hexdigest()
        self.assertEqual(validator.validate_output(path), (1440, 2560))
        self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), before)

    def test_png_disguised_as_jpeg_is_rejected(self):
        path = self.root / 'fake.jpg'
        Image.new('RGB', validator.TARGET).save(path, format='PNG')
        with self.assertRaisesRegex(ValueError, 'expected JPEG'):
            validator.validate_output(path)

    def test_truncated_jpeg_is_rejected(self):
        path = self.jpeg()
        path.write_bytes(path.read_bytes()[:2000])
        with self.assertRaises(ValueError):
            validator.validate_output(path)

    def test_non_rgb_jpeg_is_rejected(self):
        for mode in ('L', 'CMYK'):
            path = self.root / f'{mode}.jpg'
            Image.new(mode, validator.TARGET).save(path)
            with self.subTest(mode=mode), self.assertRaisesRegex(ValueError, 'expected RGB'):
                validator.validate_output(path)

    def test_jpeg_extension_and_upright_exif_pass(self):
        path = self.root / 'output.JPEG'
        exif = Image.Exif(); exif[274] = 1
        Image.new('RGB', validator.TARGET).save(path, exif=exif)
        self.assertEqual(validator.validate_output(path), validator.TARGET)

    def test_landscape_is_rejected(self):
        with self.assertRaises(ValueError):
            validator.validate_output(self.jpeg((2560, 1440)))

    def test_legacy_baseline_is_rejected(self):
        with self.assertRaises(ValueError):
            validator.validate_output(self.jpeg((1086, 1536)))

    def test_same_aspect_ratio_wrong_resolution_is_rejected(self):
        with self.assertRaises(ValueError):
            validator.validate_output(self.jpeg((720, 1280)))

    def test_oversized_canvas_is_rejected(self):
        with self.assertRaises(ValueError):
            validator.validate_output(self.jpeg((1440, 3000)))

    def test_jpeg_with_png_extension_is_rejected(self):
        path = self.root / 'fake.png'
        Image.new('RGB', validator.TARGET).save(path, format='JPEG')
        with self.assertRaises(ValueError):
            validator.validate_output(path)

    def test_multiple_frames_are_rejected(self):
        path = self.root / 'animated.jpg'
        first = Image.new('RGB', validator.TARGET, 'white')
        second = Image.new('RGB', validator.TARGET, 'black')
        first.save(path, format='PNG', save_all=True, append_images=[second], duration=100, loop=0)
        with self.assertRaises(ValueError):
            validator.validate_output(path)

    def test_exif_orientation_transform_is_rejected(self):
        path = self.root / 'rotation.jpg'
        exif = Image.Exif()
        exif[274] = 6
        Image.new('RGB', validator.TARGET).save(path, exif=exif)
        with self.assertRaises(ValueError):
            validator.validate_output(path)

    def test_corrupt_and_missing_files_are_rejected(self):
        path = self.root / 'corrupt.jpg'
        path.write_bytes(b'not an image')
        for candidate in (path, self.root / 'missing.jpg'):
            with self.subTest(path=candidate), self.assertRaises(ValueError):
                validator.validate_output(candidate)

    def test_logo_helper_preserves_synthetic_color_with_jpeg_tolerance(self):
        source = self.jpeg()
        logo_path = self.root / 'synthetic-logo.png'
        Image.new('RGB', (90, 40), (31, 22, 50)).save(logo_path)
        destination = self.root / 'composited.jpg'
        with redirect_stdout(io.StringIO()):
            logo.apply_logo(source, destination, logo_path)
        self.assertEqual(validator.validate_output(destination), (1440, 2560))
        with Image.open(destination) as output, Image.open(logo_path) as original:
            x, y = logo.DEFAULT_POS
            actual = output.getpixel((x+45, y+20))
            self.assertTrue(all(abs(a-b) <= 3 for a,b in zip(actual, original.getpixel((45,20)))))

    def test_logo_helper_rejects_landscape(self):
        logo_path = self.root / 'synthetic-logo.png'
        Image.new('RGB', (90, 40)).save(logo_path)
        with self.assertRaises(ValueError):
            logo.apply_logo(self.jpeg((2560,1440)), self.root / 'out.jpg', logo_path)

    def test_cli_exit_status(self):
        script = SKILL / 'scripts/validate_output.py'
        for path, expected in ((self.jpeg(), 0), (self.jpeg((100,100),'wrong.jpg'),1)):
            result = subprocess.run([sys.executable, str(script), str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, expected, result.stdout + result.stderr)


class PortraitPolicyTests(unittest.TestCase):
    def test_current_contracts_have_fixed_geometry(self):
        files = ['SKILL.md','references/content-contract.md','references/layout-catalog.md',
                 'references/quality-checklist.md','references/single-image-layout.md']
        obsolete = ['increase canvas dimensions','expand the single canvas when needed',
                    'enlarge the same canvas','reflow/enlarge the same canvas',
                    '1086x1536 px is only a baseline']
        for name in files:
            text=(SKILL/name).read_text(encoding='utf-8')
            with self.subTest(file=name):
                self.assertIn('1440x2560', text)
                for phrase in obsolete:
                    self.assertNotIn(phrase, text)

    def test_helpers_agree_on_width_height(self):
        self.assertEqual(logo.TARGET, (1440,2560))
        self.assertEqual(validator.TARGET, (1440,2560))

    def test_prompt_is_synced_and_explicit(self):
        text=(ROOT/'prompts/newsletter-prompt.th.md').read_text(encoding='utf-8')
        self.assertEqual(text,(SKILL/'assets/newsletter-prompt.th.md').read_text(encoding='utf-8'))
        self.assertIn('1440x2560', text)
        self.assertIn('JPG/JPEG', text)
        import re
        version = re.search(r'team edition (v[0-9.]+)', (SKILL/'SKILL.md').read_text()).group(1)
        self.assertIn(version, text)


if __name__ == '__main__':
    unittest.main()
