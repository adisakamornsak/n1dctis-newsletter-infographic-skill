"""Text-contract regression tests; not an image renderer or a model evaluation."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'pea-newsletter-infographic'


def read(path):
    return path.read_text(encoding='utf-8')


class SingleImagePolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = read(SKILL / 'SKILL.md')
        cls.guide = read(SKILL / 'references/single-image-layout.md')
        cls.prompt = read(ROOT / 'prompts/newsletter-prompt.th.md')
        cls.contract = read(SKILL / 'references/content-contract.md')
        cls.qa = read(SKILL / 'references/quality-checklist.md')
        cls.layout = read(SKILL / 'references/layout-catalog.md')

    def test_any_count_including_zero_with_real_limit_disclosure(self):
        self.assertIn('any number of supplied news images, including zero', self.skill)
        self.assertIn('no template-defined image-count cap', self.skill)
        self.assertIn('does not remove upload, memory, pixel, or export limits', self.skill)

    def test_exactly_one_static_file_not_animation(self):
        self.assertIn('Exactly one final static PNG', self.skill)
        self.assertIn('one output file and one PNG frame', self.skill)
        self.assertIn('animated/multi-frame PNG', self.skill)

    def test_no_legacy_pagination_fallbacks(self):
        obsolete = (
            'use an extra page', 'use a coordinated page 2', 'add coordinated pages',
            '\u0e16\u0e49\u0e32\u0e41\u0e19\u0e48\u0e19\u0e43\u0e2b\u0e49\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e2b\u0e19\u0e49\u0e32',
            '\u0e43\u0e0a\u0e49\u0e2b\u0e19\u0e49\u0e32\u0e15\u0e48\u0e2d',
            '\u0e43\u0e2b\u0e49\u0e17\u0e33\u0e40\u0e1b\u0e47\u0e19 2 \u0e2b\u0e19\u0e49\u0e32',
        )
        for text in (self.skill, self.guide, self.prompt, self.contract, self.qa, self.layout):
            for phrase in obsolete:
                with self.subTest(phrase=phrase):
                    self.assertNotIn(phrase.lower(), text.lower())

    def test_canvas_is_fixed_portrait(self):
        self.assertIn('Fix the output to exactly 1440x2560 px (width x height), portrait 9:16', self.skill)
        self.assertIn('Set width=1440 and height=2560 pixels', self.guide)
        self.assertIn('report the capacity conflict', self.guide)

    def test_manifest_checks_ids_not_counts_only(self):
        self.assertIn('every required news-image ID must appear', self.skill)
        self.assertIn('Counts alone cannot catch', self.guide)
        self.assertIn('IDs and placed IDs match, not merely their totals', self.qa)

    def test_no_silent_selection_or_deduplication(self):
        self.assertIn('Do not deduplicate or select a subset without permission', self.skill)
        self.assertIn('distinct ID for each supplied occurrence', self.guide)

    def test_supporting_assets_are_not_gallery_photos(self):
        self.assertIn('supporting assets, not news-photo gallery entries', self.skill)
        self.assertIn('Do not omit a news image by relabeling it as a reference', self.contract)

    def test_no_crop_overlap_or_decorative_clipping(self):
        self.assertIn('including corners, without overlap or decorative clipping', self.skill)
        self.assertIn('frame rounding must not clip its corners', self.guide)

    def test_private_intermediates_are_not_deliverables(self):
        self.assertIn('Keep intermediate tiles, individual photos, manifests and previews internal', self.skill)
        self.assertIn('Do not deliver those tiles separately', self.guide)

    def test_blockers_must_not_be_reported_as_success(self):
        self.assertIn('do not present a partial, cropped, tiny, or split result as complete', self.skill)
        self.assertIn('If the current environment cannot produce', self.guide)

    def test_guide_is_linked_and_all_five_layouts_inherit_rule(self):
        self.assertIn('(references/single-image-layout.md)', self.skill)
        self.assertIn('All five styles must place every required image', self.layout)
        for n in range(1, 6):
            self.assertIn(f'| {n:02d} |', self.skill)

    def test_logo_helper_limits_are_disclosed(self):
        self.assertIn('helper requires a 1440x2560 canvas', self.skill)
        self.assertIn('never crop or rescale a newly supplied logo', self.skill.lower())

    def test_short_prompt_is_current_and_single_image(self):
        self.assertIn('v2.3.0', self.prompt)
        self.assertLessEqual(len(self.prompt), 1800)
        self.assertLessEqual(len(self.prompt.splitlines()), 30)
        self.assertIn('\u0e23\u0e27\u0e21\u0e17\u0e38\u0e01\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e43\u0e19\u0e20\u0e32\u0e1e\u0e40\u0e14\u0e35\u0e22\u0e27', self.prompt)
        self.assertIn('\u0e2b\u0e49\u0e32\u0e21\u0e41\u0e22\u0e01\u0e2b\u0e19\u0e49\u0e32/\u0e2b\u0e25\u0e32\u0e22\u0e20\u0e32\u0e1e', self.prompt)
        self.assertEqual(self.prompt, read(SKILL / 'assets/newsletter-prompt.th.md'))


if __name__ == '__main__':
    unittest.main()
