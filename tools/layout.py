"""Shared page chrome: <head>, header/nav, footer, and the full-page wrapper."""

from content import SITE, NAV, FOOTER, CONTACT, SERVICES, SERVICES_ORDER
from icons import icon

LANGS = ("en", "ar")


def other_lang(lang: str) -> str:
    return "ar" if lang == "en" else "en"


def url_for(lang: str, slug: str) -> str:
    return f"/{lang}/{slug}.html"


def head(lang: str, slug: str, title: str, description: str) -> str:
    site = SITE[lang]
    other = other_lang(lang)
    self_url = url_for(lang, slug)
    alt_url = url_for(other, slug)
    font_family = "IBM+Plex+Sans+Arabic:wght@400;500;600;700" if lang == "ar" else "Inter:wght@400;500;600;700;800"
    return f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{self_url}">
<link rel="alternate" hreflang="{lang}" href="{self_url}">
<link rel="alternate" hreflang="{other}" href="{alt_url}">
<link rel="alternate" hreflang="x-default" href="{url_for('en', slug)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:locale" content="{site['og_locale']}">
<meta property="og:url" content="{self_url}">
<meta name="twitter:card" content="summary">
<link rel="icon" type="image/svg+xml" href="/assets/icons/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family={font_family}&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">"""


def _nav_link(lang: str, slug: str, label: str, active_slug: str) -> str:
    cls = ' class="active"' if slug == active_slug or (active_slug.startswith(slug + "/") and slug != "index") else ""
    return f'<li><a href="{url_for(lang, slug)}"{cls}>{label}</a></li>'


def header_nav(lang: str, active_slug: str) -> str:
    nav = NAV[lang]
    site = SITE[lang]
    links = [
        _nav_link(lang, "index", nav["home"], active_slug),
        _nav_link(lang, "about", nav["about"], active_slug),
        _nav_link(lang, "services/index", nav["services"], active_slug),
        _nav_link(lang, "technology", nav["technology"], active_slug),
        _nav_link(lang, "projects", nav["projects"], active_slug),
        _nav_link(lang, "blog/index", nav["blog"], active_slug),
        _nav_link(lang, "contact", nav["contact"], active_slug),
    ]
    other = other_lang(lang)
    alt_slug = active_slug
    return f"""<a class="skip-link" href="#main">{nav['skip']}</a>
<header class="site-header" id="site-header">
  <div class="container header-inner">
    <a class="brand" href="{url_for(lang, 'index')}" aria-label="{site['company']}: {site['tagline']}">
      {icon('logo', 'brand-mark')}
      <span class="brand-text"><span class="brand-name">{site['company']}</span><span class="brand-tagline">{site['tagline']}</span></span>
    </a>
    <nav class="main-nav" id="main-nav" aria-label="Primary">
      <ul>{''.join(links)}</ul>
    </nav>
    <div class="header-actions">
      <a class="lang-switch" href="{url_for(other, alt_slug)}" rel="alternate" hreflang="{other}">{nav['lang_switch']}</a>
      <a class="btn btn-primary btn-sm" href="{url_for(lang, 'contact')}">{nav['cta']}</a>
      <button class="nav-toggle" id="nav-toggle" aria-expanded="false" aria-controls="main-nav" aria-label="{nav['home']}">
        <span class="nav-toggle-icon">{icon('menu', 'icon-menu')}{icon('close', 'icon-close')}</span>
      </button>
    </div>
  </div>
</header>"""


def footer_html(lang: str) -> str:
    nav = NAV[lang]
    site = SITE[lang]
    foot = FOOTER[lang]
    service_links = "".join(
        f'<li><a href="{url_for(lang, f"services/{slug}")}">{SERVICES[slug][lang]["title"]}</a></li>'
        for slug in SERVICES_ORDER
    )
    quick_links = "".join([
        f'<li><a href="{url_for(lang, "index")}">{nav["home"]}</a></li>',
        f'<li><a href="{url_for(lang, "about")}">{nav["about"]}</a></li>',
        f'<li><a href="{url_for(lang, "technology")}">{nav["technology"]}</a></li>',
        f'<li><a href="{url_for(lang, "projects")}">{nav["projects"]}</a></li>',
        f'<li><a href="{url_for(lang, "blog/index")}">{nav["blog"]}</a></li>',
        f'<li><a href="{url_for(lang, "contact")}">{nav["contact"]}</a></li>',
    ])
    year = "2026"
    return f"""<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <a class="brand brand-footer" href="{url_for(lang, 'index')}">
        {icon('logo', 'brand-mark')}
        <span class="brand-text"><span class="brand-name">{site['company']}</span></span>
      </a>
      <p class="footer-blurb">{foot['blurb']}</p>
    </div>
    <div class="footer-col">
      <h3>{foot['quick_links']}</h3>
      <ul>{quick_links}</ul>
    </div>
    <div class="footer-col">
      <h3>{foot['our_services']}</h3>
      <ul>{service_links}</ul>
    </div>
    <div class="footer-col">
      <h3>{foot['get_in_touch']}</h3>
      <ul class="footer-contact">
        <li><a href="{CONTACT['phone1_href']}">{icon('phone', 'icon-sm')}<span>{CONTACT['phone1']}</span></a></li>
        <li><a href="{CONTACT['phone2_href']}">{icon('phone', 'icon-sm')}<span>{CONTACT['phone2']}</span></a></li>
        <li><a href="{CONTACT['email_href']}">{icon('mail', 'icon-sm')}<span>{CONTACT['email']}</span></a></li>
        <li class="footer-location">{icon('pin', 'icon-sm')}<span>{site['city']}</span></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom container">
    <p>&copy; {year} {site['full_name']}. {foot['rights']}</p>
  </div>
</footer>
<button class="back-to-top" id="back-to-top" aria-label="Back to top">{icon('chevron-up', 'icon')}</button>
<script src="/assets/js/main.js" defer></script>"""


def page(lang: str, slug: str, title: str, description: str, body: str, body_class: str = "") -> str:
    site = SITE[lang]
    cls = f' class="{body_class}"' if body_class else ""
    return f"""<!DOCTYPE html>
<html lang="{site['lang']}" dir="{site['dir']}">
<head>
{head(lang, slug, title, description)}
</head>
<body{cls}>
{header_nav(lang, slug)}
<main id="main">
{body}
</main>
{footer_html(lang)}
</body>
</html>
"""
