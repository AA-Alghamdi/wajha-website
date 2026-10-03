"""All textual content for the WAJHA site, keyed by language ('en' / 'ar').

Numeric marketing stats beyond "100+ team members" and "largest fleet in KSA"
are placeholder figures invented to populate the stats section. This is
flagged again in README; do not treat them as verified.
"""

SITE = {
    "en": {
        "company": "WAJHA",
        "tagline": "Advanced Drone Cleaning Solutions",
        "full_name": "WAJHA for Advanced Drone Cleaning Solutions",
        "city": "Riyadh, Saudi Arabia",
        "dir": "ltr",
        "lang": "en",
        "og_locale": "en_US",
    },
    "ar": {
        "company": "وجهة",
        "tagline": "حلول تنظيف متقدمة بالطائرات المسيّرة",
        "full_name": "وجهة لحلول تنظيف الدرونز المتقدمة",
        "city": "الرياض، المملكة العربية السعودية",
        "dir": "rtl",
        "lang": "ar",
        "og_locale": "ar_SA",
    },
}

CONTACT = {
    "phone1": "+966 11 488 3555",
    "phone2": "+966 11 488 3444",
    "phone1_href": "tel:+966114883555",
    "phone2_href": "tel:+966114883444",
    "email": "info@wajha.sa",
    "email_href": "mailto:info@wajha.sa",
}

NAV = {
    "en": {
        "home": "Home", "about": "About", "services": "Services",
        "technology": "Technology", "projects": "Projects", "blog": "Blog",
        "contact": "Contact", "cta": "Get a Quote", "lang_switch": "العربية",
        "skip": "Skip to main content",
    },
    "ar": {
        "home": "الرئيسية", "about": "من نحن", "services": "الخدمات",
        "technology": "التقنية", "projects": "المشاريع", "blog": "المدونة",
        "contact": "تواصل معنا", "cta": "اطلب عرض سعر", "lang_switch": "English",
        "skip": "تجاوز إلى المحتوى الرئيسي",
    },
}

FOOTER = {
    "en": {
        "blurb": "WAJHA is Saudi Arabia's largest dedicated drone cleaning company, "
                  "delivering safe, precise, high-altitude cleaning for buildings, energy, "
                  "industry, infrastructure, marine, and aviation clients across the Kingdom.",
        "quick_links": "Quick Links", "our_services": "Our Services", "get_in_touch": "Get in Touch",
        "rights": "All rights reserved.",
        "placeholder_note": "",
    },
    "ar": {
        "blurb": "وجهة هي أكبر شركة متخصصة في تنظيف الدرونز في المملكة العربية السعودية، "
                  "تقدّم تنظيفًا آمنًا ودقيقًا للمرتفعات والمواقع الصعبة لعملاء المباني والطاقة "
                  "والصناعة والبنية التحتية والقطاع البحري والطيران في جميع مناطق المملكة.",
        "quick_links": "روابط سريعة", "our_services": "خدماتنا", "get_in_touch": "تواصل معنا",
        "rights": "جميع الحقوق محفوظة.",
        "placeholder_note": "",
    },
}

SERVICES_ORDER = [
    "facade-cleaning", "solar-panel-cleaning", "road-signs",
    "industrial-walls", "marine-vessels", "aircraft-cleaning",
]

