# Search visibility and sharing: Atilivs Ironworks

This static website is deployed from GitHub to Cloudflare Pages. The main search and sharing configuration is in the HTML `<head>`, `sitemap.xml`, and `robots.txt`.

## Canonical URLs
- Public canonical domain: `https://atilivsironworks.com/`
- Each indexable page must have a unique absolute `<link rel="canonical" href="https://atilivsironworks.com/.../">`.
- The same URL must appear as `og:url` and in `sitemap.xml`.
- Do not include old redirect aliases in the sitemap; they are currently marked `noindex,follow` and canonicalize to the live destination.

## Page metadata
For each new work, research paper or article:
1. Provide a specific readable `<title>` describing that page.
2. Provide a factual, unique `<meta name="description">` (no unsupported claims or keyword stuffing).
3. Add Open Graph tags: `og:type` (`article` for published Research/Articles; otherwise `website`), `og:site_name`, `og:locale`, `og:url`, `og:title`, `og:description`, `og:image`, and `og:image:alt`.
4. Always use an **absolute publicly reachable image URL**, and check that the asset is actually in GitHub. Prefer an image showing the item; if an early work has no surviving photo, clearly label any generic forge image as such.
5. Include `<meta name="twitter:card" content="summary_large_image">` for large-image sharing.
6. Keep `article:published_time` on individual research or article pages when the publication date is confirmed.
7. If a historical image is reused, observe its license and attribution; access alone is not a reuse license.

## Sitemap and indexing
- `robots.txt` currently allows crawling and points to `https://atilivsironworks.com/sitemap.xml`.
- The sitemap must include every active indexable page exactly once, using fully qualified canonical URLs. It must exclude redirects and noindex pages.
- Use `lastmod` only when dates are accurate (not invented).
- After deploying a new page, recheck its sitemap URL and validate its preview in Meta's Sharing Debugger (https://developers.facebook.com/tools/debug/).

## Google Search Console onboarding (site-owner action)
1. Open https://search.google.com/search-console.
2. Add a **Domain** property: `atilivsironworks.com` (no protocol, no slash).
3. Copy the TXT verification record from Google. Add it to the root `@` of the authoritative DNS zone. Because Namecheap is the registrar and Cloudflare Pages is the host, check the domain's actual nameservers: edit DNS at Cloudflare **if Cloudflare manages the zone**, otherwise at Namecheap (or the actual DNS host).
4. Click Verify in Search Console once the record propagates. Do not delete the verification TXT record.
5. In **Sitemaps**, submit `https://atilivsironworks.com/sitemap.xml` (or `sitemap.xml` when the prefix is already shown). Monitor errors and page indexing.
6. Use **URL inspection** to request indexing for important new pages, starting with homepage, Works, Research and VLFBERHT.
7. Verification and sitemap submission are not Google indexing guarantees; use Page indexing and URL inspection to diagnose.

## Current state (October 28, 2026)
- The sitemap lists 17 current indexable pages.
- Two legacy Works redirect pages remain outside the sitemap with noindex.
- All 17 current pages have canonical, page-specific descriptive metadata, and Open Graph/Twitter sharing tags referencing existing media in the repository.
- Actual Search Console ownership verification, indexing status, and Facebook scraper preview must be confirmed within the site owner's accounts.
