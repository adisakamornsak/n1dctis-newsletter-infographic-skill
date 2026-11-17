# Validation report — v2.6.0, 2026-11-17

## Results

- `python3 -m unittest discover -s tests -v`: **67 tests passed**, no failures, errors or skips.
- Skill `quick_validate.py`: unavailable in the current Python environments because PyYAML is not installed. The packaging tests still exercise frontmatter name/description checks.
- `python3 tools/package_skill.py --output dist/skill.zip`: PASS, including archive checksum. Required layout references now use the current `.jpg` assets including layout 01; the retired `original-newsletter-reference.png` is no longer required. Existing logo and image source bytes are preserved.
- Repository and bundled Thai prompt versions/content: synchronized.
- `git diff --check`: PASS.

## Current change

v2.6.0 adds `tools/manage_skill.py` with install/update/status/run commands,
a persistent updater and a per-request `scripts/preflight_update.py` gate.
Every update fetches `main` before using it. The CLI launcher does not open
Codex when freshness cannot be verified; Desktop direct invocation follows the
skill instruction and is not an app-level hook.

Fourteen installer tests use isolated local Git repositories to exercise actual
fetch/archive/install operations, new commits with unchanged version numbers,
backups, local edit preservation, rollback, unsafe archive rejection, locking,
preflight and launch ordering. No GitHub writes or real Codex sessions occur.
An additional smoke check installed all 75 current skill files with the real
assets from a temporary local Git repository, verified their bytes against the
source and successfully ran the persisted preflight updater.

The actual GitHub `main` must contain v2.6.0 before public installation can work;
this work does not push or publish the repository. Live GitHub installation and
Windows execution have not been exercised here. Older unmanaged installations
need the explicit `install --replace-existing` migration. The current updater
runtime stays fixed until the user reinstalls a newer installer.

Earlier v2.5 changes preserve configurable department copy and its blank default,
consistent short prompts, and the visually reviewed illustrative layout 01.

## Earlier repair scope

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
- Installation: fresh Git fetches, validated staged files, backup/rollback,
  unchanged-version commits, preflight subprocess and fail-closed launcher.
- Packaging: required assets, source-byte preservation, checksum, font/symlink
  exclusion, and explicit overwrite rules.
- Instruction contracts: fixed JPEG delivery, all images, capacity handling,
  focal cropping versus protected logo rules, five layouts, real reference
  links, current synchronized prompt, protected copy and explicit-only motto gate.
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
