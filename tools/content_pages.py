"""Page-level content: home, about, technology, projects, contact, blog, SEO."""

from content import SERVICES

# ---------------------------------------------------------------- HOME -----

HOME = {
    "en": {
        "hero_kicker": "Saudi Arabia's Largest Drone Cleaning Company",
        "hero_title": "Precision Drone Cleaning. Zero Scaffolding. Zero Compromise.",
        "hero_sub": "WAJHA delivers safe, efficient, high-altitude and hard-to-reach cleaning "
                    "for buildings, solar farms, industry, infrastructure, marine fleets, and "
                    "aircraft across the Kingdom, all without scaffolding or rope access.",
        "hero_cta_primary": "Get a Quote",
        "hero_cta_secondary": "Explore Services",
        "value_props_title": "Why Facilities Choose WAJHA",
        "value_props": [
            ("shield", "Safer by Design", "No scaffolding, no rope access, far less risk exposure for ground and aerial crews."),
            ("bolt", "Faster Turnaround", "Drones reach difficult heights and surfaces in a fraction of the time of traditional methods."),
            ("target", "Precision Coverage", "Flight-planned passes reach every section consistently, with no missed spots."),
            ("users", "100+ Specialists", "A large, trained team of certified pilots and technicians across the Kingdom."),
        ],
        "services_title": "What We Clean",
        "services_sub": "Six specialized service lines, one dedicated drone cleaning operator.",
        "stats_title": "WAJHA by the Numbers",
        "stats_sub": "The Kingdom's largest dedicated drone cleaning operation.",
        "stats": [
            {"value": 100, "suffix": "+", "label": "Certified Pilots & Technicians"},
            {"value": 500, "suffix": "+", "label": "Projects Completed"},
            {"value": 6, "suffix": "", "label": "Cities Served Across the Kingdom"},
            {"value": 0, "suffix": "", "label": "Scaffolding Platforms Required", "is_badge": True},
        ],
        "stats_badge_label": "Largest Drone Cleaning Fleet in Saudi Arabia",
        "why_title": "Built to Operate at Scale",
        "why_items": [
            "The largest dedicated drone cleaning fleet in Saudi Arabia",
            "A single operator covering facades, solar, infrastructure, industry, marine, and aviation",
            "Pilots trained and operating in coordination with applicable civil aviation rules",
            "Scheduled maintenance programs as well as on-demand project work",
        ],
        "testimonials_title": "What Clients Say",
        "testimonials_note": "Sample testimonials. Replace with verified client feedback before publishing.",
        "testimonials": [
            ("“Switching to drone cleaning cut our facade maintenance downtime dramatically, with no scaffolding setup to wait on.”", "Facilities Manager (sample), Riyadh"),
            ("“Our panel output noticeably improves after every cleaning cycle, and the turnaround is fast.”", "Operations Lead (sample), Solar Sector"),
            ("“Professional crew, clear communication, and they worked around our plant schedule without disruption.”", "Plant Supervisor (sample), Industrial Sector"),
        ],
        "final_cta_title": "Ready to See WAJHA in Action?",
        "final_cta_sub": "Tell us about your site and we'll put together a cleaning plan built around it.",
        "final_cta_button": "Contact Our Team",
    },
    "ar": {
        "hero_kicker": "أكبر شركة لتنظيف الدرونز في المملكة العربية السعودية",
        "hero_title": "تنظيف دقيق بالطائرات المسيّرة. بدون سقالات. بدون تنازلات.",
        "hero_sub": "تقدّم وجهة تنظيفًا آمنًا وفعّالًا للمرتفعات والمواقع صعبة الوصول، للمباني، "
                    "ومحطات الطاقة الشمسية، والمصانع، والبنية التحتية، والأساطيل البحرية، والطائرات "
                    "في جميع مناطق المملكة، دون الحاجة لسقالات أو حبال تدلّي.",
        "hero_cta_primary": "اطلب عرض سعر",
        "hero_cta_secondary": "استكشف خدماتنا",
        "value_props_title": "لماذا تختار المنشآت وجهة",
        "value_props": [
            ("shield", "أكثر أمانًا بالتصميم", "دون سقالات أو حبال تدلّي، وبتعرّض أقل للمخاطر لفرق العمل الأرضية والجوية."),
            ("bolt", "تنفيذ أسرع", "تصل الدرونز إلى الارتفاعات والأسطح الصعبة في جزء من الوقت الذي تتطلبه الوسائل التقليدية."),
            ("target", "تغطية دقيقة", "مسارات طيران مخططة تصل إلى كل قسم بثبات، دون أي نقطة مفوّتة."),
            ("users", "أكثر من 100 متخصص", "فريق كبير ومدرّب من الطيارين والتقنيين المعتمدين في جميع مناطق المملكة."),
        ],
        "services_title": "ما الذي ننظّفه",
        "services_sub": "ستة خطوط خدمة متخصصة، ومشغّل واحد متخصص في تنظيف الدرونز.",
        "stats_title": "وجهة بالأرقام",
        "stats_sub": "أكبر عملية مخصصة لتنظيف الدرونز في المملكة.",
        "stats": [
            {"value": 100, "suffix": "+", "label": "طيار وتقني معتمد"},
            {"value": 500, "suffix": "+", "label": "مشروع مكتمل"},
            {"value": 6, "suffix": "", "label": "مدن مخدومة في جميع مناطق المملكة"},
            {"value": 0, "suffix": "", "label": "منصة سقالات مطلوبة", "is_badge": True},
        ],
        "stats_badge_label": "أكبر أسطول لتنظيف الدرونز في المملكة العربية السعودية",
        "why_title": "مصمّمون للعمل على نطاق واسع",
        "why_items": [
            "أكبر أسطول مخصص لتنظيف الدرونز في المملكة العربية السعودية",
            "مشغّل واحد يغطي الواجهات والطاقة الشمسية والبنية التحتية والصناعة والقطاع البحري والطيران",
            "طيارون مدرّبون يعملون بالتنسيق مع الأنظمة المعمول بها لطيران المدني",
            "برامج صيانة مجدولة إلى جانب أعمال المشاريع عند الطلب",
        ],
        "testimonials_title": "ماذا يقول عملاؤنا",
        "testimonials_note": "آراء نموذجية. تُستبدل بآراء حقيقية موثّقة من العملاء قبل النشر.",
        "testimonials": [
            ("“ساهم التحول إلى التنظيف بالدرون في خفض وقت توقف صيانة الواجهة بشكل كبير، دون انتظار تجهيز السقالات.”", "مدير منشأة (نموذجي)، الرياض"),
            ("“يتحسن أداء الألواح بشكل ملحوظ بعد كل دورة تنظيف، ووقت التنفيذ سريع.”", "مسؤول تشغيل (نموذجي)، قطاع الطاقة الشمسية"),
            ("“فريق محترف وتواصل واضح، وعملوا وفق جدول المصنع دون أي تعطيل.”", "مشرف مصنع (نموذجي)، القطاع الصناعي"),
        ],
        "final_cta_title": "هل أنت مستعد لرؤية وجهة أثناء العمل؟",
        "final_cta_sub": "أخبرنا عن موقعك وسنضع خطة تنظيف مصممة خصيصًا له.",
        "final_cta_button": "تواصل مع فريقنا",
    },
}

