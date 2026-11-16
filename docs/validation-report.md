# Validation report — v2.4.4, 2026-11-17

## Results

- `python3 -m unittest discover -s tests -v`: **49 tests passed**, no failures, errors or skips.
- Skill `quick_validate.py`: PASS.
- `python3 tools/package_skill.py --output dist/skill.zip --force`: PASS, including archive checksum.
- Repository and bundled Thai prompt versions/content: synchronized.
- `git diff --check`: PASS.

## Repair scope

The v2.4.3 baseline ran 54 tests with 21 failures and 21 errors. The old suite
called missing helper functions and still required PNG, version v2.3.0,
lossless logo pixels, prohibited photo cropping and a fixed 1800-character
prompt limit. Those expectations conflict with the current authorized JPEG,
proportional logo scaling and focal-photo-cropping requirements.

The current suite consolidates redundant wording assertions, removes obsolete
requirements, checks the current version dynamically, and adds behavioral
coverage. No failing test is skipped or marked as an expected failure.

## Tested behavior

- Copy auditing: each protected line appears exactly once, source numeric tokens
  remain present, Thai/Arabic digits are distinct, and CLI exit status matches
  callable results. Missing input files fail cleanly.
- Logo placement: fixed canvas, proportional downscaling, invalid scale and
  clipping rejection, correct placement/color with JPEG tolerance, immutable
  source bytes, separate destination requirement and JPEG naming.
- Final output: .jpg/.jpeg filename, actual RGB JPEG, exact 1440 × 2560 geometry,
  no EXIF rotation, complete image decoding, and no mutation during validation.
  Corrupt, missing, truncated, non-RGB, disguised PNG, animated PNG and wrong-size
  files are rejected. CLI success/failure statuses are exercised.
- Packaging: required assets, source-byte preservation, checksum, font/symlink
  exclusion, and explicit overwrite rules.
- Instruction contracts: fixed JPEG delivery, all images, capacity handling,
  focal cropping versus protected logo rules, five layouts, real reference
  links, current synchronized prompt, fixed copy and explicit-only motto gate.
- Approved assets: final reference passes the JPEG validator; mascot asset has
  both transparent and opaque alpha values.

## Limits

These checks do not render a new newsletter or prove model compliance. Visually
review Thai line breaks, branding, image coverage and readability in every final
output. Copy auditing detects missing numeric tokens, not every invented extra
number, changed numerical association or semantic error. The tests explicitly
retain this limitation. JPEG pixels are lossy; source files remain unchanged.

## Reproduce

```bash
python3 -m pip install -r requirements.txt
python3 -m unittest discover -s tests -v
python3 tools/package_skill.py --output dist/skill.zip --force
python3 pea-newsletter-infographic/scripts/validate_output.py final.jpg
```

Skill structure validation additionally needs PyYAML and the host's
`skill-creator/scripts/quick_validate.py`; it is not a runtime dependency of the
newsletter helpers.
