# Validation report - v2.3.0 fixed portrait output

## Baseline and scope

- GitHub main inspected at `247846ccc84567d758101cdbb30f54ff97cdf1f1` (v2.2.0).
- New target: exactly one static PNG, width=1440 px, height=2560 px, portrait 9:16.
- The user's long edge is vertical. Width=2560/height=1440 would be landscape.
- Removed the earlier canvas-expansion fallback from active instructions and both short prompts.
- Retained all-news-images, explicit-only motto, brand, source-copy and font rules.
- No PNG, original logo, font or mascot asset is changed. No complete newsletter was rendered.

## Executed checks

| Check | Result |
| --- | --- |
| Skill structure (`quick_validate.py`) | PASS |
| Copy-helper tests | 5 PASS |
| Motto instruction-contract tests | 8 PASS |
| Single-image instruction-contract tests | 13 PASS |
| Package-builder tests, synthetic fixtures | 7 PASS |
| Portrait validator/helper tests, synthetic fixtures | 12 PASS |
| Portrait instruction-contract tests | 3 PASS |
| Total selected unit tests | 48 PASS |
| Short prompt | 30 lines, 1747 Unicode code points |
| Repository and bundled prompt | Identical bytes |

The geometry tests create and inspect actual synthetic image files. They check
1440x2560 acceptance, rejection of landscape/legacy/oversized/wrong-resolution
images, non-PNG data under a PNG filename, animation, EXIF transforms, missing
or corrupt files, read-only validation, CLI exit status, and logo placement
using a synthetic fixture. These tests do not verify real PEA branding.

Run from a complete repository checkout:

```bash
python -m unittest discover -s tests -v
python pea-newsletter-infographic/scripts/validate_output.py output.png
python tools/package_skill.py --output dist/skill.zip
```

## Limits

The latest repository logo binary was not available locally in this environment.
Its Git blob is `6a809eb933f8e38ad32835db83efce23c7141811`. An older local copy was
not substituted. The three existing real-logo tests were not rerun. The
updated logo helper was tested on synthetic pixels at the new dimensions.
A full installable archive must be packaged from a complete repository checkout
with the current logo; no incomplete archive is represented as a full skill.

`validate_output.py` never resizes or edits a file. It checks PNG geometry,
frame count and orientation only, not Google Sans identity, source-photo
coverage, exact text, layout readability or whether an AI follows the skill.
The unchanged copy helper does not reject every added number.

No fixed-size canvas has infinite readable capacity. If all required content
cannot fit readably, the skill must report the conflict without changing size,
splitting pages, omitting images or claiming success. The final image still
requires visual and content QA on the actual target renderer.
