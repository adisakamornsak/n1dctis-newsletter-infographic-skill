#!/usr/bin/env python3
"""Check a final 1440x2560 portrait PNG without modifying or resizing it."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

from PIL import Image, UnidentifiedImageError

CANVAS = (1440, 2560)  # width, height; portrait 9:16


def validate_output(path: Path) -> tuple[int, int]:
    """Require valid PNG bytes, exact dimensions, one frame and no EXIF rotation.

    This checks geometry only, not fonts, wording, photo completeness or branding.
    """
    path = Path(path)
    if not path.is_file():
        raise ValueError(f'Output file does not exist: {path}')
    try:
        with Image.open(path) as image:
            if image.format != 'PNG':
                raise ValueError('Output must contain PNG data, regardless of filename')
            if image.size != CANVAS:
                raise ValueError(f'Expected {CANVAS[0]}x{CANVAS[1]} px (width x height), got {image.size}')
            if getattr(image, 'n_frames', 1) != 1:
                raise ValueError('Output must be a single-frame static PNG')
            if image.getexif().get(274, 1) != 1:
                raise ValueError('Output must not rely on EXIF rotation or mirroring')
            image.load()
        # Reopen for PNG structural/CRC verification after decoding.
        with Image.open(path) as image:
            image.verify()
    except (OSError, SyntaxError, UnidentifiedImageError) as exc:
        raise ValueError(f'Unreadable or corrupt PNG: {path}') from exc
    return CANVAS


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output_png', type=Path)
    args = parser.parse_args()
    try:
        width, height = validate_output(args.output_png)
    except (OSError, ValueError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        return 1
    print(f'PASS: one static PNG, {width}x{height} px, portrait 9:16; geometry only')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
