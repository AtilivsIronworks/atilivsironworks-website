#!/usr/bin/env python3
"""Make lightweight web copies of three large VLFBERHT photographs.

Source JPGs are never edited. Only switch HTML references when the copy is
at least 15% smaller. Captions, attributions and original URLs remain intact.
"""
from pathlib import Path
from PIL import Image, ImageOps
import re

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "research" / "vlfberht-swords"
PAGE = DIR / "index.html"
PHOTOS = (
    "01-mannheim-ulfberht.jpg",
    "03-schwedt-inscription.jpg",
    "04-schwedt-sword.jpg",
)
MAX_EDGE = 2400
MIN_SAVING = 0.15

def main():
    html = PAGE.read_text(encoding="utf-8")
    changed = False
    for filename in PHOTOS:
        original = DIR / filename
        if not original.is_file():
            raise SystemExit(f"Missing source image: {original}")
        output_name = filename.replace(".jpg", "-web.jpg")
        output = DIR / output_name
        with Image.open(original) as source:
            source = ImageOps.exif_transpose(source)
            source = source.convert("RGB")
            size_before = source.size
            source.thumbnail((MAX_EDGE, MAX_EDGE), Image.Resampling.LANCZOS)
            source.save(output, format="JPEG", quality=86, optimize=True, progressive=True, subsampling=0)
            size_after = source.size
        old_bytes = original.stat().st_size
        new_bytes = output.stat().st_size
        savings = (old_bytes - new_bytes) / old_bytes
        if savings < MIN_SAVING:
            output.unlink()
            print(f"KEEP ORIGINAL {filename}: {size_before} -> {size_after}, savings {savings:.1%}")
            continue
        # Replace only the src attribute, not caption credits, alt or source links.
        before = f'src="{filename}"'
        after = f'src="{output_name}"'
        occurrences = html.count(before) + html.count(after)
        if occurrences != 1:
            raise SystemExit(f"Expected exactly one reference to {filename} or its web copy; found {occurrences}")
        html = html.replace(before, after)
        changed = True
        print(f"USE WEB COPY {output_name}: {size_before} -> {size_after}, {old_bytes:,} -> {new_bytes:,} bytes ({savings:.1%} smaller)")
    if changed:
        PAGE.write_text(html, encoding="utf-8")
    print("Original photographs were preserved.")

if __name__ == "__main__":
    main()
