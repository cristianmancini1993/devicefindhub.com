#!/usr/bin/env python3
"""Convert Elementor page JSON export to standalone preview HTML."""

import json
import sys
from pathlib import Path


def px(val, default=0):
    if isinstance(val, dict):
        return val.get("size", default)
    return val if val is not None else default


def section_style(settings):
    styles = []
    bg = settings.get("background_color")
    if bg:
        styles.append(f"background:{bg}")
    pad = settings.get("padding") or {}
    if pad:
        styles.append(
            f"padding:{px(pad.get('top'))}px {px(pad.get('right'))}px "
            f"{px(pad.get('bottom'))}px {px(pad.get('left'))}px"
        )
    margin = settings.get("margin") or {}
    if margin:
        styles.append(
            f"margin:{px(margin.get('top'))}px {px(margin.get('right'))}px "
            f"{px(margin.get('bottom'))}px {px(margin.get('left'))}px"
        )
    if settings.get("border_border") == "solid":
        bw = settings.get("border_width") or {}
        bc = settings.get("border_color", "#E4E0DB")
        styles.append(
            f"border:{px(bw.get('top', 1))}px solid {bc}"
        )
    br = settings.get("border_radius") or {}
    if br:
        styles.append(
            f"border-radius:{px(br.get('top'))}px"
        )
    shadow = settings.get("box_shadow_box_shadow") or {}
    if shadow:
        styles.append(
            "box-shadow:"
            f"{shadow.get('horizontal', 0)}px {shadow.get('vertical', 0)}px "
            f"{shadow.get('blur', 0)}px {shadow.get('spread', 0)}px {shadow.get('color', 'rgba(0,0,0,.1)')}"
        )
    return ";".join(styles)


def heading_tag(settings):
    return settings.get("header_size") or "h2"


def heading_style(settings):
    styles = [
        "font-family:Verdana,sans-serif",
        f"font-size:{px((settings.get('typography_font_size') or {}).get('size'), 21)}px",
        f"font-weight:{settings.get('typography_font_weight', 'bold')}",
        f"color:{settings.get('title_color', '#262626')}",
        f"line-height:{px((settings.get('typography_line_height') or {}).get('size'), 1.35)}",
        f"text-align:{settings.get('align', 'center')}",
        "margin:0",
    ]
    return ";".join(styles)


def text_style(settings):
    styles = [
        "font-family:Verdana,sans-serif",
        f"font-size:{px((settings.get('typography_font_size') or {}).get('size'), 16)}px",
        f"font-weight:{settings.get('typography_font_weight', 'normal')}",
        f"color:{settings.get('color', '#262626')}",
        f"line-height:{px((settings.get('typography_line_height') or {}).get('size'), 1.7)}",
        f"text-align:{settings.get('align', 'center')}",
        "margin:0",
    ]
    return ";".join(styles)


def button_style(settings):
    br = settings.get("border_radius") or {}
    tp = settings.get("text_padding") or {}
    shadow = settings.get("button_box_shadow_box_shadow") or {}
    styles = [
        "display:inline-block",
        "text-decoration:none",
        "cursor:pointer",
        "border:none",
        "font-family:Verdana,sans-serif",
        f"font-size:{px((settings.get('typography_font_size') or {}).size if hasattr((settings.get('typography_font_size') or {}), 'size') else (settings.get('typography_font_size') or {}).get('size'), 17)}px",
        f"font-weight:{settings.get('typography_font_weight', 'bold')}",
        f"background:{settings.get('background_color', '#A65A2E')}",
        f"color:{settings.get('button_text_color', '#FFFFFF')}",
        f"border-radius:{px(br.get('top', 6))}px",
        f"padding:{px(tp.get('top', 15))}px {px(tp.get('right', 28))}px {px(tp.get('bottom', 15))}px {px(tp.get('left', 28))}px",
    ]
    if shadow:
        styles.append(
            "box-shadow:"
            f"{shadow.get('horizontal', 0)}px {shadow.get('vertical', 2)}px "
            f"{shadow.get('blur', 8)}px {shadow.get('spread', 0)}px {shadow.get('color', 'rgba(122,66,32,0.25)')}"
        )
    return ";".join(styles)


def render_form(settings):
    fields = settings.get("form_fields") or []
    rows = []
    for field in fields:
        fid = field.get("custom_id") or field.get("_id", "field")
        label = field.get("field_label", "")
        placeholder = field.get("placeholder", "")
        ftype = field.get("field_type", "text")
        required = field.get("required") == "true"
        req = " required" if required and ftype != "hidden" else ""
        if ftype == "hidden":
            rows.append(f'<input type="hidden" name="{fid}" id="{fid}" value="">')
            continue
        rows.append(
            f'<label style="display:block;font-family:Verdana;font-size:16px;font-weight:bold;color:#262626;margin-bottom:8px;">{label}</label>'
            f'<input type="{ftype}" name="{fid}" placeholder="{placeholder}"{req} '
            f'style="width:100%;box-sizing:border-box;height:50px;padding:0 14px;border:2px solid #A65A2E;border-radius:10px;font-family:Verdana;font-size:17px;margin-bottom:18px;">'
        )
    btn = settings.get("button_text", "INVIA")
    return (
        '<form class="order-form" style="max-width:480px;margin:0 auto;" onsubmit="event.preventDefault();alert(\'Preview: form non collegato.\');">'
        + "".join(rows)
        + f'<button type="submit" style="width:100%;{button_style({"background_color":"#A65A2E","button_text_color":"#FFFFFF","typography_font_size":{"size":18},"typography_font_weight":"bold","border_radius":{"top":50},"text_padding":{"top":16,"right":30,"bottom":16,"left":30}})}">{btn}</button>'
        + "</form>"
    )


