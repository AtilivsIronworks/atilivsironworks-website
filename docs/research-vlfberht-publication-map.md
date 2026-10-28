# Research publication map — VLFBERHT Swords

**Status:** Published October 28, 2026  
**Live URL:** https://atilivsironworks.com/research/vlfberht-swords/  
**GitHub publication PR:** https://github.com/AtilivsIronworks/atilivsironworks-website/pull/1 (merged into `main`)

## Published routes

- `research/index.html`: Research archive listing with link to the published study.
- `research/vlfberht-swords/index.html`: full article, seven sections, conclusion, references and seven locally hosted figure credits and an external link to the Pohansko archaeological drawing.
- `sitemap.xml`: includes the published URL and the publication date.
- `research/vlfberht-swords/*.jpg`: six uploaded article photographs. The unlicensed Pohansko JPG was removed from the current tree.
- `assets/river-witham/inscription-and-guard.jpg`: seventh locally hosted image, referenced by absolute path.
- `assets/research/vlfberht-swords/README.md`: image filename/permission manifest. The actual images are in `research/`, **not** in `assets/research/`.

## Manuscript content

Introduction (final approved opening with the popular magical-steel reputation and a bladesmith's curiosity); Sections 1–7 on provenance, inscription variants, blade construction, crucible steel, the Pohansko sword, inscription techniques, and the workshop question; conclusion, nine cited works, seven figure captions, and an accurate AI assistance note.

## Historical cautions to preserve

- Williams' 2009 groups A–D differ from his 2012 categories I–V.
- Stalsberg suggested that `+VLFBERHT+` may be slightly older than `+VLFBERH+T`, which complicates an original/copy sequence.
- Moilanen discussed cut grooves but did not test that method among his 13 experiments.
- The Pohansko cross-section does not prove complete-blade metallurgy or a specific heat-treatment sequence.
- Similar inscription variants and blade constructions cannot, alone, establish shared workshops.
- The author's River Witham sword demonstrates a practical modern approach, not direct evidence of Viking Age manufacturing.
- The Pohansko drawing by N. Koštová, Košta et al. (2019), fig. 21, p. 192, is linked externally at [the original journal PDF](https://pamatkyarcheologicke.cz/archiv/pa_2019_173-235.pdf#page=20), not reproduced. The journal's CC BY-NC-ND 4.0 license does not authorize commercial reuse; separate written permission has not been obtained.

## Future edits

Keep the article title, publication date, canonical link, image paths, sitemap URL and Research archive entry synchronized. Do not restore `pohansko-2019-fig21.jpg` without written permission covering business-site publication and inclusion in the downloadable PDF. An original steel-construction diagram may be added later with accurate labels and captions. Preserve full photographer credits and license links with third-party photographs.

## PDF export

- `research/vlfberht-swords/vlfberht-swords.pdf`: complete research paper with figures, measurements table, references and editorial note.
- `scripts/build_vlfberht_pdf.py`: reproducible exporter. The website HTML is authoritative.
- `.github/workflows/build-vlfberht-pdf.yml`: rebuilds, verifies and commits the downloadable PDF when source HTML or figures change.
- The bottom of the live article contains the PDF download link, followed by the existing support section.
