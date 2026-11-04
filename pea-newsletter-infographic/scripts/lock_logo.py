#!/usr/bin/env python3
"""Paste unmodified original PEA-logo pixels on a 1086x1536 PNG."""
from argparse import ArgumentParser
from pathlib import Path
from PIL import Image

CANVAS = (1086, 1536)
DEFAULT_POS = (50, 17)

def apply_logo(src: Path, dst: Path, logo_path: Path, pos=DEFAULT_POS):
    page = Image.open(src).convert('RGB')
    if page.size != CANVAS:
        raise ValueError(f'Expected {CANVAS[0]}x{CANVAS[1]} pixels, got {page.size}. Do not resize the logo.')
    logo = Image.open(logo_path).convert('RGB')
    x, y = pos
    if x < 0 or y < 0 or x + logo.width > page.width or y + logo.height > page.height:
        raise ValueError(f'Logo does not fit at {pos} with size {logo.size} on {page.size}')
    page.paste(logo, (x, y))
    dst.parent.mkdir(parents=True, exist_ok=True)
    page.save(dst)
    check = Image.open(dst).convert('RGB').crop((x, y, x + logo.width, y + logo.height))
    if check.tobytes() != logo.tobytes():
        raise RuntimeError('Original logo pixels were not preserved in saved PNG')
    print(f'PASS: exact {logo.width}x{logo.height} logo pixels preserved at {(x, y)}; saved {dst}')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('input_png', type=Path)
    parser.add_argument('output_png', type=Path)
    parser.add_argument('--logo', type=Path,
                        default=Path(__file__).resolve().parent.parent / 'assets/pea-logo-exact-original.png')
    parser.add_argument('--x', type=int, default=DEFAULT_POS[0])
    parser.add_argument('--y', type=int, default=DEFAULT_POS[1])
    args = parser.parse_args()
    apply_logo(args.input_png, args.output_png, args.logo, (args.x, args.y))
