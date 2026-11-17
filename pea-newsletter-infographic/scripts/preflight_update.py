#!/usr/bin/env python3
"""Require a fresh main-branch check before every newsletter invocation."""
from __future__ import annotations
import json
from pathlib import Path
import subprocess
import sys


def main() -> int:
    skill = Path(__file__).resolve().parents[1]
    try:
        data = json.loads((skill / '.pea-install.json').read_text(encoding='utf-8'))
        if not isinstance(data, dict) or data.get('schema') != 1:
            raise ValueError('Invalid installation receipt')
        state = Path(data['state_dir'])
        updater = state / 'manage_skill.py'
        if not updater.is_file():
            raise ValueError('Installed updater is missing')
        return subprocess.call([sys.executable, str(updater), '--skills-dir', str(skill.parent),
                                '--state-dir', str(state), 'update'])
    except (OSError, ValueError, KeyError) as exc:
        print(f'ERROR: {exc}\nต้องติดตั้งผ่าน tools/manage_skill.py install ก่อนใช้สกิลนี้ '
              '(ดูคู่มือ docs/install-update.th.md ใน GitHub repository); '
              'ยังยืนยันเวอร์ชันล่าสุดไม่ได้ จึงไม่เริ่มผลิตข่าว', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
