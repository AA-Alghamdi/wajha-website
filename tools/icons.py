"""Original inline SVG icon set for WAJHA. No stock art, no third-party assets.

Every icon is authored here as raw SVG path/shape data. Stroke-based icons use
fill="none" + stroke="currentColor" so color is controlled purely via CSS
`color`; the few fill-based glyphs (aircraft, drone rotors) set fill directly.
"""

LOGO_MARK = """<svg class="{cls}" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
<g stroke="currentColor" stroke-width="2.5" stroke-linecap="round">
<line x1="24" y1="24" x2="10" y2="10"/>
<line x1="24" y1="24" x2="38" y2="10"/>
<line x1="24" y1="24" x2="10" y2="38"/>
<line x1="24" y1="24" x2="38" y2="38"/>
</g>
<circle cx="10" cy="10" r="5" fill="none" stroke="currentColor" stroke-width="2.5"/>
<circle cx="38" cy="10" r="5" fill="none" stroke="currentColor" stroke-width="2.5"/>
<circle cx="10" cy="38" r="5" fill="none" stroke="currentColor" stroke-width="2.5"/>
<circle cx="38" cy="38" r="5" fill="none" stroke="currentColor" stroke-width="2.5"/>
<circle cx="24" cy="24" r="6.5" class="logo-core" fill="currentColor"/>
</svg>"""

_ICON_BODY = {
    "facade": """<rect x="5" y="3" width="14" height="18" rx="0.6"/>
<line x1="5" y1="9" x2="19" y2="9"/>
<line x1="5" y1="15" x2="19" y2="15"/>
<line x1="12" y1="3" x2="12" y2="21"/>
<rect x="9.6" y="16.4" width="4.8" height="4.6"/>""",

    "solar": """<rect x="3" y="7" width="18" height="12" rx="0.4"/>
<line x1="3" y1="13" x2="21" y2="13"/>
<line x1="9" y1="7" x2="9" y2="19"/>
<line x1="15" y1="7" x2="15" y2="19"/>
<circle cx="12" cy="2.6" r="1" fill="currentColor" stroke="none"/>
<line x1="7.5" y1="3.2" x2="8.3" y2="4.3"/>
<line x1="16.5" y1="3.2" x2="15.7" y2="4.3"/>""",

    "road-sign": """<polygon points="12,3 20.2,17.5 3.8,17.5"/>
<line x1="12" y1="8.2" x2="12" y2="12.4"/>
<circle cx="12" cy="14.6" r="0.55" fill="currentColor" stroke="none"/>
<line x1="12" y1="17.5" x2="12" y2="21.2"/>
<line x1="9" y1="21.2" x2="15" y2="21.2"/>""",

    "factory": """<path d="M3 21V12.2l4.2 2.6V12.2l4.2 2.6V12.2l4.2 2.6V12.2L21 15v6z"/>
<line x1="7.2" y1="8.4" x2="7.2" y2="12"/>
<line x1="16.8" y1="5.6" x2="16.8" y2="10.4"/>
<line x1="3" y1="21" x2="21" y2="21"/>""",

    "marine": """<path d="M4.2 16h15.6l-2.1 4.4H6.3z"/>
<line x1="12" y1="3.6" x2="12" y2="16"/>
<path d="M12 4.6 L17.6 14 L12 14 Z"/>""",

    "aircraft": """<path d="M21 15.3v-1.9l-7.8-4.8V4.1a1.3 1.3 0 10-2.6 0v4.5L2.8 13.4v1.9l7.8-2.3v4.3l-2.6 1.8v1.4l4.1-1.2 4.1 1.2v-1.4l-2.6-1.8v-4.3z" fill="currentColor" stroke="none"/>""",
}

_ICON_ATTRS = {
    "facade": 'fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"',
    "solar": 'fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"',
    "road-sign": 'fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"',
    "factory": 'fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"',
    "marine": 'fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"',
    "aircraft": 'fill="none"',
}

