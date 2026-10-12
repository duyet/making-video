#!/usr/bin/env python3
"""Map downloaded Flow images (e.g. 2K upscales) back to reference images (e.g. 1K shots
named by shot id) with a perceptual difference hash (dHash).

Usage: python3 flow_match.py <downloads_dir> <reference_dir> [--max 10] [--rename]
  Prints: <download>  ->  <best reference>  dist=<hamming>  (second best for ambiguity)
  --rename  copies each confident match to <downloads_dir>/matched/<ref_stem><ext>
Distance on a 64-bit hash: 0-5 same image, 6-10 likely same, >12 different.
"""
import argparse
import os
import shutil
import sys

from PIL import Image

EXTS = {".jpg", ".jpeg", ".png", ".webp"}


def dhash(path, size=8):
    img = Image.open(path).convert("L").resize((size + 1, size), Image.LANCZOS)
    px = img.tobytes()
    bits = 0
    for row in range(size):
        for col in range(size):
            left = px[row * (size + 1) + col]
            right = px[row * (size + 1) + col + 1]
            bits = (bits << 1) | (left > right)
    return bits


def images(folder):
    return sorted(
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if os.path.splitext(f)[1].lower() in EXTS
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("downloads_dir")
    ap.add_argument("reference_dir")
    ap.add_argument("--max", type=int, default=10, help="max distance counted as a match")
    ap.add_argument("--rename", action="store_true")
    args = ap.parse_args()

    refs = {p: dhash(p) for p in images(args.reference_dir)}
    if not refs:
        sys.exit(f"no reference images in {args.reference_dir}")
    out_dir = os.path.join(args.downloads_dir, "matched")

    for d in images(args.downloads_dir):
        h = dhash(d)
        ranked = sorted((bin(h ^ rh).count("1"), r) for r, rh in refs.items())
        (best_d, best), second = ranked[0], ranked[1] if len(ranked) > 1 else (None, None)
        flag = "OK" if best_d <= args.max else "NO-MATCH"
        alt = f"  next={os.path.basename(second[1])}:{second[0]}" if second[0] is not None else ""
        print(f"{flag:8} {os.path.basename(d)}  ->  {os.path.basename(best)}  dist={best_d}{alt}")
        if args.rename and flag == "OK":
            os.makedirs(out_dir, exist_ok=True)
            stem = os.path.splitext(os.path.basename(best))[0]
            shutil.copy2(d, os.path.join(out_dir, stem + os.path.splitext(d)[1].lower()))


if __name__ == "__main__":
    main()