# --------------------------------------------------------------- ABOUT -----

ABOUT = {
    "en": {
        "title": "About WAJHA",
        "hero": "The Kingdom's Largest Dedicated Drone Cleaning Operator",
        "intro": "WAJHA was founded to modernize how Saudi Arabia cleans and maintains the "
                 "surfaces that keep buildings, energy infrastructure, and industry running, "
                 "replacing scaffolding and rope access with precision drone technology. Today, "
                 "WAJHA operates the largest dedicated drone cleaning fleet in the Kingdom, with "
                 "a team of over 100 certified pilots and technicians working across Riyadh and "
                 "beyond.",
        "mission_title": "Our Mission",
        "mission": "To make high-altitude and hard-to-reach cleaning safer, faster, and more "
                   "consistent for every client, from solar operators protecting energy yield "
                   "to facility managers protecting their buildings.",
        "why_drones_title": "Why Drones Instead of Scaffolding or Rope Access",
        "why_drones": [
            ("Safety", "Removing the need for workers to rig, climb, or suspend from scaffolding and ropes removes a major source of risk at height."),
            ("Speed", "A flight-planned drone pass covers large or tall surfaces far faster than manual rigging and access setup."),
            ("Consistency", "Planned flight paths cover every section the same way, every time, reducing missed spots."),
            ("Less Disruption", "No scaffolding footprint on the ground and no long rigging setup means less interruption to daily operations."),
        ],
        "team_title": "Our Team",
        "team": "WAJHA's team of 100+ pilots and technicians is trained to operate specialized "
                "cleaning drones safely across a wide range of environments, from residential "
                "towers to industrial plants, solar farms, ports, and airside aircraft stands. "
                "Pilots operate in coordination with applicable civil aviation rules and "
                "facility-specific safety procedures on every project.",
        "safety_title": "Our Safety & Quality Ethos",
        "safety": "Every project begins with a site risk assessment and a planned flight path, "
                  "and ends with an inspection and sign-off. We treat safety planning and quality "
                  "verification as standard steps on every job, not optional extras.",
        "cta_title": "Want to Work With the Largest Drone Cleaning Team in Saudi Arabia?",
        "cta_button": "Get in Touch",
    },
    "ar": {
        "title": "عن وجهة",
        "hero": "أكبر مشغّل مخصص لتنظيف الدرونز في المملكة",
        "intro": "تأسست وجهة لتحديث طريقة تنظيف وصيانة الأسطح التي تحافظ على استمرار عمل المباني "
                 "والبنية التحتية للطاقة والصناعة في المملكة العربية السعودية، عبر استبدال السقالات "
                 "وحبال التدلّي بتقنية الدرون الدقيقة. واليوم، تشغّل وجهة أكبر أسطول مخصص لتنظيف "
                 "الدرونز في المملكة، بفريق يضم أكثر من 100 طيار وتقني معتمد يعملون في الرياض وخارجها.",
        "mission_title": "رسالتنا",
        "mission": "جعل التنظيف في المرتفعات والمواقع صعبة الوصول أكثر أمانًا وسرعة واتساقًا لكل "
                   "عميل، من مشغّلي الطاقة الشمسية الذين يحافظون على إنتاجية الطاقة إلى مديري "
                   "المنشآت الذين يحافظون على مبانيهم.",
        "why_drones_title": "لماذا الدرونز بدلًا من السقالات أو حبال التدلّي",
        "why_drones": [
            ("السلامة", "إزالة الحاجة إلى تسلّق العمال أو تعليقهم على السقالات والحبال تُلغي مصدرًا رئيسيًا للخطر في المرتفعات."),
            ("السرعة", "تغطي طلعة الدرون المخطط لها الأسطح الواسعة أو العالية أسرع بكثير من التجهيز اليدوي للوصول."),
            ("الاتساق", "تغطي مسارات الطيران المخططة كل قسم بالطريقة نفسها في كل مرة، مما يقلل من النقاط المفوّتة."),
            ("أقل تعطيل", "عدم وجود سقالات على الأرض أو تجهيزات طويلة يعني تعطيلًا أقل لسير العمل اليومي."),
        ],
        "team_title": "فريقنا",
        "team": "يضم فريق وجهة أكثر من 100 طيار وتقني مدرّبين على تشغيل درونز التنظيف المتخصصة بأمان "
                "في بيئات متنوعة، من الأبراج السكنية إلى المصانع الصناعية ومحطات الطاقة الشمسية "
                "والموانئ ومواقف الطائرات. يعمل الطيارون بالتنسيق مع أنظمة الطيران المدني المعمول "
                "بها وإجراءات السلامة الخاصة بكل منشأة في كل مشروع.",
        "safety_title": "فلسفتنا في السلامة والجودة",
        "safety": "يبدأ كل مشروع بتقييم مخاطر الموقع ومسار طيران مخطط، وينتهي بفحص وتوقيع على "
                  "الإنجاز. نتعامل مع تخطيط السلامة والتحقق من الجودة كخطوات أساسية في كل عمل، "
                  "لا كإضافات اختيارية.",
        "cta_title": "تريد العمل مع أكبر فريق لتنظيف الدرونز في السعودية؟",
        "cta_button": "تواصل معنا",
    },
}

