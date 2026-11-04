# ข้อตกลงการจัดเนื้อหาสำหรับทีม

## ข้อมูลที่รับจากทีม

ใช้ `assets/content-input-example.md` เป็นแบบฟอร์มตัวอย่าง (กรอกเท่าที่มีจริง):
- หัวข้อ: ประเด็นหลักของข่าว/กิจกรรม
- เนื้อหาต้นฉบับ: ข้อความเต็มก่อนสรุป
- วัน/ช่วงเวลา: คงตามต้นฉบับทุกหลัก
- ภาพหลัก: ระบุไฟล์ภาพแนบตามจริง
- ภาพกิจกรรม/ภาคสนาม: ระบุไฟล์ตามจริงและเรียงตามที่ผู้ใช้กำหนด
- ประเด็นสำคัญ: สกัดจากข้อความจริง ไม่สร้างขั้นตอนใหม่
- ข้อมูลเพิ่มเติม: มีเฉพาะเมื่อมีหลักฐานในต้นฉบับ
- ตัวเลือกเสริม: `layout_choice`, `subject_focus`, `mascot_usage`, `background_direction`

## กฎถ้อยคำ

- รักษาข้อมูลที่มีผลต่อความเข้าใจ: ใคร ทำอะไร ที่ไหน เมื่อใด ผลลัพธ์อะไร พร้อมค่าตัวเลขเดิม
- ย่อ/รวมประโยคซ้ำได้ แต่ห้ามเปลี่ยนคำปฏิเสธ (เช่น ยังไม่พร้อม → พร้อม), ความถี่, ขอบเขตหรือเงื่อนไข
- ไม่สร้างจำนวนขั้นตอน 4 ข้อเพียงเพื่อให้เหมือนภาพตัวอย่าง; จำนวนกล่องขึ้นกับเนื้อหาจริง
- ห้ามแปลง `OFC`, `ODF`, `Industrial Switch` หรือคำเทคนิคอื่นโดยไม่มีคำยืนยัน
- Keep all required copy and images in one final PNG. When space is tight, condense without losing meaning, reduce decoration, reflow within the fixed 1440x2560 portrait canvas; never add pages or omit evidence.
- ถ้าข้อความขัดแย้งในไฟล์ต่าง ๆ ให้แจ้งผู้ใช้ก่อนสรุป ไม่แก้ข้อมูลเอง

## กฎภาพ

- ต้องมีต้นฉบับของภาพทุกภาพในผลลัพธ์; จัดขนาดแบบ contain โดยไม่ crop
- ห้าม re-generate จากคำบรรยายภาพ หรือใช้ภาพ stock แทนภาพผู้ใช้
- ห้ามแต่งสี, ลบพื้นหลัง, ขยายภาพด้วย AI, เพิ่มโลโก้ทับภาพจริง
- หากออกแบบภาพตกแต่งใหม่ ให้แยกเลเยอร์จากภาพจริง
- สามารถใช้ PEA Watt-D เป็นองค์ประกอบตกแต่งได้เมื่อเหมาะกับน้ำเสียงของข่าว แต่ห้ามบังภาพจริงหรือข้อความบังคับ
- ภาพพื้นหลังสามารถเปลี่ยนได้ตามลักษณะข่าว เช่น cyber, digital operations, field work, awareness, festive/internal fun หรือ neutral โดยต้องเป็นเพียงงานตกแต่ง ไม่ใช่หลักฐานเหตุการณ์จริง
- ตรวจชื่อไฟล์และจำนวนภาพที่นำเข้า/ใส่ผลลัพธ์ให้ตรงกัน

## กฎฟอนต์

- ใช้ตระกูลฟอนต์ `Google Sans` ที่มีสิทธิใช้งานและแสดงอักษรไทยได้ครบทั้งหนา/ปกติ
- ห้ามสลับไป `Arial`, `Noto Sans Thai`, `Roboto`, `Prompt` หรือฟอนต์อื่นในข้อความแม้เพียงบางส่วน
- หากพบ glyph ภาษาไทยหาย หรือ font fallback แทรก ให้หยุดส่งภาพนั้นจนแก้ฟอนต์ได้
- ภาพ preview ที่ AI สร้างเพียงอย่างเดียวไม่ใช่หลักฐานว่าใช้ Google Sans จริง

