# Atilivs Ironworks website

The official portfolio and historical research archive for [Atilivs Ironworks](https://atilivsironworks.com/), by Corey Peterson. The primary focus is documenting historical blades, construction, workshop experience, and researched evidence. Sales are secondary.

## Hosting and publishing

- Repository: `AtilivsIronworks/atilivsironworks-website`, branch `main`
- Hosting: Cloudflare Pages; commits to `main` trigger deployments
- Domain: `atilivsironworks.com`
- Architecture: static HTML and CSS; no general site build step
- Shared stylesheet: `assets/style.css`

Before changing a page, read the relevant `docs/` standard and preserve existing content, figure credits, links, and layout conventions.

## Site structure

- `index.html`: homepage
- `works/`: finished work gallery and project pages
- `research/`: historical studies and their source references
- `articles/`: workshop documentation and practical lessons
- `about/`, `contact/`: author and contact information
- `assets/`: shared images, styles, and media
- `sitemap.xml`, `robots.txt`: public search configuration

The active published pages are listed in `sitemap.xml`. Legacy redirects are excluded from the sitemap.

## Publication and editorial standards

- `docs/works-page-sidebar-standard.md`: At a Glance measurements and materials
- `docs/works-page-narrative-standard.md`: Works narrative format and sourcing
- `docs/publication-header-standard.md`: author, publication dates and PDF metadata
- `docs/search-and-sharing-standard.md`: canonical URLs, sitemap and social sharing
- `docs/research-vlfberht-publication-map.md`: VLFBERHT research asset and publication map

Use verified references, distinguish evidence from interpretation, and never invent measurements or dates. Preserve publication dates separately from object completion dates.

## VLFBERHT PDF workflow

The article at `research/vlfberht-swords/index.html` is the authoritative source. GitHub Actions runs `.github/workflows/build-vlfberht-pdf.yml` with `scripts/build_vlfberht_pdf.py` to regenerate the downloadable PDF after relevant article or image changes. Do not edit the PDF separately.

The Pohansko sword illustration by N. Koštová (Košta et al., 2019, fig. 21, p. 192) is **linked to the original journal**, not hosted or embedded in the PDF, because reuse permission for this website has not been established. See the image manifest at `assets/research/vlfberht-swords/README.md`.

## Maintenance checklist

1. Review the relevant current files and documentation before editing.
2. Change only what is needed; avoid rebuilding existing features.
3. Confirm internal links, image files, captions, attribution, and canonical paths.
4. Update the sitemap and publication maps when adding or changing published routes.
5. Confirm GitHub Actions results when affected, and separately verify Cloudflare deployment when available.
6. Test desktop and mobile layouts when presentation changes.

Support: [Buy Me a Coffee](https://buymeacoffee.com/Atilivsironworks).  
Motto: *Ars longa, vita brevis.*
