"""Body-HTML builders, one function per page type."""

from content import SITE, NAV, CONTACT, SERVICES, SERVICES_ORDER
from content_pages import HOME, ABOUT, TECHNOLOGY, PROJECTS, CONTACT_PAGE
from content_blog import BLOG_POSTS, BLOG_ORDER
from icons import icon, SERVICE_ICON_KEYS
from layout import url_for
from photos import photo_img, SERVICE_PHOTOS, PROJECT_CATEGORY_PHOTOS, BLOG_PHOTOS


def _service_card(lang: str, slug: str, learn_more: str) -> str:
    svc = SERVICES[slug][lang]
    icon_key = SERVICES[slug]["icon"]
    return f"""<article class="card service-card reveal">
  <div class="card-icon">{icon(icon_key, 'icon-lg')}</div>
  <h3>{svc['title']}</h3>
  <p>{svc['short']}</p>
  <a class="card-link" href="{url_for(lang, f'services/{slug}')}">{learn_more}{icon('arrow', 'icon-sm icon-end')}</a>
</article>"""


def _services_grid(lang: str) -> str:
    learn_more = "Learn More" if lang == "en" else "اعرف أكثر"
    cards = "".join(_service_card(lang, slug, learn_more) for slug in SERVICES_ORDER)
    return f'<div class="grid services-grid">{cards}</div>'


def _page_hero(kicker: str, title: str, sub: str = "") -> str:
    sub_html = f'<p class="hero-sub">{sub}</p>' if sub else ""
    return f"""<section class="page-hero">
  <div class="container">
    <p class="kicker reveal">{kicker}</p>
    <h1 class="reveal">{title}</h1>
    {sub_html}
  </div>
</section>"""


def _photo_banner(key: str, lang: str, loading: str = "lazy") -> str:
    return f"""<div class="container">
  <figure class="photo-banner reveal">{photo_img(key, lang, 'photo-banner-img', loading)}</figure>
</div>"""


def _cta_band(lang: str, title: str, sub: str, button: str) -> str:
    return f"""<section class="cta-band">
  <div class="container cta-band-inner reveal">
    <h2>{title}</h2>
    <p>{sub}</p>
    <a class="btn btn-accent" href="{url_for(lang, 'contact')}">{button}{icon('arrow', 'icon-sm icon-end')}</a>
  </div>
</section>"""


# ------------------------------------------------------------------ HOME ----

def build_home(lang: str) -> str:
    h = HOME[lang]
    value_props = "".join(f"""<div class="value-prop reveal">
      <div class="value-prop-icon">{icon(key, 'icon-lg')}</div>
      <h3>{title}</h3>
      <p>{desc}</p>
    </div>""" for key, title, desc in h["value_props"])

    stat_cards = []
    for s in h["stats"]:
        if s.get("is_badge"):
            stat_cards.append(f"""<div class="stat-card stat-card-badge reveal">
      <div class="stat-badge-icon">{icon('shield', 'icon-lg')}</div>
      <p class="stat-badge-label">{h['stats_badge_label']}</p>
    </div>""")
        else:
            stat_cards.append(f"""<div class="stat-card reveal">
      <p class="stat-value"><span class="count-up" data-target="{s['value']}">0</span>{s['suffix']}</p>
      <p class="stat-label">{s['label']}</p>
    </div>""")
    stats_html = "".join(stat_cards)

    why_items = "".join(f'<li class="reveal">{icon("check", "icon-sm")}<span>{item}</span></li>' for item in h["why_items"])

    testimonials = "".join(f"""<figure class="testimonial-card reveal">
      {icon('quote', 'icon-quote')}
      <blockquote>{quote}</blockquote>
      <figcaption>{author}</figcaption>
    </figure>""" for quote, author in h["testimonials"])

    return f"""<section class="hero">
  <div class="container hero-inner">
    <div class="hero-copy">
      <p class="kicker reveal">{h['hero_kicker']}</p>
      <h1 class="reveal">{h['hero_title']}</h1>
      <p class="hero-sub reveal">{h['hero_sub']}</p>
      <div class="hero-actions reveal">
        <a class="btn btn-accent" href="{url_for(lang, 'contact')}">{h['hero_cta_primary']}{icon('arrow', 'icon-sm icon-end')}</a>
        <a class="btn btn-ghost" href="{url_for(lang, 'services/index')}">{h['hero_cta_secondary']}</a>
      </div>
    </div>
    <div class="hero-art reveal">
      <div class="hero-art-shape shape-1" aria-hidden="true"></div>
      <div class="hero-art-shape shape-2" aria-hidden="true"></div>
      <figure class="hero-photo-frame">
        {photo_img('hero-drone', lang, 'hero-photo', 'eager')}
        <span class="hero-photo-badge" aria-hidden="true">{icon('logo', 'hero-logo-mark-sm')}</span>
      </figure>
    </div>
  </div>
</section>

<section class="section value-props-section">
  <div class="container">
    <h2 class="section-title reveal">{h['value_props_title']}</h2>
    <div class="grid value-props-grid">{value_props}</div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <h2 class="section-title reveal">{h['services_title']}</h2>
      <p class="section-sub reveal">{h['services_sub']}</p>
    </div>
    {_services_grid(lang)}
  </div>
</section>

<section class="section stats-section">
  <div class="container">
    <div class="section-head">
      <h2 class="section-title reveal">{h['stats_title']}</h2>
      <p class="section-sub reveal">{h['stats_sub']}</p>
    </div>
    <div class="grid stats-grid">{stats_html}</div>
  </div>
</section>

<section class="section section-alt why-section">
  <div class="container why-inner">
    <h2 class="section-title reveal">{h['why_title']}</h2>
    <ul class="why-list">{why_items}</ul>
  </div>
</section>

<section class="section testimonials-section">
  <div class="container">
    <div class="section-head">
      <h2 class="section-title reveal">{h['testimonials_title']}</h2>
      <p class="section-sub section-sub-note reveal">{h['testimonials_note']}</p>
    </div>
    <div class="grid testimonials-grid">{testimonials}</div>
  </div>
</section>

{_cta_band(lang, h['final_cta_title'], h['final_cta_sub'], h['final_cta_button'])}
"""


