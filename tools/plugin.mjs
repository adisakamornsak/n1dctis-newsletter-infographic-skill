/** Maintainer-only packaging. Nothing here runs when a user invokes the Plugin. */
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';

export const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
export const NAME = 'pea-newsletter-infographic';
export const REQUIRED = [
  'SKILL.md', 'agents/openai.yaml', 'references/CHANGELOG.md',
  'references/content-contract.md', 'references/layout-catalog.md',
  'references/quality-checklist.md', 'references/mascot-background-rules.md',
  'references/approved-photo-grid.md', 'references/single-image-layout.md',
  'assets/content-input-example.md', 'assets/newsletter-prompt.th.md',
  'assets/pea-logo-exact-original.png', 'assets/approved-layout-reference.jpg',
  'assets/approved-photo-grid-reference.jpg', 'assets/layout-01-chiang-mai-classic.jpg',
  'assets/layout-02-digital-operations.jpg', 'assets/layout-03-cyber-shield.jpg',
  'assets/layout-04-enterprise-analytics.jpg', 'assets/layout-05-cyber-ops-infrastructure.jpg',
  'assets/watt-d/35-speed-running-transparent-approved.png',
  'assets/watt-d/35.SpeedRunning.png',
];
const allowed = new Set(['.md', '.txt', '.yaml', '.yml', '.json', '.png', '.jpg', '.jpeg', '.webp', '.svg']);
const fonts = new Set(['.ttf', '.otf', '.ttc', '.woff', '.woff2', '.eot']);
const excluded = new Set(['__pycache__', '.DS_Store', 'Thumbs.db']);
const sha = bytes => createHash('sha256').update(bytes).digest('hex');
function assert(ok, message) { if (!ok) throw new Error(message); }

// Implements every validation keyword used by the vendored official 1.0.0 schema.
export function validateSchema(value, schema, label = 'plugin.json') {
  if ('const' in schema) assert(value === schema.const, label + ': wrong constant');
  if (schema.type) {
    const actual = Array.isArray(value) ? 'array' : value === null ? 'null' : typeof value;
    assert(actual === schema.type, label + ': expected ' + schema.type);
  }
  if (typeof value === 'string') {
    if (schema.minLength !== undefined) assert([...value].length >= schema.minLength, label + ': too short');
    if (schema.maxLength !== undefined) assert([...value].length <= schema.maxLength, label + ': too long');
    if (schema.pattern) assert(new RegExp(schema.pattern).test(value), label + ': invalid pattern');
  }
  if (Array.isArray(value) && schema.items) value.forEach((item, i) => validateSchema(item, schema.items, label + '[' + i + ']'));
  if (value && typeof value === 'object' && !Array.isArray(value)) {
    for (const key of schema.required ?? []) assert(Object.hasOwn(value, key), label + ': missing ' + key);
    for (const [key, child] of Object.entries(value)) {
      if (schema.properties?.[key]) validateSchema(child, schema.properties[key], label + '.' + key);
      else if (schema.additionalProperties === false) throw new Error(label + ': unknown field ' + key);
      else if (typeof schema.additionalProperties === 'object') validateSchema(child, schema.additionalProperties, label + '.' + key);
    }
  }
}

export async function inventory(root, { ignoreHidden = false } = {}) {
  assert(!(await fs.lstat(root)).isSymbolicLink(), `Symlink root: ${root}`);
  const files = new Map();
  async function walk(folder, relative = '') {
    for (const entry of await fs.readdir(folder, { withFileTypes: true })) {
      const rel = path.posix.join(relative, entry.name);
      assert(!entry.isSymbolicLink(), `Symlink is not allowed: ${rel}`);
      if (ignoreHidden && (entry.name.startsWith('.') || excluded.has(entry.name))) continue;
      if (entry.isDirectory()) await walk(path.join(folder, entry.name), rel);
      else {
        assert(entry.isFile(), `Special file: ${rel}`);
        const suffix = path.extname(entry.name).toLowerCase();
        assert(!fonts.has(suffix), `Font files must not be distributed: ${rel}`);
        assert(allowed.has(suffix), `Runtime or unsupported file is not allowed: ${rel}`);
        files.set(rel, sha(await fs.readFile(path.join(root, rel))));
      }
    }
  }
  await walk(root);
  return files;
}

