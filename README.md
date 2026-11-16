# PEA Newsletter Infographic - N1 DCTIS

**Skill v2.4.4 - 1440x2560 portrait JPG, bento grids, all supplied news images**

Use this instruction bundle and its Thai prompt with a compatible assistant or a manual design workflow. No model, API key or Google Sans font file is included. The bundle includes the supplied running Watt-D original, its user-approved transparent derivative, and a user-approved example newsletter.

## Start here

1. Copy [the short Thai prompt](prompts/newsletter-prompt.th.md), fill the input fields and provide all source images.
2. Make the complete [skill folder](pea-newsletter-infographic/SKILL.md) and required assets readable to the tool you use.
3. Deliver exactly one final JPG/JPEG at 1440x2560 px, portrait.

## v2.4.4 validation fixes

The helper APIs and tests now target RGB JPEG output. Validation fully decodes the image and rejects incorrect file extensions, truncated data and EXIF rotation. Copy auditing requires each protected organization line exactly once. Logo export requires a separate JPG/JPEG destination.

Run `python3 -m unittest discover -s tests -v` after installing `requirements.txt`.

## Layout behavior

- Prefer the approved photo-grid treatment for activity news; adapt the number of images and sections to each story.
- Place a transparent Watt-D cutout beside the headline when appropriate, without a white backing card.
- Let Thai copy flow to the available width with natural word boundaries; verify line breaks after rendering.

- Allow proportional logo downscaling to suit the infographic; preserve the entire logo, original colors, details, and clear space.
- Accept all required user-supplied news images.
- Allow bento-grid, gallery, collage, grid and filmstrip arrangements.
- In layout frames, images may be scaled, zoomed, cropped and repositioned to fill cells without aspect-ratio gaps, while preserving important subjects and avoiding distortion.
- Generate story-matched backgrounds, icons, illustrations and filler visuals when useful so the page does not contain excessive plain white empty areas.
- Keep generated/decorative visuals separate from factual event evidence.
- Do not invent a motto unless explicitly requested for the current issue.

Header: กองเทคโนโลยีดิจิทัลและการสื่อสาร
Sub-header: แผนกระบบสารสนเทศและความปลอดภัยไซเบอร์
Footer: การไฟฟ้าส่วนภูมิภาค เขต 1 ภาคเหนือ (จังหวัดเชียงใหม่)

See [layout catalog](pea-newsletter-infographic/references/layout-catalog.md), [content rules](pea-newsletter-infographic/references/content-contract.md), [mascot/background rules](pea-newsletter-infographic/references/mascot-background-rules.md), [single-image rules](pea-newsletter-infographic/references/single-image-layout.md), and [QA](pea-newsletter-infographic/references/quality-checklist.md).

The existing reference PNG assets and exact logo are preserved; v2.4.3 added the approved reference and mascot cutout without replacing protected source assets.
