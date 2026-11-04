# PEA Newsletter Infographic - N1 DCTIS

**Skill v2.3.0 - 1440x2560 portrait PNG, all supplied news images**

Use this instruction bundle and its Thai prompt with a compatible assistant or a manual design workflow. It is not an image generator, web app or automatic newsletter renderer. No model, API key, Google Sans font file or official Watt-D artwork is included.

## Start here

1. Copy [the short Thai prompt](prompts/newsletter-prompt.th.md), fill the five input fields and provide all source images.
2. Make the complete [skill folder](pea-newsletter-infographic/SKILL.md) and required assets readable to the tool you use. A prompt is not a native installation by itself.
3. Deliver exactly one final static PNG containing every required news image. Output width is 1440 pixels and height is 2560 pixels, portrait 9:16. The long edge is vertical; 2560x1440 in width-by-height order would be landscape.

There is no template-defined image-count cap. Actual attachment, memory, pixel, font and export limits still apply. Reduce decoration, reflow the image grid within the fixed dimensions rather than silently omitting images, shrinking screenshots beyond readability or splitting pages. Report a capacity conflict if all content cannot fit readably; do not change dimensions. See the [single-image rules](pea-newsletter-infographic/references/single-image-layout.md).

## Brand and source protection

Keep the original logo at the top left, original news images uncropped and unobscured, exact numbers and names, purple/gold CI, and verified Google Sans for newly composed text. Do not invent a motto unless explicitly asked for the current issue. Preserve supplied motto wording. Watt-D requires verified source artwork.

Header: กองเทคโนโลยีดิจิทัลและการสื่อสาร
Sub-header: แผนกระบบสารสนเทศและความปลอดภัยไซเบอร์
Footer: การไฟฟ้าส่วนภูมิภาค เขต 1 ภาคเหนือ (จังหวัดเชียงใหม่)

Choose layout 01 (general), 02 (digital operations), 03 (cyber awareness), 04 (analytics) or 05 (network/infrastructure), or leave all design controls on AUTO. See [layout catalog](pea-newsletter-infographic/references/layout-catalog.md), [content rules](pea-newsletter-infographic/references/content-contract.md), [mascot/background rules](pea-newsletter-infographic/references/mascot-background-rules.md), and [QA](pea-newsletter-infographic/references/quality-checklist.md).

## Assets and distribution

The inspected repository main snapshot contains seven PNG assets. This ready-to-commit update intentionally replaces no PNG, logo, font or mascot file. Keep your current `pea-newsletter-infographic/assets/` files. Reference mockups are art direction, not verified story facts or font/logo proof. Review [brand asset guidance](docs/brand-assets.th.md) before further distribution.

## Tests

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

Documentation-contract tests check instructions only, not generated images or AI behavior. Existing helpers are not a full renderer. `lock_logo.py` now requires a 1440x2560 canvas. `scripts/validate_output.py` checks PNG encoding, dimensions, single-frame output and orientation without resizing. Check the actual logo dimensions before using it. The copy checker also has known limitations. See [validation report](docs/validation-report.md).

## Package the full skill using current repository assets

```bash
python tools/package_skill.py --output dist/skill.zip
```

This builds the complete skill folder from local repository files without downloading or changing any assets. It refuses missing required files, fonts and symbolic links. The archive is a distribution bundle, not a multi-image newsletter output. Inspect it before sharing. It does not commit, push, merge, or change repository visibility.

For the preceding update's local-commit steps, see [the historical v2.2.0 guide](docs/update-v2.2.0.md). For the current geometry checks, see [validation](docs/validation-report.md). For other hosts, see [usage guidance](docs/usage-with-other-tools.th.md). Read the [changelog](pea-newsletter-infographic/references/CHANGELOG.md) for version history.
