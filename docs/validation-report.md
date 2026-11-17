# Validation report — v3.0.0, 2026-11-17

## Results

- `npm run build:plugin`: PASS; creates the portable Plugin at `plugins/pea-newsletter-infographic/`.
- `npm test`: **13 tests passed**, no failures or skipped tests.
- `npm run check:plugin`: PASS; **72 packaged files**, comprising the portable manifest and **71 canonical skill files**. Every copied file hash matches its maintained source.
- Manifest validated against the vendored Agent Plugins 1.0.0 schema; source: https://agent-plugins.org/schemas/1.0.0/plugin.schema.json. The local validator implements the validation keywords used in that schema, not a general JSON Schema engine. Host-specific extension semantics and publication approval remain outside this check.
- All 59 original image/artwork files in the canonical skill were compared with Git HEAD and remain byte-for-byte unchanged. No active Python source files or runtime dependency manifest remain.
- Canonical and packaged Thai prompts, skill version, manifest version and maintainer package version: synchronized.
- `git diff --check`: PASS.

## Current change

The Plugin now contains instructions and assets only. Local updater, installer,
copy-audit, logo-composition and image-validation scripts and their runtime
dependencies were removed. Their earlier tests were retired with the removed
implementations; the 13 current tests do not imply equivalent image-rendering
coverage. End users do not need a terminal or local software installation.

Use the latest version already synced by the Plugin system. No runtime GitHub
fetch, local updater, per-request freshness gate or downloaded executable code
is required. A synced version is not claimed to be the newest GitHub commit.
The host's image/file tools perform production and verification where available.
If source-image preservation, font identity or final export properties cannot
be verified, the skill requires a specific limitation report and a draft label.

The canonical skill folder is maintained separately from the generated, tracked
portable Plugin copy. This preserves the existing source paths while supplying
the standard `skills/<name>/SKILL.md` layout without external links or symlinks.
Rebuild the Plugin copy after changing the canonical source. The GitHub
marketplace points at this complete tracked folder, not an ignored build folder.

## Tested behavior

- Build/check use the complete canonical file set, preserve source bytes and detect modified protected logo copies, missing files, stale generated files and version/prompt mismatches.
- Rebuild removes stale generated files and is repeatable.
- Missing original logo blocks a build without replacing the previous Plugin.
- Symlinks, font files and executable runtime files are rejected; hidden private inputs are excluded.
- The portable manifest's schema rejects unknown fields and incorrect types. This skills-only package disallows declared local hooks or registered-app dependencies.
- Marketplace source resolves to the complete Plugin folder in this repo.
- Contract checks retain configurable sub-header/default, all news images, five layouts, original assets, disclosed font fallback, explicit-only motto gate and single portrait JPG/JPEG output.

## Limits

No Plugin was published or imported into a live account during this work.
Web/Desktop/mobile image production has not been tested. The package structure
supports portable distribution, but available tools, fonts, asset access and
permissions vary by host. The Plugin does not provision an image renderer,
export service, MCP server or font installation. The current tests do not
render a newsletter, decode image files, prove Thai shaping, inspect every
factual association or verify the identity of a font used by another tool.
Visual and file-property QA remain required for each final image.

The image assets are existing reference material, not newly verified event
facts. Historical checksum and update records remain historical only.
The old generated `dist/skill.zip` was retired because it contained the former
local-runtime workflow. Use the complete current Plugin directory instead.

## Reproduce — maintainers only

Node.js 20+; no package installation or network access needed for these checks:

```bash
npm run build:plugin
npm test
npm run check:plugin
git diff --check
```

End users install the published/synced Plugin and do not run these commands.