## การตรวจตัวเลข

เก็บทั้ง `26 - 30`, `2569`, เปอร์เซ็นต์, หมายเลขสาย/อุปกรณ์, หมายเลขข้อ และข้อความข้างหน่วยตามต้นฉบับ ตรวจด้วย script `audit_copy.py` ก่อน QA ภาพ และตรวจซ้ำด้วยสายตาหลังจัดหน้าจริง

## v2.1 - five style input

Optional field: `layout_choice: 01 | 02 | 03 | 04 | 05 | auto` (default: auto).

Optional field: `subject_focus: general | digital-operations | cyber-safety | enterprise-analytics | cyber-ops-infrastructure | internal-fun`.

Optional field: `mascot_usage: auto | include | omit` (default: auto).

Optional field: `background_direction: auto | cyber | digital | field | awareness | festive | neutral | custom description` (default: auto).

Decorative digital/cyber art, PEA Watt-D, and icons may vary with story, but must remain separate from original attached photos and screenshots. Do not read source statistics/dates from the four new concept designs.

If `layout_choice` conflicts with the topic, prioritize the explicitly requested template while adapting unused infographic panels; never invent missing content to fit its shape.

## Motto / slogan authorization (retained from v2.1.1)

- Never invent a motto, slogan, tagline, catchphrase or inspirational sign-off without an explicit request for the current newsletter.
- Preserve a supplied motto verbatim unless the user explicitly requests its revision.
- If neither supplied wording nor a creation request exists, omit the element entirely; do not add a placeholder or ask for a motto by default.
- AUTO, a fun tone, spare space and reference text do not authorize invention. Apply this rule to headings used as slogans, banners, captions, mascot speech bubbles, background text and the Footer.
- Ordinary source-grounded titles and summaries remain allowed. Even an explicitly requested motto must not invent facts or be presented as the official PEA motto.

| Input | Required behavior |
| --- | --- |
| No motto; AUTO or a request for a fun design | Omit the motto section; do not invent one |
| User supplies a motto | Keep the exact wording |
| User explicitly asks to create a motto for this issue | Create only within that request |
| A reference image contains a motto | Do not reuse it as live news content |

## Single-image contract (v2.3.0)

- Accept any number of supplied news images with no template-defined image-count cap, including zero; actual upload, memory, pixel and export limits still apply.
- Include every supplied news image in exactly one final static PNG at 1440x2560 px (width x height), portrait 9:16, except images explicitly excluded by the user. Do not invent images when none were provided.
- Assign each submitted news-image occurrence its own ID; preserve the order across batches. Do not silently deduplicate identical images or discard files with similar names.
- Distinguish news images from reference layouts, the protected logo and mascot assets. Do not omit a news image by relabeling it as a reference. Report inaccessible/corrupt inputs rather than treating them as absent.
- Record an image manifest with ID, filename, source role, inclusion/exclusion decision and final placement rectangle. Check expected IDs against placed IDs, not just counts.
- Use contain placement without cropping, stretching, rounded clipping, recoloring, content edits, overlays or AI replacement. Native originals must remain unchanged.
- Use an adaptive grid, gallery, collage or filmstrip; the example layouts do not prescribe a maximum photo count.
- Reduce decoration, condense prose without losing locked facts, then reflow within the same fixed canvas. Do not expand it, swap width and height, or substitute A4. Keep screenshots and text usable at native resolution.
- Check one file, one PNG frame, exactly 1440x2560 pixels, one header/footer and all required images before delivery. Never use pagination, animation or a ZIP of separate images as a workaround.
- If real tool limits or fixed-size capacity make the complete readable single PNG impossible in the current environment, report the blocker. Do not silently split, discard, crop or claim completion. Processing in batches is internal only; the final output is still one image.