# ----------------------------------------------------------------- ABOUT ----

def build_about(lang: str) -> str:
    a = ABOUT[lang]
    why_drones = "".join(f"""<div class="why-card reveal">
      <h3>{t}</h3>
      <p>{d}</p>
    </div>""" for t, d in a["why_drones"])
    return f"""{_page_hero(a['title'], a['hero'])}
{_photo_banner('riyadh-skyline', lang, 'eager')}
<section class="section">
  <div class="container narrow">
    <p class="lede reveal">{a['intro']}</p>
  </div>
</section>
<section class="section section-alt">
  <div class="container narrow">
    <h2 class="section-title reveal">{a['mission_title']}</h2>
    <p class="reveal">{a['mission']}</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <h2 class="section-title reveal">{a['why_drones_title']}</h2>
    <div class="grid why-cards-grid">{why_drones}</div>
  </div>
</section>
<section class="section section-alt">
  <div class="container narrow">
    <h2 class="section-title reveal">{a['team_title']}</h2>
    <p class="reveal">{a['team']}</p>
  </div>
</section>
<section class="section">
  <div class="container narrow">
    <h2 class="section-title reveal">{a['safety_title']}</h2>
    <p class="reveal">{a['safety']}</p>
  </div>
</section>
{_cta_band(lang, a['cta_title'], '', a['cta_button'])}
"""


# ------------------------------------------------------------- SERVICES -----

def build_services_index(lang: str) -> str:
    nav = NAV[lang]
    kicker = nav["services"]
    heading = "What We Clean" if lang == "en" else "ما الذي ننظّفه"
    sub = ("Six specialized service lines, one dedicated drone cleaning operator."
           if lang == "en" else "ستة خطوط خدمة متخصصة، ومشغّل واحد متخصص في تنظيف الدرونز.")
    return f"""{_page_hero(kicker, heading, sub)}
<section class="section">
  <div class="container">
    {_services_grid(lang)}
  </div>
</section>
"""


