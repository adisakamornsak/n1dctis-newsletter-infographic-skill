# ติดตั้ง PEA Newsletter Infographic สำหรับ Claude Code

รองรับ Claude Code CLI และ Claude Code ในแอป Desktop ที่รองรับ Plugins (ขึ้นกับเวอร์ชันและสิทธิ์ผู้ใช้)

## ติดตั้งผ่าน GitHub Marketplace

เปิด Claude Code แล้วพิมพ์คำสั่งต่อไปนี้ในหน้าสนทนา (ไม่ใช่คำสั่ง shell):

```text
/plugin marketplace add adisakamornsak/n1dctis-newsletter-infographic-skill
/plugin install pea-newsletter-infographic@n1dctis-newsletter
```

เลือกระดับการติดตั้งและยืนยันตามหน้าจอ หากระบบแจ้งให้รีโหลด ให้รัน `/reload-plugins`

## เรียกใช้งาน

```text
/pea-newsletter-infographic:pea-newsletter-infographic
```

หรือพิมพ์คำขอว่า "ใช้ PEA Newsletter Infographic สร้างข่าวภาษาไทยจากข้อความและภาพที่แนบ" แล้วแนบไฟล์ที่จำเป็น

## อัปเดต

```text
/plugin marketplace update n1dctis-newsletter
```

หากใช้ `version` ใน Plugin manifest ให้ผู้ดูแลเพิ่มเลขเวอร์ชันเมื่อเผยแพร่การเปลี่ยนแปลง เพื่อให้ระบบติดตั้งอัปเดตได้ตามแนวทางของ Claude Code

## ข้อจำกัด

- Marketplace นี้เป็นแหล่ง Plugin ที่คุณแชร์เอง ไม่ใช่ Anthropic Official Marketplace และไม่ทำให้ Plugin ปรากฏใน Claude Chat ทั่วไป
- Skill มีคำสั่งและ asset สำหรับผลิตงาน แต่ไม่ได้ติดตั้งฟอนต์หรือเครื่องมือประกอบภาพโดยอัตโนมัติ หากระบบไม่มีเครื่องมือที่ยืนยันไฟล์ JPG ขนาด 1440×2560 หรือฟอนต์ได้ ต้องระบุว่าเป็นร่างแทนการอ้างว่างานผ่านเกณฑ์
- โลโก้ PEA และภาพมาสคอตต้องใช้งานภายใต้สิทธิ์ที่เกี่ยวข้อง
- โครงสร้างเดียวกันใน `plugins/pea-newsletter-infographic/skills/` ยังใช้ร่วมกับ ChatGPT และ Codex ได้ ไม่ต้องคัดลอกภาพซ้ำ

เอกสารอ้างอิง: https://code.claude.com/docs/en/plugin-marketplaces