SERVICES = {
    "facade-cleaning": {
        "icon": "facade",
        "en": {
            "title": "Building Facade Cleaning",
            "short": "Professional exterior cleaning for high-rise buildings, commercial "
                      "properties, and residential complexes, without scaffolding or rope access.",
            "tagline": "Every floor, every facade, without a single rope or scaffold platform.",
            "benefits": [
                "No scaffolding or rope access required at any building height",
                "Minimal disruption to occupants, tenants, and daily operations",
                "Consistent access to complex facade geometry and curtain-wall glass",
                "Faster turnaround than traditional access methods",
                "Reduced safety exposure for ground and aerial crews alike",
            ],
            "process": [
                ("Site Survey & Risk Assessment", "We assess the building envelope, surrounding airspace, and site-specific hazards before any flight is planned."),
                ("Flight Path Planning", "A precision flight plan is mapped to cover every facade section safely and efficiently."),
                ("Precision Drone Cleaning", "Trained pilots operate industrial-grade cleaning drones along the planned path, section by section."),
                ("Quality Inspection & Handover", "Every elevation is inspected on completion and the results are handed over to the client."),
            ],
        },
        "ar": {
            "title": "تنظيف واجهات المباني",
            "short": "تنظيف احترافي لواجهات المباني العالية والعقارات التجارية والمجمعات السكنية، بدون سقالات أو حبال تدلّي.",
            "tagline": "كل طابق وكل واجهة، دون الحاجة إلى سقالة أو حبل تدلّي واحد.",
            "benefits": [
                "لا حاجة لسقالات أو حبال تدلّي بغض النظر عن ارتفاع المبنى",
                "أقل تأثير على الشاغلين والمستأجرين وسير العمل اليومي",
                "تغطية موثوقة لهندسة الواجهات المعقدة والواجهات الزجاجية",
                "وقت تنفيذ أسرع مقارنة بوسائل الوصول التقليدية",
                "تقليل التعرّض الأمني لفرق العمل الأرضية والجوية على حد سواء",
            ],
            "process": [
                ("مسح الموقع وتقييم المخاطر", "نقوم بتقييم هيكل المبنى والمجال الجوي المحيط والمخاطر الخاصة بالموقع قبل التخطيط لأي طلعة جوية."),
                ("تخطيط مسار الطيران", "يتم رسم مسار طيران دقيق لتغطية كل قسم من الواجهة بأمان وكفاءة."),
                ("تنظيف دقيق بالدرون", "يقوم طيارون مدرّبون بتشغيل درونز تنظيف صناعية عالية الجودة وفق المسار المخطط، قسمًا تلو الآخر."),
                ("فحص الجودة والتسليم", "يتم فحص كل واجهة عند الانتهاء، وتُسلَّم النتائج للعميل."),
            ],
        },
    },
    "solar-panel-cleaning": {
        "icon": "solar",
        "en": {
            "title": "Solar Panel Cleaning",
            "short": "Maintain peak energy efficiency with regular solar panel cleaning. "
                      "Specialized drones remove dust, sand, and debris without damaging "
                      "delicate photovoltaic surfaces.",
            "tagline": "Keep every panel generating at its best, without touching the surface by hand.",
            "benefits": [
                "Helps restore energy output lost to dust, sand, and soiling",
                "Gentle, damage-free cleaning of delicate photovoltaic surfaces",
                "Scheduled maintenance programs for solar farms and rooftop arrays",
                "Efficient, low-water coverage of large panel fields",
                "Rapid turnaround that minimizes generation downtime",
            ],
            "process": [
                ("Site Assessment", "We review array layout, access points, and soiling conditions across the site."),
                ("Soiling Review", "Panel surfaces are checked to plan the right cleaning pass for current conditions."),
                ("Drone-Based Cleaning Pass", "Specialized drones clean each row without contact damage to photovoltaic cells."),
                ("Performance Verification", "A post-clean walk-through confirms panel condition and coverage."),
            ],
        },
        "ar": {
            "title": "تنظيف الألواح الشمسية",
            "short": "حافظ على أعلى كفاءة لتوليد الطاقة من خلال التنظيف الدوري للألواح الشمسية. تزيل درونز متخصصة الغبار والرمال والأتربة دون إتلاف الأسطح الكهروضوئية الحساسة.",
            "tagline": "حافظ على أداء كل لوح شمسي دون لمس السطح يدويًا.",
            "benefits": [
                "يساعد على استعادة الطاقة المفقودة بسبب الغبار والرمل والأتربة",
                "تنظيف لطيف لا يُلحق الضرر بالأسطح الكهروضوئية الحساسة",
                "برامج صيانة دورية لمحطات الطاقة الشمسية والمصفوفات على الأسطح",
                "تغطية فعّالة لحقول الألواح الواسعة باستخدام كمية ماء منخفضة",
                "وقت تنفيذ سريع يقلّل من فترة توقف التوليد",
            ],
            "process": [
                ("تقييم الموقع", "نراجع تخطيط المصفوفة ونقاط الوصول وحالة التلوث السطحي في الموقع."),
                ("فحص حالة الأتربة", "تُفحص أسطح الألواح لتحديد طريقة التنظيف المناسبة للحالة الراهنة."),
                ("تنظيف بالدرون", "تقوم درونز متخصصة بتنظيف كل صف دون أي تلامس يضر بالخلايا الكهروضوئية."),
                ("التحقق من الأداء", "جولة تفقدية بعد التنظيف للتأكد من حالة الألواح ومدى التغطية."),
            ],
        },
    },
    "road-signs": {
        "icon": "road-sign",
        "en": {
            "title": "Road Signs & Street Infrastructure",
            "short": "Keep traffic signs, street lights, and public infrastructure clean and "
                      "visible with efficient drone cleaning for hard-to-reach roadside installations.",
            "tagline": "Clear signage and safer roads, reached without lane closures.",
            "benefits": [
                "Improves sign and signal visibility for road safety",
                "Reaches tall gantries, overhead signs, and light poles directly",
                "No lane closures or extended traffic disruption required",
                "Efficient route-based cleaning across large infrastructure networks",
                "Lower cost than crane- or lift-based maintenance",
            ],
            "process": [
                ("Route & Asset Mapping", "Signs, gantries, and lighting assets along the route are mapped and prioritized."),
                ("Traffic-Aware Scheduling", "Cleaning windows are scheduled to minimize impact on traffic flow."),
                ("Drone Cleaning Pass", "Each asset is cleaned in sequence along the planned route."),
                ("Visibility Verification", "A final check confirms signage is clear and fully visible."),
            ],
        },
        "ar": {
            "title": "تنظيف لوحات الطرق والبنية التحتية",
            "short": "حافظ على نظافة ووضوح لوحات المرور وإنارة الشوارع والبنية التحتية العامة من خلال تنظيف فعّال بالدرون للمنشآت صعبة الوصول على جانب الطريق.",
            "tagline": "لوحات أوضح وطرق أكثر أمانًا، دون الحاجة لإغلاق أي مسار.",
            "benefits": [
                "تحسين وضوح اللوحات والإشارات لتعزيز السلامة المرورية",
                "الوصول المباشر إلى البوابات العلوية واللوحات المعلّقة وأعمدة الإنارة",
                "دون الحاجة لإغلاق المسارات أو تعطيل حركة المرور لفترات طويلة",
                "تنظيف فعّال على مستوى المسار لشبكات البنية التحتية الواسعة",
                "تكلفة أقل من وسائل الصيانة بالرافعات أو السلال الهوائية",
            ],
            "process": [
                ("رسم خريطة المسار والأصول", "يتم رصد اللوحات والبوابات وأصول الإنارة على طول المسار وترتيبها حسب الأولوية."),
                ("جدولة مرتبطة بحركة المرور", "تُحدَّد أوقات التنظيف لتقليل التأثير على تدفق حركة المرور."),
                ("تنظيف بالدرون", "يتم تنظيف كل أصل بالتتابع على طول المسار المخطط."),
                ("التحقق من الوضوح", "فحص نهائي للتأكد من وضوح اللوحات ورؤيتها بالكامل."),
            ],
        },
    },
    "industrial-walls": {
        "icon": "factory",
        "en": {
            "title": "Factory & Industrial Walls",
            "short": "Comprehensive cleaning for industrial facilities, warehouses, and "
                      "manufacturing plants, removing grime, dust, and pollutants from large "
                      "exterior surfaces.",
            "tagline": "Large-scale exteriors, cleaned without shutting operations down.",
            "benefits": [
                "Removes industrial grime, dust, and pollutant buildup",
                "Covers large exterior wall and roof surfaces efficiently",
                "Minimal disruption to ongoing plant operations",
                "Improves facility appearance and helps protect surfaces from buildup",
                "Scheduled maintenance programs available for recurring upkeep",
            ],
            "process": [
                ("Facility Walkthrough & Hazard Review", "We review the facility layout and identify any site-specific operational hazards."),
                ("Cleaning Plan & Scheduling", "A cleaning plan is scheduled around plant operations to minimize disruption."),
                ("Drone-Based Cleaning", "Exterior walls and roof surfaces are cleaned systematically, section by section."),
                ("Final Inspection", "Completed areas are inspected and signed off with the facility team."),
            ],
        },
        "ar": {
            "title": "تنظيف جدران المصانع والمنشآت الصناعية",
            "short": "تنظيف شامل للمنشآت الصناعية والمستودعات ومصانع التصنيع، يزيل الأوساخ والغبار والملوثات من الأسطح الخارجية الواسعة.",
            "tagline": "واجهات صناعية واسعة تُنظَّف دون إيقاف التشغيل.",
            "benefits": [
                "إزالة الأوساخ الصناعية والغبار والملوثات المتراكمة",
                "تغطية فعّالة للجدران الخارجية وأسطح الأسقف الواسعة",
                "أقل تأثير ممكن على استمرارية تشغيل المصنع",
                "تحسين المظهر العام للمنشأة والمساهمة في حمايتها من التراكمات",
                "برامج صيانة دورية متاحة للصيانة المستمرة",
            ],
            "process": [
                ("جولة تفقدية وتقييم المخاطر", "نراجع تخطيط المنشأة ونحدد أي مخاطر تشغيلية خاصة بالموقع."),
                ("خطة التنظيف والجدولة", "تُجدوَل خطة التنظيف بما يتوافق مع عمليات المصنع لتقليل التعطيل."),
                ("تنظيف بالدرون", "يتم تنظيف الجدران الخارجية وأسطح الأسقف بشكل منظم، قسمًا تلو الآخر."),
                ("الفحص النهائي", "تُفحص المناطق المكتملة ويتم التوقيع عليها مع فريق المنشأة."),
            ],
        },
    },
    "marine-vessels": {
        "icon": "marine",
        "en": {
            "title": "Marine Vessel Cleaning",
            "short": "Professional hull and deck cleaning for yachts, boats, and commercial "
                      "vessels, cleaned thoroughly while the vessel remains in water.",
            "tagline": "Hull and deck cleaning without taking the vessel out of the water.",
            "benefits": [
                "Hull and deck cleaning without dry-docking the vessel",
                "High-speed specialized drones built for marine operating conditions",
                "Helps keep hull surfaces clear of fouling buildup between dry-dock cycles",
                "Safe operation around crewed vessels while afloat",
                "Flexible scheduling for commercial fleets and leisure vessels alike",
            ],
            "process": [
                ("Vessel Assessment", "We assess hull condition, deck layout, and the vessel's berth or mooring environment."),
                ("Access & Safety Planning", "A safety and access plan is set for operating around the vessel and crew."),
                ("High-Speed Drone Cleaning", "Specialized high-speed drones clean hull and deck surfaces in planned passes."),
                ("Post-Clean Inspection", "Surfaces are inspected after cleaning and results reviewed with the vessel operator."),
            ],
        },
        "ar": {
            "title": "تنظيف السفن والمراكب البحرية",
            "short": "تنظيف احترافي لهياكل وأسطح اليخوت والقوارب والسفن التجارية، مع تنظيف شامل بينما تبقى السفينة في الماء.",
            "tagline": "تنظيف الهيكل والسطح دون الحاجة لإخراج السفينة من الماء.",
            "benefits": [
                "تنظيف الهيكل والسطح دون سحب السفينة إلى الحوض الجاف",
                "درونز متخصصة عالية السرعة مصممة لظروف التشغيل البحرية",
                "تساهم في الحفاظ على نظافة الهيكل من التراكمات بين دورات الحوض الجاف",
                "تشغيل آمن حول السفن المطاقمة وهي عائمة",
                "جدولة مرنة تناسب الأساطيل التجارية والمراكب الترفيهية على حد سواء",
            ],
            "process": [
                ("تقييم السفينة", "نقيّم حالة الهيكل وتخطيط السطح وبيئة الرصيف أو الإرساء الخاصة بالسفينة."),
                ("التخطيط للوصول والسلامة", "يتم وضع خطة سلامة ووصول للتشغيل حول السفينة وطاقمها."),
                ("تنظيف بدرونز عالية السرعة", "تقوم درونز متخصصة عالية السرعة بتنظيف أسطح الهيكل والسطح وفق مسارات مخططة."),
                ("فحص ما بعد التنظيف", "تُفحص الأسطح بعد التنظيف ويتم مراجعة النتائج مع مشغّل السفينة."),
            ],
        },
    },
    "aircraft-cleaning": {
        "icon": "aircraft",
        "en": {
            "title": "Aircraft Cleaning",
            "short": "Specialized exterior cleaning for aircraft that meets aviation industry "
                      "standards, with safe, efficient cleaning for fuselage, wings, and tail sections.",
            "tagline": "Fuselage, wings, and tail: cleaned with aviation-grade precision.",
            "benefits": [
                "Specialized high-speed drones built for fuselage, wing, and tail sections",
                "Operations coordinated to aviation-appropriate safety procedures",
                "Can reduce aircraft ground downtime versus manual exterior cleaning",
                "Careful, precision-controlled operation around sensitive surfaces",
                "Scheduled or on-demand cleaning programs for fleet operators",
            ],
            "process": [
                ("Pre-Flight Site & Aircraft Assessment", "The aircraft, apron area, and surrounding ground operations are assessed before any drone activity begins."),
                ("Ground & Airport Coordination", "Cleaning windows are coordinated with ground handling and airport procedures."),
                ("Precision Drone Cleaning", "Specialized high-speed drones clean fuselage, wing, and tail sections with controlled precision."),
                ("Final Inspection & Sign-off", "Surfaces are inspected and the completed work is signed off with the operator."),
            ],
        },
        "ar": {
            "title": "تنظيف الطائرات",
            "short": "تنظيف خارجي متخصص للطائرات يستوفي معايير صناعة الطيران، بتنظيف آمن وفعّال لجسم الطائرة والأجنحة والذيل.",
            "tagline": "جسم الطائرة والأجنحة والذيل، بتنظيف بدقة تناسب معايير الطيران.",
            "benefits": [
                "درونز متخصصة عالية السرعة مصممة لجسم الطائرة والأجنحة والذيل",
                "تنسيق العمليات وفق إجراءات السلامة المناسبة لبيئة الطيران",
                "يمكن أن يقلّل من فترة توقف الطائرة أرضًا مقارنة بالتنظيف اليدوي الخارجي",
                "تشغيل دقيق ومتحكّم به حول الأسطح الحساسة",
                "برامج تنظيف مجدولة أو عند الطلب لمشغّلي الأساطيل",
            ],
            "process": [
                ("تقييم الموقع والطائرة قبل التشغيل", "يتم تقييم الطائرة ومنطقة الساحة والعمليات الأرضية المحيطة قبل بدء أي نشاط للدرون."),
                ("التنسيق مع المناولة الأرضية والمطار", "تُنسَّق أوقات التنظيف مع إجراءات المناولة الأرضية والمطار."),
                ("تنظيف دقيق بالدرون", "تقوم درونز متخصصة عالية السرعة بتنظيف جسم الطائرة والأجنحة والذيل بدقة متحكّم بها."),
                ("الفحص النهائي والتوقيع", "تُفحص الأسطح ويتم التوقيع على العمل المكتمل مع المشغّل."),
            ],
        },
    },
}
