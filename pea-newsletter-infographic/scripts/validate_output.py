#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
import sys
from PIL import Image

TARGET = (1440, 2560)
ORIENTATION_TAG = 274

def fail(msg: str) -> int:
    print(f'ERROR: {msg}', file=sys.stderr)
    return 1

def main() -> int:
    p = argparse.ArgumentParser(description='Validate final newsletter JPEG output.')
    p.add_argument('image')
    args = p.parse_args()
    path = Path(args.image)
    if not path.is_file():
        return fail('file not found')
    try:
        img = Image.open(path)
    except Exception as exc:
        return fail(f'cannot open image: {exc}')
    if img.format != 'JPEG':
        return fail(f'expected JPEG, got {img.format!r}')
    if img.size != TARGET:
        return fail(f'expected {TARGET[0]}x{TARGET[1]}, got {img.size[0]}x{img.size[1]}')
    n_frames = getattr(img, 'n_frames', 1)
    if n_frames != 1:
        return fail(f'expected single frame, got {n_frames}')
    exif = img.getexif()
    orientation = exif.get(ORIENTATION_TAG, 1) if exif else 1
    if orientation not in (1, None):
        return fail(f'unsupported EXIF orientation {orientation}')
    print('validate_output: PASS')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
