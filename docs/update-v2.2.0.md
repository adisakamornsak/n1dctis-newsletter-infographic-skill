# Apply the v2.2.0 single-image update

This bundle contains complete replacement/additional text and code files, not a patch. It is an update overlay, not the whole repository and not an installable skill.zip.

## Apply without changing source images

1. Obtain your current complete repository checkout and start from a clean working tree. The inspected base was `fd75db67a7a695b808564eb4dba19dfe6274cfbb`; review later changes before overwriting any same-named file.
2. Create a local working branch, for example `update/single-image-v2.2.0`.
3. Copy the contents inside this archive's `n1dctis-newsletter-infographic-skill/` folder into the repository root, preserving relative paths. Merge directories; do not delete or replace the entire assets folder. No PNG or font file is provided by this update.
4. Inspect the diff, run the tests below, and review the content. Commit only the listed changes. This bundle does not execute any push or merge.

```bash
git switch -c update/single-image-v2.2.0
# Copy the update files into this repository, then:
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
git diff --check
git diff --stat
```

The existing real-logo tests must run against your current logo file; see [validation report](validation-report.md) for this session's tested scope and known helper limitations. Do not weaken a failing test merely to make a report green.

## Commit

After inspecting and approving the local diff:

```bash
git add -- ".gitignore" "AGENTS.md" "README.md" "docs/update-v2.2.0.md" "docs/validation-report.md" "pea-newsletter-infographic/SKILL.md" "pea-newsletter-infographic/agents/openai.yaml" "pea-newsletter-infographic/assets/README.md" "pea-newsletter-infographic/assets/content-input-example.md" "pea-newsletter-infographic/assets/newsletter-prompt.th.md" "pea-newsletter-infographic/references/CHANGELOG.md" "pea-newsletter-infographic/references/content-contract.md" "pea-newsletter-infographic/references/layout-catalog.md" "pea-newsletter-infographic/references/quality-checklist.md" "pea-newsletter-infographic/references/single-image-layout.md" "prompts/newsletter-prompt.th.md" "tests/test_motto_policy.py" "tests/test_packaging.py" "tests/test_single_image_policy.py" "tools/package_skill.py" "docs/update-v2.2.0-manifest.json"
git commit -m "feat: combine all news images into one infographic (v2.2.0)"
```

Publishing this local commit or opening a pull request is a separate, explicit step. No remote operation was performed by the update tools.

## Build the complete installable archive

Use the assets that are already in your repository, not older attachments from a chat:

```bash
python tools/package_skill.py --output dist/skill.zip
```

The output must be named `skill.zip`. It contains the full `pea-newsletter-infographic/` folder and current source assets. If any required asset is missing, the builder stops rather than producing an incomplete substitute. Use `--force` only when deliberately replacing an existing output archive. `dist/` is ignored by Git.

The one-image newsletter rule concerns the final newsletter PNG, not this software distribution archive. Supporting source files, instructions, tests and packaging metadata are expected in the repository.

## Changes supplied

- `.gitignore`
- `AGENTS.md`
- `README.md`
- `docs/update-v2.2.0.md`
- `docs/validation-report.md`
- `pea-newsletter-infographic/SKILL.md`
- `pea-newsletter-infographic/agents/openai.yaml`
- `pea-newsletter-infographic/assets/README.md`
- `pea-newsletter-infographic/assets/content-input-example.md`
- `pea-newsletter-infographic/assets/newsletter-prompt.th.md`
- `pea-newsletter-infographic/references/CHANGELOG.md`
- `pea-newsletter-infographic/references/content-contract.md`
- `pea-newsletter-infographic/references/layout-catalog.md`
- `pea-newsletter-infographic/references/quality-checklist.md`
- `pea-newsletter-infographic/references/single-image-layout.md`
- `prompts/newsletter-prompt.th.md`
- `tests/test_motto_policy.py`
- `tests/test_packaging.py`
- `tests/test_single_image_policy.py`
- `tools/package_skill.py`
- `docs/update-v2.2.0-manifest.json` (SHA-256 checksums for the files above; the manifest does not hash itself)

The existing PNG assets, `scripts/lock_logo.py`, `scripts/audit_copy.py`, `tests/test_helpers.py` and the current mascot-background reference remain untouched. The no-motto-without-explicit-request rule stays in effect.
