"""Licensed stock photography registry.

Every file here was downloaded from Pexels or Unsplash under their standard
free license (commercial use allowed, no attribution legally required). Full
source attribution (photographer, source URL, license) is recorded in
PHOTO_CREDITS.md at the project root, not in this module.

None of these photos depict WAJHA's own staff, drones, offices, or a real
completed project. They are generic, illustrative stand-ins, and alt text below
is deliberately plain and generic for that reason: it must never claim a
specific real person, piece of equipment, or project that doesn't exist.
Swap in real company photography when available; see README.md.
"""

PHOTOS = {
    "hero-drone": {
        "file": "hero-drone-flight.jpg", "w": 1600, "h": 897,
        "alt": {
            "en": "Aerial drone in flight against a clear sky",
            "ar": "طائرة مسيّرة تحلّق في سماء صافية",
        },
    },
    "riyadh-skyline": {
        "file": "riyadh-skyline.jpg", "w": 1200, "h": 1600,
        "alt": {
            "en": "Aerial view of the Riyadh, Saudi Arabia skyline",
            "ar": "منظر جوي لأفق مدينة الرياض، المملكة العربية السعودية",
        },
    },
    "drone-equipment": {
        "file": "drone-equipment-closeup.jpg", "w": 1600, "h": 1066,
        "alt": {
            "en": "Close-up of a multirotor drone in flight",
            "ar": "لقطة مقربة لطائرة مسيّرة متعددة المراوح أثناء الطيران",
        },
    },
    "service-facade": {
        "file": "service-facade.jpg", "w": 1200, "h": 1600,
        "alt": {
            "en": "Glass facade of a modern high-rise building",
            "ar": "واجهة زجاجية لمبنى حديث شاهق",
        },
    },
    "service-solar": {
        "file": "service-solar.jpg", "w": 1600, "h": 898,
        "alt": {
            "en": "Solar panel array in a desert setting",
            "ar": "مصفوفة ألواح شمسية في بيئة صحراوية",
        },
    },
    "service-road-signs": {
        "file": "service-road-signs.jpg", "w": 1600, "h": 1066,
        "alt": {
            "en": "Street sign and traffic light mounted on a roadside pole",
            "ar": "لوحة شارع وإشارة مرور على عمود بجانب الطريق",
        },
    },
    "service-industrial": {
        "file": "service-industrial.jpg", "w": 1600, "h": 1066,
        "alt": {
            "en": "Exterior wall of an industrial facility",
            "ar": "جدار خارجي لمنشأة صناعية",
        },
    },
    "service-marine": {
        "file": "service-marine.jpg", "w": 1600, "h": 1091,
        "alt": {
            "en": "Yachts moored at a marina",
            "ar": "يخوت مرساة في مرسى بحري",
        },
    },
    "service-aircraft": {
        "file": "service-aircraft.jpg", "w": 1600, "h": 1066,
        "alt": {
            "en": "Close-up of an aircraft wing and fuselage",
            "ar": "لقطة مقربة لجناح طائرة وجسمها",
        },
    },
    "blog-solar-dust": {
        "file": "blog-solar-dust.jpg", "w": 1600, "h": 898,
        "alt": {
            "en": "Aerial view of solar panels in a desert landscape",
            "ar": "منظر جوي لألواح شمسية في بيئة صحراوية",
        },
    },
    "blog-airspace": {
        "file": "blog-airspace.jpg", "w": 1600, "h": 1066,
        "alt": {
            "en": "Silhouette of a drone in flight against the sky",
            "ar": "ظل طائرة مسيّرة أثناء الطيران في السماء",
        },
    },
}

# Service slug -> photo key, in SERVICES_ORDER.
SERVICE_PHOTOS = {
    "facade-cleaning": "service-facade",
    "solar-panel-cleaning": "service-solar",
    "road-signs": "service-road-signs",
    "industrial-walls": "service-industrial",
    "marine-vessels": "service-marine",
    "aircraft-cleaning": "service-aircraft",
}

# Projects-page category key (matches SERVICE_ICON_KEYS values) -> photo key.
PROJECT_CATEGORY_PHOTOS = {
    "facade": "service-facade",
    "solar": "service-solar",
    "road-sign": "service-road-signs",
    "factory": "service-industrial",
    "marine": "service-marine",
    "aircraft": "service-aircraft",
}

# Blog slug -> photo key. drones-vs-scaffolding reuses the facade photo.
BLOG_PHOTOS = {
    "solar-dust-efficiency": "blog-solar-dust",
    "drones-vs-scaffolding": "service-facade",
    "drone-airspace-safety": "blog-airspace",
}


def photo_img(key: str, lang: str, css_class: str = "photo-img", loading: str = "lazy") -> str:
    p = PHOTOS[key]
    return (f'<img class="{css_class}" src="/assets/img/photos/{p["file"]}" '
            f'width="{p["w"]}" height="{p["h"]}" alt="{p["alt"][lang]}" '
            f'loading="{loading}" decoding="async">')