export async function validateSource(root = ROOT) {
  const skill = path.join(root, NAME);
  const files = await inventory(skill, { ignoreHidden: true });
  for (const rel of REQUIRED) assert(files.has(rel), `Missing required file: ${rel}`);
  const text = await fs.readFile(path.join(skill, 'SKILL.md'), 'utf8');
  assert(new RegExp(`^---\\r?\\nname: ${NAME}\\r?\\ndescription: .+\\r?\\n---`, 'u').test(text), 'Invalid skill frontmatter');
  const version = text.match(/team edition v(\d+\.\d+\.\d+)/)?.[1];
  assert(version, 'Missing skill version');
  const manifest = JSON.parse(await fs.readFile(path.join(root, 'plugin.manifest.json'), 'utf8'));
  validateSchema(manifest, JSON.parse(await fs.readFile(path.join(ROOT, 'tools/plugin.schema.json'), 'utf8')));
  assert(manifest.name === NAME && manifest.version === version, 'Manifest/skill version mismatch');
  const openai = manifest.extensions?.['com.openai'] ?? {};
  assert(!('hooks' in openai) && !('apps' in openai), 'Skills-only Plugin must not require hooks or apps');
  const bundledPrompt = await fs.readFile(path.join(skill, 'assets/newsletter-prompt.th.md'), 'utf8');
  assert(bundledPrompt === await fs.readFile(path.join(root, 'prompts/newsletter-prompt.th.md'), 'utf8'), 'Thai prompts are out of sync');
  assert(bundledPrompt.includes(`v${version}`), 'Prompt version mismatch');
  const pkg = JSON.parse(await fs.readFile(path.join(root, 'package.json'), 'utf8'));
  assert(pkg.version === version, 'Maintainer package version mismatch');
  // Packaged Markdown references must resolve inside the skill. No external source dependency.
  for (const rel of files.keys()) {
    if (!rel.endsWith('.md')) continue;
    const md = await fs.readFile(path.join(skill, rel), 'utf8');
    for (const match of md.matchAll(/\]\(([^)]+)\)/g)) {
      const link = match[1];
      if (/^(?:https?:|#)/.test(link)) continue;
      const resolved = path.resolve(skill, path.dirname(rel), link.split('#')[0]);
      assert(resolved.startsWith(skill + path.sep), `Link leaves packaged skill: ${rel}: ${link}`);
      await fs.access(resolved);
    }
  }
  return { files, manifest, skill };
}

export async function build(root = ROOT) {
  const source = await validateSource(root);
  const parent = path.join(root, 'plugins');
  await fs.mkdir(parent, { recursive: true });
  const output = path.join(parent, NAME);
  const staging = await fs.mkdtemp(path.join(parent, '.pea-build-'));
  const previous = staging + '-previous';
  let moved = false;
  try {
    for (const rel of source.files.keys()) {
      const dest = path.join(staging, 'skills', NAME, rel);
      await fs.mkdir(path.dirname(dest), { recursive: true });
      await fs.copyFile(path.join(source.skill, rel), dest);
    }
    await fs.writeFile(path.join(staging, 'plugin.json'), JSON.stringify(source.manifest, null, 2) + '\n');
    try {
      const stat = await fs.lstat(output);
      assert(stat.isDirectory() && !stat.isSymbolicLink(), 'Generated Plugin destination must be a directory');
      assert((await fs.readFile(path.join(output, 'plugin.json'), 'utf8')).includes(`"${NAME}"`), 'Refusing to replace an unrecognized directory');
      await fs.rename(output, previous);
      moved = true;
    } catch (error) { if (error.code !== 'ENOENT') throw error; }
    try { await fs.rename(staging, output); }
    catch (error) { if (moved) await fs.rename(previous, output); throw error; }
    if (moved) await fs.rm(previous, { recursive: true });
    return output;
  } finally { await fs.rm(staging, { recursive: true, force: true }); }
}

export async function check(root = ROOT) {
  const source = await validateSource(root);
  const output = path.join(root, 'plugins', NAME);
  const files = await inventory(output);
  const expected = new Map([...source.files].map(([p, hash]) => [`skills/${NAME}/${p}`, hash]));
  const manifestBytes = await fs.readFile(path.join(root, 'plugin.manifest.json'));
  const manifest = JSON.parse(manifestBytes);
  expected.set('plugin.json', sha(Buffer.from(JSON.stringify(manifest, null, 2) + '\n')));
  assert(files.size === expected.size, 'Generated Plugin has missing or extra files; rebuild it');
  for (const [p, hash] of expected) assert(files.get(p) === hash, `Generated Plugin differs from source: ${p}`);
  const market = JSON.parse(await fs.readFile(path.join(root, '.agents/plugins/marketplace.json'), 'utf8'));
  const entries = market.plugins?.filter(p => p.name === NAME) ?? [];
  assert(entries.length === 1, 'Marketplace must include this Plugin once');
  assert(entries[0].source.source === 'local' && entries[0].source.path === `./plugins/${NAME}`, 'Wrong marketplace source path');
  assert(entries[0].policy.installation === 'AVAILABLE' && entries[0].category === 'Productivity', 'Missing marketplace policy/category');
  return { output, count: files.size, version: source.manifest.version };
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    if (process.argv[2] === 'build') console.log('Built portable Plugin:', await build());
    else if (process.argv[2] === 'check') console.log('Plugin check PASS:', await check());
    else throw new Error('Usage: node tools/plugin.mjs build|check');
  } catch (error) { console.error('ERROR:', error.message); process.exitCode = 1; }
}
