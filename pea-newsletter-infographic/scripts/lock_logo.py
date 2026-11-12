#!/usr/bin/env python3
from __future__ import annotations
import argparse
from PIL import Image

TARGET = (1440, 2560)

def main() -> int:
    p = argparse.ArgumentParser(description='Paste an exact logo onto a fixed 1440x2560 canvas without scaling the logo.')
    p.add_argument('input')
    p.add_argument('output')
    p.add_argument('--logo', required=True)
    p.add_argument('--x', type=int, default=60)
    p.add_argument('--y', type=int, default=60)
    args = p.parse_args()
    base = Image.open(args.input).convert('RGB')
    if base.size != TARGET:
        raise SystemExit(f'Input image must be {TARGET[0]}x{TARGET[1]}')
    logo = Image.open(args.logo).convert('RGBA')
    base_rgba = base.convert('RGBA')
    base_rgba.alpha_composite(logo, (args.x, args.y))
    out = base_rgba.convert('RGB')
    out.save(args.output, format='JPEG', quality=92, optimize=True)
    print(f'Wrote {args.output}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
