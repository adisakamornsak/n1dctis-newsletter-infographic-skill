#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
import sys
from PIL import Image

TARGET = (1440, 2560)
ORIENTATION_TAG = 274


def validate_output(path: str | Path) -> tuple[int, int]:
    """Decode and validate a final RGB JPEG without modifying its bytes.

    Raises ValueError for invalid output or unreadable files. This checks the
    export contract, not text accuracy, branding or visual quality.
    """
    path = Path(path)
    if path.suffix.lower() not in {'.jpg', '.jpeg'}:
        raise ValueError('expected a .jpg or .jpeg filename')
    try:
        with Image.open(path) as img:
            if img.format != 'JPEG':
                raise ValueError(f'expected JPEG, got {img.format!r}')
            if img.size != TARGET:
                raise ValueError(f'expected {TARGET[0]}x{TARGET[1]}, got {img.width}x{img.height}')
            if getattr(img, 'n_frames', 1) != 1:
                raise ValueError('expected single frame')
            if img.mode != 'RGB':
                raise ValueError(f'expected RGB, got {img.mode!r}')
            orientation = img.getexif().get(ORIENTATION_TAG, 1)
            if orientation not in (1, None):
                raise ValueError(f'unsupported EXIF orientation {orientation}')
            img.load()  # Opening only the header can miss truncated image data.
            return img.size
    except (OSError, SyntaxError) as exc:
        raise ValueError(f'cannot read image: {exc}') from exc


def main() -> int:
    parser = argparse.ArgumentParser(description='Validate final newsletter JPEG output.')
    parser.add_argument('image')
    args = parser.parse_args()
    try:
        validate_output(args.image)
    except ValueError as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    print('validate_output: PASS')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
