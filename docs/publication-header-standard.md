# Long-form publication header standard

Apply this standard to **individual pages under `/research/` and `/articles/`**, not to Works detail pages, archives, or generic landing pages.

A clean publication metadata bar appears under the H1 and brief description. It uses the shared site stylesheet's `.publication-meta` classes.

## Structure

- Preserve the article title and subtitle before the metadata bar.
- Include a hairline divider, followed by the linked author byline **Corey Peterson** (`/about/`).
- Display the actual **publication date** using a semantic `<time datetime="YYYY-MM-DD">`. Never substitute the object's completion date.
- For workshop or project articles that document an older work, include a **separately labelled object-completion date**, if known.
- Show the compact **PDF** download link only when a PDF actually exists at the linked URL; never show a dead placeholder or invent a DOI.
- Preserve the full article, figure captions, references, chronological context, and footer links. The metadata bar is a presentation element, not a manuscript rewrite.
- Use the shared `/assets/style.css` rules instead of individual page-specific layout variations.

## Sample markup

```html
<div class="publication-meta" aria-label="Publication details">
  <div class="publication-meta-items">
    <span class="publication-meta-item">
      <!-- decorative person SVG aria-hidden="true" -->
      <a href="/about/" rel="author">Corey Peterson</a>
    </span>
    <span class="publication-meta-item">
      <!-- decorative calendar SVG aria-hidden="true" -->
      <span><span class="publication-meta-label">Published:</span>
        <time datetime="2026-10-28">October 28, 2026</time></span>
    </span>
    <!-- optional labelled project completion date -->
  </div>
  <!-- PDF link only when the file exists -->
</div>
```

## Current published examples

- Research: `/research/vlfberht-swords/`. Published October 28, 2026. Has a PDF download button at the top and a full PDF download section at the bottom.
- Workshop article: `/articles/when-a-sword-becomes-a-knife/`. Published October 24, 2026; knife completed June 20, 2026. No PDF at this time.

PDF generation for VLFBERHT is handled by `scripts/build_vlfberht_pdf.py` and `.github/workflows/build-vlfberht-pdf.yml`, which must continue extracting the publication date from `.publication-meta-item time`.
