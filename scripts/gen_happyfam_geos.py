#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate HappyFam landing + thank-you pages for all geos."""
from __future__ import annotations

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from happyfam_i18n import t
from happyfam_network_forms import UID, WEBHOOK, ACTION, SCRIPT, FORMS, CPA

GEOS = [
    {"geo": "hu", "lang": "hu", "offer": "2409", "price": "31.999 Ft", "old_price": "106.663 Ft",
     "price_num": 31999, "pkg": ("89.500 Ft", "14.000 Ft", "17.000 Ft", "3.200 Ft", "123.700 Ft")},
    {"geo": "es", "lang": "es", "offer": "3176", "price": "89€", "old_price": "299€",
     "price_num": 89, "pkg": ("249€", "39€", "48€", "9€", "345€")},
    {"geo": "de", "lang": "de", "offer": "3177", "price": "109€", "old_price": "363€",
     "price_num": 109, "pkg": ("305€", "48€", "59€", "11€", "423€")},
    {"geo": "lt", "lang": "lt", "offer": "3178", "price": "89€", "old_price": "299€",
     "price_num": 89, "pkg": ("249€", "39€", "48€", "9€", "345€")},
    {"geo": "pl", "lang": "pl", "offer": "3179", "price": "399 zł", "old_price": "1.330 zł",
     "price_num": 399, "pkg": ("1.115 zł", "175 zł", "215 zł", "40 zł", "1.545 zł")},
    {"geo": "cz", "lang": "cs", "offer": "3251", "price": "1.999 Kč", "old_price": "6.663 Kč",
     "price_num": 1999, "pkg": ("5.590 Kč", "875 Kč", "1.075 Kč", "200 Kč", "7.740 Kč")},
    {"geo": "sk", "lang": "sk", "offer": "3702", "price": "89€", "old_price": "299€",
     "price_num": 89, "pkg": ("249€", "39€", "48€", "9€", "345€")},
    {"geo": "lv", "lang": "lv", "offer": "4095", "price": "99€", "old_price": "330€",
     "price_num": 99, "pkg": ("277€", "43€", "53€", "10€", "383€")},
    {"geo": "pt", "lang": "pt", "offer": "1476", "price": "99€", "old_price": "330€",
     "price_num": 99, "pkg": ("277€", "43€", "53€", "10€", "383€"), "pieces": 12},
]

