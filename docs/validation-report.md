# Validation report

Date: 2026-11-04
Canonical skill: PEA Newsletter Infographic v2.1
Repository: `adisakamornsak/n1dctis-newsletter-infographic-skill`

## Publication scope

The text distribution is prepared for the requested repository. The seven original
PNG files are not included in this remote text-only publication. See
`../pea-newsletter-infographic/assets/README.md`. This is not a complete
asset-inclusive installation. Original skill text and helper scripts are retained;
publication documentation has been updated to disclose the missing assets.

No font binaries, official Watt-D art, recent food-news photos, API keys, or
credentials are included. No new license or repository visibility change is made.

## Local checks

- The complete v2.1 source package preserves 17 canonical files byte-for-byte.
- Skill frontmatter/name/description validation: PASS.
- `python -m unittest discover -s tests -v` on the complete local package: 8 passed.
- Original logo pixel preservation on a 1086 x 1536 PNG: PASS.
- Wrong canvas size and out-of-bounds logo placement: correctly rejected.
- Numeric preservation, changed numbers, duplicate fixed text, and Thai/Arabic
  digit differences: tested.
- Existing limitation that extra numeric tokens are not rejected: documented.

These results apply to the full local package, NOT proof that the remote assets
are present. Logo tests require the missing original logo file. Rerun all tests
on a fresh clone after restoring the seven assets. Compare the canonical files
against `source-skill-sha256.txt`.

## Not verified

- End-to-end newsletter rendering on other AI hosts or design programs.
- Google Sans availability, licensing, Thai glyph coverage, or font fallback.
- Official Watt-D asset availability (no mascot file is supplied).
- Public redistribution rights for logos, reference images, people, or brand art.
- Visual quality of a newly rendered newsletter; this publication renders none.

## Helper limitations

`audit_copy.py` audits a text transcription, not image pixels or OCR. It checks
fixed strings and retained source numeric-token counts. It does not reject every
new number, prove numeric context/order/units, or validate fonts and photography.

`lock_logo.py` pastes the packaged raster at its native size and checks the saved
logo pixels. Reserve its placement area first. It can overwrite underlying
content and is not a complete layout engine or brand-ownership validator.
