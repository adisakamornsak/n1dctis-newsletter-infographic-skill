# เพิ่มภาพต้นฉบับและอัปเดต repository

Repository: `adisakamornsak/n1dctis-newsletter-infographic-skill`

ชุดข้อความถูกจัดเตรียมสำหรับเผยแพร่ผ่านการเชื่อมต่อ GitHub หลังเข้าถึง repo ได้แล้ว ข้อจำกัดที่เหลือคือภาพ PNG ต้นฉบับ 7 ไฟล์จากพื้นที่ทำงาน ซึ่งยังไม่รวมในการอัปโหลดข้อความนี้ ไม่ต้องสร้าง repo ใหม่หรือส่ง token ให้ผู้ช่วย

## เพิ่มภาพผ่านหน้า repository

ใช้ชุดเต็มที่ดาวน์โหลดไว้หรือ ZIP เฉพาะภาพที่ได้รับ แตกไฟล์ก่อน แล้วนำไฟล์ทั้ง 7 ไปไว้ที่ `pea-newsletter-infographic/assets/` ตาม [รายการภาพ](../pea-newsletter-infographic/assets/README.md) โดยคงชื่อและข้อมูลต้นฉบับ ตรวจสิทธิ์ใน [คู่มือแบรนด์](brand-assets.th.md) ก่อนเผยแพร่

ใช้การอัปโหลดไฟล์ของ GitHub ไปยังโฟลเดอร์ปลายทาง ตรวจเส้นทางก่อน commit ไม่อัปโหลด ZIP แทนภาพทั้งเจ็ด และไม่ซ้อนโฟลเดอร์ชื่อ repo เพิ่มอีกชั้น หากหน้าเว็บไม่รองรับการอัปโหลดตามที่ต้องการ ให้ใช้ Git บนเครื่องของคุณ

## ใช้ Git ในเครื่องที่เข้าสู่ระบบแล้ว

```bash
git clone https://github.com/adisakamornsak/n1dctis-newsletter-infographic-skill.git
cd n1dctis-newsletter-infographic-skill
git switch -c add/original-reference-assets
```

คัดลอก PNG ทั้ง 7 จากชุดต้นฉบับไปไว้ที่ `pea-newsletter-infographic/assets/` จากนั้น:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
git status --short
git add pea-newsletter-infographic/assets/*.png
git diff --cached --stat
git diff --cached --check
git commit -m "Add original newsletter reference assets"
git push -u origin add/original-reference-assets
```

เปิด Pull Request ตรวจภาพและผลทดสอบก่อน merge หลังภาพครบและตรวจ checksum แล้วจึงแก้ข้อความสถานะใน README, assets/README และ validation report เป็นพร้อมภาพครบ ห้ามลบคำเตือนก่อนตรวจจริง

ไม่ใช้ force push ไม่เปลี่ยน visibility เพื่อแก้ปัญหาการเชื่อมต่อ ไม่ฝัง token ในไฟล์หรือ URL และไม่ commit ภาพข่าวใหม่หรือข้อมูลลับโดยอัตโนมัติ