# ----------------------------------------------------------- TECHNOLOGY ----

TECHNOLOGY = {
    "en": {
        "title": "Our Technology",
        "hero": "A Fleet Built for Every Surface",
        "intro": "WAJHA operates the largest dedicated drone cleaning fleet in Saudi Arabia, "
                 "matching the right drone platform to each environment, from building facades "
                 "and solar arrays to the high-speed demands of marine hulls and aircraft "
                 "exteriors.",
        "sections": [
            ("bolt", "Our Fleet", "We deploy industrial-grade cleaning drones for buildings, "
             "solar, infrastructure, and industrial surfaces, alongside specialized high-speed "
             "drone platforms for marine vessels and aircraft, where faster, more controlled "
             "passes are required."),
            ("shield", "Safety Systems", "Every flight follows a pre-flight site risk "
             "assessment and a planned flight path. Pilots are trained to operate with "
             "airspace awareness and to coordinate with facility-specific safety procedures "
             "on every project."),
            ("target", "Precision Cleaning Systems", "Our drones use controlled cleaning "
             "mechanisms engineered to avoid damaging delicate surfaces such as photovoltaic "
             "cells, painted facades, and aircraft skin, while still removing dust, grime, and "
             "debris effectively."),
            ("users", "Pilot Training & Operations", "Pilots and technicians are trained to "
             "operate in coordination with the rules set by Saudi Arabia's General Authority "
             "of Civil Aviation (GACA) and with each site's own operating procedures."),
        ],
        "investment_title": "Continuous Fleet Investment",
        "investment": "As the largest drone cleaning operator in the Kingdom, WAJHA continues "
                      "to expand its fleet and refine its operating procedures to serve more "
                      "cities, more sectors, and more demanding environments.",
    },
    "ar": {
        "title": "تقنيتنا",
        "hero": "أسطول مصمم لكل نوع من الأسطح",
        "intro": "تشغّل وجهة أكبر أسطول مخصص لتنظيف الدرونز في المملكة العربية السعودية، "
                 "وتختار النوع المناسب من الدرونز لكل بيئة، من واجهات المباني والمصفوفات "
                 "الشمسية إلى المتطلبات عالية السرعة لهياكل السفن وأسطح الطائرات.",
        "sections": [
            ("bolt", "أسطولنا", "ننشر درونز تنظيف صناعية عالية الجودة للمباني والطاقة الشمسية "
             "والبنية التحتية والأسطح الصناعية، إلى جانب منصات درون متخصصة عالية السرعة للسفن "
             "والطائرات حيث تتطلب العمليات تمريرات أسرع وأكثر تحكمًا."),
            ("shield", "أنظمة السلامة", "تخضع كل طلعة جوية لتقييم مخاطر الموقع قبل التشغيل ومسار "
             "طيران مخطط. يتم تدريب الطيارين على التشغيل بوعي بالمجال الجوي والتنسيق مع إجراءات "
             "السلامة الخاصة بكل منشأة في كل مشروع."),
            ("target", "أنظمة تنظيف دقيقة", "تستخدم دروناتنا آليات تنظيف متحكّم بها مصممة لتجنّب "
             "إتلاف الأسطح الحساسة مثل الخلايا الكهروضوئية والواجهات المطلية وهياكل الطائرات، مع "
             "إزالة الغبار والأوساخ والأتربة بفعالية."),
            ("users", "تدريب الطيارين والتشغيل", "يتم تدريب الطيارين والتقنيين على العمل بالتنسيق "
             "مع الأنظمة التي وضعتها الهيئة العامة للطيران المدني في المملكة العربية السعودية "
             "ومع إجراءات التشغيل الخاصة بكل موقع."),
        ],
        "investment_title": "استثمار مستمر في الأسطول",
        "investment": "بصفتها أكبر مشغّل لتنظيف الدرونز في المملكة، تستمر وجهة في توسيع أسطولها "
                      "وتطوير إجراءات تشغيلها لخدمة مزيد من المدن والقطاعات والبيئات الأكثر تطلبًا.",
    },
}

