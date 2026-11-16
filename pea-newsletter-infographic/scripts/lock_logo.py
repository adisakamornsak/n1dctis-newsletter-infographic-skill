#!/usr/bin/env python3
from __future__ import annotations
import argparse
import math
from pathlib import Path
from PIL import Image

TARGET = (1440, 2560)
DEFAULT_POS = (60, 60)


def apply_logo(input_path, output_path, logo_path, position=DEFAULT_POS, *, scale=1.0):
    """Composite a complete proportionally scaled logo and export RGB JPEG."""
    if not math.isfinite(scale) or not 0 < scale <= 1:
        raise ValueError('--scale must be finite and greater than 0 and at most 1')
    destination = Path(output_path)
    if destination.suffix.lower() not in {'.jpg', '.jpeg'}:
        raise ValueError('Output filename must end in .jpg or .jpeg')
    if destination.resolve() in {Path(input_path).resolve(), Path(logo_path).resolve()}:
        raise ValueError('Output must not overwrite a source image')
    with Image.open(input_path) as source:
        if source.size != TARGET:
            raise ValueError(f'Input image must be {TARGET[0]}x{TARGET[1]}')
        base = source.convert('RGBA')
    with Image.open(logo_path) as source:
        logo = source.convert('RGBA')
    if scale < 1:
        size = (round(logo.width * scale), round(logo.height * scale))
        if min(size) < 1:
            raise ValueError('--scale makes the logo smaller than one pixel')
        logo = logo.resize(size, Image.Resampling.LANCZOS)
    x, y = position
    if x < 0 or y < 0 or x + logo.width > base.width or y + logo.height > base.height:
        raise ValueError('The complete logo must fit within the canvas; cropping is not allowed')
    base.alpha_composite(logo, (x, y))
    base.convert('RGB').save(destination, format='JPEG', quality=92, optimize=True)


def main() -> int:
    parser = argparse.ArgumentParser(description='Place the original logo on a fixed 1440x2560 canvas; optional proportional downscaling only.')
    parser.add_argument('input')
    parser.add_argument('output')
    parser.add_argument('--logo', required=True)
    parser.add_argument('--x', type=int, default=DEFAULT_POS[0])
    parser.add_argument('--y', type=int, default=DEFAULT_POS[1])
    parser.add_argument('--scale', type=float, default=1.0, help='Uniform logo scale: 0 < scale <= 1; default keeps original size.')
    args = parser.parse_args()
    try:
        apply_logo(args.input, args.output, args.logo, (args.x, args.y), scale=args.scale)
    except (OSError, ValueError) as exc:
        parser.exit(1, f'ERROR: {exc}\n')
    print(f'Wrote {args.output}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