_UTILITY = {
    "phone": """<path d="M6.6 10.8c1.4 2.8 3.8 5.2 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.3 1.2.4 2.5.6 3.8.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4.8c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.6.6 3.8.1.3 0 .7-.3 1z"/>""",
    "mail": """<rect x="3" y="5.5" width="18" height="13" rx="1.2"/><path d="M4 7l8 6 8-6"/>""",
    "pin": """<path d="M12 21s7-6.1 7-11.5A7 7 0 005 9.5C5 14.9 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.4"/>""",
    "menu": """<line x1="3.5" y1="6.5" x2="20.5" y2="6.5"/><line x1="3.5" y1="12" x2="20.5" y2="12"/><line x1="3.5" y1="17.5" x2="20.5" y2="17.5"/>""",
    "close": """<line x1="5" y1="5" x2="19" y2="19"/><line x1="19" y1="5" x2="5" y2="19"/>""",
    "chevron-up": """<polyline points="5,15 12,8 19,15"/>""",
    "check": """<polyline points="4,12.5 9.5,18 20,6"/>""",
    "arrow": """<line x1="4" y1="12" x2="19" y2="12"/><polyline points="13,6 19,12 13,18"/>""",
    "quote": """<path d="M7.5 15.5c0-3.3 1.6-5.8 4.3-7.3l.9 1.5c-1.7 1-2.7 2.3-2.9 3.9.3-.1.6-.1.9-.1 1.6 0 2.8 1.2 2.8 2.7 0 1.6-1.3 2.8-2.9 2.8-1.7 0-3.1-1.4-3.1-3.5zm8 0c0-3.3 1.6-5.8 4.3-7.3l.9 1.5c-1.7 1-2.7 2.3-2.9 3.9.3-.1.6-.1.9-.1 1.6 0 2.8 1.2 2.8 2.7 0 1.6-1.3 2.8-2.9 2.8-1.7 0-3.1-1.4-3.1-3.5z"/>""",
    "shield": """<path d="M12 3l7 3v5.5c0 4.6-3 7.9-7 9.5-4-1.6-7-4.9-7-9.5V6z"/><polyline points="9,12 11.2,14.2 15.5,9.5"/>""",
    "bolt": """<polygon points="13,2 4,14 11,14 10,22 20,9 13,9"/>""",
    "target": """<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="0.8" fill="currentColor" stroke="none"/>""",
    "users": """<circle cx="9" cy="8.5" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9.5" r="2.4"/><path d="M15.5 14.2c2.6.4 4.5 2.6 4.5 5.3"/>""",
    "whatsapp": """<path d="M12 3a9 9 0 00-7.8 13.5L3 21l4.7-1.2A9 9 0 1012 3z"/><path d="M8.3 8.6c.2-.5.5-.5.8-.5h.6c.2 0 .4 0 .6.5s.7 1.7.7 1.8.1.3 0 .5l-.5.7c-.1.2-.2.3 0 .6.8 1.3 1.7 2 2.9 2.6.2.1.4.1.5-.1l.6-.8c.2-.2.4-.2.6-.1l1.6.8c.2.1.4.2.4.4 0 .5-.2 1.2-.6 1.6-.5.5-1.4.8-2.2.6-1.9-.4-4.3-1.8-5.8-3.8-1.1-1.4-1.5-2.7-1.2-3.8z" fill="currentColor" stroke="none"/>""",
}


def icon(name: str, css_class: str = "icon") -> str:
    if name in _ICON_BODY:
        attrs = _ICON_ATTRS[name]
        return (f'<svg class="{css_class}" viewBox="0 0 24 24" {attrs} '
                f'xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">'
                f'{_ICON_BODY[name]}</svg>')
    if name in _UTILITY:
        return (f'<svg class="{css_class}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" '
                f'xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">'
                f'{_UTILITY[name]}</svg>')
    if name == "logo":
        return LOGO_MARK.format(cls=css_class)
    raise KeyError(f"unknown icon: {name}")


SERVICE_ICON_KEYS = {
    "facade-cleaning": "facade",
    "solar-panel-cleaning": "solar",
    "road-signs": "road-sign",
    "industrial-walls": "factory",
    "marine-vessels": "marine",
    "aircraft-cleaning": "aircraft",
}

FAVICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="14" fill="#0A1930"/>
<g transform="translate(8,8)" stroke="#0EA5B7" stroke-width="2.6" stroke-linecap="round">
<line x1="24" y1="24" x2="10" y2="10"/>
<line x1="24" y1="24" x2="38" y2="10"/>
<line x1="24" y1="24" x2="10" y2="38"/>
<line x1="24" y1="24" x2="38" y2="38"/>
</g>
<g transform="translate(8,8)" fill="none" stroke="#0EA5B7" stroke-width="2.6">
<circle cx="10" cy="10" r="5"/>
<circle cx="38" cy="10" r="5"/>
<circle cx="10" cy="38" r="5"/>
<circle cx="38" cy="38" r="5"/>
</g>
<circle cx="32" cy="32" r="7" fill="#FFB703"/>
</svg>"""