# ------------------------------------------------------------- PROJECTS ----

PROJECTS = {
    "en": {
        "title": "Projects",
        "hero": "Where We Work",
        "intro": "As the largest drone cleaning operator in Saudi Arabia, WAJHA works across "
                 "the categories below. These are representative project categories, not "
                 "individual case studies. Project photography and detailed case studies will "
                 "be added here as they become available.",
        "categories": [
            ("facade", "Commercial High-Rise Facades", "Recurring and one-off exterior cleaning for office towers and commercial complexes across Riyadh."),
            ("solar", "Utility-Scale & Rooftop Solar", "Scheduled cleaning programs for solar farms and rooftop installations to help protect energy yield."),
            ("road-sign", "Municipal Road Infrastructure", "Cleaning programs for signage, gantries, and street lighting along key road networks."),
            ("factory", "Industrial & Manufacturing Facilities", "Exterior wall and roof cleaning for plants and warehouses with minimal disruption to operations."),
            ("marine", "Marine Fleets", "In-water hull and deck cleaning for commercial and leisure vessels."),
            ("aircraft", "Aviation Ground Support", "Specialized exterior cleaning coordinated with ground and airside procedures."),
        ],
        "note": "Representative categories shown, not verified individual case studies.",
    },
    "ar": {
        "title": "المشاريع",
        "hero": "أين نعمل",
        "intro": "بصفتها أكبر مشغّل لتنظيف الدرونز في المملكة العربية السعودية، تعمل وجهة عبر "
                 "الفئات أدناه. هذه فئات مشاريع تمثيلية وليست دراسات حالة فردية. وستُضاف صور "
                 "المشاريع ودراسات الحالة التفصيلية هنا عند توفرها.",
        "categories": [
            ("facade", "واجهات الأبراج التجارية", "تنظيف خارجي دوري وغير دوري لأبراج المكاتب والمجمعات التجارية في الرياض."),
            ("solar", "الطاقة الشمسية بمستوى المرافق والأسطح", "برامج تنظيف مجدولة لمحطات الطاقة الشمسية والمنشآت على الأسطح للمساهمة في حماية إنتاجية الطاقة."),
            ("road-sign", "البنية التحتية للطرق البلدية", "برامج تنظيف للوحات والبوابات العلوية وإنارة الشوارع على طول شبكات الطرق الرئيسية."),
            ("factory", "المنشآت الصناعية ومصانع التصنيع", "تنظيف الجدران الخارجية والأسقف للمصانع والمستودعات بأقل تعطيل ممكن للعمليات."),
            ("marine", "الأساطيل البحرية", "تنظيف الهيكل والسطح وهي في الماء للسفن التجارية والترفيهية."),
            ("aircraft", "الدعم الأرضي للطيران", "تنظيف خارجي متخصص منسّق مع إجراءات المناولة الأرضية وإجراءات الساحة."),
        ],
        "note": "الفئات المعروضة تمثيلية، وليست دراسات حالة فردية موثّقة.",
    },
}

