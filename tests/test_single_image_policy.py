"""Current JPEG/layout instruction checks; rendered-image QA remains separate."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'pea-newsletter-infographic'


class SingleImagePolicyTests(unittest.TestCase):
    def test_all_active_contracts_specify_fixed_jpeg_geometry(self):
        for name in ('SKILL.md', 'references/single-image-layout.md',
                     'references/content-contract.md', 'references/layout-catalog.md',
                     'references/quality-checklist.md', 'assets/newsletter-prompt.th.md'):
            text = (SKILL / name).read_text()
            with self.subTest(file=name):
                self.assertIn('1440x2560', text)
                self.assertIn('JPG/JPEG', text)
                self.assertNotIn('Exactly one final static PNG', text)
                self.assertNotIn('expand the single canvas when needed', text)

    def test_all_images_and_capacity_conflict_are_explicit(self):
        text = (SKILL / 'SKILL.md').read_text()
        self.assertIn('any number of supplied news images, including zero', text)
        self.assertIn('Map every required news image to a visible placement', text)
        self.assertIn('Do not paginate, split into multiple images, animate, or rotate', text)
        self.assertIn('Do not resize the canvas, split pages, omit required images, or claim completion', text)
        self.assertIn('supporting assets, not as report images', text)

    def test_focal_cropping_and_logo_scaling_rules_are_distinct(self):
        text = (SKILL / 'SKILL.md').read_text()
        self.assertIn('scale, crop, zoom, and reposition supplied news images', text)
        self.assertIn('Preserve essential people, objects, text, and context', text)
        self.assertIn('apply one uniform scale factor to both width and height', text)
        self.assertIn('The crop-to-fill permission for news images does not apply to the logo', text)
        self.assertIn('it does not verify logo identity or readability', text)

    def test_five_layouts_and_relative_reference_links_exist(self):
        text = (SKILL / 'SKILL.md').read_text()
        for n in range(1, 6):
            self.assertIn(f'| {n:02d} |', text)
        # Catch broken guidance links without pinning its paragraph wording.
        for path in re.findall(r'\]\(([^)]+\.md)\)', text):
            with self.subTest(link=path):
                self.assertTrue((SKILL / path).is_file())

    def test_approved_reference_and_transparent_mascot_are_usable(self):
        from PIL import Image
        from test_portrait_output import validator
        self.assertEqual(validator.validate_output(SKILL / 'assets/approved-photo-grid-reference.jpg'), (1440, 2560))
        with Image.open(SKILL / 'assets/watt-d/35-speed-running-transparent-approved.png') as im:
            self.assertEqual(im.mode, 'RGBA')
            self.assertEqual(im.getchannel('A').getextrema(), (0, 255))
        self.assertTrue((SKILL / 'references/approved-photo-grid.md').is_file())


if __name__ == '__main__':
    unittest.main()