GTAG = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18376580748"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'AW-18376580748');
</script>"""


def slug_for(geo: str, offer: str) -> str:
    return f"happyfam-{geo}-{offer}"


def _field_html(fm: dict, field: str) -> str:
    if field == "name":
        return (
            f'<div class="hf-field"><label for="name">{fm["label_name"]}</label>'
            f'<input id="name" type="text" name="name" autocomplete="name" placeholder="{fm["ph_name"]}" required></div>'
        )
    if field == "tel":
        return (
            f'<div class="hf-field"><label for="tel">{fm["label_tel"]}</label>'
            f'<input id="tel" type="tel" name="tel" autocomplete="tel" placeholder="{fm["ph_tel"]}" required></div>'
        )
    return (
        f'<div class="hf-field"><label for="street-address">{fm["label_address"]}</label>'
        f'<input id="street-address" type="text" name="street-address" autocomplete="street-address" placeholder="{fm["ph_address"]}" required></div>'
    )


def form_block(offer: str, ty_url: str, form_id: str = "") -> str:
    fm = FORMS[offer]
    fields = "\n        ".join(_field_html(fm, f) for f in fm["field_order"])
    id_attr = f' id="{form_id}"' if form_id else ""
    return f"""<form class="hf-form tm-order-form order-form"{id_attr} action="{ACTION}" method="post">
        {fields}
        <input name="uid" type="hidden" value="{UID}" />
        <input name="offer" type="hidden" value="{offer}" />
        <input name="lp" type="hidden" value="{fm['lp']}" />
        <input name="thankyoupage" type="hidden" value="{ty_url}" />
        <input name="webhook" type="hidden" value="{WEBHOOK}" />
        <input name="_key" type="hidden" value="{fm['key']}" />
        <button class="hf-btn" name="submit" type="submit"><span>{fm['submit']}</span></button>
        <script src="{SCRIPT}" async></script>
      </form>"""


FOOTER_LINKS = {
    "hu": {
        "about": "Rólunk", "contact": "Kapcsolat", "privacy": "Adatvédelmi irányelvek",
        "terms": "Általános szerződési feltételek", "cookie": "Cookie szabályzat",
        "shipping": "Szállítási feltételek", "refund": "Visszatérítési szabályzat",
    },
    "es": {
        "about": "Sobre nosotros", "contact": "Contáctanos", "privacy": "Política de privacidad",
        "terms": "Términos y condiciones", "cookie": "Política de cookies",
        "shipping": "Política de envío", "refund": "Política de reembolso",
    },
    "de": {
        "about": "Über uns", "contact": "Kontaktieren Sie uns", "privacy": "Datenschutzrichtlinie",
        "terms": "Allgemeine Geschäftsbedingungen", "cookie": "Cookie-Richtlinie",
        "shipping": "Versandbedingungen", "refund": "Rückerstattungsrichtlinie",
    },
    "lt": {
        "about": "Apie mus", "contact": "Susisiekite", "privacy": "Privatumo politika",
        "terms": "Sąlygos", "cookie": "Slapukų politika",
        "shipping": "Pristatymo politika", "refund": "Grąžinimo politika",
    },
    "pl": {
        "about": "O nas", "contact": "Kontakt", "privacy": "Polityka prywatności",
        "terms": "Regulamin", "cookie": "Polityka cookies",
        "shipping": "Polityka wysyłki", "refund": "Polityka zwrotów",
    },
    "cs": {
        "about": "O nás", "contact": "Kontaktujte nás", "privacy": "Zásady ochrany osobních údajů",
        "terms": "Smluvní podmínky", "cookie": "Zásady používání souborů cookie",
        "shipping": "Zásady dopravy", "refund": "Zásady vrácení peněz",
    },
    "sk": {
        "about": "O nás", "contact": "Kontaktujte nás", "privacy": "Zásady ochrany osobných údajov",
        "terms": "Zmluvné podmienky", "cookie": "Zásady používania súborov cookie",
        "shipping": "Pravidlá prepravy", "refund": "Pravidlá vrátenia peňazí",
    },
    "lv": {
        "about": "Par mums", "contact": "Sazinieties ar mums", "privacy": "Privātuma politika",
        "terms": "Noteikumi un nosacījumi", "cookie": "Sīkdatņu politika",
        "shipping": "Piegādes politika", "refund": "Atmaksas politika",
    },
    "pt": {
        "about": "Sobre nós", "contact": "Contacte-nos", "privacy": "Política de Privacidade",
        "terms": "Termos e Condições", "cookie": "Política de Cookies",
        "shipping": "Política de envio", "refund": "Política de reembolso",
    },
}


def ty_footer(geo: str, lang: str, s: dict) -> str:
    links = FOOTER_LINKS[lang]
    return f"""<footer class="site-footer"><div class="container">
  <div class="site-footer__grid">
    <div>
      <a href="/" class="site-logo">
        <span class="site-logo__text" style="display:inline"><span class="site-logo__text-primary">devicefindhub</span><span class="site-logo__text-accent">.com</span></span>
      </a>
      <p style="margin-top:12px;max-width:320px;line-height:1.65;color:var(--color-text-muted,#9a948a);font-size:13px">{s['footer_desc']}</p>
    </div>
    <div>
      <h4 class="site-footer__heading">{s['footer_info']}</h4>
      <ul class="site-footer__list">
        <li><a href="/{geo}/about-us.html">{links['about']}</a></li>
        <li><a href="/{geo}/contact-us.html">{links['contact']}</a></li>
        <li><a href="/{geo}/privacy-policy.html">{links['privacy']}</a></li>
        <li><a href="/{geo}/terms-conditions.html">{links['terms']}</a></li>
        <li><a href="/{geo}/cookie-policy.html">{links['cookie']}</a></li>
        <li><a href="/{geo}/shipping-policy.html">{links['shipping']}</a></li>
        <li><a href="/{geo}/refund-policy.html">{links['refund']}</a></li>
      </ul>
    </div>
    <div>
      <h4 class="site-footer__heading">{s['footer_contact']}</h4>
      <ul class="site-footer__list">
        <li><strong>The Lead Empire L.L.C-FZ</strong></li>
        <li>Meydan Grandstand, 6th floor, Meydan Road, Dubai, United Arab Emirates</li>
        <li><a href="mailto:info@devicefindhub.com">info@devicefindhub.com</a></li>
      </ul>
    </div>
  </div>
  <div class="site-footer__bottom">© <span data-year>2026</span> <strong>The Lead Empire L.L.C-FZ</strong> — {s['footer_rights']} <a href="/">devicefindhub.com</a></div>
