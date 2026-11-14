#!/usr/bin/env python3
"""Prepare web-size copies of the Viking utility knife photographs.

Keep uploaded originals unchanged. Optimize for display while preserving
their natural aspect ratios and high-quality detail.
"""
from pathlib import Path
from PIL import Image, ImageOps
import re

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "viking-utility-knife"
PHOTOS = ["IMG_1581.jpeg", "IMG_1582.jpeg", "IMG_1584.jpeg",
          "IMG_1585.jpeg", "IMG_1586.jpeg", "IMG_1587.jpeg"]
PAGES = [ROOT / "index.html", ROOT / "works" / "index.html",
         ROOT / "works" / "viking-utility-knife" / "index.html"]

def main():
    replacements = {}
    for name in PHOTOS:
        original = ASSETS / name
        if not original.exists():
            raise SystemExit(f"Missing original photograph: {original}")
        out_name = name.replace(".jpeg", "-web.jpg")
        target = ASSETS / out_name
        with Image.open(original) as source:
            source = ImageOps.exif_transpose(source)
            source = source.convert("RGB")
            before_size = source.size
            source.thumbnail((2200, 2200), Image.Resampling.LANCZOS)
            source.save(target, "JPEG", quality=87, optimize=True,
                        progressive=True, subsampling=0)
            after_size = source.size
        original_bytes = original.stat().st_size
        optimized_bytes = target.stat().st_size
        if optimized_bytes >= original_bytes * .85:
            raise SystemExit(f"Insufficient savings for {name}: {original_bytes} -> {optimized_bytes}")
        replacements[name] = out_name
        print(f"{name}: {before_size} -> {after_size}; {original_bytes:,} -> {optimized_bytes:,} bytes")
    for page in PAGES:
        html = page.read_text(encoding="utf-8")
        for old, new in replacements.items():
            html = html.replace("/assets/viking-utility-knife/" + old,
                                "/assets/viking-utility-knife/" + new)
        if page.name == "index.html" and page.parent.name == "viking-utility-knife":
            refs = re.findall(r'<img\s+src="([^"]+)"', html)
            if len(refs) != 6 or not all(ref.endswith("-web.jpg") for ref in refs):
                raise SystemExit("Detail page should contain six optimized photographs")
        page.write_text(html, encoding="utf-8")
    print("Original uploads preserved and web references updated.")

if __name__ == "__main__":
    main()
