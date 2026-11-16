"""Exercise proportional logo placement through the supported CLI."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from PIL import Image

SCRIPT = Path(__file__).resolve().parents[1] / 'pea-newsletter-infographic/scripts/lock_logo.py'

class LogoScalingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        Image.new('RGB', (1440, 2560), 'white').save(self.root / 'input.png')
        Image.new('RGBA', (240, 120), (120, 0, 90, 255)).save(self.root / 'logo.png')
        self.original = (self.root / 'logo.png').read_bytes()

    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), str(self.root / 'input.png'), str(self.root / 'output.jpg'), '--logo', str(self.root / 'logo.png'), *args], capture_output=True, text=True)

    def test_scaled_and_default_sizes(self):
        for args, size in [((), (240, 120)), (('--scale', '0.5'), (120, 60))]:
            with self.subTest(args=args):
                result = self.run_cli(*args)
                self.assertEqual(result.returncode, 0, result.stderr)
                with Image.open(self.root / 'output.jpg') as im:
                    self.assertEqual(im.format, 'JPEG')
                    self.assertEqual(im.size, (1440, 2560))
                    # Locate the colored region; tolerate JPEG edge ringing.
                    mask = im.convert('L').point(lambda v: 255 if v < 180 else 0)
                    self.assertEqual(mask.getbbox(), (60, 60, 60 + size[0], 60 + size[1]))
                self.assertEqual((self.root / 'logo.png').read_bytes(), self.original)

    def test_invalid_scales_produce_no_output(self):
        for scale in ['0', '-1', '1.1', 'nan', 'inf', '0.00001']:
            with self.subTest(scale=scale):
                self.assertNotEqual(self.run_cli('--scale', scale).returncode, 0)
                self.assertFalse((self.root / 'output.jpg').exists())

    def test_clipping_is_rejected(self):
        for args in [('--x', '-1'), ('--x', '1400'), ('--y', '2550')]:
            with self.subTest(args=args):
                self.assertNotEqual(self.run_cli(*args).returncode, 0)
                self.assertFalse((self.root / 'output.jpg').exists())

if __name__ == '__main__':
    unittest.main()
