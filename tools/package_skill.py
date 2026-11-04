#!/usr/bin/env python3
"""Package current local skill assets; no downloads, Git writes or font bundles."""
from __future__ import annotations
import argparse
from pathlib import Path
import re
import sys
import zipfile

ASSET_NAMES = (
    'approved-layout-reference.png', 'original-newsletter-reference.png',
    'layout-02-digital-operations.png', 'layout-03-cyber-shield.png',
    'layout-04-enterprise-analytics.png', 'layout-05-cyber-ops-infrastructure.png',
    'pea-logo-exact-original.png',
)
REQUIRED = (
    'SKILL.md', 'agents/openai.yaml',
    'references/CHANGELOG.md', 'references/content-contract.md',
    'references/layout-catalog.md', 'references/mascot-background-rules.md',
    'references/quality-checklist.md', 'references/single-image-layout.md',
    'assets/content-input-example.md', 'assets/newsletter-prompt.th.md',
    'scripts/audit_copy.py', 'scripts/lock_logo.py', 'scripts/validate_output.py',
) + tuple('assets/' + name for name in ASSET_NAMES)
FONT_EXTENSIONS = {'.ttf', '.otf', '.ttc', '.woff', '.woff2', '.eot'}
ALLOWED_EXTENSIONS = {'.md', '.txt', '.py', '.yaml', '.yml', '.json', '.png', '.jpg', '.jpeg', '.svg', '.webp'}
EXCLUDED_DIRS = {'__pycache__', '.git', '.venv', 'venv', 'private-inputs', 'outputs', 'output', 'dist'}


def collect_files(skill_folder: Path) -> list[Path]:
    if skill_folder.is_symlink():
        raise ValueError('Skill root must not be a symbolic link')
    root = skill_folder.resolve()
    if not root.is_dir():
        raise ValueError(f'No skill folder: {root}')
    missing = [name for name in REQUIRED if not (root / name).is_file()]
    if missing:
        raise ValueError('Missing required files; keep current repository assets: ' + ', '.join(missing))
    text = (root / 'SKILL.md').read_text(encoding='utf-8')
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    if match is None:
        raise ValueError('SKILL.md requires YAML frontmatter')
    name_match = re.search(r'^name:\s*([a-z0-9-]+)\s*$', match.group(1), re.M)
    if not name_match or name_match.group(1) != root.name:
        raise ValueError('Frontmatter name must match the lowercase skill folder name')
    if not re.search(r'^description:\s*\S', match.group(1), re.M):
        raise ValueError('Frontmatter description is missing')
    files = []
    for path in sorted(root.rglob('*')):
        relative = path.relative_to(root)
        if path.is_symlink():
            raise ValueError(f'Symbolic link not packaged: {relative}')
        if any(part in EXCLUDED_DIRS or part.startswith('.') for part in relative.parts):
            continue
        if not path.is_file():
            continue
        suffix = path.suffix.lower()
        if suffix in FONT_EXTENSIONS:
            raise ValueError(f'Font files must not be distributed: {relative}')
        if suffix in {'.pyc', '.pyo'}:
            continue
        if suffix not in ALLOWED_EXTENSIONS:
            raise ValueError(f'Unexpected file type; review before sharing: {relative}')
        files.append(path)
    return files


def package_skill(skill_folder: Path, output: Path, *, overwrite: bool = False) -> Path:
    root = skill_folder.resolve()
    destination = output.resolve()
    if destination.name != 'skill.zip':
        raise ValueError('Output filename must be skill.zip')
    if destination.is_relative_to(root):
        raise ValueError('Place the ZIP outside the skill folder')
    files = collect_files(skill_folder)
    if destination.exists() and not overwrite:
        raise FileExistsError(f'Output exists: {destination}; pass --force to replace it')
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Source files are read unchanged. No substitutions for a missing logo.
    mode = 'w' if overwrite else 'x'
    with zipfile.ZipFile(destination, mode, compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, (Path(root.name) / path.relative_to(root)).as_posix())
    with zipfile.ZipFile(destination) as archive:
        bad = archive.testzip()
        if bad:
            raise RuntimeError(f'Archive checksum failed: {bad}')
    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skill-folder', type=Path, default=Path(__file__).resolve().parents[1] / 'pea-newsletter-infographic')
    parser.add_argument('--output', type=Path, default=Path('dist/skill.zip'))
    parser.add_argument('--force', action='store_true', help='Replace an existing output archive')
    args = parser.parse_args()
    try:
        result = package_skill(args.skill_folder, args.output, overwrite=args.force)
    except (OSError, ValueError, RuntimeError, zipfile.BadZipFile) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    print(f'Packaged current local skill files: {result}')
    print('This validates packaging, not final artwork, font identity or AI behavior.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
