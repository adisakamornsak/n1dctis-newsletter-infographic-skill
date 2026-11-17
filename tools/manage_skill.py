#!/usr/bin/env python3
"""Install/update PEA from GitHub; run Codex only after a successful fresh check."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import uuid

try:
    from .package_skill import collect_files
except ImportError:
    from package_skill import collect_files

NAME = 'pea-newsletter-infographic'
REPO = 'https://github.com/adisakamornsak/n1dctis-newsletter-infographic-skill.git'
RECEIPT = '.pea-install.json'
BRANCH = 'main'


def default_skills_dir() -> Path:
    modern = Path.home() / '.agents/skills'
    legacy = Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'skills'
    if (modern / NAME).exists() and (legacy / NAME).exists() and modern != legacy:
        raise ValueError('พบสกิลซ้ำใน .agents และ .codex; ระบุ --skills-dir และจัดการสำเนาซ้ำก่อนใช้')
    return legacy if (legacy / NAME).exists() else modern


def command(args: list[str], *, timeout: int = 60) -> str:
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0')
    result = subprocess.run(args, capture_output=True, text=True, env=env, timeout=timeout)
    if result.returncode:
        raise RuntimeError(f'คำสั่งล้มเหลว: {args[0]}\n{result.stderr.strip()}')
    return result.stdout.strip()


def inventory(root: Path) -> dict[str, str]:
    result = {}
    for p in root.rglob('*'):
        rel = p.relative_to(root)
        if p.is_symlink():
            raise ValueError(f'ไม่รองรับ symlink ในชุดติดตั้ง: {rel}')
        if '__pycache__' in rel.parts or p.name == '.DS_Store':
            continue
        if p.is_file() and rel.as_posix() != RECEIPT:
            result[rel.as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def receipt(target: Path) -> dict:
    data = json.loads((target / RECEIPT).read_text(encoding='utf-8'))
    if not isinstance(data, dict) or data.get('schema') != 1 or not isinstance(data.get('files'), dict):
        raise ValueError('ข้อมูลการติดตั้งไม่ถูกต้อง; ใช้ install --replace-existing เพื่อสำรองและติดตั้งใหม่')
    return data


@contextmanager
def update_lock(state: Path):
    state.mkdir(parents=True, exist_ok=True)
    lock = state / '.update.lock'
    try:
        lock.mkdir()
    except FileExistsError:
        raise RuntimeError(f'มีการอัปเดตอื่นทำงานอยู่; ถ้าหยุดไปแล้วให้ตรวจและลบ {lock}') from None
    try:
        yield
    finally:
        lock.rmdir()


def bootstrap(state: Path) -> None:
    """Persist this reviewed installer, without executing downloaded repo code."""
    for name in ('manage_skill.py', 'package_skill.py'):
        source = Path(__file__).resolve().with_name(name)
        dest = state / name
        if source == dest:
            continue
        pending = state / (name + '.new')
        shutil.copyfile(source, pending)
        pending.replace(dest)


def fetch_skill(repo: str, state: Path, staging: Path) -> tuple[Path, str]:
    cache = state / 'repository.git'
    if cache.is_symlink():
        raise ValueError('Git cache must not be a symlink')
    if not cache.exists():
        command(['git', 'init', '--bare', str(cache)])
    git = ['git', '-c', 'core.hooksPath=/dev/null', '--git-dir', str(cache)]
    command(git + ['fetch', '--depth=1', '--no-tags', '--', repo, BRANCH])
    commit = command(git + ['rev-parse', '--verify', 'FETCH_HEAD^{commit}'])
    archive = staging / 'download.tar'
    command(git + ['archive', '--format=tar', '--output', str(archive), commit, NAME])
    with tarfile.open(archive) as tar:
        for member in tar:
            path = PurePosixPath(member.name)
            if path.is_absolute() or '..' in path.parts or not path.parts or path.parts[0] != NAME:
                raise ValueError('Unsafe archive path')
            destination = staging.joinpath(*path.parts)
            if member.isdir():
                destination.mkdir(parents=True, exist_ok=True)
            elif member.isfile():
                destination.parent.mkdir(parents=True, exist_ok=True)
                with tar.extractfile(member) as src, destination.open('wb') as dst:
                    shutil.copyfileobj(src, dst)
            else:
                raise ValueError('Archive links and special files are not allowed')
    root = (staging / NAME).resolve()
    # Reuse packaging policy; remove excluded files instead of installing them.
    allowed = set(collect_files(root))
    if not (root / 'scripts/preflight_update.py').is_file():
        raise ValueError('สาขา main ยังไม่มีตัวตรวจอัปเดตก่อนใช้งาน; ให้เจ้าของ repo เผยแพร่เวอร์ชันนี้ก่อน')
    for p in root.rglob('*'):
        if p.is_file() and p not in allowed:
            p.unlink()
    return root, commit


def synchronize(skills_dir: Path, state_dir: Path, *, repo: str | None = None,
                installing: bool = False, replace_existing: bool = False) -> dict:
    skills_dir, state_dir = skills_dir.expanduser().absolute(), state_dir.expanduser().absolute()
    if skills_dir.is_symlink() or state_dir.is_symlink():
        raise ValueError('Installation/state directories must not be symlinks')
    skills_dir, state_dir = skills_dir.resolve(), state_dir.resolve()
    target = skills_dir / NAME
    if target.is_symlink():
        raise ValueError('สกิลเดิมเป็น symlink; สำรองและนำลิงก์ออกก่อนติดตั้ง')
    if target.exists() and not target.is_dir():
        raise ValueError('Skill destination is not a directory')
    if state_dir == skills_dir or state_dir.is_relative_to(skills_dir):
        raise ValueError('Keep state directory outside the skills directory')
    skills_dir.mkdir(parents=True, exist_ok=True)
    with update_lock(state_dir):
        old = None
        previous_files = None
        if target.exists():
            if (target / RECEIPT).is_file():
                old = receipt(target)
                previous_files = inventory(target)
                if previous_files != old['files'] and not replace_existing:
                    raise ValueError('ไฟล์สกิลถูกแก้ในเครื่อง; หยุดเพื่อรักษาไฟล์เดิม ใช้ install --replace-existing เพื่อสำรองก่อนแทนที่')
                if Path(old['state_dir']) != state_dir:
                    raise ValueError('Use the same --state-dir as the installed copy')
            elif not (installing and replace_existing):
                raise ValueError('มีสกิลเดิมที่ไม่ได้ติดตั้งด้วยเครื่องมือนี้; ใช้ install --replace-existing เพื่อสำรองก่อนแทนที่')
        elif not installing:
            raise ValueError('ยังไม่ได้ติดตั้ง; เรียก install ก่อน')
        selected_repo = repo or (old['repo'] if old else REPO)
        if old and selected_repo != old['repo']:
            raise ValueError('แหล่งอัปเดตไม่ตรงกับการติดตั้งเดิม')
        with tempfile.TemporaryDirectory(prefix='.pea-stage-', dir=skills_dir.parent) as folder:
            candidate, commit = fetch_skill(selected_repo, state_dir, Path(folder))
            text = (candidate / 'SKILL.md').read_text(encoding='utf-8')
            match = re.search(r'team edition (v\d+\.\d+\.\d+)', text)
            if not match:
                raise ValueError('Missing skill version')
            files = inventory(candidate)
            if installing:
                bootstrap(state_dir)
            if not (state_dir / 'manage_skill.py').is_file():
                raise ValueError('ตัวอัปเดตหายไป; ติดตั้งใหม่ด้วย install')
            data = dict(schema=1, repo=selected_repo, branch=BRANCH, commit=commit,
                        version=match.group(1), state_dir=str(state_dir),
                        checked_at=datetime.now(timezone.utc).isoformat(), files=files)
            (candidate / RECEIPT).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            backup = None
            if target.exists():
                backup_dir = skills_dir.parent / 'pea-newsletter-backups'
                backup_dir.mkdir(parents=True, exist_ok=True)
                backup = backup_dir / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S') + '-' + uuid.uuid4().hex[:8])
                # Same filesystem as the destination; a failed replacement can roll back.
                target.rename(backup)
            try:
                candidate.rename(target)
            except OSError:
                if backup:
                    backup.rename(target)
                raise
            # Avoid accumulating an identical backup on each fresh online check.
            if backup and old and previous_files == files and old['commit'] == commit:
                shutil.rmtree(backup)
                backup = None
            print(f'ตรวจ main สำเร็จ: {data["version"]} ({commit[:12]})', flush=True)
            print(f'Skill: {target}', flush=True)
            if backup:
                print(f'สำรองเวอร์ชันเดิม: {backup}', flush=True)
            return data


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skills-dir', type=Path)
    parser.add_argument('--state-dir', type=Path, default=Path.home() / '.local/share/pea-newsletter')
    parser.add_argument('--repo', help='Override source for an explicitly selected fork; default: official GitHub repo')
    sub = parser.add_subparsers(dest='action', required=True)
    install = sub.add_parser('install', help='Install and persist the updater')
    install.add_argument('--replace-existing', action='store_true', help='Back up an existing/modified copy before replacing it')
    sub.add_parser('update', help='Fetch main and update; stop on network failure or local edits')
    sub.add_parser('status', help='Show local version; does not check GitHub')
    run = sub.add_parser('run', help='Update first, then start a new Codex CLI session')
    run.add_argument('--prompt', default='', help='Initial newsletter request')
    run.add_argument('--image', action='append', default=[], type=Path, help='News image; repeat for every image')
    run.add_argument('--codex', default='codex', help='Codex CLI executable')
    args = parser.parse_args(argv)
    try:
        skills_dir = args.skills_dir or default_skills_dir()
        if args.action == 'status':
            data = receipt(skills_dir / NAME)
            print(f'{data["version"]} ({data["commit"][:12]}) — ข้อมูลในเครื่อง ไม่ใช่การตรวจ GitHub')
            return 0
        synchronize(skills_dir, args.state_dir, repo=args.repo,
                    installing=args.action == 'install',
                    replace_existing=getattr(args, 'replace_existing', False))
        if args.action == 'run':
            cmd = [args.codex]
            for image in args.image:
                cmd += ['--image', str(image)]
            cmd.append('$' + NAME + '\n' + args.prompt)
            return subprocess.call(cmd)
        return 0
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError, tarfile.TarError, KeyError) as exc:
        print(f'ERROR: {exc}\nหยุดการทำงาน กรุณาแก้ข้อผิดพลาดข้างต้นก่อนเริ่มใช้งานสกิล', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
