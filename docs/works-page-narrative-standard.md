# Works pages: hybrid narrative standard

This is the ongoing editorial structure for `/works/<project>/` pages. See also `works-page-sidebar-standard.md`.

## Purpose

Works pages document an individual finished object in the maker's first-person voice. Articles are separate, deeper explorations of historical questions, techniques, or failures. Keep the Works page as a readable story rather than a spec sheet.

## Preferred major headings, in order

1. **The Project**: why it was made, when, for whom, intention and relevant personal context.
2. **Historical Inspiration**: primary archaeological examples and source-based comparisons; distinguish "inspired by" from "reconstruction of," and identify maker interpretation. Cite only material examined.
3. **Construction**: chronological workshop story, material choices explained in context, methods, assembly, finishing and testing. Add optional `h3` subsections such as "The Blade", "The Hilt", "Heraldry and Decoration", "Measurements and Proportions" or "Heat Treatment and Finishing" only when the material is long or complex enough to benefit. Place build photographs near the passages they document; retain proper proportions and captions.
4. **Challenges and Lessons**: failures, repairs, technical limitations, feedback from other makers and what would change if the object were made again. Clearly mark tests and estimates as estimates.
5. **Final Reflections**: presentation, donation, how the object is used, personal meaning and outcomes; don't write generic closure purely to fill a heading.
6. **References**: after the narrative, only when meaningful verified references exist. The original item and modern maker decisions should never be conflated.

These are the **default headings for fuller projects**, not a requirement to publish empty sections. Older projects with limited surviving notes may have only "The Project" and additional appropriate sections if evidence exists. Never invent undocumented steps or measurements. Do not use vacant "documentation pending" headings as padding.

## Consistency and voice
- Preserve the maker's authentic first-person observations and phrasing.
- Prefer normal paragraphs to long checklists of technical data.
- The At a Glance sidebar carries concise grouped dimensions and materials; repeat a value in the narrative only to explain an important construction or historical comparison.
- Credit outside smiths and collaborators in the actual build narrative, not in the sidebar.
- Put hardness, weld counts, process notes, challenges, and awards in the relevant narrative sections.
- Keep existing photo assets, captions, internal links and historically qualified language.
- Do not claim a source was consulted if it wasn't actually reviewed.
- For future content, distinguish the object's completion date from the website publication date.

## Implementation
- Use one `h1` for the object title; `h2` for major narrative sections and `h3` only for useful subsections.
- Share `/assets/style.css` for section hierarchy; do not introduce a different design per Works page.
- Keep old anchor destinations functional when changing existing section IDs.
- Preview both narrow/mobile and desktop screens; do not crop important historical metalwork.