def build_service_detail(lang: str, slug: str) -> str:
    svc = SERVICES[slug][lang]
    icon_key = SERVICES[slug]["icon"]
    nav = NAV[lang]
    benefits = "".join(f'<li>{icon("check", "icon-sm")}<span>{b}</span></li>' for b in svc["benefits"])
    steps = "".join(f"""<div class="process-step reveal">
      <div class="process-step-num">{i}</div>
      <h3>{t}</h3>
      <p>{d}</p>
    </div>""" for i, (t, d) in enumerate(svc["process"], start=1))
    how_it_works = "How It Works" if lang == "en" else "كيف نعمل"
    key_benefits = "Key Benefits" if lang == "en" else "أهم المزايا"
    other_services = "Other Services" if lang == "en" else "خدمات أخرى"
    others = [s for s in SERVICES_ORDER if s != slug]
    other_cards = "".join(_service_card(lang, s, "Learn More" if lang == "en" else "اعرف أكثر") for s in others[:3])
    return f"""<section class="page-hero service-hero">
  <div class="container service-hero-inner">
    <div>
      <p class="kicker reveal">{nav['services']}</p>
      <h1 class="reveal">{svc['title']}</h1>
      <p class="hero-sub reveal">{svc['tagline']}</p>
    </div>
    <div class="service-hero-icon reveal" aria-hidden="true">{icon(icon_key, 'icon-xl')}</div>
  </div>
</section>
{_photo_banner(SERVICE_PHOTOS[slug], lang, 'eager')}
<section class="section">
  <div class="container narrow">
    <p class="lede reveal">{svc['short']}</p>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <h2 class="section-title reveal">{key_benefits}</h2>
    <ul class="benefits-list">{benefits}</ul>
  </div>
</section>
<section class="section">
  <div class="container">
    <h2 class="section-title reveal">{how_it_works}</h2>
    <div class="grid process-grid">{steps}</div>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <h2 class="section-title reveal">{other_services}</h2>
    <div class="grid services-grid">{other_cards}</div>
  </div>
</section>
{_cta_band(lang, svc['title'], '', NAV[lang]['cta'])}
"""


# ---------------------------------------------------------- TECHNOLOGY -----

def build_technology(lang: str) -> str:
    t = TECHNOLOGY[lang]
    sections = "".join(f"""<div class="tech-card reveal">
      <div class="tech-card-icon">{icon(key, 'icon-lg')}</div>
      <h3>{title}</h3>
      <p>{desc}</p>
    </div>""" for key, title, desc in t["sections"])
    return f"""{_page_hero(t['title'], t['hero'])}
{_photo_banner('drone-equipment', lang, 'eager')}
<section class="section">
  <div class="container narrow">
    <p class="lede reveal">{t['intro']}</p>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="grid tech-grid">{sections}</div>
  </div>
</section>
<section class="section">
  <div class="container narrow">
    <h2 class="section-title reveal">{t['investment_title']}</h2>
    <p class="reveal">{t['investment']}</p>
  </div>
</section>
"""


# ------------------------------------------------------------- PROJECTS -----

def build_projects(lang: str) -> str:
    p = PROJECTS[lang]
    cards = "".join(f"""<article class="card project-card reveal">
      <div class="project-card-photo">
        {photo_img(PROJECT_CATEGORY_PHOTOS[key], lang, 'project-card-img')}
        <span class="card-icon project-card-icon">{icon(key, 'icon-lg')}</span>
      </div>
      <h3>{title}</h3>
      <p>{desc}</p>
      <span class="project-placeholder-tag">{'Representative category' if lang == 'en' else 'فئة تمثيلية'}</span>
    </article>""" for key, title, desc in p["categories"])
    return f"""{_page_hero(p['title'], p['hero'])}
<section class="section">
  <div class="container narrow">
    <p class="lede reveal">{p['intro']}</p>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="grid project-grid">{cards}</div>
    <p class="fine-print reveal">{p['note']}</p>
  </div>
</section>
"""


# ----------------------------------------------------------------- BLOG -----

def _format_date(iso: str, lang: str) -> str:
    y, m, d = iso.split("-")
    months_en = ["", "January", "February", "March", "April", "May", "June",
                 "July", "August", "September", "October", "November", "December"]
    months_ar = ["", "يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو",
                 "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"]
    months = months_ar if lang == "ar" else months_en
    return f"{months[int(m)]} {int(d)}, {y}" if lang == "en" else f"{int(d)} {months[int(m)]} {y}"


def build_blog_index(lang: str) -> str:
    nav = NAV[lang]
    heading = "Insights From the Field" if lang == "en" else "رؤى من الميدان"
    read_more = "Read Article" if lang == "en" else "اقرأ المقال"
    cards = []
    for slug in BLOG_ORDER:
        post = BLOG_POSTS[slug]
        p = post[lang]
        cards.append(f"""<article class="card blog-card reveal">
      <div class="card-icon">{icon(post['icon'], 'icon-lg')}</div>
      <p class="blog-date">{_format_date(p['date'], lang)}</p>
      <h3><a href="{url_for(lang, f'blog/{slug}')}">{p['title']}</a></h3>
      <p>{p['excerpt']}</p>
      <a class="card-link" href="{url_for(lang, f'blog/{slug}')}">{read_more}{icon('arrow', 'icon-sm icon-end')}</a>
    </article>""")
    return f"""{_page_hero(nav['blog'], heading)}
<section class="section">
  <div class="container">
    <div class="grid blog-grid">{''.join(cards)}</div>
  </div>
</section>
"""


