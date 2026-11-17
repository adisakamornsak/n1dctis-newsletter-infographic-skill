import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { ROOT, NAME, REQUIRED, build, check, inventory, validateSource, validateSchema } from '../tools/plugin.mjs';

async function fixture(t) {
  const root = await fs.mkdtemp(path.join(os.tmpdir(), 'pea-plugin-'));
  t.after(() => fs.rm(root, { recursive: true, force: true }));
  for (const file of ['package.json', 'plugin.manifest.json', 'prompts/newsletter-prompt.th.md', '.agents/plugins/marketplace.json']) {
    await fs.mkdir(path.dirname(path.join(root, file)), { recursive: true });
    await fs.copyFile(path.join(ROOT, file), path.join(root, file));
  }
  const source = await validateSource(ROOT);
  for (const rel of source.files.keys()) {
    const dest = path.join(root, NAME, rel);
    await fs.mkdir(path.dirname(dest), { recursive: true });
    await fs.copyFile(path.join(source.skill, rel), dest);
  }
  return root;
}

const read = p => fs.readFile(p, 'utf8');

test('current portable Plugin exactly matches canonical files and version', async () => {
  const result = await check();
  const source = await validateSource();
  assert.equal(result.count, source.files.size + 1);
  for (const rel of REQUIRED) assert(source.files.has(rel));
  assert.equal(result.version, '3.0.0');
});

test('building preserves every asset byte and has no external skill dependency', async t => {
  const root = await fixture(t);
  const output = await build(root);
  const result = await check(root);
  const canonical = await inventory(path.join(root, NAME));
  const packaged = await inventory(path.join(output, 'skills', NAME));
  assert.deepEqual(packaged, canonical);
  assert.equal(result.count, canonical.size + 1);
});

test('build is repeatable and removes stale generated files', async t => {
  const root = await fixture(t);
  const output = await build(root);
  const before = await inventory(output);
  await fs.writeFile(path.join(output, 'retired.md'), 'old');
  await assert.rejects(check(root), /missing or extra/);
  await build(root);
  assert.deepEqual(await inventory(output), before);
  await check(root);
});

test('changed protected logo is detected, and rebuild copies the maintained source', async t => {
  const root = await fixture(t);
  const output = await build(root);
  const rel = 'assets/pea-logo-exact-original.png';
  const original = await fs.readFile(path.join(root, NAME, rel));
  await fs.writeFile(path.join(output, 'skills', NAME, rel), 'tampered');
  await assert.rejects(check(root), /differs from source/);
  await build(root);
  assert.deepEqual(await fs.readFile(path.join(output, 'skills', NAME, rel)), original);
});

test('missing logo fails before replacing an existing build', async t => {
  const root = await fixture(t);
  const output = await build(root);
  const before = await inventory(output);
  await fs.unlink(path.join(root, NAME, 'assets/pea-logo-exact-original.png'));
  await assert.rejects(build(root), /Missing required file/);
  assert.deepEqual(await inventory(output), before);
});

test('source symlinks, fonts and executable runtime files are rejected', async t => {
  const root = await fixture(t);
  const folder = path.join(root, NAME, 'assets');
  const link = path.join(folder, 'linked.md');
  await fs.symlink(path.join(root, 'package.json'), link);
  await assert.rejects(build(root), /Symlink/);
  await fs.unlink(link);
  for (const name of ['font.ttf', 'font.woff2', 'updater.py', 'run.sh', 'code.js']) {
    const file = path.join(folder, name);
    await fs.writeFile(file, 'fixture');
    await assert.rejects(build(root), /Font files|unsupported file/);
    await fs.unlink(file);
  }
});

test('private hidden inputs are omitted from builds', async t => {
  const root = await fixture(t);
  await fs.writeFile(path.join(root, NAME, '.env'), 'NOT FOR DISTRIBUTION');
  const output = await build(root);
  const files = await inventory(output);
  assert(![...files.keys()].some(p => p.endsWith('.env')));
  await check(root);
});

test('prompt mismatch blocks packaging', async t => {
  const root = await fixture(t);
  await fs.appendFile(path.join(root, 'prompts/newsletter-prompt.th.md'), '\nchanged');
  await assert.rejects(build(root), /prompts are out of sync/);
});

test('version mismatch blocks packaging', async t => {
  const root = await fixture(t);
  const p = path.join(root, 'plugin.manifest.json');
  const data = JSON.parse(await read(p));
  data.version = '0.0.0';
  await fs.writeFile(p, JSON.stringify(data));
  await assert.rejects(build(root), /version mismatch/);
});

test('official portable schema rejects unknown fields and wrong data types', async () => {
  const schema = JSON.parse(await read(path.join(ROOT, 'tools/plugin.schema.json')));
  const manifest = JSON.parse(await read(path.join(ROOT, 'plugin.manifest.json')));
  validateSchema(manifest, schema);
  assert.throws(() => validateSchema({ ...manifest, skills: './elsewhere' }, schema), /unknown field/);
  assert.throws(() => validateSchema({ ...manifest, version: 3 }, schema), /expected string/);
  assert.throws(() => validateSchema({ ...manifest, author: { email: 5 } }, schema), /expected string/);
  assert.throws(() => validateSchema({ ...manifest, name: 'Invalid Name' }, schema), /pattern/);
});

test('skills-only Plugin does not accept a mandatory local hook', async t => {
  const root = await fixture(t);
  const p = path.join(root, 'plugin.manifest.json');
  const data = JSON.parse(await read(p));
  data.extensions['com.openai'].hooks = './hooks/hooks.json';
  await fs.writeFile(p, JSON.stringify(data));
  await assert.rejects(build(root), /must not require hooks/);
});

test('marketplace points to the complete tracked portable Plugin', async t => {
  const root = await fixture(t);
  await build(root);
  const p = path.join(root, '.agents/plugins/marketplace.json');
  const data = JSON.parse(await read(p));
  data.plugins[0].source.path = './dist/missing-plugin';
  await fs.writeFile(p, JSON.stringify(data));
  await assert.rejects(check(root), /Wrong marketplace source path/);
});

test('runtime keeps synced-version, capability, protected-copy and single-image contracts', async () => {
  const source = await validateSource();
  const skill = await read(path.join(ROOT, NAME, 'SKILL.md'));
  assert(skill.includes('no per-request online version check is required'));
  assert(skill.includes('Plugin installation alone does not supply these tools or fonts'));
  assert(skill.includes('do not call it a compliant final deliverable'));
  assert(skill.includes('any number of supplied news images, including zero'));
  assert(skill.includes('Never invent a motto without an explicit user request'));
  assert(skill.includes('Google Prompt (Prompt)'));
  assert(skill.includes('1440 × 2560'));
  assert(skill.includes('If omitted, empty, or whitespace-only'));
  assert(skill.includes('แผนกระบบสารสนเทศและความปลอดภัยไซเบอร์'));
  for (let i = 1; i <= 5; i++) assert(skill.includes(`| 0${i} |`));
  const prompt = await read(path.join(ROOT, 'prompts/newsletter-prompt.th.md'));
  assert(prompt.includes('เว้นแต่ฉันสั่งให้แต่งโดยตรง'));
  assert(prompt.includes('ล่าสุดที่ระบบ Plugin ซิงก์แล้ว'));
  assert(!/preflight_update|manage_skill|\.py\b/.test(skill + prompt));
  assert(![...source.files.keys()].some(p => /\.(?:py|sh|js|mjs)$/.test(p)));
});
