# Works pages: "At a glance" standard

Editorial and presentation rules for every individual page under `/works/<project>/`.

## Sidebar headings and order
Every Works detail page uses exactly these three grouped sections inside the **At a glance** sidebar:

1. **Inspiration** — identify the historical tradition, study, find or individual artifact that informed the design. State *inspired by* rather than *based on* unless this is actually a reconstruction of a named original. Distinguish comparison from replication when needed.
2. **Blade Dimensions** — in **one paragraph**, report whatever values are actually known, in this order: blade length; width at shoulder; maximum blade/spine thickness; handle length; overall length; weight; point of balance. Use explicit units. Do not present excavated-original dimensions as measurements of the modern work. A blade-base measurement must not silently become a shoulder measurement. If unknown, omit those individual measurements; when all are unknown say they were not recorded. Never estimate missing measurements.
3. **Work Materials** — in **one paragraph**, cover the blade, grip/handle, guard/pommel (if applicable), and non-ferrous fittings/decorations (if applicable). Include only historically attested or maker-confirmed build details and identify modern choices honestly.

### Required markup
```html
<aside>
  <span class="stamp">At a glance</span>
  <div class="facts facts--standard">
    <div class="fact-group"><strong>Inspiration</strong><p>...</p></div>
    <div class="fact-group"><strong>Blade Dimensions</strong><p>...</p></div>
    <div class="fact-group"><strong>Work Materials</strong><p>...</p></div>
  </div>
</aside>
```
Some pages add a class to `aside`; keep it when updating.

## Keep out of the sidebar
- Documentation status and publication notes
- HRC / hardness testing information
- Smiths, collaborators, acknowledgements or outside feedback
- Events, awards, presentation dates, completions, gifting/donation or provenance notes
- Heat treatments, weld counts, methods and learning notes

Those details belong in the **main body of the project page**, with appropriate sourcing and attribution. Do not delete meaningful information while standardizing the sidebar.

The three headings stay the same even when a work has only limited early construction notes. Do not invent measurements, materials, sources or credits to fill missing fields. Preserve photos, captions and existing research unless a specific correction is requested.