def build_blog_post(lang: str, slug: str) -> str:
    post = BLOG_POSTS[slug]
    p = post[lang]
    nav = NAV[lang]
    paragraphs = "".join(f"<p>{para}</p>" for para in p["body"])
    back_to_blog = "Back to Blog" if lang == "en" else "العودة إلى المدونة"
    return f"""<article class="section blog-post">
  <div class="container narrow">
    <p class="kicker reveal">{_format_date(p['date'], lang)}</p>
    <h1 class="reveal">{p['title']}</h1>
    <figure class="photo-banner photo-banner-post reveal">{photo_img(BLOG_PHOTOS[slug], lang, 'photo-banner-img', 'eager')}</figure>
    <div class="blog-post-body reveal">{paragraphs}</div>
    <a class="card-link" href="{url_for(lang, 'blog/index')}">{icon('arrow', 'icon-sm icon-start icon-rotate')}{back_to_blog}</a>
  </div>
</article>
{_cta_band(lang, nav['cta'], '', nav['cta'])}
"""


# ---------------------------------------------------------------- CONTACT --

def build_contact(lang: str) -> str:
    c = CONTACT_PAGE[lang]
    service_options = "".join(
        f'<option value="{SERVICES[slug][lang]["title"]}">{SERVICES[slug][lang]["title"]}</option>'
        for slug in SERVICES_ORDER
    )
    return f"""{_page_hero(c['title'], c['hero'], c['intro'])}
<section class="section">
  <div class="container contact-grid">
    <div class="contact-info reveal">
      <h2>{c['office_title']}</h2>
      <ul class="contact-info-list">
        <li>{icon('pin', 'icon-md')}<span>{SITE[lang]['city']}</span></li>
        <li><a href="{CONTACT['phone1_href']}">{icon('phone', 'icon-md')}<span>{CONTACT['phone1']}</span></a></li>
        <li><a href="{CONTACT['phone2_href']}">{icon('phone', 'icon-md')}<span>{CONTACT['phone2']}</span></a></li>
        <li><a href="{CONTACT['email_href']}">{icon('mail', 'icon-md')}<span>{CONTACT['email']}</span></a></li>
      </ul>
      <figure class="contact-photo">{photo_img('riyadh-skyline', lang, 'contact-photo-img')}</figure>
      <div class="map-placeholder" role="img" aria-label="{c['map_label']}">
        <svg viewBox="0 0 200 140" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
          <rect width="200" height="140" fill="none"/>
          <path d="M10 110 L40 70 L70 95 L100 50 L130 85 L160 60 L190 100" stroke="currentColor" stroke-width="1.5" fill="none" opacity="0.4"/>
          <circle cx="100" cy="60" r="5" fill="currentColor"/>
        </svg>
        <span>{c['map_label']}</span>
      </div>
    </div>
    <form class="contact-form reveal" id="contact-form" data-formspree-endpoint="https://formspree.io/f/YOUR_FORM_ID" novalidate>
      <!-- Replace YOUR_FORM_ID above (and in /assets/js/main.js) with your real Formspree endpoint. See README.md. -->
      <div class="form-row">
        <label for="name">{c['form_name']}</label>
        <input type="text" id="name" name="name" required autocomplete="name">
      </div>
      <div class="form-row form-row-split">
        <div>
          <label for="email">{c['form_email']}</label>
          <input type="email" id="email" name="email" required autocomplete="email">
        </div>
        <div>
          <label for="phone">{c['form_phone']}</label>
          <input type="tel" id="phone" name="phone" autocomplete="tel">
        </div>
      </div>
      <div class="form-row">
        <label for="service">{c['form_service']}</label>
        <select id="service" name="service">
          {service_options}
          <option value="{c['form_service_other']}">{c['form_service_other']}</option>
        </select>
      </div>
      <div class="form-row">
        <label for="message">{c['form_message']}</label>
        <textarea id="message" name="message" rows="5" required></textarea>
      </div>
      <button type="submit" class="btn btn-accent form-submit">
        <span class="form-submit-label">{c['form_submit']}</span>
      </button>
      <p class="form-status" id="form-status" role="status" aria-live="polite"
         data-sending="{c['form_sending']}" data-success="{c['form_success']}"
         data-error="{c['form_error']}" data-setup-error="{c['form_setup_error']}"></p>
    </form>
  </div>
</section>
"""