# --------------------------------------------------------------- CONTACT ---

CONTACT_PAGE = {
    "en": {
        "title": "Contact Us",
        "hero": "Let's Talk About Your Site",
        "intro": "Reach WAJHA's team in Riyadh by phone, email, or the form below. We'll "
                 "respond with next steps for your project.",
        "form_name": "Full Name", "form_email": "Email Address", "form_phone": "Phone Number",
        "form_service": "Service of Interest", "form_service_other": "Other",
        "form_message": "Tell us about your site", "form_submit": "Send Message",
        "form_sending": "Sending…", "form_success": "Thank you. Your message has been sent and our team will be in touch shortly.",
        "form_error": "Something went wrong sending your message. Please try again, or reach us directly by phone or email.",
        "form_setup_error": "The contact form is not yet connected to an inbox. Please reach us directly by phone or email below.",
        "office_title": "Our Office", "phones_title": "Phone", "email_title": "Email",
        "map_label": "Riyadh, Saudi Arabia, serving clients across the Kingdom",
    },
    "ar": {
        "title": "تواصل معنا",
        "hero": "لنتحدث عن موقعك",
        "intro": "تواصل مع فريق وجهة في الرياض عبر الهاتف أو البريد الإلكتروني أو النموذج "
                 "أدناه، وسنرد عليك بخطوات العمل التالية لمشروعك.",
        "form_name": "الاسم الكامل", "form_email": "البريد الإلكتروني", "form_phone": "رقم الهاتف",
        "form_service": "الخدمة المطلوبة", "form_service_other": "أخرى",
        "form_message": "أخبرنا عن موقعك", "form_submit": "إرسال الرسالة",
        "form_sending": "جارٍ الإرسال…", "form_success": "شكرًا لك. تم إرسال رسالتك بنجاح، وسيتواصل معك فريقنا قريبًا.",
        "form_error": "حدث خطأ أثناء إرسال رسالتك. يرجى المحاولة مرة أخرى أو التواصل معنا مباشرة عبر الهاتف أو البريد الإلكتروني.",
        "form_setup_error": "نموذج التواصل غير مرتبط بعد ببريد إلكتروني. يرجى التواصل معنا مباشرة عبر الهاتف أو البريد الإلكتروني أدناه.",
        "office_title": "مكتبنا", "phones_title": "الهاتف", "email_title": "البريد الإلكتروني",
        "map_label": "الرياض، المملكة العربية السعودية، نخدم العملاء في جميع مناطق المملكة",
    },
}

