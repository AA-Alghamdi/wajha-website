# WAJHA for Advanced Drone Cleaning Solutions: Website

A bilingual (Arabic/English), static marketing website for WAJHA, generated
from Python content/template modules. No build step is required to serve
the site. The generator just writes plain HTML/CSS/JS into this folder.

## What was built

- **16 unique pages**, each in `/en/` and `/ar/` (33 HTML files total incl.
  the root language-redirect page): Home, About, Services (index + 6 detail
  pages), Technology, Projects, Blog (index + 3 posts), Contact.
- **Bilingual with a language toggle**: every page has a same-slug twin in
  the other language, with `hreflang` alternate links wired between them.
  Arabic pages render `<html lang="ar" dir="rtl">` and the whole layout is
  built with CSS logical properties (`margin-inline`, `inset-inline`,
  `text-align: start/end`, etc.) in the **one shared stylesheet**
  (`assets/css/style.css`), with no separate mirrored CSS file to maintain.
- **Original visual identity**: an inline SVG drone/rotor wordmark (used as
  the header logo and the favicon), six original line-icon SVGs (one per
  service), and CSS gradient/shape decoration.
- **Licensed stock photography** on every page (hero, About, Technology, all
  6 service pages, Projects, Contact, all 3 blog posts): 11 real photos
  sourced from Pexels and Unsplash under their free commercial-use licenses,
  self-hosted under `assets/img/photos/`. These are generic, illustrative
  photos, not real photos of WAJHA's own staff, drones, office, or a
  completed project. See `PHOTO_CREDITS.md` for full source attribution and
  "Before you publish" below for what to swap once you have your own
  photography.
- **Six service pages**: Building Facade Cleaning, Solar Panel Cleaning,
  Road Signs & Street Infrastructure, Factory & Industrial Walls, Marine
  Vessel Cleaning, Aircraft Cleaning. Each has benefits, a 4-step "how it
  works" process, and a closing CTA.
- **Projects page** presents six *representative project categories*
  (illustrated cards), not fabricated case studies with invented client
  names or numbers, since there was no real project photography or verified
  case data to build those from.
- **3 blog posts**, written to be factually conservative: no invented
  statistics, no fabricated citations, and references to Saudi Arabia's
  General Authority of Civil Aviation (GACA) are generic (a real regulator,
  but no specific regulation numbers are invented).
- **Contact form** wired to POST to Formspree via `fetch()`, with inline
  success/error states (no page reload). **It is not yet live**; see below.
- **Stats section** on the homepage, numeric values animate via a scroll-
  triggered count-up.
- Per-page SEO: unique `<title>`, meta description, Open Graph tags,
  canonical link, and `hreflang` alternates between the EN/AR twin pages.

## Directory structure

```
wajha-website/
├── index.html              ← language-detect redirect (JS; no-JS fallback links)
├── en/ ar/                 ← the 16 pages × 2 languages (identical slugs)
│   ├── index.html, about.html, technology.html, projects.html, contact.html
│   ├── services/           ← index.html + 6 service detail pages
│   └── blog/               ← index.html + 3 posts
├── assets/
│   ├── css/style.css       ← single stylesheet, serves both LTR and RTL
│   ├── js/main.js          ← nav, scroll effects, count-up, contact form
│   ├── icons/favicon.svg
│   └── img/photos/         ← 11 licensed stock photos (see PHOTO_CREDITS.md)
├── tools/                  ← the generator, KEEP this to regenerate after edits
│   ├── content.py          ← site-wide strings, contact info, 6 services (EN+AR)
│   ├── content_pages.py    ← home/about/technology/projects/contact copy + SEO
│   ├── content_blog.py     ← the 3 blog posts (EN+AR)
│   ├── icons.py            ← every inline SVG icon + the logo + favicon
│   ├── photos.py           ← photo registry: filenames, alt text, page-to-photo mapping
│   ├── layout.py           ← <head>, header/nav, footer, page wrapper
│   ├── pages.py            ← body-HTML builder for each page type
│   └── generate.py         ← driver script, run this after editing content
├── PHOTO_CREDITS.md        ← source/license/photographer for every stock photo
└── README.md
```

### Regenerating after a content edit

Edit the relevant file in `tools/` (plain Python data, no templating syntax
to learn), then from the project root run:

```
python3 tools/generate.py
```

This rewrites every HTML file in `en/` and `ar/` plus the favicon and root
redirect page. It is stdlib-only: no `pip install` needed, works with any
Python 3.