</div></footer>"""


def footer_links(geo: str, lang: str, s: dict) -> str:
    links = FOOTER_LINKS[lang]
    return f"""<footer class="hf-footer">
    <div class="hf-container hf-footer-row">
      <div>
        <a href="/" class="hf-logo" style="color:#fff;text-decoration:none;display:inline-block;margin-bottom:14px">devicefindhub<span style="color:var(--copper2)">.com</span></a>
        <p style="max-width:340px;line-height:1.7;margin:0">{s['footer_desc']}</p>
      </div>
      <div>
        <h4 style="color:#fff;font-size:12px;text-transform:uppercase;letter-spacing:.12em;margin:0 0 14px;font-weight:700">{s['footer_info']}</h4>
        <ul style="list-style:none;padding:0;margin:0;line-height:2">
          <li><a href="/{geo}/about-us.html">{links['about']}</a></li>
          <li><a href="/{geo}/contact-us.html">{links['contact']}</a></li>
          <li><a href="/{geo}/privacy-policy.html">{links['privacy']}</a></li>
          <li><a href="/{geo}/terms-conditions.html">{links['terms']}</a></li>
          <li><a href="/{geo}/cookie-policy.html">{links['cookie']}</a></li>
          <li><a href="/{geo}/shipping-policy.html">{links['shipping']}</a></li>
          <li><a href="/{geo}/refund-policy.html">{links['refund']}</a></li>
        </ul>
      </div>
      <div>
        <h4 style="color:#fff;font-size:12px;text-transform:uppercase;letter-spacing:.12em;margin:0 0 14px;font-weight:700">{s['footer_contact']}</h4>
        <ul style="list-style:none;padding:0;margin:0;line-height:1.9">
          <li><strong style="color:#fff">The Lead Empire L.L.C-FZ</strong></li>
          <li>Meydan Grandstand, 6th floor</li>
          <li>Meydan Road, Dubai</li>
          <li>{s['country_name']}</li>
          <li><a href="mailto:info@devicefindhub.com">info@devicefindhub.com</a></li>
        </ul>
      </div>
    </div>
    <div class="hf-container" style="margin-top:28px;padding-top:20px;border-top:1px solid rgba(255,255,255,.12);font-size:11px;color:#9a948a">
      © <span data-year>2026</span> <strong style="color:#bfb8ad">The Lead Empire L.L.C-FZ</strong> — {s['footer_rights']} <a href="/">devicefindhub.com</a>
    </div>
  </footer>"""


def render_landing(cfg: dict) -> str:
    geo, lang, offer = cfg["geo"], cfg["lang"], cfg["offer"]
    slug = slug_for(geo, offer)
    canonical = f"https://devicefindhub.com/{geo}/{slug}/landing.html"
    ty_url = f"https://devicefindhub.com/{geo}/{slug}/thank-you.html"
    s = t(lang, price=cfg["price"], old_price=cfg["old_price"])
    p1, p2, p3, p4, p_total = cfg["pkg"]
    form1 = form_block(offer, ty_url, "order-form-1")
    form2 = form_block(offer, ty_url, "order-form-2")

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
{GTAG}
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{s['meta_title']}</title>
<meta name="description" content="{s['meta_desc']}">
<meta name="contact" content="info@devicefindhub.com">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="stylesheet" href="/assets/css/happyfam-landing.css">
<script>
window.SITE_CONFIG = {{
  GEO: '{geo}',
  PRODUCT_SLUG: '{slug}',
  CURRENCY: '{cfg.get("currency", "EUR")}',
  PRICE: {cfg['price_num']},
  OFFER_NAME: 'HappyFam {offer}',
  LP_ID: '{geo}-{offer}',
  FORM_ENDPOINT: '{ACTION}'
}};
</script>
<script src="/assets/js/tracking.js" defer></script>
</head>
<body>
<div class="hf-page" id="happyfam-top">
  <div class="hf-banner">{s['banner']}</div>
  <header class="hf-container hf-nav"><div class="hf-logo">Happy<span>Fam</span>™</div><div class="hf-navnote">{s['navnote']}</div></header>
  <section class="hf-hero">
    <div class="hf-container hf-grid">
      <div>
        <div class="hf-kicker">{s['kicker']}</div>
        <h1>{s['h1']}</h1>
        <div class="hf-rating"><span class="hf-stars">★★★★★</span> {s['rating']}</div>
        <p class="hf-lead">{s['lead']}</p>
        <div class="hf-actions"><a class="hf-btn" href="#ordine">{s['cta']}</a><span class="hf-micro">{s['micro']}</span></div>
      </div>
      <div class="hf-product hf-image-1x1"><img src="/assets/img/products/happyfam/01-set-completo.png" alt="HappyFam" loading="eager"></div>
    </div>
  </section>
  <div class="hf-trustbar"><div class="hf-container hf-trustgrid"><div>{s['trust1']}</div><div>{s['trust2']}</div><div>{s['trust3']}</div><div>{s['trust4']}</div></div></div>

  <section class="hf-section">
    <div class="hf-container hf-center"><div class="hf-eyebrow">{s['sec_benefits_eyebrow']}</div><h2 class="hf-title">{s['sec_benefits_title']}</h2><p class="hf-sub">{s['sec_benefits_sub']}</p></div>
    <div class="hf-container hf-benefits">
      <div class="hf-card"><span class="hf-num">{s['b1_num']}</span><b>{s['b1_title']}</b><p>{s['b1_text']}</p></div>
      <div class="hf-card"><span class="hf-num">{s['b2_num']}</span><b>{s['b2_title']}</b><p>{s['b2_text']}</p></div>
      <div class="hf-card"><span class="hf-num">{s['b3_num']}</span><b>{s['b3_title']}</b><p>{s['b3_text']}</p></div>
      <div class="hf-card"><span class="hf-num">{s['b4_num']}</span><b>{s['b4_title']}</b><p>{s['b4_text']}</p></div>
      <div class="hf-card"><span class="hf-num">{s['b5_num']}</span><b>{s['b5_title']}</b><p>{s['b5_text']}</p></div>
      <div class="hf-card"><span class="hf-num">{s['b6_num']}</span><b>{s['b6_title']}</b><p>{s['b6_text']}</p></div>
    </div>
    <div class="hf-container hf-pricebox"><div><span class="hf-badge">{s['badge']}</span><p style="margin:14px 0 0;color:#ffe4cc">{s['warranty_note']}</p></div><div><s>{cfg['old_price']}</s><span class="hf-price">{cfg['price']}</span></div></div>
  </section>

  <section class="hf-section alt" id="ordine">
    <div class="hf-container hf-formwrap">
      <div class="hf-formcopy"><div class="hf-eyebrow">{s['form1_eyebrow']}</div><h2>{s['form1_h2']}</h2><p>{s['form1_p1']}</p><p>{s['form1_p2']}</p></div>
      {form1}
    </div>
  </section>

  <section class="hf-section">
    <div class="hf-container hf-center"><div class="hf-eyebrow">{s['feat_eyebrow']}</div><h2 class="hf-title">{s['feat_title']}</h2></div>
    <div class="hf-container hf-feature"><div><div class="hf-eyebrow">{s['f1_eyebrow']}</div><h3>{s['f1_h3']}</h3><p>{s['f1_p']}</p></div><div class="hf-visual hf-image-1x1"><img src="/assets/img/products/happyfam/02-sul-fuoco.png" alt="HappyFam" loading="lazy"></div></div>
    <div class="hf-container hf-feature rev"><div><div class="hf-eyebrow">{s['f2_eyebrow']}</div><h3>{s['f2_h3']}</h3><p>{s['f2_p']}</p></div><div class="hf-visual split hf-image-1x1"><img src="/assets/img/products/happyfam/03-confronto-graffi.png" alt="HappyFam" loading="lazy"></div></div>
    <div class="hf-container hf-feature"><div><div class="hf-eyebrow">{s['f3_eyebrow']}</div><h3>{s['f3_h3']}</h3><p>{s['f3_p']}</p><a class="hf-btn" href="#ordine-finale">{s['cta']}</a></div><div class="hf-visual light hf-image-1x1"><img src="/assets/img/products/happyfam/04-set-coltelli.png" alt="HappyFam" loading="lazy"></div></div>
  </section>

  <section class="hf-quote"><div class="hf-container"><div class="hf-rating" style="justify-content:center"><span class="hf-stars">★★★★★</span></div><blockquote>{s['quote']}</blockquote><footer>{s['quote_author']}</footer></div></section>
  <section class="hf-section alt"><div class="hf-container hf-center"><div class="hf-eyebrow">{s['gal_eyebrow']}</div><h2 class="hf-title">{s['gal_title']}</h2></div><div class="hf-container hf-gallery"><div class="hf-visual hf-image-1x1"><img src="/assets/img/products/happyfam/05-cliente-cucina.png" alt="HappyFam" loading="lazy"></div><div class="hf-visual light hf-image-1x1"><img src="/assets/img/products/happyfam/06-unboxing.png" alt="HappyFam" loading="lazy"></div><div class="hf-visual hf-image-1x1"><img src="/assets/img/products/happyfam/07-coltelli-ceppo.png" alt="HappyFam" loading="lazy"></div></div><div class="hf-center" style="margin-top:38px"><a class="hf-btn" href="#ordine-finale">{s['cta']}</a></div></section>

  <section class="hf-section" id="ordine-finale"><div class="hf-container hf-stack"><div class="hf-product hf-image-1x1"><img src="/assets/img/products/happyfam/08-contenuto-pacco.png" alt="HappyFam" loading="lazy"></div><div><div class="hf-eyebrow">{s['pkg_eyebrow']}</div><h2 class="hf-title" style="margin-left:0">{s['pkg_h2']}</h2><p>{s['pkg_intro']}</p><ul class="hf-list"><li><span>{s['pkg_item1']}</span><b>{p1}</b></li><li><span>{s['pkg_item2']}</span><b>{p2}</b></li><li><span>{s['pkg_item3']}</span><b>{p3}</b></li><li><span>{s['pkg_item4']}</span><b>{p4}</b></li></ul><p class="hf-total">{s['pkg_total']}</p></div></div></section>

  <section class="hf-section alt"><div class="hf-container hf-formwrap"><div class="hf-formcopy"><div class="hf-eyebrow">{s['form2_eyebrow']}</div><h2>{s['form2_h2']}</h2><p>{s['form2_p']}</p><p>{s['form2_bullets']}</p></div>{form2}</div></section>

  <section class="hf-section"><div class="hf-container hf-center"><div class="hf-eyebrow">{s['faq_eyebrow']}</div><h2 class="hf-title">{s['faq_title']}</h2></div><div class="hf-container hf-faq"><details><summary>{s['faq_q1']}</summary><p>{s['faq_a1']}</p></details><details><summary>{s['faq_q2']}</summary><p>{s['faq_a2']}</p></details><details><summary>{s['faq_q3']}</summary><p>{s['faq_a3']}</p></details><details><summary>{s['faq_q4']}</summary><p>{s['faq_a4']}</p></details><details><summary>{s['faq_q5']}</summary><p>{s['faq_a5']}</p></details></div></section>

  {footer_links(geo, lang, s)}

  <div class="hf-sticky"><a class="hf-btn" href="#ordine">{s['cta']}</a></div>
</div>
<script>
(function(){{
  var yearEl = document.querySelector('[data-year]');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
}})();
</script>
</body>
</html>"""


