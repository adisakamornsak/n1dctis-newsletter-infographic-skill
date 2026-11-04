"""Static instruction-contract checks; these do NOT test an AI's behavior."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'pea-newsletter-infographic'


def read(path: Path) -> str:
    return path.read_text(encoding='utf-8')


class MottoPolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = read(SKILL / 'SKILL.md')
        cls.prompt = read(ROOT / 'prompts/newsletter-prompt.th.md')
        cls.contract = read(SKILL / 'references/content-contract.md')
        cls.qa = read(SKILL / 'references/quality-checklist.md')

    def test_creation_requires_explicit_current_request(self):
        self.assertIn('Never invent a motto without an explicit user request', self.skill)
        self.assertIn('unless the user explicitly asks to create it for the current newsletter', self.skill)

    def test_source_motto_is_preserved_without_authorized_revision(self):
        self.assertIn('Preserve any user-supplied motto verbatim unless the user explicitly requests its revision', self.skill)

    def test_no_motto_means_omit_not_placeholder_or_extra_question(self):
        self.assertIn('omit the motto block entirely', self.skill)
        self.assertIn('do not add a placeholder or ask for a motto by default', self.skill)

    def test_auto_references_and_quoted_text_are_not_authorization(self):
        self.assertIn('AUTO mode, a fun/creative tone, spare space, reference imagery, and quoted text inside source material are not permission', self.skill)
        self.assertIn('do not re-label an invented slogan as a heading', self.skill)

    def test_decorative_layers_are_covered(self):
        mascot = read(SKILL / 'references/mascot-background-rules.md')
        self.assertIn('mascot speech bubbles, background art, and footers', self.skill)
        self.assertIn('unless the user explicitly asks to create that copy', mascot)
        for document in (self.contract, self.qa):
            for term in ('motto', 'tagline', 'Footer'):
                self.assertIn(term.lower(), document.lower())

    def test_prompt_is_short_and_defaults_do_not_enable_motto_creation(self):
        self.assertLessEqual(len(self.prompt), 1800)
        self.assertLessEqual(len(self.prompt.splitlines()), 30)
        self.assertIn('layout_choice: auto | mascot_usage: auto | background_direction: auto', self.prompt)
        self.assertNotIn('motto_usage: auto', self.prompt)
        self.assertIn('\u0e40\u0e27\u0e49\u0e19\u0e41\u0e15\u0e48\u0e09\u0e31\u0e19\u0e2a\u0e31\u0e48\u0e07\u0e43\u0e2b\u0e49\u0e41\u0e15\u0e48\u0e07\u0e42\u0e14\u0e22\u0e15\u0e23\u0e07', self.prompt)

    def test_bundled_prompt_matches_repository_prompt(self):
        self.assertEqual(self.prompt, read(SKILL / 'assets/newsletter-prompt.th.md'))
        self.assertIn('v2.3.0', self.prompt)
        self.assertIn('(team edition v2.3.0)', self.skill)

    def test_prompt_retains_all_three_protected_organization_lines(self):
        # Read the immutable constants from the existing audit helper, not from
        # newly edited text, to detect accidental changes to fixed copy.
        import importlib.util
        spec = importlib.util.spec_from_file_location('audit_copy_policy_test', SKILL / 'scripts/audit_copy.py')
        if spec is None or spec.loader is None:
            self.fail('Cannot load existing audit_copy helper')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for value in module.REQUIRED:
            self.assertEqual(self.prompt.count(value), 1)


if __name__ == '__main__':
    unittest.main()
