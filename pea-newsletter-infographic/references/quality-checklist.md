# Checklist ก่อนส่ง Newsletter

- [ ] โลโก้ กฟภ. ใช้ asset ต้นฉบับโดยไม่ redraw/recolor/distort
- [ ] Header = `กองเทคโนโลยีดิจิทัลและการสื่อสาร` ตรงทุกตัวอักษร
- [ ] Sub-header = `แผนกระบบสารสนเทศและความปลอดภัยไซเบอร์` ตรงทุกตัวอักษร
- [ ] Footer = `การไฟฟ้าส่วนภูมิภาค เขต 1 ภาคเหนือ (จังหวัดเชียงใหม่)` ตรงทุกตัวอักษร
- [ ] ทุกข้อความใหม่เป็น Google Sans จริงและรองรับภาษาไทย ไม่มี fallback
- [ ] ตัวเลข วันที่ หน่วยวัด และรหัส ตรงต้นฉบับทุกตัวและครบทุกตำแหน่งที่จำเป็น
- [ ] สรุปใจความแล้วความหมายไม่เปลี่ยน ไม่เพิ่มข้อเท็จจริงหรือขั้นตอนเอง
- [ ] ใช้ภาพแนบจริงครบทุกภาพ ไม่มี crop/retouch/re-generate/overlay วัตถุ
- [ ] ทุกภาพรักษาสัดส่วน และเห็นเนื้อหาครบ ไม่มีภาพยืด
- [ ] Layout ยึดตัวอย่าง สีม่วงทอง บรรทัดอ่านง่าย ระยะห่างพอดี
- [ ] ตัวอักษรไทยไม่แตก ไม่ขาด เส้นวรรณยุกต์ไม่หลุด ไม่มีข้อความทับหรือหลุดขอบ
- [ ] Dense content is reflowed into the same readable canvas; no pagination, silent omissions or illegibly small text.
- [ ] ตรวจ final export 100% และดูหน้าจอมือถืออีกครั้ง

## v2.1 - mascot / background checks

- [ ] Chosen style is explicitly recorded as 01-05 and matches the content's theme.
- [ ] PEA Watt-D usage decision is recorded as include / omit / auto and is appropriate to the tone.
- [ ] If PEA Watt-D appears, its identity is consistent, secondary to the content, and does not overlap the protected logo, locked text, or original attached photos.
- [ ] Decorative background matches the news theme and improves mood/readability without introducing unverified facts or overpowering the content.
- [ ] Four new style reference pictures have been treated as art direction, not as source text, a verified logo, or real project documentation.
- [ ] Added decorative cybersecurity/IT icons and mascot layers are separate from original imagery.
- [ ] Timeline steps, KPIs, chart values, dates, user names and outcomes originate from user-supplied content, not concept pictures.
- [ ] All attached screenshots are unmodified and unobscured, including numerical values already inside the screenshot.
- [ ] If fonts could not be verified as Google Sans for every newly composed Thai glyph, that limitation is explicitly disclosed before delivery.
- [ ] Style variation does not alter the required Thai header, sub-header, footer, exact PEA logo, or unchanged source images.

## Motto checks (retained from v2.1.1)

- [ ] No newly created motto / slogan / tagline / catchphrase without an explicit request for this issue.
- [ ] Supplied motto wording is verbatim unless its revision was requested.
- [ ] Without supplied wording or authorization, there is no motto section or placeholder.
- [ ] Inspect headings, banners, captions, Watt-D speech, background art and the Footer too.
- [ ] AUTO, fun tone, reference text and empty space are not authorization; no slogan is disguised as a factual heading.

## Single-image checks (v2.2.0)

- [ ] Accept news-image count without a template-defined cap; distinguish real tool capacity limits.
- [ ] Inventory all accessible attachments and flag missing/corrupt files. No arbitrary subset or unapproved deduplication.
- [ ] Every required news-image ID has a visible placement; exclusions have explicit user authorization.
- [ ] Required IDs and placed IDs match, not merely their totals. Supporting logo/mascot/reference assets are classified separately.
- [ ] Every source image is fully visible with proportional contain placement; no cropping, obscuring overlays, clipping or substitutions.
- [ ] Expand the single canvas before sacrificing meaningful copy, locked numbers or screenshot readability. A4 is optional.
- [ ] Exactly one final static PNG file with one frame, one header and one footer; no alternate pages, animation or separate image parts.
- [ ] Inspect the whole composition and full-resolution detail; disclose any mobile zoom/scroll requirement.
- [ ] Counts and dimensions are reported only after actual placement/export verification. Internal tiles are not user deliverables.
- [ ] If capacity prevents a complete readable single image, report the limitation rather than presenting an incomplete result as finished.

Static tests check instruction consistency, not actual AI behavior, font identity, photo placement or final-image fidelity. Inspect every real export separately.
