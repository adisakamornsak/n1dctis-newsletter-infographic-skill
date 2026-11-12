#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
import re

REQUIRED = [
    'กองเทคโนโลยีดิจิทัลและการสื่อสาร',
    'แผนกระบบสารสนเทศและความปลอดภัยไซเบอร์',
    'การไฟฟ้าส่วนภูมิภาค เขต 1 ภาคเหนือ (จังหวัดเชียงใหม่)',
]

def extract_numbers(text: str) -> list[str]:
    return re.findall(r'[0-9๐-๙][0-9๐-๙,./:-]*', text)

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument('--source', required=True)
    p.add_argument('--final', required=True)
    args = p.parse_args()
    source = Path(args.source).read_text(encoding='utf-8')
    final = Path(args.final).read_text(encoding='utf-8')
    ok = True
    for item in REQUIRED:
        if item not in final:
            print(f'MISSING REQUIRED TEXT: {item}')
            ok = False
    source_nums = set(extract_numbers(source))
    final_nums = set(extract_numbers(final))
    missing_nums = sorted(x for x in source_nums if x not in final_nums)
    if missing_nums:
        print('MISSING NUMERIC TOKENS:', ', '.join(missing_nums[:50]))
        ok = False
    print('audit_copy:', 'PASS' if ok else 'FAIL')
    return 0 if ok else 1

if __name__ == '__main__':
    raise SystemExit(main())