# ----------------------------------------------------------------- SEO -----

PAGE_SEO = {
    "index": {
        "en": ("WAJHA | Advanced Drone Cleaning Solutions in Saudi Arabia",
               "WAJHA is Saudi Arabia's largest drone cleaning company, serving Riyadh and beyond with safe, precise cleaning for buildings, solar, infrastructure, industry, marine, and aviation."),
        "ar": ("وجهة | حلول تنظيف متقدمة بالطائرات المسيّرة في السعودية",
               "وجهة هي أكبر شركة لتنظيف الدرونز في المملكة العربية السعودية، تخدم الرياض وما حولها بتنظيف آمن ودقيق للمباني والطاقة الشمسية والبنية التحتية والصناعة والقطاع البحري والطيران."),
    },
    "about": {
        "en": ("About WAJHA | Saudi Arabia's Largest Drone Cleaning Company",
               "Learn about WAJHA, the largest dedicated drone cleaning operator in Saudi Arabia, our mission, our 100+ specialist team, and our safety-first approach."),
        "ar": ("عن وجهة | أكبر شركة لتنظيف الدرونز في السعودية",
               "تعرّف على وجهة، أكبر مشغّل مخصص لتنظيف الدرونز في المملكة العربية السعودية، ورسالتنا، وفريقنا المكوّن من أكثر من 100 متخصص، ونهجنا القائم على السلامة."),
    },
    "technology": {
        "en": ("Our Technology | WAJHA Drone Cleaning Fleet",
               "Explore WAJHA's drone cleaning fleet, safety systems, precision cleaning technology, and pilot training across Saudi Arabia."),
        "ar": ("تقنيتنا | أسطول وجهة لتنظيف الدرونز",
               "تعرّف على أسطول وجهة لتنظيف الدرونز وأنظمة السلامة وتقنية التنظيف الدقيقة وتدريب الطيارين في المملكة العربية السعودية."),
    },
    "projects": {
        "en": ("Projects | WAJHA Drone Cleaning",
               "See the project categories WAJHA serves across Saudi Arabia, from commercial facades to solar, infrastructure, industry, marine, and aviation."),
        "ar": ("المشاريع | تنظيف وجهة بالدرون",
               "تعرّف على فئات المشاريع التي تخدمها وجهة في المملكة العربية السعودية، من الواجهات التجارية إلى الطاقة الشمسية والبنية التحتية والصناعة والقطاع البحري والطيران."),
    },
    "contact": {
        "en": ("Contact WAJHA | Drone Cleaning in Riyadh, Saudi Arabia",
               "Contact WAJHA's team in Riyadh by phone, email, or our contact form to discuss your drone cleaning project."),
        "ar": ("تواصل مع وجهة | تنظيف بالدرون في الرياض، السعودية",
               "تواصل مع فريق وجهة في الرياض عبر الهاتف أو البريد الإلكتروني أو نموذج التواصل لمناقشة مشروع التنظيف بالدرون الخاص بك."),
    },
    "services/index": {
        "en": ("Our Services | WAJHA Drone Cleaning Solutions",
               "Explore WAJHA's six drone cleaning service lines: facades, solar panels, road infrastructure, industrial walls, marine vessels, and aircraft."),
        "ar": ("خدماتنا | حلول وجهة لتنظيف الدرونز",
               "تعرّف على خطوط خدمة وجهة الست لتنظيف الدرونز: الواجهات، الألواح الشمسية، بنية الطرق، الجدران الصناعية، السفن، والطائرات."),
    },
    "blog/index": {
        "en": ("Blog | WAJHA Drone Cleaning Insights",
               "Insights on drone cleaning, solar panel efficiency, facade maintenance, and safe drone operations in Saudi Arabia from WAJHA."),
        "ar": ("المدونة | رؤى وجهة حول تنظيف الدرونز",
               "رؤى حول تنظيف الدرونز وكفاءة الألواح الشمسية وصيانة الواجهات والتشغيل الآمن للدرونز في المملكة العربية السعودية من وجهة."),
    },
}

for _slug, _data in SERVICES.items():
    PAGE_SEO[f"services/{_slug}"] = {
        "en": (f"{_data['en']['title']} | WAJHA", _data["en"]["short"]),
        "ar": (f"{_data['ar']['title']} | وجهة", _data["ar"]["short"]),
    }
