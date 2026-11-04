# Validation report - v2.2.0 ready-to-commit update

## Baseline and scope

- Inspected GitHub main ref: `fd75db67a7a695b808564eb4dba19dfe6274cfbb`.
- Reconstructed the inspected main SKILL text and verified its Git blob SHA as `11f281f2fcaa5ec5c0184562a9c458249f5f8799` before applying the v2.2.0 edits.
- Retained the explicit-only motto gate and the protected organization strings.
- No remote branch, commit, pull request, merge, push or visibility change was made in this update.
- No PNG asset, font or official mascot artwork is included or replaced by this update bundle.

## Executed checks

| Check | Result |
| --- | --- |
| Hosted skill-creator `quick_validate.py` | PASS |
| Existing copy-helper tests (`CopyTests`) | 5 PASS |
| Motto instruction-contract tests | 8 PASS |
| Single-image instruction-contract tests | 13 PASS |
| Local package-builder tests using temporary synthetic fixtures | 7 PASS |
| Total selected unit tests | 33 PASS |
| Short prompt | 29 lines, 1,703 Unicode code points |
| Repository and bundled prompt | Identical bytes |
| Old pagination fallback scan in active skill documents and prompt | PASS |

Commands run from the repository root:

```bash
python -m unittest discover -s tests -k CopyTests -v
python -m unittest discover -s tests -p test_motto_policy.py -v
python -m unittest discover -s tests -p test_single_image_policy.py -v
python -m unittest discover -s tests -p test_packaging.py -v
```

## What these results do not establish

Text-contract tests verify that instructions are present and consistent; they do not prove an AI follows them. No newsletter was generated in this task. There was no end-to-end evaluation of arbitrary photo counts, real image placement, Google Sans/Thai shaping, real image fidelity, mobile readability or renderer limits.

The latest remote logo was not available as a local binary. The remote Git blob is `6a809eb933f8e38ad32835db83efce23c7141811` (137,262 bytes); the older chat asset is different and was deliberately not substituted. Therefore the three existing real-logo tests were not rerun and a complete installable skill.zip was not produced in this session. The package builder correctly refused to package the staging folder when that required logo was absent.

The owner should run the complete suite against current repository assets before publishing. The unchanged `lock_logo.py` accepts a 1086x1536 canvas only; larger single canvases need another verified compositing path. Current asset dimensions must be checked. The unchanged copy checker does not reject every added number and is not a full factual or visual validator.

## Complete packaging using current local assets

After applying the update to a complete repository checkout:

```bash
python tools/package_skill.py --output dist/skill.zip
```

The builder reads the actual current skill directory, requires the seven PNG assets and core files, preserves their bytes, rejects fonts and symbolic links, and verifies ZIP checksums. These are packaging checks, not image validation. Review all included content before sharing. It performs no Git or network operations.
