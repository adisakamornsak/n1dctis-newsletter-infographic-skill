"""Check maintained motto guidance and prompt consistency, not model behavior."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'pea-newsletter-infographic'


class MottoPolicyTests(unittest.TestCase):
    def test_explicit_request_and_preservation_rules_are_present(self):
        text = (SKILL / 'SKILL.md').read_text()
        self.assertIn('Never invent a motto without an explicit user request', text)
        self.assertIn('unless the user explicitly asks for it in the current newsletter', text)
        self.assertIn('Preserve a supplied motto verbatim unless revision is explicitly requested', text)

    def test_mascot_and_prompt_do_not_bypass_the_gate(self):
        mascot = (SKILL / 'references/mascot-background-rules.md').read_text()
        self.assertIn('ห้ามให้ Watt-D พูด motto หรือ slogan ที่แต่งขึ้นเองโดยไม่ได้รับคำสั่งชัดเจน', mascot)
        prompt = (ROOT / 'prompts/newsletter-prompt.th.md').read_text()
        self.assertIn('เว้นแต่ฉันสั่งให้แต่งโดยตรง', prompt)
        self.assertIn('ถ้าไม่มีให้ละส่วนนี้ รวมถึงในภาพและคำพูดมาสคอต', prompt)
        self.assertNotIn('motto_usage: auto', prompt)

    def test_prompt_is_synced_with_current_version_and_fixed_copy(self):
        prompt = (ROOT / 'prompts/newsletter-prompt.th.md').read_text()
        self.assertEqual(prompt, (SKILL / 'assets/newsletter-prompt.th.md').read_text())
        version = re.search(r'team edition (v[0-9.]+)', (SKILL / 'SKILL.md').read_text()).group(1)
        self.assertIn(version, prompt)
        from test_helpers import copy
        for value in copy.REQUIRED:
            self.assertEqual(prompt.count(value), 1)


if __name__ == '__main__':
    unittest.main()
