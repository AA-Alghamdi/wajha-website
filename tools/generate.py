#!/usr/bin/env python3
"""Generate the static WAJHA site into the repo root from the content/layout
modules in this directory. Stdlib only, run with any python3.

Usage: python3 tools/generate.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from content import SERVICES, SERVICES_ORDER, SITE  # noqa: E402
from content_pages import PAGE_SEO  # noqa: E402
from content_blog import BLOG_POSTS, BLOG_ORDER  # noqa: E402
from icons import FAVICON_SVG  # noqa: E402
from layout import BASE_URL, canonical_url_for  # noqa: E402
import pages  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ("en", "ar")

# Every internal link/asset reference is authored as a root-absolute path
# (e.g. "/en/about.html", "/assets/css/style.css") because that's what the
# templates in layout.py/pages.py/photos.py produce. That only works if the
# site is served from its host's true root. To stay portable across hosts
# that serve from a subpath (a GitHub Pages project site at
# "/wajha-website/", for instance) as well as any future custom domain at
# true root, every written file is rewritten here into relative paths based
# on its own depth below the site root — a single, exhaustive fix point
# instead of threading "current page depth" through every template
# function. Matches any double-quoted string starting with /en/, /ar/, or
# /assets/, wherever it appears (href=, src=, or inside the root redirect's
# inline JS) — external absolute URLs (https://fonts.googleapis.com/...)
# and non-path schemes (tel:, mailto:) never start with "/", so they're
# never touched.
INTERNAL_PATH_RE = re.compile(r'"(/(?:en|ar|assets)/[^"]*)"')


def relativize(content: str, depth: int) -> str:
    prefix = "../" * depth

    def repl(match: "re.Match[str]") -> str:
        return f'"{prefix}{match.group(1)[1:]}"'

    return INTERNAL_PATH_RE.sub(repl, content)


def write(path: str, content: str) -> None:
    depth = path.count("/")
    content = relativize(content, depth)
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def seo(slug: str, lang: str):
    return PAGE_SEO[slug][lang]


def build_all():
    count = 0
    all_slugs = []  # every indexable (lang, slug) pair, for the sitemap
    for lang in LANGS:
        title, desc = seo("index", lang)
        write(f"{lang}/index.html", pages_page(lang, "index", title, desc, pages.build_home(lang)))
        all_slugs.append((lang, "index"))
        count += 1

        title, desc = seo("about", lang)
        write(f"{lang}/about.html", pages_page(lang, "about", title, desc, pages.build_about(lang)))
        all_slugs.append((lang, "about"))
        count += 1

        title, desc = seo("services/index", lang)
        write(f"{lang}/services/index.html", pages_page(lang, "services/index", title, desc, pages.build_services_index(lang)))
        all_slugs.append((lang, "services/index"))
        count += 1

        for slug in SERVICES_ORDER:
            page_slug = f"services/{slug}"
            title, desc = seo(page_slug, lang)
            write(f"{lang}/{page_slug}.html", pages_page(lang, page_slug, title, desc, pages.build_service_detail(lang, slug)))
            all_slugs.append((lang, page_slug))
            count += 1

        title, desc = seo("technology", lang)
        write(f"{lang}/technology.html", pages_page(lang, "technology", title, desc, pages.build_technology(lang)))
        all_slugs.append((lang, "technology"))
        count += 1

        title, desc = seo("projects", lang)
        write(f"{lang}/projects.html", pages_page(lang, "projects", title, desc, pages.build_projects(lang)))
        all_slugs.append((lang, "projects"))
        count += 1

        title, desc = seo("blog/index", lang)
        write(f"{lang}/blog/index.html", pages_page(lang, "blog/index", title, desc, pages.build_blog_index(lang)))
        all_slugs.append((lang, "blog/index"))
        count += 1

        for slug in BLOG_ORDER:
            post = BLOG_POSTS[slug][lang]
            page_slug = f"blog/{slug}"
            write(f"{lang}/{page_slug}.html", pages_page(
                lang, page_slug, f"{post['title']} | WAJHA" if lang == "en" else f"{post['title']} | وجهة",
                post["excerpt"], pages.build_blog_post(lang, slug)))
            all_slugs.append((lang, page_slug))
            count += 1

        title, desc = seo("contact", lang)
        write(f"{lang}/contact.html", pages_page(lang, "contact", title, desc, pages.build_contact(lang)))
        all_slugs.append((lang, "contact"))
        count += 1

    write("assets/icons/favicon.svg", FAVICON_SVG)
    write("index.html", build_root_redirect())
    count += 1

    write("sitemap.xml", build_sitemap(all_slugs))
    write("robots.txt", build_robots())

    print(f"Generated {count} HTML pages under en/ and ar/, plus favicon.svg, root index.html, sitemap.xml, and robots.txt.")


def build_sitemap(all_slugs) -> str:
    # One <url> entry per (lang, slug), each listing hreflang alternates to
    # every language version of that same slug — the format Google
    # recommends for bilingual sites. Every internal reference here is a
    # full absolute URL (required by the sitemap spec), unlike ordinary
    # navigation links elsewhere in the site, which stay relative.
    slugs_seen = []
    for _, slug in all_slugs:
        if slug not in slugs_seen:
            slugs_seen.append(slug)

    entries = []
    for lang, slug in all_slugs:
        alt_links = "\n".join(
            f'    <xhtml:link rel="alternate" hreflang="{alt_lang}" href="{canonical_url_for(alt_lang, slug)}"/>'
            for alt_lang in LANGS
        )
        entries.append(
            f"  <url>\n"
            f"    <loc>{canonical_url_for(lang, slug)}</loc>\n"
            f"{alt_links}\n"
            f'    <xhtml:link rel="alternate" hreflang="x-default" href="{canonical_url_for("en", slug)}"/>\n'
            f"  </url>"
        )

    body = "\n".join(entries)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        f"{body}\n"
        "</urlset>\n"
    )


def build_robots() -> str:
    return (
        "User-agent: *\n"
        "Allow: /\n\n"
        f"Sitemap: {BASE_URL}/sitemap.xml\n"
    )


def pages_page(lang, slug, title, desc, body):
    from layout import page
    return page(lang, slug, title, desc, body)


def build_root_redirect() -> str:
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>WAJHA | وجهة</title>
<meta name="robots" content="noindex">
<script>
(function () {
  var lang = (navigator.language || navigator.userLanguage || "en").toLowerCase();
  var target = lang.indexOf("ar") === 0 ? "/ar/index.html" : "/en/index.html";
  window.location.replace(target);
})();
</script>
<style>
  body { font-family: system-ui, sans-serif; background: #0A1930; color: #fff; display: flex;
         align-items: center; justify-content: center; min-height: 100vh; margin: 0; }
  .choice { text-align: center; }
  .choice a { color: #FFB703; font-size: 1.25rem; margin: 0 1rem; text-decoration: none; font-weight: 600; }
  .choice a:hover { text-decoration: underline; }
</style>
</head>
<body>
  <noscript>
    <div class="choice">
      <p>WAJHA: Advanced Drone Cleaning Solutions</p>
      <a href="/ar/index.html">العربية</a>
      <a href="/en/index.html">English</a>
    </div>
  </noscript>
</body>
</html>
"""


if __name__ == "__main__":
    build_all()