def render_accordion(settings):
    tabs = settings.get("tabs") or []
    parts = ['<div style="max-width:640px;margin:0 auto;">']
    for tab in tabs:
        title = tab.get("tab_title", "")
        content = tab.get("tab_content", "")
        parts.append(
            '<details style="border:1px solid #EADFD3;border-radius:8px;margin-bottom:12px;padding:0;background:#fff;">'
            f'<summary style="cursor:pointer;list-style:none;padding:16px 18px;font-family:Verdana;font-size:17px;font-weight:bold;color:#7A4220;">{title}</summary>'
            f'<div style="padding:0 18px 16px;">{content}</div>'
            "</details>"
        )
    parts.append("</div>")
    return "".join(parts)


def render_widget(widget):
    wtype = widget.get("widgetType")
    settings = widget.get("settings") or {}

    if wtype == "html":
        return settings.get("html", "")

    if wtype == "text-editor":
        return f'<div style="{text_style(settings)}">{settings.get("editor", "")}</div>'

    if wtype == "heading":
        tag = heading_tag(settings)
        return f'<{tag} style="{heading_style(settings)}">{settings.get("title", "")}</{tag}>'

    if wtype == "spacer":
        h = px((settings.get("space") or {}).get("size"), 10)
        return f'<div style="height:{h}px"></div>'

    if wtype == "image":
        br = settings.get("border_radius") or {}
        radius = px(br.get("top", 12))
        url = (settings.get("image") or {}).get("url") or ""
        if url:
            return f'<img src="{url}" alt="" style="display:block;max-width:100%;margin:0 auto;border-radius:{radius}px;">'
        return (
            f'<div style="max-width:520px;margin:0 auto;height:220px;border:2px dashed #E4E0DB;border-radius:{radius}px;'
            'background:#FAF7F4;display:flex;align-items:center;justify-content:center;color:#9A9A9A;font-family:Verdana;font-size:13px;">'
            "📷 Placeholder immagine</div>"
        )

    if wtype == "button":
        text = settings.get("text", "CTA")
        align = settings.get("align", "center")
        return (
            f'<div style="text-align:{align}">'
            f'<a href="#order-form" class="cta-scroll" style="{button_style(settings)}">{text}</a>'
            "</div>"
        )

    if wtype == "form":
        return f'<div id="order-form">{render_form(settings)}</div>'

    if wtype == "accordion":
        return render_accordion(settings)

    return ""


def render_column(column):
    chunks = []
    for widget in column.get("elements") or []:
        if widget.get("elType") == "widget":
            chunks.append(render_widget(widget))
    align = "center"
    return f'<div style="max-width:720px;margin:0 auto;">{"".join(chunks)}</div>'


def render_section(section):
    style = section_style(section.get("settings") or {})
    cols = []
    for col in section.get("elements") or []:
        if col.get("elType") == "column":
            cols.append(render_column(col))
    return f'<section style="{style}">{"".join(cols)}</section>'


def convert(data):
    title = data.get("title", "Landing Preview")
    page_bg = (data.get("page_settings") or {}).get("background_color", "#FFFFFF")
    sections = "".join(render_section(s) for s in data.get("content") or [])
    return f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: {page_bg}; }}
summary::-webkit-details-marker {{ display: none; }}
summary::after {{ content: '+'; float: right; color: #A65A2E; }}
details[open] summary::after {{ content: '−'; }}
.cta-scroll:hover {{ opacity: .92; }}
</style>
</head>
<body>
{sections}
<script>
(function(){{
  function getParam(name){{
    var m = new RegExp('[?&]'+name+'=([^&]*)').exec(window.location.search);
    return m ? decodeURIComponent(m[1].replace(/\\+/g,' ')) : '';
  }}
  var subid = getParam('subid') || getParam('utm_campaign') || '';
  document.querySelectorAll('input[name="subid"]').forEach(function(el){{ el.value = subid; }});
  document.querySelectorAll('.cta-scroll').forEach(function(el){{
    el.addEventListener('click', function(e){{
      var form = document.getElementById('order-form');
      if (form) {{ e.preventDefault(); form.scrollIntoView({{behavior:'smooth'}}); }}
    }});
  }});
}})();
</script>
</body>
</html>"""


def main():
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".html")
    data = json.loads(src.read_text(encoding="utf-8"))
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(convert(data), encoding="utf-8")
    print(dst)


if __name__ == "__main__":
    main()