def render_thank_you(cfg: dict) -> str:
    geo, lang, offer = cfg["geo"], cfg["lang"], cfg["offer"]
    slug = slug_for(geo, offer)
    s = t(lang, price=cfg["price"], old_price=cfg["old_price"])
    cpa = CPA[offer]

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
{GTAG}
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{s['ty_title']}</title>
<meta name="description" content="{s['ty_sub']}">
<meta name="contact" content="info@devicefindhub.com">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="stylesheet" href="/assets/css/variables.css">
<link rel="stylesheet" href="/assets/css/reset.css">
<link rel="stylesheet" href="/assets/css/components.css">
<style>
body {{ background: #f8fafc; }}
.ty-page {{ max-width: 540px; margin: 0 auto; padding: 1.5rem 1rem 3rem; }}
.ty-check {{ width: 64px; height: 64px; border-radius: 9999px; background: #fff; border: 2px solid var(--color-primary); display: flex; align-items: center; justify-content: center; margin: 1rem auto 1.5rem; font-size: 2rem; color: var(--color-primary); font-weight: 800; box-shadow: 0 4px 12px -4px rgba(22,163,74,0.25); }}
.ty-headline {{ font-size: 1.625rem; font-weight: 800; line-height: 1.2; text-align: center; margin-bottom: 0.875rem; letter-spacing: -0.02em; }}
.ty-subhead {{ text-align: center; color: var(--color-text-muted); font-size: 1rem; line-height: 1.5; margin-bottom: 1.5rem; max-width: 440px; margin-left: auto; margin-right: auto; }}
.ty-action {{ background: #fef9e7; border: 1.5px solid #f5d07a; border-radius: 0.75rem; padding: 1.25rem 1.25rem 1.5rem; margin-bottom: 1rem; }}
.ty-action__eyebrow {{ font-size: 0.7rem; font-weight: 800; letter-spacing: 0.15em; text-transform: uppercase; color: #92400e; margin-bottom: 0.625rem; }}
.ty-action__title {{ font-size: 1.125rem; font-weight: 800; margin-bottom: 0.5rem; color: #1c1917; }}
.ty-action__text {{ font-size: 0.9375rem; line-height: 1.55; color: #44403c; margin: 0; }}
.ty-steps {{ list-style: none; padding: 0; margin: 0 0 1.5rem; }}
.ty-steps li {{ display: flex; gap: 0.75rem; padding: 0.875rem 0; border-bottom: 1px solid #e7e5e4; font-size: 0.9375rem; line-height: 1.45; }}
.ty-steps li:last-child {{ border-bottom: 0; }}
.ty-steps__num {{ flex-shrink: 0; width: 1.75rem; height: 1.75rem; border-radius: 9999px; background: var(--color-primary); color: #fff; font-weight: 800; font-size: 0.8125rem; display: flex; align-items: center; justify-content: center; }}
.ty-trust {{ display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center; }}
.ty-trust__badge {{ font-size: 0.75rem; font-weight: 700; color: #57534e; background: #fff; border: 1px solid #e7e5e4; border-radius: 9999px; padding: 0.375rem 0.75rem; }}
</style>
</head>
<body>
<main class="ty-page">
  <div class="ty-check">✓</div>
  <h1 class="ty-headline">{s['ty_title']}</h1>
  <p class="ty-subhead">{s['ty_sub']}</p>
  <div class="ty-action">
    <div class="ty-action__eyebrow">{s['ty_action_eyebrow']}</div>
    <div class="ty-action__title">{s['ty_action_h']}</div>
    <p class="ty-action__text">{s['ty_action_p']}</p>
  </div>
  <ol class="ty-steps">
    <li><span class="ty-steps__num">1</span><span>{s['ty_step1']}</span></li>
    <li><span class="ty-steps__num">2</span><span>{s['ty_step2']}</span></li>
    <li><span class="ty-steps__num">3</span><span>{s['ty_step3']}</span></li>
  </ol>
  <div class="ty-trust"><span class="ty-trust__badge">{s['ty_trust_ssl']}</span></div>
</main>
{ty_footer(geo, lang, s)}
<script>
(function(){{
  var yearEl = document.querySelector('[data-year]');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
}})();
</script>
<script>
  (function () {{
    var p = new URLSearchParams(window.location.search);
    function stored(name) {{
      try {{ return window.localStorage.getItem('df_' + name) || ''; }}
      catch (e) {{ return ''; }}
    }}
    var subid = p.get('subid') || p.get('campaign_id') || stored('subid') || stored('campaign_id') || '';
    var transactionId = p.get('order_id') || p.get('transaction_id') || p.get('tid') || subid || '';
    gtag('event', 'conversion', {{
      'send_to': 'AW-18376580748/K45WCPGxpescEIy90bpE',
      'value': {cpa},
      'currency': 'USD',
      'transaction_id': transactionId
    }});
  }})();
</script>
</body>
</html>"""


def main() -> None:
    urls = []
    for cfg in GEOS:
        slug = slug_for(cfg["geo"], cfg["offer"])
        out_dir = os.path.join(ROOT, cfg["geo"], slug)
        os.makedirs(out_dir, exist_ok=True)
        landing_path = os.path.join(out_dir, "landing.html")
        ty_path = os.path.join(out_dir, "thank-you.html")
        with open(landing_path, "w", encoding="utf-8") as f:
            f.write(render_landing(cfg))
        with open(ty_path, "w", encoding="utf-8") as f:
            f.write(render_thank_you(cfg))
        url = f"https://devicefindhub.com/{cfg['geo']}/{slug}/landing.html"
        urls.append(url)
        print(f"✓ {url}")

    print(f"\nGenerated {len(urls)} landings + {len(urls)} thank-you pages.")


if __name__ == "__main__":
    main()
