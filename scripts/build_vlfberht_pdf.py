#!/usr/bin/env python3
"""Export the canonical VLFBERHT research webpage as a complete, print-ready PDF.

Runs entirely from checked-in site content. No web fetching or replacement prose.
"""
from __future__ import annotations

from pathlib import Path
from html import escape
from bs4 import BeautifulSoup
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
ARTICLE_DIR = ROOT / "research" / "vlfberht-swords"
SOURCE = ARTICLE_DIR / "index.html"
OUTPUT = ARTICLE_DIR / "vlfberht-swords.pdf"

CSS = r"""
@page {
  size: Letter;
  margin: 0.75in 0.82in 0.82in 0.82in;
  @bottom-left {
    content: "ATILIVS IRONWORKS  ·  VLFBERHT SWORDS";
    color: #6b6258;
    font: 7pt "DejaVu Sans", sans-serif;
    letter-spacing: 0.04em;
  }
  @bottom-right {
    content: counter(page);
    color: #6b6258;
    font: 8.5pt "DejaVu Sans", sans-serif;
  }
}
html { font-size: 10.7pt; }
body { margin: 0; color: #232628; background: #fff; font-family: "DejaVu Serif", Georgia, serif; line-height: 1.52; }
.masthead { padding-bottom: 17pt; margin-bottom: 23pt; border-bottom: 1.3pt solid #a78455; }
.kicker { text-transform: uppercase; letter-spacing: 0.13em; font: bold 8pt "DejaVu Sans", sans-serif; color: #846b48; margin: 0 0 9pt; }
h1 { font-family: "DejaVu Serif", Georgia, serif; font-size: 23pt; font-weight: bold; line-height: 1.19; margin: 0 0 12pt; color: #222522; }
.subtitle { font-size: 12pt; color: #645b50; font-style: italic; margin: 0 0 8pt; }
.pubdate { font: 8.6pt "DejaVu Sans", sans-serif; color: #666; margin: 5pt 0 0; }
article > h2:first-child { margin-top: 12pt; }
h2 { font: bold 15.2pt "DejaVu Serif", Georgia, serif; color: #302f2a; margin: 26pt 0 11pt; padding-bottom: 5pt; border-bottom: .65pt solid #d0c1ab; break-after: avoid; }
h3 { font: bold 12.1pt "DejaVu Serif", Georgia, serif; color: #40392f; margin: 18pt 0 8pt; break-after: avoid; }
p { margin: 0 0 10pt; orphans: 3; widows: 3; }
.essay-lede { font-size: 11.6pt; line-height: 1.58; color: #333; }
strong { font-weight: bold; }
em { font-style: italic; }
a { color: #565042; text-decoration: underline; }
figure { margin: 16pt 0 19pt; break-inside: avoid; text-align: center; }
figure img { display: block; max-width: 100%; max-height: 5.3in; width: auto; height: auto; object-fit: contain; margin: 0 auto 8pt; }
figure figcaption { font: 8.25pt/1.5 "DejaVu Sans", sans-serif; color: #55534f; text-align: left; }
figure figcaption strong { color: #272727; }
.photo-pair { display: block; }
.photo-pair figure { display: block; }
.essay-table-scroll { margin: 12pt 0 18pt; }
table { border-collapse: collapse; width: 100%; font: 9.2pt/1.38 "DejaVu Sans", sans-serif; }
caption { text-align: left; color: #555; font-style: italic; padding: 0 0 6pt; }
th { border-bottom: 1pt solid #b3a38c; background: #f2eee8; text-align: left; font-weight: bold; }
td, th { padding: 5pt 7pt; border-bottom: .4pt solid #d7d4cf; vertical-align: top; }
tr { break-inside: avoid; }
ul, ol { padding-left: 20pt; }
li { margin-bottom: 8pt; break-inside: avoid; }
.essay-sources { font-size: 9.3pt; line-height: 1.52; padding-left: 21pt; }
.research-note { border-top: 1pt solid #d1c2af; padding-top: 11pt; margin-top: 20pt; }
.research-note h3 { margin-top: 4pt; font-size: 10.3pt; }
.research-note p { font-size: 9pt; color: #555; }
sup { font-size: 7pt; }
"""
def main() -> None:
    soup = BeautifulSoup(SOURCE.read_text(encoding="utf-8"), "html.parser")
    heading = soup.select_one(".page-intro h1")
    article = soup.select_one("article.essay-copy")
    intro = soup.select_one(".page-intro")
    if heading is None or article is None or intro is None:
        raise SystemExit("Expected article structure not found; refusing incomplete PDF.")

    title = heading.get_text(" ", strip=True)
    subtitle_tag = intro.select_one("h1 + p")
    date_tag = intro.select_one(".article-dates time")

    # A research-paper export includes all approved scholarship, captions, tables,
    # references and editorial note; it omits website navigation/donation controls.
    for selector in [".article-support", ".article-download", ".essay-back"]:
        for el in article.select(selector):
            el.decompose()

    images = article.select("img")
    if len(images) != 8:
        raise SystemExit(f"Expected exactly eight illustrations; found {len(images)}.")

    for img in images:
        raw = img.get("src", "")
        if raw.startswith("/"):
            source = ROOT / raw.lstrip("/")
        elif "://" in raw or not raw:
            raise SystemExit(f"Unrecognized or remote image reference: {raw}")
        else:
            source = ARTICLE_DIR / raw
        if not source.is_file():
            raise SystemExit(f"Missing illustration: {source}")
        img["src"] = source.resolve().as_uri()
        for attr in ("loading", "decoding"):
            img.attrs.pop(attr, None)

    if len(article.select("figcaption")) != 8:
        raise SystemExit("Figure caption count does not match image count.")
    if len(article.select("ol.essay-sources > li")) != 9:
        raise SystemExit("Bibliography differs from expected nine entries.")
    for a in article.select("a[href^='/']"):
        # Relative site navigation is not usable inside an offline PDF.
        href = str(a.get("href", ""))
        a["href"] = "https://atilivsironworks.com" + href

    subtitle = subtitle_tag.get_text(" ", strip=True) if subtitle_tag else ""
    date = date_tag.get_text(" ", strip=True) if date_tag else ""
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
    <title>{escape(title)}</title><style>{CSS}</style></head><body>
    <header class="masthead">
    <p class="kicker">Atilivs Ironworks · Historical research</p>
    <h1>{escape(title)}</h1>
    <p class="subtitle">{escape(subtitle)}</p>
    <p class="pubdate">Published {escape(date)} · atilivsironworks.com</p>
    </header>
    <article>{str(article.decode_contents())}</article>
    </body></html>"""
    HTML(string=doc, base_url=ROOT.as_uri() + "/").write_pdf(str(OUTPUT), presentational_hints=True)
    if OUTPUT.stat().st_size < 100_000:
        raise SystemExit("PDF seems unexpectedly small: check images and text.")
    print(f"PDF generated: {OUTPUT} ({OUTPUT.stat().st_size:,} bytes)")
if __name__ == "__main__":
    main()
