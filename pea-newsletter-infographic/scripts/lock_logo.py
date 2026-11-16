#!/usr/bin/env python3
from __future__ import annotations
import argparse
import math
from PIL import Image

TARGET = (1440, 2560)

def main() -> int:
    p = argparse.ArgumentParser(description='Place the original logo on a fixed 1440x2560 canvas; optional proportional downscaling only.')
    p.add_argument('input')
    p.add_argument('output')
    p.add_argument('--logo', required=True)
    p.add_argument('--x', type=int, default=60)
    p.add_argument('--y', type=int, default=60)
    p.add_argument('--scale', type=float, default=1.0, help='Uniform logo scale: 0 < scale <= 1; default keeps original size.')
    args = p.parse_args()
    if not math.isfinite(args.scale) or not 0 < args.scale <= 1:
        p.error('--scale must be finite and greater than 0 and at most 1')
    base = Image.open(args.input).convert('RGB')
    if base.size != TARGET:
        raise SystemExit(f'Input image must be {TARGET[0]}x{TARGET[1]}')
    logo = Image.open(args.logo).convert('RGBA')
    if args.scale < 1:
        size = (round(logo.width * args.scale), round(logo.height * args.scale))
        if min(size) < 1:
            p.error('--scale makes the logo smaller than one pixel')
        logo = logo.resize(size, Image.Resampling.LANCZOS)
    if args.x < 0 or args.y < 0 or args.x + logo.width > base.width or args.y + logo.height > base.height:
        p.error('The complete logo must fit within the canvas; cropping is not allowed')
    base_rgba = base.convert('RGBA')
    base_rgba.alpha_composite(logo, (args.x, args.y))
    out = base_rgba.convert('RGB')
    out.save(args.output, format='JPEG', quality=92, optimize=True)
    print(f'Wrote {args.output}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
