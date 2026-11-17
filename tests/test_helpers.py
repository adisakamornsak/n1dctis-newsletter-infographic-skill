"""Copy and logo helper regression tests; not a newsletter renderer test."""
from contextlib import redirect_stdout
import importlib.util
import io
from pathlib import Path
import tempfile
import subprocess
import sys
import unittest

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'pea-newsletter-infographic'


def load_module(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, SKILL / relative)
    if spec is None or spec.loader is None:
        raise RuntimeError('Cannot load helper: ' + relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


copy = load_module('audit_copy', 'scripts/audit_copy.py')
logo = load_module('lock_logo', 'scripts/lock_logo.py')


class CopyTests(unittest.TestCase):
    def final(self, body: str) -> str:
        return '\n'.join(copy.REQUIRED) + '\n' + body

    def test_exact_fixed_copy_and_numbers_pass(self):
        source = '26 - 30 / 2569 / 5G / 99.9%'
        self.assertEqual(copy.audit(source, self.final(source)), [])

    def test_custom_department_replaces_default_requirement(self):
        department = 'แผนกบริการลูกค้า'
        final = self.final('2569').replace(copy.DEFAULT_SUB_HEADER, department)
        self.assertEqual(copy.audit('2569', final, sub_header=department), [])
        self.assertTrue(copy.audit('2569', final))
        self.assertTrue(copy.audit('2569', self.final('2569'), sub_header=department))
        self.assertTrue(copy.audit('2569', final + department, sub_header=department))
        self.assertTrue(copy.audit('2570', final, sub_header=department))

    def test_blank_department_keeps_default_and_custom_value_is_trimmed(self):
        for value in (None, '', '  \t\n'):
            with self.subTest(value=value):
                self.assertEqual(copy.audit('', self.final(''), sub_header=value), [])
        department = 'แผนกบริการลูกค้า'
        final = self.final('').replace(copy.DEFAULT_SUB_HEADER, department)
        self.assertEqual(copy.audit('', final, sub_header='  ' + department + '  '), [])
        self.assertEqual(copy.REQUIRED[1], copy.DEFAULT_SUB_HEADER)

    def test_cli_custom_department_and_blank_default(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source, final = root/'source.txt', root/'final.txt'
            source.write_text('2569', encoding='utf-8')
            command = [sys.executable, str(SKILL/'scripts/audit_copy.py'),
                       '--source', str(source), '--final', str(final)]
            department = 'แผนกบริการลูกค้า'
            final.write_text(self.final('2569').replace(copy.DEFAULT_SUB_HEADER, department), encoding='utf-8')
            self.assertEqual(subprocess.run(command + ['--sub-header', department], capture_output=True).returncode, 0)
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 1)
            final.write_text(self.final('2569'), encoding='utf-8')
            self.assertEqual(subprocess.run(command + ['--sub-header', '  '], capture_output=True).returncode, 0)
            self.assertEqual(subprocess.run(command + ['--sub-header', department], capture_output=True).returncode, 1)

    def test_changed_number_is_reported(self):
        self.assertTrue(copy.audit('2569', self.final('2570')))

    def test_duplicate_fixed_text_is_reported(self):
        self.assertTrue(copy.audit('', self.final(copy.REQUIRED[0])))

    def test_thai_digits_are_not_interchangeable_with_arabic(self):
        source = '\u0e52\u0e55\u0e56\u0e59'
        self.assertTrue(copy.audit(source, self.final('2569')))

    def test_known_limitation_extra_numbers_are_not_checked(self):
        # Documents a real limitation; PASS is NOT proof that new numbers are safe.
        self.assertEqual(copy.audit('2569', self.final('2569 99999')), [])

    def test_cli_reports_missing_input_and_duplicate_copy(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source, final = root/'source.txt', root/'final.txt'
            command = [sys.executable, str(SKILL/'scripts/audit_copy.py'),
                       '--source', str(source), '--final', str(final)]
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 1)
            source.write_text('2569'); final.write_text(self.final('2569'))
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 0)
            final.write_text(self.final('2569') + copy.REQUIRED[0])
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 1)

    def test_missing_required_copy_is_reported(self):
        self.assertTrue(copy.audit('2569', '2569'))


class LogoTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.tmp = Path(self.temp.name)
        self.logo_path = SKILL / 'assets/pea-logo-exact-original.png'

    def test_original_logo_source_preserved_and_jpeg_exported(self):
        # The source is immutable; JPEG output cannot preserve exact pixels.
        src, dst = self.tmp / 'input.png', self.tmp / 'output.jpg'
        Image.new('RGB', logo.TARGET, 'white').save(src)
        original = self.logo_path.read_bytes()
        logo.apply_logo(src, dst, self.logo_path, scale=0.12)
        self.assertEqual(self.logo_path.read_bytes(), original)
        with Image.open(dst) as out:
            self.assertEqual((out.format, out.mode, out.size), ('JPEG', 'RGB', logo.TARGET))
            x, y = logo.DEFAULT_POS
            self.assertLess(min(out.crop((x, y, x+306, y+219)).convert('L').getextrema()), 100)

    def test_wrong_canvas_rejected(self):
        src = self.tmp / 'wrong-size.png'
        Image.new('RGB', (100, 100), 'white').save(src)
        with self.assertRaises(ValueError):
            logo.apply_logo(src, self.tmp / 'out.jpg', self.logo_path)

    def test_out_of_bounds_rejected(self):
        src = self.tmp / 'input.png'
        Image.new('RGB', logo.TARGET, 'white').save(src)
        with self.assertRaises(ValueError):
            logo.apply_logo(src, self.tmp / 'out.jpg', self.logo_path, (-1, 0))

    def test_source_overwrite_is_rejected_without_changing_bytes(self):
        src = self.tmp / 'source.jpg'
        Image.new('RGB', logo.TARGET, 'white').save(src)
        before = src.read_bytes()
        with self.assertRaisesRegex(ValueError, 'overwrite'):
            logo.apply_logo(src, src, self.logo_path, scale=0.12)
        self.assertEqual(src.read_bytes(), before)

    def test_non_jpeg_destination_is_rejected(self):
        src = self.tmp / 'input.png'
        Image.new('RGB', logo.TARGET, 'white').save(src)
        destination = self.tmp / 'output.png'
        with self.assertRaisesRegex(ValueError, 'filename'):
            logo.apply_logo(src, destination, self.logo_path, scale=0.12)
        self.assertFalse(destination.exists())


if __name__ == '__main__':
    unittest.main()
