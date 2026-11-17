# แพ็กและเผยแพร่ Plugin จาก GitHub

## โครงสร้างปัจจุบัน

```text
.agents/plugins/marketplace.json         รายการสำหรับระบบนำเข้า
plugin.manifest.json                     ต้นฉบับ metadata ของ Plugin
pea-newsletter-infographic/               ต้นฉบับสกิล กฎ และภาพ
plugins/pea-newsletter-infographic/       แพ็กที่สร้างแล้วและต้อง commit
  plugin.json                            portable Agent Plugins 1.0.0
  skills/pea-newsletter-infographic/
    SKILL.md
    agents/
    references/
    assets/
```

แพ็กใช้คำสั่งและทรัพยากรในตัว ไม่ต้องติดตั้ง runtime, hooks, MCP server หรือ API key เพิ่ม ไม่มีไฟล์ฟอนต์ และไม่ต้องให้ผู้ใช้ดึง GitHub ทุกครั้ง
Plugin ไม่ใช่บริการสร้างภาพอัตโนมัติ เครื่องมือผลิตและตรวจไฟล์มาจากระบบแชทปลายทาง

เก็บโฟลเดอร์สกิลต้นฉบับไว้ตามเดิม แก้ที่ต้นฉบับแล้วใช้เครื่องมือ build คัดลอกเป็นโครงสร้างมาตรฐาน `skills/` สำเนา Plugin ต้อง commit ไปด้วยเพื่อให้ระบบซิงก์อ่านได้โดยไม่ต้อง build บนเครื่องผู้ใช้ Git เก็บไฟล์ภาพที่มีเนื้อหาเหมือนกันเป็น blob เดียว จึงไม่เพิ่ม blob ภาพซ้ำเพราะการคัดลอกนี้

## ขั้นตอนของผู้ดูแล repo

ใช้ Node.js 20 ขึ้นไป ไม่ต้องติดตั้ง package เพิ่ม:

```bash
npm run build:plugin
npm test
npm run check:plugin
git diff --check
git status --short
```

ตัว build ตรวจไฟล์บังคับและเส้นทางอ้างอิง ไม่แพ็กฟอนต์ ไฟล์ลับ symlink หรือสคริปต์ runtime และคัดลอกโลโก้/ภาพแบบข้อมูลตรงต้นฉบับ ตัว check เทียบ hash ของทุกไฟล์ในสำเนา Plugin กับต้นฉบับ รวม manifest, version และพรอมป์ต์ทั้งสองชุด

เมื่อแก้กฎ ภาพ หรือเวอร์ชัน ให้ build ใหม่ก่อนตรวจ อย่าแก้สำเนา `plugins/.../skills/` โดยตรง
`npm test` ตรวจความสอดคล้องและพฤติกรรม build/check ไม่ได้ผลิตข่าวจริงหรือรับรองว่ามือถือมีเครื่องมือส่งออกครบ

ก่อน commit ให้ตรวจ diff ของ `.agents/plugins/marketplace.json`, `plugin.manifest.json`, `plugins/`, ต้นฉบับสกิล พรอมป์ต์ และคู่มือ เผยแพร่เฉพาะไฟล์ที่ตั้งใจแชร์ ไม่รวมภาพข่าวใหม่ ข้อมูลส่วนบุคคลหรือข้อมูลภายในโดยอัตโนมัติ
เจ้าของ repo เป็นผู้ commit/push หรืออนุมัติการเผยแพร่ผ่านช่องทางที่ได้รับสิทธิ์ ไม่มีคำสั่ง publish/push ในตัว build

## เพิ่มเวอร์ชัน

เพิ่ม version ให้ตรงกันใน:

- `plugin.manifest.json`
- `package.json` (เฉพาะชุดเครื่องมือผู้ดูแล)
- `pea-newsletter-infographic/SKILL.md`
- พรอมป์ต์ `prompts/newsletter-prompt.th.md` และ `pea-newsletter-infographic/assets/newsletter-prompt.th.md`
- changelog และ validation report

จากนั้น build จะนำ version ใหม่ไปยัง `plugins/pea-newsletter-infographic/plugin.json` และสำเนาสกิล

## นำเข้าใน Workspace เพื่อใช้ข้ามอุปกรณ์

ทำตาม [คู่มือติดตั้ง](install-update.th.md) โดยให้ผู้ดูแลนำเข้า repository marketplace แล้วเชื่อมสาขา `main`
ระบบซิงก์ของ Workspace รับอัปเดตตามรอบหรือเมื่อกด Sync now ผู้ใช้ทำงานด้วยเวอร์ชันที่ระบบซิงก์แล้ว ไม่ใช่ commit ล่าสุดแบบตรวจสดก่อนทุกงาน

## เผยแพร่สาธารณะ

การ push GitHub หรือ import Workspace ไม่เท่ากับเผยแพร่ใน public Plugin directory
ใช้โฟลเดอร์ `plugins/pea-newsletter-infographic/` เป็นแพ็กเริ่มต้น แล้วทำขั้นตอนส่งตรวจและเผยแพร่ตามช่องทางปัจจุบันของ OpenAI รวมข้อมูลผู้เผยแพร่/นโยบายที่ระบบขอ ไม่มีการสร้าง URL นโยบายหรืออ้างว่าได้รับอนุมัติแล้วในชุดนี้

ก่อนเผยแพร่จริง ควรทดลองโหลด Plugin ในบัญชีทดสอบบนเว็บ เดสก์ท็อป และมือถือ ให้ตรวจว่าระบบอ่านไฟล์อ้างอิงได้ และจัดการข้อจำกัดเครื่องมืออย่างตรงไปตรงมา รวมกรณีที่ส่งออก JPG หรือยืนยันฟอนต์ไม่ได้

อ้างอิง: [Package your plugin](https://developers.openai.com/plugins/build/plugins), [Import and sync plugins from GitHub](https://learn.chatgpt.com/docs/enterprise/plugin-management)