## Before you publish: checklist

These are things that were deliberately left as clearly-flagged placeholders
rather than invented as if real:

- [ ] **Contact form is not live.** Go to [formspree.io](https://formspree.io),
      create a free form, and get your real endpoint
      (`https://formspree.io/f/xxxxxxxx`). Replace `YOUR_FORM_ID` in:
      - `en/contact.html` and `ar/contact.html`, but better, edit
        `tools/pages.py` (search `YOUR_FORM_ID` in `build_contact`) and
        regenerate, so the fix survives the next `generate.py` run.
      Until this is done, the form shows a "not yet connected" message
      instead of silently failing.
- [ ] **Email address `info@wajha.sa` is a placeholder.** Swap it for your
      real company inbox in `tools/content.py` (`CONTACT` dict) and
      regenerate.
- [ ] **No exact street address.** Only city-level location (Riyadh, Saudi
      Arabia) is used anywhere. Add your real office address to the Contact
      page (`tools/content_pages.py` → `CONTACT_PAGE`, and the
      `map-placeholder` block in `tools/pages.py`) if you want one listed.
- [ ] **All numeric stats beyond "100+ team members" and "largest fleet in
      Saudi Arabia" are placeholder marketing figures** (500+ projects, 6
      cities, etc.) invented to populate the homepage stats section. This is
      not verified data. Replace with your real numbers in
      `tools/content_pages.py` (`HOME["en"]["stats"]` / `HOME["ar"]["stats"]`)
      before publishing.
- [ ] **Photos are licensed stock, not real WAJHA photography.** Every photo
      (hero, About, Technology, services, Projects, Contact, blog) is a
      generic Pexels/Unsplash photo standing in for your own drones, team,
      and completed work. See `PHOTO_CREDITS.md` for exactly which one is
      where. Once you have real photography, replace the relevant file in
      `assets/img/photos/` (keep the same filename to avoid touching
      `tools/photos.py`, or update the registry there if you rename it) and
      regenerate.
- [ ] **Testimonials on the homepage are explicitly labeled "sample."**
      Replace with real, verified client quotes (with permission) before
      publishing, or remove the section. See `tools/content_pages.py` →
      `HOME["en"]["testimonials"]` / `HOME["ar"]["testimonials"]`.
- [ ] **Logo is a placeholder brand mark**, not a professionally designed
      logo. If you commission a real logo, replace the inline SVG in
      `tools/icons.py` (`LOGO_MARK`, `FAVICON_SVG`) and regenerate.
- [ ] **No analytics or Search Console wired up.** Add your analytics
      snippet (e.g. a privacy-respecting analytics provider or Google
      Analytics) to `tools/layout.py` (`head()` function) if you want
      traffic data, and verify the domain in Google Search Console once
      it's live so the site gets indexed.
- [ ] **Root-absolute paths assume the site is deployed at a domain root**
      (e.g. `wajha.sa` or a Netlify/Vercel subdomain). See the GitHub Pages
      note below if you're using a project subpath instead.

## Deployment

The site is plain static files, so any static host works. Three easy options:

### Netlify (drag-and-drop, easiest)
1. Go to [app.netlify.com/drop](https://app.netlify.com/drop).
2. Drag the entire `wajha-website` folder onto the page.
3. Netlify gives you a live URL immediately; add a custom domain under
   **Site settings → Domain management** when ready.

### Vercel
1. Install the CLI (`npm i -g vercel`) or use the Vercel dashboard's "Add
   New Project" → "Upload" flow.
2. From this folder, run `vercel` and follow the prompts (no build command
   needed, since it's static files).

### GitHub Pages
1. Push this folder to a GitHub repository.
2. In **Settings → Pages**, set the source to the root of the branch you
   pushed.
3. **Important:** this site's internal links are root-absolute (e.g.
   `/en/index.html`), which only works if the site is served from the
   domain root. A GitHub Pages *project* site is served from
   `username.github.io/repo-name/`, which would break those links. Either:
   - name the repository `username.github.io` (served from the true root), or
   - attach a custom domain in Pages settings (also serves from root), or
   - ask for the generator to be adapted to relative paths if you need a
     project-subpath deployment without a custom domain.

## Local preview

From this folder:

```
python3 -m http.server 8000
```

Then open **http://localhost:8000/en/index.html** (or `/ar/index.html`) in
a browser. Opening `index.html` directly via `file://` also works for the
language-redirect page, but a local server is recommended so relative
root-absolute asset paths resolve correctly.
