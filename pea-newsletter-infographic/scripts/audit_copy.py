#!/usr/bin/env python3
"""Check required Thai labels and exact numeric strings in final copy."""
from argparse import ArgumentParser
from collections import Counter
from pathlib import Path
import re

REQUIRED=(
'กองเทคโนโลยีดิจิทัลและการสื่อสาร',
'แผนกระบบสารสนเทศและความปลอดภัยไซเบอร์',
'การไฟฟ้าส่วนภูมิภาค เขต 1 ภาคเหนือ (จังหวัดเชียงใหม่)',
)
# Capture literal numeric groups; preserve their written scripts and punctuation.
NUMBERS=re.compile(r'[0-9๐-๙]+(?:[.,:/%-][0-9๐-๙]+)*')

def audit(source: str, final: str):
    errors=[]
    for part in REQUIRED:
        if final.count(part)!=1:
            errors.append(f'Fixed text missing or repeated ({final.count(part)}): {part}')
    original=Counter(NUMBERS.findall(source))
    produced=Counter(NUMBERS.findall(final))
    for token,count in original.items():
        if produced[token] < count:
            errors.append(f'Numeric token changed/omitted: {token!r}; source {count}, final {produced[token]}')
    return errors

if __name__=='__main__':
    parser=ArgumentParser()
    parser.add_argument('--source',required=True,type=Path)
    parser.add_argument('--final',required=True,type=Path)
    a=parser.parse_args()
    errors=audit(a.source.read_text(encoding='utf-8'),a.final.read_text(encoding='utf-8'))
    if errors:
        print('FAIL: ' + str(len(errors)) + ' issue(s)')
        for e in errors: print('- ' + e)
        raise SystemExit(1)
    print('PASS: fixed text once each; all source numeric tokens retained verbatim')
    print('NOTE: manually inspect final raster and image preservation; this audits transcription only')
