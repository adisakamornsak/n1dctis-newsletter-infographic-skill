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

def audit(source: str, final: str) -> list[str]:
    """Check required copy once and missing numeric tokens.

    Extra numbers and factual meaning still require human/visual review.
    """
    errors = []
    for item in REQUIRED:
        count = final.count(item)
        if count != 1:
            errors.append(f'REQUIRED TEXT MUST APPEAR ONCE (found {count}): {item}')
    missing = sorted(set(extract_numbers(source)) - set(extract_numbers(final)))
    if missing:
        errors.append('MISSING NUMERIC TOKENS: ' + ', '.join(missing))
    return errors


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument('--source', required=True)
    p.add_argument('--final', required=True)
    args = p.parse_args()
    try:
        source = Path(args.source).read_text(encoding='utf-8')
        final = Path(args.final).read_text(encoding='utf-8')
    except (OSError, UnicodeError) as exc:
        print(f'ERROR: {exc}')
        return 1
    errors = audit(source, final)
    for error in errors:
        print(error)
    print('audit_copy:', 'FAIL' if errors else 'PASS')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
