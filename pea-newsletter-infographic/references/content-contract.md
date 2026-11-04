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
- ถ้าสื่อข้อความไม่ครบใน 1 หน้า ให้ทำเป็น 2 หน้าในดีไซน์เดียวกัน
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
