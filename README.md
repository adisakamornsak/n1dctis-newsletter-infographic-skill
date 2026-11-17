# PEA Newsletter Infographic - N1 DCTIS

**Skill v2.6.0 - 1440x2560 portrait JPG, bento grids, all supplied news images**

Use this instruction bundle and its Thai prompt with a compatible assistant or a manual design workflow. No model, API key, Google Sans or Google Prompt font file is included. The bundle includes the supplied running Watt-D original, its user-approved transparent derivative, and a user-approved example newsletter.

## ติดตั้งจาก GitHub และอัปเดตก่อนใช้ทุกครั้ง

อ่าน [คู่มือติดตั้งและอัปเดตภาษาไทย](docs/install-update.th.md) สำหรับการตั้งค่าครั้งแรกและการย้ายจาก ZIP

```bash
git clone https://github.com/adisakamornsak/n1dctis-newsletter-infographic-skill.git
cd n1dctis-newsletter-infographic-skill
python3 tools/manage_skill.py install
python3 ~/.local/share/pea-newsletter/manage_skill.py run --prompt "สร้างข่าวจากข้อมูลที่ฉันจะให้"
```

`run` ตรวจและอัปเดตจาก `main` ก่อนเปิดแชท Codex CLI ใหม่ทุกครั้ง หากตรวจไม่ได้จะหยุด สกิลที่เรียกตรงใน Desktop ต้องรัน preflight ตามคำสั่งสกิลทุกคำขอ; ไม่ใช่ hook ของแอป ต้องเผยแพร่ชุดนี้ไปยัง `main` ก่อนผู้อื่นติดตั้งได้

## Start here

1. Install the managed GitHub workflow above, then copy [the short Thai prompt](prompts/newsletter-prompt.th.md), fill the input fields and provide all source images.
2. Make the complete [skill folder](pea-newsletter-infographic/SKILL.md) and required assets readable to the tool you use.
3. Deliver exactly one final JPG/JPEG at 1440x2560 px, portrait.

Google Sans is preferred; use Thai-capable Google Prompt as the disclosed fallback when Google Sans is unavailable. If neither is available, report the blocker.

## Configurable department line

Set `sub_header` to the department name to display immediately below the top header. Omitted, empty or whitespace-only values keep the existing default. Supplied values are trimmed at the edges and otherwise preserved exactly. For example: `sub_header: แผนกบริการลูกค้า`. Pass the same value to `audit_copy.py --sub-header "แผนกบริการลูกค้า"` when auditing custom copy.

## Helper validation

The helper APIs and tests now target RGB JPEG output. Validation fully decodes the image and rejects incorrect file extensions, truncated data and EXIF rotation. Copy auditing requires each protected organization line exactly once. Logo export requires a separate JPG/JPEG destination.

Run `python3 -m unittest discover -s tests -v` after installing `requirements.txt`.

## Layout behavior

Layout 01 now has its own [JPG reference](pea-newsletter-infographic/assets/layout-01-chiang-mai-classic.jpg). Its abstract purple/gold backdrop is an example: change backgrounds to suit each story, without requiring Doi Suthep or another landmark.

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
Default sub-header (overridable with `sub_header`): แผนกระบบสารสนเทศและความปลอดภัยไซเบอร์
Footer: การไฟฟ้าส่วนภูมิภาค เขต 1 ภาคเหนือ (จังหวัดเชียงใหม่)

See [layout catalog](pea-newsletter-infographic/references/layout-catalog.md), [content rules](pea-newsletter-infographic/references/content-contract.md), [mascot/background rules](pea-newsletter-infographic/references/mascot-background-rules.md), [single-image rules](pea-newsletter-infographic/references/single-image-layout.md), and [QA](pea-newsletter-infographic/references/quality-checklist.md).

Layout references use the current JPG/JPEG assets; `original-newsletter-reference.png` is no longer required. The exact logo remains unchanged. v2.4.3 added the approved photo-grid reference and mascot cutout.
