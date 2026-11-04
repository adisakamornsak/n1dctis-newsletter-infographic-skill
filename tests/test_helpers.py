"""Smoke tests for the unchanged v2.1 helpers; not a newsletter renderer test."""
from contextlib import redirect_stdout
import importlib.util
import io
from pathlib import Path
import tempfile
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


class LogoTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.tmp = Path(self.temp.name)
        self.logo_path = SKILL / 'assets/pea-logo-exact-original.png'

    def test_original_logo_pixels_preserved(self):
        src, dst = self.tmp / 'input.png', self.tmp / 'output.png'
        Image.new('RGB', logo.CANVAS, 'white').save(src)
        with redirect_stdout(io.StringIO()):
            logo.apply_logo(src, dst, self.logo_path)
        with Image.open(self.logo_path) as original_image:
            original = original_image.convert('RGB')
        x, y = logo.DEFAULT_POS
        with Image.open(dst) as out:
            actual = out.convert('RGB').crop((x, y, x + original.width, y + original.height))
        self.assertEqual(actual.tobytes(), original.tobytes())

    def test_wrong_canvas_rejected(self):
        src = self.tmp / 'wrong-size.png'
        Image.new('RGB', (100, 100), 'white').save(src)
        with self.assertRaises(ValueError):
            logo.apply_logo(src, self.tmp / 'out.png', self.logo_path)

    def test_out_of_bounds_rejected(self):
        src = self.tmp / 'input.png'
        Image.new('RGB', logo.CANVAS, 'white').save(src)
        with self.assertRaises(ValueError):
            logo.apply_logo(src, self.tmp / 'out.png', self.logo_path, (-1, 0))


if __name__ == '__main__':
    unittest.main()
