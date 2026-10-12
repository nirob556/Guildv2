# -*- coding: utf-8 -*-

_FONTS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Orbitron:wght@500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
"""

_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{font-family:'Inter',system-ui,sans-serif;background:#000;color:#fff;min-height:100vh;-webkit-font-smoothing:antialiased}
:root{--bg:#000;--card:#08080c;--card2:#101015;--line:#1a1a22;--line2:#25252e;--txt:#fff;--mut:#8a8a95;--dim:#55555f;--green:#22c55e;--red:#ef4444;--blue:#3b82f6;--purple:#8b5cf6;--gold:#f59e0b}
.mono{font-family:'JetBrains Mono',monospace}
.orb{font-family:'Orbitron',sans-serif}
::-webkit-scrollbar{width:8px;height:8px}
::-webkit-scrollbar-track{background:#0a0a0a}
::-webkit-scrollbar-thumb{background:#262626;border-radius:4px}
::-webkit-scrollbar-thumb:hover{background:#3a3a3a}
"""

_ICONS = {
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>',
    "fast": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 19 22 12 13 5 13 19"></polygon><polygon points="2 19 11 12 2 5 2 19"></polygon></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>',
    "refresh": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 4 23 10 17 10"></polyline><polyline points="1 20 1 14 7 14"></polyline><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path></svg>',
    "cloud": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"></path></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>',
    "list": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="6" height="4" rx="1"></rect><rect x="3" y="15" width="6" height="4" rx="1"></rect><line x1="14" y1="7" x2="21" y2="7"></line><line x1="14" y1="17" x2="21" y2="17"></line></svg>',
    "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>',
    "star": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>',
    "crown": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 18h20l-1.5-9-4 3-4.5-7-4.5 7-4-3z"></path></svg>',
    "gear": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>',
    "pause": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="4" width="4" height="16" rx="1"></rect><rect x="14" y="4" width="4" height="16" rx="1"></rect></svg>',
    "play": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="6 4 20 12 6 20 6 4"></polygon></svg>',
    "trash": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"></path><path d="M10 11v6M14 11v6"></path><path d="M9 6V4a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"></path></svg>',
    "monitor": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>',
    "gamepad": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="6" y1="12" x2="10" y2="12"></line><line x1="8" y1="10" x2="8" y2="14"></line><line x1="15" y1="13" x2="15.01" y2="13"></line><line x1="18" y1="11" x2="18.01" y2="11"></line><rect x="2" y="6" width="20" height="12" rx="6"></rect></svg>',
    "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>',
    "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>',
    "id": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"></rect><circle cx="9" cy="11" r="2"></circle><path d="M15 10h3M15 14h3"></path></svg>',
    "trophy": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 21h8M12 17v4M7 4h10v6a5 5 0 0 1-10 0V4z"></path><path d="M17 5h3a2 2 0 0 1 0 4h-1M7 5H4a2 2 0 0 0 0 4h1"></path></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>',
    "warn": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>',
    "x": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>',
    "plus": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>',
    "arrow_right": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>',
    "star_fill": '<svg viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>',
    "bolt_fill": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>',
    "crown_fill": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 18h20l-1.5-9-4 3-4.5-7-4.5 7-4-3z"></path></svg>',
}


def _icon(name, color="currentColor", size=16, stroke_extra=""):
    svg = _ICONS.get(name, "")
    if not svg:
        return ""
    svg = svg.replace('stroke="currentColor"', f'stroke="{color}"')
    svg = svg.replace('<svg ', f'<svg width="{size}" height="{size}" ', 1)
    return svg


def _icon_inline(name, color="currentColor", size=16):
    svg = _ICONS.get(name, "")
    if not svg:
        return ""
    svg = svg.replace('stroke="currentColor"', f'stroke="{color}"')
    svg = svg.replace('<svg ', f'<svg width="{size}" height="{size}" style="display:inline-block;vertical-align:middle" ', 1)
    return svg


# ==================== HOME (Landing) ====================
HOME_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>NIROB X LEVEL - Free Fire Automation</title>
""" + _FONTS + """
<style>
""" + _CSS + """
html{scroll-behavior:smooth}
html,body{height:100%}
body{background:#050505;min-height:100vh;position:relative;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;background:
  linear-gradient(rgba(255,255,255,0.015) 1px,transparent 1px),
  linear-gradient(90deg,rgba(255,255,255,0.015) 1px,transparent 1px);
  background-size:60px 60px;pointer-events:none;z-index:0;
  mask-image:radial-gradient(ellipse at 50% 40%,#000 20%,transparent 75%);
  -webkit-mask-image:radial-gradient(ellipse at 50% 40%,#000 20%,transparent 75%)}

/* Announcement */
.ann{position:relative;z-index:5;background:#fff;color:#000;padding:9px 40px 9px 14px;text-align:center;font-size:12px;font-weight:600;font-family:'Inter',sans-serif}
.ann a{color:#000;text-decoration:underline;font-weight:800}
.ann .cls{position:absolute;right:12px;top:50%;transform:translateY(-50%);background:transparent;border:none;cursor:pointer;color:#000;font-size:16px;line-height:1;padding:4px}

/* Header */
.hdr{position:relative;z-index:5;display:flex;align-items:center;justify-content:space-between;padding:14px 18px;border-bottom:1px solid #151515}
.hlogo{display:flex;align-items:center;gap:10px}
.hshield{width:34px;height:34px;display:inline-flex;align-items:center;justify-content:center}
.hshield svg{width:34px;height:34px;stroke:#fff;fill:none;stroke-width:1.8}
.hname{font-family:'Inter',sans-serif;font-size:14px;font-weight:800;letter-spacing:2.5px;color:#fff}
.hbell{background:transparent;border:none;cursor:pointer;padding:6px;color:#fff}
.hbell svg{width:20px;height:20px;stroke:#fff;fill:none;stroke-width:1.8}

/* Status pill */
.status{position:relative;z-index:5;display:flex;justify-content:center;padding:16px 18px 0}
.spill{display:inline-flex;align-items:center;gap:8px;background:#0d0d0d;border:1px solid #1c1c1c;border-radius:24px;padding:7px 14px 7px 11px;font-family:'Inter',sans-serif;font-size:11px;font-weight:600;color:#b8b8b8}
.spill .dot{width:7px;height:7px;border-radius:50%;background:#22c55e;box-shadow:0 0 8px #22c55e;animation:pl 1.4s infinite}
.spill .mut{color:#5a5a5a;font-weight:400;margin-left:2px}
@keyframes pl{0%,100%{opacity:1}50%{opacity:0.4}}

/* Hero */
.hero{position:relative;z-index:5;padding:50px 22px 20px;max-width:640px;margin:0 auto;text-align:center}
.hero h1{font-family:'Inter',sans-serif;font-size:26px;font-weight:800;letter-spacing:1.5px;margin-bottom:36px;
  background:linear-gradient(90deg,#22d3ee,#a78bfa,#22d3ee);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
  filter:drop-shadow(0 0 24px rgba(34,211,238,0.35));}
.hero p{font-family:'Inter',sans-serif;font-size:17px;font-weight:500;line-height:1.65;color:#b8b8b8;letter-spacing:0.2px}
.hero p + p{margin-top:14px}

/* CTA buttons */
.ctas{position:relative;z-index:5;display:flex;gap:12px;justify-content:center;padding:24px 18px 50px;flex-wrap:wrap;max-width:440px;margin:0 auto}
.cbtn{flex:1;min-width:140px;padding:14px 20px;border-radius:10px;font-family:'Inter',sans-serif;font-size:14px;font-weight:800;letter-spacing:0.5px;cursor:pointer;text-decoration:none;display:inline-flex;align-items:center;justify-content:center;gap:8px;border:1px solid transparent;transition:all 0.2s}
.cb-white{background:#fff;color:#000}
.cb-white:hover{background:#e5e5e5}
.cb-out{background:transparent;border-color:#2a2a2a;color:#fff}
.cb-out:hover{border-color:#555;background:#0d0d0d}
.cbtn svg{width:16px;height:16px;stroke:currentColor;fill:none;stroke-width:2.2}

/* Pricing section */
.psec{position:relative;z-index:5;max-width:1200px;margin:0 auto;padding:0 18px 80px;scroll-margin-top:20px}
.ptitle{text-align:center;font-family:'Inter',sans-serif;font-size:24px;font-weight:800;letter-spacing:1px;color:#fff;margin-bottom:8px}
.psub{text-align:center;font-size:11px;color:#7a7a7a;letter-spacing:3px;text-transform:uppercase;margin-bottom:14px;font-weight:600}
.pnote{text-align:center;font-size:11px;color:#7a8ba0;max-width:560px;margin:0 auto 30px;line-height:1.6;padding:10px 16px;background:rgba(59,130,246,0.05);border:1px solid rgba(59,130,246,0.15);border-radius:10px}
.pgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}
@media(max-width:700px){.pgrid{grid-template-columns:1fr}}

.pc{background:#0b0b0e;border:1.5px solid #1f1f24;border-radius:18px;padding:32px 22px 22px;position:relative;display:flex;flex-direction:column;transition:all 0.3s}
.pc.blue{border-color:rgba(59,130,246,0.45)}
.pc.blue:hover{border-color:#3b82f6;box-shadow:0 0 40px rgba(59,130,246,0.25);transform:translateY(-4px)}
.pc.purple{border-color:rgba(139,92,246,0.5)}
.pc.purple:hover{border-color:#8b5cf6;box-shadow:0 0 40px rgba(139,92,246,0.3);transform:translateY(-4px)}
.pc.gold{border-color:rgba(245,158,11,0.5)}
.pc.gold:hover{border-color:#f59e0b;box-shadow:0 0 40px rgba(245,158,11,0.25);transform:translateY(-4px)}
.ribbon{position:absolute;top:-11px;right:20px;background:linear-gradient(135deg,#8b5cf6,#6d28d9);color:#fff;font-family:'Inter',sans-serif;font-size:9px;font-weight:800;letter-spacing:1.5px;padding:5px 12px;border-radius:20px;text-transform:uppercase;box-shadow:0 4px 20px rgba(139,92,246,0.5)}
.pi{width:64px;height:64px;margin:0 auto 20px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.pc.blue .pi{background:rgba(59,130,246,0.08);border:1.5px solid rgba(59,130,246,0.35);color:#60a5fa}
.pc.purple .pi{background:rgba(139,92,246,0.08);border:1.5px solid rgba(139,92,246,0.4);color:#a78bfa}
.pc.gold .pi{background:rgba(245,158,11,0.08);border:1.5px solid rgba(245,158,11,0.4);color:#fbbf24}
.pi svg{width:28px;height:28px}
.pn{text-align:center;font-family:'Inter',sans-serif;font-size:20px;font-weight:800;letter-spacing:5px;margin-bottom:14px;color:#fff;text-transform:uppercase}
.pl{display:flex;justify-content:center;align-items:center;gap:10px;margin-bottom:8px}
.op{font-family:'Inter',sans-serif;font-size:15px;font-weight:700;color:#4a4a4a;text-decoration:line-through}
.deal{background:#dc2626;color:#fff;font-family:'Inter',sans-serif;font-size:9px;font-weight:800;letter-spacing:1.2px;padding:3px 8px;border-radius:5px}
.pm{text-align:center;font-family:'Inter',sans-serif;font-size:48px;font-weight:900;letter-spacing:-1px;margin-bottom:26px;line-height:1;color:#fff}
.pm .cur{font-size:26px;font-weight:700;vertical-align:top;line-height:1;display:inline-block;margin-right:2px}
.feats{list-style:none;margin-bottom:22px;flex:1}
.feats li{display:flex;align-items:flex-start;gap:10px;padding:7px 0;font-size:13px;color:#d8d8dd;line-height:1.45;font-weight:500}
.feats li .ic{flex-shrink:0;width:18px;height:18px;display:flex;align-items:center;justify-content:center;margin-top:2px;color:#22c55e}
.feats li .ic svg{width:14px;height:14px}
.bb{width:100%;padding:13px;border-radius:10px;font-family:'Inter',sans-serif;font-size:12px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;border:none;cursor:pointer;transition:all 0.25s;color:#fff}
.pc.blue .bb{background:linear-gradient(135deg,#3b82f6,#2563eb);box-shadow:0 6px 24px rgba(59,130,246,0.3)}
.pc.purple .bb{background:linear-gradient(135deg,#8b5cf6,#7c3aed);box-shadow:0 6px 24px rgba(139,92,246,0.35)}
.pc.gold .bb{background:linear-gradient(135deg,#f59e0b,#d97706);box-shadow:0 6px 24px rgba(245,158,11,0.3);color:#000}
.an{text-align:center;font-size:10px;color:#4a4a4a;margin-top:10px;letter-spacing:0.5px;font-weight:500}

/* Telegram float */
.tg{position:fixed;right:18px;bottom:18px;width:52px;height:52px;border-radius:50%;background:#22a7e8;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 28px rgba(34,167,232,0.5);cursor:pointer;z-index:20;border:none;text-decoration:none}
.tg svg{width:26px;height:26px;fill:#fff}

</style>
</head>
<body>

<div class="ann" id="ann">
IND server is disabled &mdash; please wait patiently! <a href="#pricing">Learn More</a>
<button class="cls" onclick="document.getElementById('ann').style.display='none'">✕</button>
</div>

<div class="hdr">
<div class="hlogo">
<span class="hshield"><svg viewBox="0 0 24 24"><path d="M12 2L4 5v6c0 5 3.5 9.5 8 11 4.5-1.5 8-6 8-11V5l-8-3z"/><path d="M9 12l2 2 4-4"/></svg></span>
<span class="hname">NIROB X LEVEL</span>
</div>
<button class="hbell"><svg viewBox="0 0 24 24"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg></button>
</div>

<div class="status">
<span class="spill"><span class="dot"></span> System Operational <span class="mut">0ms</span></span>
</div>

<div class="hero">
<h1>NIROB X LEVEL</h1>
<p>Fast, reliable Free Fire level-up automation built for players who want results without the grind. Simple setup, real progress.</p>
<p>Level up your account faster &mdash; stay ahead of the competition.</p>
</div>

<div class="ctas">
<a href="/dashboard" class="cbtn cb-white">Get Started <svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></a>
<a href="#pricing" class="cbtn cb-out">Pricing <svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></a>
</div>

<!-- Pricing -->
<div class="psec" id="pricing">
<div class="ptitle">Choose Your Plan</div>
<div class="psub">Works On All Servers</div>
<div class="pnote">All plans work globally across every Free Fire server &mdash; IND, BD, EUROPE, SG, TH, PH, VN, MY, ID, HK, TW and more. Price shown in USD.</div>
<div class="pgrid" id="pgrid"></div>
</div>

<a class="tg" href="https://t.me/+gvq4rDtcjdwwYzU1" target="_blank"><svg viewBox="0 0 24 24"><path d="M9.78 18.65l.28-4.23 7.68-6.92c.34-.31-.07-.46-.52-.19L7.74 13.3 3.64 12c-.88-.25-.89-.86.2-1.3l15.97-6.16c.73-.33 1.43.18 1.15 1.3l-2.72 12.81c-.19.91-.74 1.13-1.5.71L12.6 16.3l-1.99 1.93c-.23.23-.42.42-.83.42z"/></svg></a>


<script>
const PLANS=[
{id:'starting',name:'STARTING',style:'blue',icon:'bolt',hours:24,slots:3,price:'1',old:'2',pop:false},
{id:'basic',name:'BASIC',style:'purple',icon:'star',hours:48,slots:3,price:'2',old:'4',pop:true},
{id:'premium',name:'PREMIUM',style:'gold',icon:'crown',hours:72,slots:4,price:'2.5',old:'6',pop:false}
];
const TG='vaibhavff570';
const ICONS={
bolt:'__SVG_BOLT__',
star:'__SVG_STAR__',
crown:'__SVG_CROWN__',
check:'__SVG_CHECK__'
};

function feat(p){
const d=p.hours>=24?Math.round(p.hours/24)+' Day'+(p.hours>=48?'s':''):p.hours+' Hours';
const sp=p.id==='premium'?'Fastest Leveling Speed Available':'Fast Leveling Performance';
const off=p.id==='premium'?'Runs 24/7 — No Need To Stay Online':'Runs While You Are Offline';
return[
'Access To The Panel For '+d,
sp,
'Run Multiple Accounts At Once',
'Restart & Manage Accounts Anytime',
off,
'Telegram Payment Support & Quick Help',
p.slots+' Concurrent Account'+(p.slots>1?'s':'')
];
}

function render(){
const g=document.getElementById('pgrid');
let h='';
PLANS.forEach(p=>{
let fh='';
feat(p).forEach(t=>{fh+='<li><span class="ic">'+ICONS.check+'</span><span>'+t+'</span></li>';});
h+='<div class="pc '+p.style+'">';
if(p.pop)h+='<div class="ribbon">Most Popular</div>';
h+='<div class="pi">'+ICONS[p.icon]+'</div>';
h+='<div class="pn">'+p.name+'</div>';
h+='<div class="pl"><span class="op">$'+p.old+'</span><span class="deal">Deal</span></div>';
h+='<div class="pm"><span class="cur">$</span>'+p.price+'</div>';
h+='<ul class="feats">'+fh+'</ul>';
h+='<button class="bb" onclick="buy(\\''+p.id+'\\')">Buy '+p.name+'</button>';
h+='<div class="an">Instant Activation After Payment</div>';
h+='</div>';
});
g.innerHTML=h;
}

function buy(id){
const p=PLANS.find(x=>x.id===id);
let m='Hi, I Want To Buy The '+p.name+' Plan.\\n\\nPlan: $'+p.price+'\\nDuration: '+p.hours+' Hours\\nSlots: '+p.slots+'\\n\\nPlease Send Payment Details.';
window.open('https://t.me/'+TG+'?text='+encodeURIComponent(m),'_blank');
}
render();

/* Smooth scroll for #pricing */
document.querySelectorAll('a[href^="#"]').forEach(a=>{
  a.addEventListener('click',e=>{
    const id=a.getAttribute('href');
    if(id.length>1){
      const el=document.querySelector(id);
      if(el){
        e.preventDefault();
        el.scrollIntoView({behavior:'smooth',block:'start'});
      }
    }
  });
});

</script>
</body>
</html>
"""

HOME_HTML = HOME_HTML.replace("__SVG_BOLT__", _icon("bolt_fill", "currentColor", 28).replace('"', '\\"'))
HOME_HTML = HOME_HTML.replace("__SVG_STAR__", _icon("star_fill", "currentColor", 28).replace('"', '\\"'))
HOME_HTML = HOME_HTML.replace("__SVG_CROWN__", _icon("crown_fill", "currentColor", 28).replace('"', '\\"'))
HOME_HTML = HOME_HTML.replace("__SVG_CHECK__", _icon("check", "#22c55e", 14).replace('"', '\\"'))

# ==================== LOGIN ====================
LOGIN_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>Login - NIROB X LEVEL</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{background:#0a0a0a;display:flex;align-items:center;justify-content:center;padding:20px;min-height:100vh;position:relative}
body::before{content:'';position:absolute;inset:0;background:
  linear-gradient(rgba(255,255,255,0.015) 1px,transparent 1px),
  linear-gradient(90deg,rgba(255,255,255,0.015) 1px,transparent 1px);
  background-size:60px 60px;pointer-events:none;mask-image:radial-gradient(ellipse at center,#000 20%,transparent 80%);
  -webkit-mask-image:radial-gradient(ellipse at center,#000 20%,transparent 80%)}

.wrap{width:100%;max-width:440px;position:relative;z-index:1}
.brand{display:flex;align-items:center;justify-content:center;gap:12px;margin-bottom:60px}
.shield{
  width:36px;height:36px;
  display:inline-flex;align-items:center;justify-content:center;
}
.shield svg{width:36px;height:36px;stroke:#fff;fill:none;stroke-width:1.8}
.brand-txt{font-family:'Inter',sans-serif;font-size:18px;font-weight:800;letter-spacing:3px;color:#fff}
.brand-txt .dot{color:#555;font-weight:700}

.welcome{text-align:center;margin-bottom:36px}
.welcome h1{font-family:'Inter',sans-serif;font-size:28px;font-weight:700;letter-spacing:-0.5px;color:#fff;margin-bottom:8px}
.welcome p{font-size:13px;color:#7a7a7a;font-weight:400}

.err{background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.3);color:#ef4444;padding:11px;border-radius:10px;font-size:12px;margin-bottom:16px;display:none;text-align:center}
.err.on{display:block}

.f{margin-bottom:20px}
.f label{display:block;font-size:13px;font-weight:700;color:#fff;margin-bottom:9px;text-align:center}
.iw{position:relative}
.iw svg.lft{position:absolute;left:16px;top:50%;transform:translateY(-50%);width:18px;height:18px;stroke:#6a6a6a;fill:none;stroke-width:1.8;pointer-events:none}
.iw svg.rgt{position:absolute;right:16px;top:50%;transform:translateY(-50%);width:18px;height:18px;stroke:#6a6a6a;fill:none;stroke-width:1.8;cursor:pointer;transition:stroke 0.2s}
.iw svg.rgt:hover{stroke:#fff}
.f input{
  width:100%;background:transparent;
  border:1px solid #2a2a2a;border-radius:10px;
  padding:15px 46px;
  color:#fff;font-size:14px;
  font-family:'Inter',sans-serif;font-weight:500;
  outline:none;transition:all 0.2s;
}
.f input::placeholder{color:#4a4a4a;font-weight:400}
.f input:focus{border-color:#555;background:rgba(255,255,255,0.02)}

.remember{display:flex;align-items:center;justify-content:center;gap:10px;margin:24px 0 22px}
.remember input[type=checkbox]{
  appearance:none;-webkit-appearance:none;
  width:20px;height:20px;border-radius:5px;
  border:1.5px solid #444;background:transparent;
  cursor:pointer;position:relative;transition:all 0.2s;flex-shrink:0;
}
.remember input[type=checkbox]:checked{background:#fff;border-color:#fff}
.remember input[type=checkbox]:checked::after{
  content:'';position:absolute;left:6px;top:2px;
  width:6px;height:11px;
  border:solid #000;border-width:0 2px 2px 0;
  transform:rotate(45deg);
}
.remember label{font-size:14px;color:#b8b8b8;cursor:pointer;font-weight:500}

.btn{
  width:100%;padding:17px;border-radius:10px;
  background:#8a8a8a;color:#0a0a0a;
  border:none;cursor:pointer;
  font-family:'Inter',sans-serif;
  font-size:15px;font-weight:700;
  letter-spacing:0.3px;
  display:flex;align-items:center;justify-content:center;gap:10px;
  transition:all 0.2s;
}
.btn:hover{background:#a0a0a0}
.btn svg{width:18px;height:18px;stroke:#0a0a0a;fill:none;stroke-width:2}
.btn:disabled{opacity:0.6;cursor:not-allowed}

.foot{text-align:center;margin-top:28px;font-size:13px;color:#6a6a6a}
.foot a{color:#fff;text-decoration:none;font-weight:600;border-bottom:1px solid #333;padding-bottom:1px}
.foot a:hover{border-color:#fff}
</style>
</head>
<body>
<div class="wrap">

<div class="brand">
<span class="shield">
<svg viewBox="0 0 24 24"><path d="M12 2L4 5v6c0 5 3.5 9.5 8 11 4.5-1.5 8-6 8-11V5l-8-3z"/><path d="M9 12l2 2 4-4"/></svg>
</span>
<span class="brand-txt">GHOST X<span class="space"> </span>LVL</span>
</div>

<div class="welcome">
<h1>Welcome back</h1>
<p>Secure login &mdash; tokens protected.</p>
</div>

<div class="err" id="err"></div>

<form id="f">
<div class="f">
<label>Username</label>
<div class="iw">
<svg class="lft" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
<input type="text" id="u" placeholder="jane.doe" autocomplete="username" required>
</div>
</div>

<div class="f">
<label>Password</label>
<div class="iw">
<svg class="lft" viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
<svg class="rgt" id="eye" viewBox="0 0 24 24"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
<input type="password" id="p" placeholder="••••••••••" autocomplete="current-password" required>
</div>
</div>

<div class="remember">
<input type="checkbox" id="rm" checked>
<label for="rm">Remember me</label>
</div>

<button type="submit" class="btn" id="sb">
Login
<svg viewBox="0 0 24 24"><path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"/><polyline points="10 17 15 12 10 7"/><line x1="15" y1="12" x2="3" y2="12"/></svg>
</button>
</form>

<div class="foot">New here? <a href="/plans">Create account</a></div>
</div>

<script>
const eye=document.getElementById('eye');
const pw=document.getElementById('p');
eye.addEventListener('click',()=>{
const t=pw.type==='password'?'text':'password';
pw.type=t;
eye.style.stroke=t==='text'?'#fff':'#6a6a6a';
});

document.getElementById('f').addEventListener('submit',async(e)=>{
e.preventDefault();
const err=document.getElementById('err');
const btn=document.getElementById('sb');
err.classList.remove('on');
btn.disabled=true;btn.firstChild.textContent='Signing in...';
const u=document.getElementById('u').value.trim();
const p=document.getElementById('p').value;
try{
const r=await fetch('/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,password:p})});
const d=await r.json();
if(d.status==='ok')window.location.href=d.redirect||'/dashboard';
else{err.textContent=d.error||'Login Failed';err.classList.add('on')}
}catch(ex){err.textContent='Network Error';err.classList.add('on')}
btn.disabled=false;btn.firstChild.textContent='Login';
});
</script>
</body>
</html>
"""


# ==================== PLANS ====================
PLANS_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Pricing - NIROB X LEVEL</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{background:radial-gradient(ellipse at top,#0a1020 0%,#000 55%);padding-bottom:60px}
.head{display:flex;align-items:center;justify-content:space-between;padding:18px 22px;border-bottom:1px solid var(--line);max-width:1400px;margin:0 auto}
.logo{display:flex;align-items:center;gap:10px;font-family:'Orbitron',sans-serif;font-size:14px;font-weight:700;letter-spacing:2px}
.logo .lm{width:36px;height:36px;background:linear-gradient(135deg,#3b82f6,#8b5cf6);border-radius:10px;display:inline-flex;align-items:center;justify-content:center;font-weight:900;font-size:16px;box-shadow:0 0 20px rgba(59,130,246,0.35)}
.wrap{max-width:1200px;margin:0 auto;padding:44px 22px 0}
.t{text-align:center;font-family:'Orbitron',sans-serif;font-size:30px;font-weight:800;letter-spacing:2px;text-transform:uppercase;margin-bottom:10px}
.sub{text-align:center;font-size:11px;color:var(--mut);letter-spacing:4px;text-transform:uppercase;margin-bottom:14px;font-weight:600}
.note{text-align:center;font-size:12px;color:#7a8ba0;max-width:640px;margin:0 auto 40px;line-height:1.6;padding:12px 18px;background:rgba(59,130,246,0.05);border:1px solid rgba(59,130,246,0.15);border-radius:10px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:20px}
@media(max-width:700px){.grid{grid-template-columns:1fr}}

.pc{background:var(--card);border:1.5px solid var(--line2);border-radius:20px;padding:36px 24px 24px;position:relative;transition:all 0.3s;display:flex;flex-direction:column}
.pc.blue{border-color:rgba(59,130,246,0.45)}
.pc.blue:hover{border-color:#3b82f6;box-shadow:0 0 40px rgba(59,130,246,0.25);transform:translateY(-4px)}
.pc.purple{border-color:rgba(139,92,246,0.5)}
.pc.purple:hover{border-color:#8b5cf6;box-shadow:0 0 40px rgba(139,92,246,0.3);transform:translateY(-4px)}
.pc.gold{border-color:rgba(245,158,11,0.5)}
.pc.gold:hover{border-color:#f59e0b;box-shadow:0 0 40px rgba(245,158,11,0.25);transform:translateY(-4px)}
.ribbon{position:absolute;top:-12px;right:22px;background:linear-gradient(135deg,#8b5cf6,#6d28d9);color:#fff;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1.5px;padding:6px 14px;border-radius:20px;text-transform:uppercase;box-shadow:0 4px 20px rgba(139,92,246,0.5)}
.pi{width:70px;height:70px;margin:0 auto 22px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.pc.blue .pi{background:rgba(59,130,246,0.08);border:1.5px solid rgba(59,130,246,0.35);color:#60a5fa}
.pc.purple .pi{background:rgba(139,92,246,0.08);border:1.5px solid rgba(139,92,246,0.4);color:#a78bfa}
.pc.gold .pi{background:rgba(245,158,11,0.08);border:1.5px solid rgba(245,158,11,0.4);color:#fbbf24}
.pi svg{width:30px;height:30px}
.pn{text-align:center;font-family:'Orbitron',sans-serif;font-size:24px;font-weight:700;letter-spacing:6px;margin-bottom:16px;color:#fff}
.pl{display:flex;justify-content:center;align-items:center;gap:12px;margin-bottom:8px}
.op{font-family:'Inter',sans-serif;font-size:16px;font-weight:700;color:var(--dim);text-decoration:line-through}
.deal{background:#dc2626;color:#fff;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1.5px;padding:3px 9px;border-radius:5px}
.pm{text-align:center;font-family:'Orbitron',sans-serif;font-size:52px;font-weight:900;letter-spacing:-1px;margin-bottom:30px;line-height:1;color:#fff}
.pm .cur{font-size:30px;font-weight:700;vertical-align:top;line-height:1;display:inline-block;margin-right:2px}
.feats{list-style:none;margin-bottom:26px;flex:1}
.feats li{display:flex;align-items:flex-start;gap:12px;padding:8px 0;font-size:14px;color:#d8d8dd;line-height:1.45;font-weight:500}
.feats li .ic{flex-shrink:0;width:18px;height:18px;display:flex;align-items:center;justify-content:center;margin-top:2px;color:#22c55e}
.feats li .ic svg{width:15px;height:15px}
.bb{width:100%;padding:15px;border-radius:12px;font-family:'Orbitron',sans-serif;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;border:none;cursor:pointer;transition:all 0.25s;color:#fff}
.pc.blue .bb{background:linear-gradient(135deg,#3b82f6,#2563eb);box-shadow:0 6px 24px rgba(59,130,246,0.3)}
.pc.purple .bb{background:linear-gradient(135deg,#8b5cf6,#7c3aed);box-shadow:0 6px 24px rgba(139,92,246,0.35)}
.pc.gold .bb{background:linear-gradient(135deg,#f59e0b,#d97706);box-shadow:0 6px 24px rgba(245,158,11,0.3);color:#000}
.an{text-align:center;font-size:11px;color:var(--dim);margin-top:12px;letter-spacing:0.5px;font-weight:500}
.flink{text-align:center;margin-top:36px;font-size:13px;color:var(--mut)}
.flink a{color:#60a5fa;text-decoration:none;font-weight:700}
</style>
</head>
<body>
<div class="head">
<div class="logo"><span class="lm">G</span><span>NIROB X LEVEL</span></div>
<a href="/login" style="color:#fff;text-decoration:none;font-size:13px;font-weight:700">Login →</a>
</div>
<div class="wrap">
<div class="t">Choose Your Plan</div>
<div class="sub">Works On All Servers</div>
<div class="note">All plans work globally across every Free Fire server &mdash; IND, BD, EUROPE, SG, TH, PH, VN, MY, ID, HK, TW and more. Price shown in USD.</div>
<div class="grid" id="grid"></div>
<div class="flink">Already Have An Account? <a href="/login">Sign In</a></div>
</div>
<script>
const SVG={
check:'__SVG_CHECK__',
bolt:'__SVG_BOLT__',
star:'__SVG_STAR__',
crown:'__SVG_CROWN__'
};
const PLANS=[
{id:'starting',name:'STARTING',style:'blue',icon:'bolt',hours:24,slots:3,price:'1',old:'2',pop:false},
{id:'basic',name:'BASIC',style:'purple',icon:'star',hours:48,slots:3,price:'2',old:'4',pop:true},
{id:'premium',name:'PREMIUM',style:'gold',icon:'crown',hours:72,slots:4,price:'2.5',old:'6',pop:false}
];
const TG='vaibhavff570';

function feat(p){
const d=p.hours>=24?Math.round(p.hours/24)+' Day'+(p.hours>=48?'s':''):p.hours+' Hours';
const sp=p.id==='premium'?'Fastest Leveling Speed Available':'Fast Leveling Performance';
const off=p.id==='premium'?'Runs 24/7 &mdash; No Need To Stay Online':'Runs While You Are Offline';
return[
{ic:'check',txt:'Access To The Panel For '+d},
{ic:'check',txt:sp},
{ic:'check',txt:'Run Multiple Accounts At Once'},
{ic:'check',txt:'Restart & Manage Accounts Anytime'},
{ic:'check',txt:off},
{ic:'check',txt:'Telegram Payment Support & Quick Help'},
{ic:'check',txt:p.slots+' Concurrent Account'+(p.slots>1?'s':'')}
];
}

function render(){
const g=document.getElementById('grid');
let h='';
PLANS.forEach(p=>{
let fh='';
feat(p).forEach(f=>{
fh+='<li><span class="ic">'+SVG.check+'</span><span>'+f.txt+'</span></li>';
});
h+='<div class="pc '+p.style+'">';
if(p.pop)h+='<div class="ribbon">Most Popular</div>';
h+='<div class="pi">'+SVG[p.icon]+'</div>';
h+='<div class="pn">'+p.name+'</div>';
h+='<div class="pl"><span class="op">$'+p.old+'</span><span class="deal">Deal</span></div>';
h+='<div class="pm"><span class="cur">$</span>'+p.price+'</div>';
h+='<ul class="feats">'+fh+'</ul>';
h+='<button class="bb" onclick="buy(\\''+p.id+'\\')">Buy '+p.name+'</button>';
h+='<div class="an">Instant Activation After Payment</div>';
h+='</div>';
});
g.innerHTML=h;
}

function buy(id){
const p=PLANS.find(x=>x.id===id);
let m='Hi, I Want To Buy The '+p.name+' Plan.\\n\\nPlan: $'+p.price+'\\nDuration: '+p.hours+' Hours\\nSlots: '+p.slots+'\\n\\nPlease Send Payment Details.';
window.open('https://t.me/'+TG+'?text='+encodeURIComponent(m),'_blank');
}
render();
</script>
</body>
</html>
"""

PLANS_HTML = PLANS_HTML.replace("__SVG_CHECK__", _icon("check", "#22c55e", 15).replace('"', '\\"'))
PLANS_HTML = PLANS_HTML.replace("__SVG_BOLT__", _icon("bolt_fill", "currentColor", 30).replace('"', '\\"'))
PLANS_HTML = PLANS_HTML.replace("__SVG_STAR__", _icon("star_fill", "currentColor", 30).replace('"', '\\"'))
PLANS_HTML = PLANS_HTML.replace("__SVG_CROWN__", _icon("crown_fill", "currentColor", 30).replace('"', '\\"'))


# ==================== EXPIRED ====================
EXPIRED_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Plan Expired - NIROB X LEVEL</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{display:flex;align-items:center;justify-content:center;padding:24px;background:radial-gradient(ellipse at top,#200a0a 0%,#000 60%)}
.wrap{width:100%;max-width:460px;text-align:center}
.ic{width:84px;height:84px;border-radius:50%;background:rgba(239,68,68,0.08);border:1.5px solid var(--red);display:inline-flex;align-items:center;justify-content:center;margin-bottom:24px;color:var(--red)}
h1{font-family:'Orbitron',sans-serif;font-size:26px;font-weight:800;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px}
p{font-size:14px;color:var(--mut);line-height:1.7;margin-bottom:30px}
.br{display:flex;flex-direction:column;gap:10px;max-width:300px;margin:0 auto}
.b{display:block;padding:14px;border-radius:10px;font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;text-decoration:none;text-align:center;transition:all 0.2s;border:none;cursor:pointer}
.b1{background:linear-gradient(135deg,#3b82f6,#2563eb);color:#fff}
.b1:hover{box-shadow:0 8px 28px rgba(59,130,246,0.5)}
.b2{background:transparent;border:1px solid var(--line2);color:var(--mut)}
.b2:hover{border-color:var(--red);color:var(--red)}
</style>
</head>
<body>
<div class="wrap">
<div class="ic">""" + _icon("warn", "currentColor", 40) + """</div>
<h1>Plan Expired</h1>
<p>Your Plan Has Ended And All Bots Have Been Stopped.<br>To Renew, Contact @NIROB_BBZ On Telegram.</p>
<div class="br">
<a class="b b1" href="/plans">Renew Plan</a>
<a class="b b2" href="/logout">Logout</a>
</div>
</div>
</body>
</html>
"""


# ==================== DASHBOARD ====================
# ==================== DASHBOARD ====================
DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>Dashboard - NIROB X LEVEL</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{background:radial-gradient(ellipse at top,#0a1020 0%,#000 55%);padding-bottom:80px;overflow-x:hidden}
*{-webkit-tap-highlight-color:transparent}

/* ===== TOP BAR ===== */
.top{position:sticky;top:0;z-index:50;background:rgba(0,0,0,0.9);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.top-in{max-width:1200px;margin:0 auto;padding:12px 16px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap}
.logo{display:flex;align-items:center;gap:8px;font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;letter-spacing:1.5px}
.lm{width:28px;height:28px;background:linear-gradient(135deg,#3b82f6,#8b5cf6);color:#fff;border-radius:8px;display:inline-flex;align-items:center;justify-content:center;font-weight:900;font-size:13px;box-shadow:0 0 12px rgba(59,130,246,0.4)}
.meta{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.mi{display:flex;flex-direction:column;gap:1px;padding:3px 9px;border-left:2px solid #3b82f6}
.mi .l{font-size:8px;color:var(--mut);letter-spacing:1.2px;text-transform:uppercase;font-weight:800;font-family:'Orbitron',sans-serif}
.mi .v{font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;white-space:nowrap}
.act{display:flex;gap:5px}
.bs{padding:8px 12px;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;border-radius:8px;cursor:pointer;text-decoration:none;border:1px solid transparent;display:inline-flex;align-items:center;justify-content:center;gap:4px;transition:all 0.2s;white-space:nowrap}
.bw{background:#fff;color:#000}
.bw:hover{opacity:0.88}
.bg{background:transparent;border-color:var(--line2);color:var(--mut)}
.bg:hover{border-color:var(--red);color:var(--red)}
.bf{background:transparent;border-color:var(--line2);color:#fff;width:32px;height:32px;padding:0}
.bf:hover{background:var(--card2)}
.bf.sp svg{animation:sp 0.7s linear infinite}
@keyframes sp{to{transform:rotate(360deg)}}
@keyframes pl{0%,100%{opacity:1}50%{opacity:0.4}}

/* ===== MAIN ===== */
.main{max-width:1200px;margin:0 auto;padding:18px 14px 80px}
.grid{display:grid;grid-template-columns:1fr;gap:14px}

/* ===== CARD ===== */
.cc{
  position:relative;
  background:linear-gradient(145deg,#0b1220 0%,#080c14 100%);
  border:1px solid #1a2740;
  border-radius:16px;
  overflow:hidden;
  transition:border-color 0.25s, box-shadow 0.25s;
}
.cc:hover{border-color:#1e3a5f;box-shadow:0 0 0 1px rgba(59,130,246,0.08), 0 8px 32px rgba(0,0,0,0.5)}

/* ===== PILLS + STATUS ===== */
.tagline{padding:14px 16px 10px;display:flex;align-items:center;gap:7px;flex-wrap:wrap}
.pill{
  display:inline-flex;align-items:center;gap:6px;
  background:rgba(255,255,255,0.03);
  border:1px solid rgba(255,255,255,0.08);
  border-radius:20px;
  padding:5px 12px;
  font-family:'Orbitron',sans-serif;
  font-size:9px;font-weight:700;
  letter-spacing:1.2px;
  text-transform:uppercase;
  color:#d0d5dd;
}
.pill.uid{font-family:'JetBrains Mono',monospace;letter-spacing:0.4px;font-size:10px}
.pill svg{width:11px;height:11px;opacity:0.75}

.status-top{
  display:inline-flex;align-items:center;gap:5px;
  background:rgba(34,197,94,0.12);
  border:1px solid rgba(34,197,94,0.5);
  border-radius:20px;
  padding:5px 12px;
  font-family:'Orbitron',sans-serif;
  font-size:9px;font-weight:800;
  letter-spacing:1.2px;
  text-transform:uppercase;
  color:#22c55e;
  white-space:nowrap;
  margin-left:auto;
}
.status-top .dot{width:6px;height:6px;border-radius:50%;background:#22c55e;box-shadow:0 0 6px #22c55e;animation:pl 1.4s infinite}
.status-top.paused{background:rgba(138,138,149,0.12);border-color:rgba(138,138,149,0.4);color:#8a8a95}
.status-top.paused .dot{background:#8a8a95;box-shadow:none;animation:none}
.status-top.match{background:rgba(245,158,11,0.12);border-color:rgba(245,158,11,0.5);color:#f59e0b}
.status-top.match .dot{background:#f59e0b;box-shadow:0 0 6px #f59e0b}
.status-top.online{background:rgba(59,130,246,0.12);border-color:rgba(59,130,246,0.5);color:#60a5fa}
.status-top.online .dot{background:#3b82f6;box-shadow:0 0 6px #3b82f6}

/* ===== REFRESH ===== */
.refresh-btn{
  display:inline-flex;align-items:center;gap:6px;
  background:rgba(34,197,94,0.08);
  border:1px solid rgba(34,197,94,0.35);
  border-radius:9px;
  padding:7px 14px;
  color:#22c55e;
  font-size:12px;font-weight:700;
  cursor:pointer;
  transition:all 0.2s;
  margin:0 16px 14px;
  font-family:'Inter',sans-serif;
}
.refresh-btn:hover{background:rgba(34,197,94,0.15);border-color:#22c55e}
.refresh-btn svg{width:12px;height:12px}
.refresh-btn.spin svg{animation:sp 0.7s linear infinite}

/* ===== AVATAR ===== */
.acc-head{
  display:flex;align-items:center;gap:12px;
  padding:14px 16px;
  background:linear-gradient(135deg,rgba(59,130,246,0.08),rgba(59,130,246,0.02));
  border-top:1px solid rgba(59,130,246,0.1);
  border-bottom:1px solid rgba(59,130,246,0.1);
}
.avatar{
  width:48px;height:48px;border-radius:11px;
  background:linear-gradient(135deg,#1e3a5f,#0f1e33);
  border:1px solid rgba(59,130,246,0.3);
  display:flex;align-items:center;justify-content:center;
  font-family:'Orbitron',sans-serif;
  font-weight:900;font-size:19px;color:#fff;
  flex-shrink:0;
  box-shadow:inset 0 0 16px rgba(59,130,246,0.1);
}
.hinfo{flex:1;min-width:0}
.hinfo h3{
  font-family:'Orbitron',sans-serif;
  font-size:14px;font-weight:800;
  letter-spacing:0.3px;
  color:#fff;
  margin-bottom:3px;
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
}
.hinfo p{
  font-family:'JetBrains Mono',monospace;
  font-size:10px;color:#7c869a;
  letter-spacing:0.3px;
}
.lvl-badge{
  background:rgba(59,130,246,0.12);
  border:1px solid rgba(59,130,246,0.45);
  border-radius:8px;
  padding:6px 11px;
  font-family:'Orbitron',sans-serif;
  font-size:11px;font-weight:800;
  letter-spacing:0.8px;
  color:#60a5fa;
  white-space:nowrap;
  flex-shrink:0;
}

/* ===== INFO ROWS ===== */
.cd{padding:12px 16px;border-bottom:1px solid rgba(255,255,255,0.05);display:grid;grid-template-columns:1fr 1fr;gap:8px 22px}
@media(max-width:560px){.cd{grid-template-columns:1fr}}
.row{display:flex;align-items:center;gap:7px;font-size:12px;min-width:0}
.row .k{color:var(--mut);font-size:9px;font-weight:800;letter-spacing:1.3px;text-transform:uppercase;min-width:76px;font-family:'Orbitron',sans-serif}
.row .v{color:#fff;font-weight:700;font-family:'JetBrains Mono',monospace;font-size:11px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}

.timerow{padding:9px 16px;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;align-items:center;gap:7px;font-size:10px;color:var(--mut);font-family:'JetBrains Mono',monospace}
.td{width:4px;height:4px;border-radius:50%;background:#fff;opacity:0.5}

.lvlrow{padding:11px 16px;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;justify-content:space-between;align-items:center;font-size:10px;color:var(--mut);font-weight:800;letter-spacing:1.5px;text-transform:uppercase;font-family:'Orbitron',sans-serif}
.lvlrow .v{font-family:'Orbitron',sans-serif;color:#fff;font-weight:800;font-size:14px;letter-spacing:1px}

.statrow{display:grid;grid-template-columns:1fr 1fr 1fr;border-bottom:1px solid rgba(255,255,255,0.05);background:rgba(0,0,0,0.25)}
.sc{padding:12px 6px;text-align:center;border-right:1px solid rgba(255,255,255,0.05)}
.sc:last-child{border-right:none}
.sc .l{font-size:8px;color:var(--mut);letter-spacing:1.3px;text-transform:uppercase;font-weight:800;margin-bottom:5px;font-family:'Orbitron',sans-serif}
.sc .v{font-family:'JetBrains Mono',monospace;font-size:14px;font-weight:800;color:#fff;word-break:break-all}
.sc .v.g{color:#22c55e}
@media(max-width:400px){.sc .v{font-size:12px}}

.matchrow{padding:11px 16px;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;justify-content:space-between;align-items:center;font-size:10px;color:var(--mut);font-family:'Orbitron',sans-serif;font-weight:800;letter-spacing:1.5px;text-transform:uppercase}
.matchrow .v{color:#fff;font-family:'JetBrains Mono',monospace;font-weight:700;font-size:13px;letter-spacing:0.5px}

/* ===== END BUTTONS ===== */
.acc-actions{
  display:flex;
  gap:8px;
  padding:12px 14px 14px;
  background:transparent;
}
.acc-actions button{
  flex:1;
  padding:11px 6px;
  background:#1c1c1e;
  border:1px solid #2a2a2e;
  border-radius:10px;
  color:#fff;
  font-family:'Inter',sans-serif;
  font-size:11px;
  font-weight:800;
  letter-spacing:0.8px;
  text-transform:uppercase;
  cursor:pointer;
  transition:all 0.18s;
  display:flex;
  align-items:center;
  justify-content:center;
  gap:5px;
  min-width:0;
}
.acc-actions button:hover{background:#242428;border-color:#3a3a40}
.acc-actions button svg{width:13px;height:13px;flex-shrink:0}
.acc-actions button.danger{
  background:#1a0f10;
  border:1px solid #7a1f1f;
  color:#ff3b3b;
}
.acc-actions button.danger:hover{background:#241012;border-color:#ff3b3b}
.acc-actions button.danger svg{stroke:#ff3b3b}

@media(max-width:360px){
  .acc-actions{gap:6px;padding:10px 12px}
  .acc-actions button{padding:10px 3px;font-size:10px;letter-spacing:0.5px;gap:4px}
  .acc-actions button svg{width:11px;height:11px}
}

/* ===== ADD CARD ===== */
.add{
  background:transparent;
  border:1.5px dashed var(--line2);
  border-radius:14px;
  padding:40px 20px;
  text-align:center;cursor:pointer;
  color:var(--mut);font-family:inherit;
  width:100%;transition:all 0.2s;
}
.add:hover{border-color:#3a3a4a;color:#fff}
.add .plus{display:flex;justify-content:center;margin-bottom:10px;color:#fff}
.add .plus svg{width:32px;height:32px}
.add .txt{font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase}
.add .sub{font-size:9px;color:var(--dim);margin-top:6px;letter-spacing:1px}

.empty{text-align:center;padding:60px 20px;color:var(--mut)}
.empty .big{display:flex;justify-content:center;margin-bottom:12px;opacity:0.25}
.empty .big svg{width:44px;height:44px}

/* ===== MODALS ===== */
.modal{position:fixed;inset:0;background:rgba(0,0,0,0.9);backdrop-filter:blur(6px);display:none;align-items:center;justify-content:center;z-index:100;padding:16px}
.modal.on{display:flex}
.mc{background:var(--card);border:1px solid var(--line2);border-radius:16px;padding:22px;max-width:420px;width:100%;max-height:90vh;overflow-y:auto}
.mh{display:flex;justify-content:space-between;align-items:center;margin-bottom:18px}
.mh h3{font-family:'Orbitron',sans-serif;font-size:13px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase}
.mx{background:transparent;border:none;color:var(--mut);cursor:pointer;padding:0;width:28px;height:28px;display:flex;align-items:center;justify-content:center;border-radius:6px;transition:all 0.2s}
.mx:hover{background:var(--card2);color:#fff}
.mx svg{width:18px;height:18px}
.tabs{display:flex;gap:4px;background:var(--card2);padding:4px;border-radius:10px;margin-bottom:16px}
.tb{flex:1;padding:10px;text-align:center;font-family:'Orbitron',sans-serif;font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;border-radius:7px;cursor:pointer;color:var(--mut);border:none;background:transparent;transition:all 0.2s}
.tb.on{background:#fff;color:#000}
.f{margin-bottom:14px}
.f label{display:block;font-size:10px;font-weight:800;color:var(--mut);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:6px}
.f input,.f textarea{width:100%;background:var(--card2);border:1px solid var(--line2);border-radius:10px;padding:12px 14px;color:#fff;font-size:14px;font-family:'Inter',sans-serif;outline:none;transition:border 0.2s;resize:none}
.f input:focus,.f textarea:focus{border-color:#3b82f6;box-shadow:0 0 0 3px rgba(59,130,246,0.15)}
.sb{width:100%;padding:14px;border-radius:10px;font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;cursor:pointer;border:none;background:linear-gradient(135deg,#3b82f6,#2563eb);color:#fff;transition:all 0.2s}
.sb:hover{box-shadow:0 8px 24px rgba(59,130,246,0.4)}
.sb:disabled{opacity:0.5;cursor:not-allowed}
.err{background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.3);color:var(--red);padding:10px;border-radius:10px;font-size:12px;margin-bottom:14px;display:none}
.err.on{display:block}
.hide{display:none!important}

/* Confirm modal */
.conf{position:fixed;inset:0;background:rgba(0,0,0,0.88);backdrop-filter:blur(8px);display:none;align-items:center;justify-content:center;z-index:200;padding:18px}
.conf.on{display:flex}
.conf-box{background:#141414;border:1px solid #262626;border-radius:16px;padding:22px;max-width:400px;width:100%;font-family:'Inter',sans-serif}
.conf-head{font-size:16px;font-weight:700;color:#fff;margin-bottom:14px;text-align:center}
.conf-msg{font-size:13px;line-height:1.65;color:#a8a8a8;text-align:center;margin-bottom:22px}
.conf-btns{display:flex;gap:10px}
.conf-btns button{flex:1;padding:13px 10px;border-radius:10px;font-family:'Inter',sans-serif;font-size:13px;font-weight:700;cursor:pointer;border:none;transition:all 0.2s}
.conf-yes{background:#fff;color:#000}
.conf-yes:hover{background:#e5e5e5}
.conf-no{background:#1c1c1e;color:#fff;border:1px solid #2a2a2e!important}
.conf-no:hover{background:#242428}
.modes{display:flex;gap:8px;margin-bottom:6px}
.mdb{flex:1;text-align:left;padding:10px 12px;border-radius:10px;border:1px solid var(--line2);background:var(--card2);color:var(--mut);cursor:pointer;transition:all .2s}
.mdb b{display:block;font-family:'Orbitron',sans-serif;font-size:9px;letter-spacing:1px;text-transform:uppercase;color:#d0d5dd;margin-bottom:4px}
.mdb span{display:block;font-size:11px;line-height:1.35}
.mdb.on{border-color:#3b82f6;background:rgba(59,130,246,.12);color:#fff}
.mdb.on b{color:#fff}
.lmax{font-style:normal;font-weight:700}
.dl-note{font-size:11px;color:var(--mut);margin:0 0 12px;line-height:1.5}
.dl-list{max-height:260px;overflow-y:auto;margin:0 0 14px;border:1px solid var(--line2);border-radius:10px}
.dl-row{display:flex;justify-content:space-between;gap:10px;padding:9px 12px;font-size:12px;border-bottom:1px solid var(--line2)}
.dl-row:last-child{border-bottom:none}
.dl-row .u{font-family:'JetBrains Mono',monospace;word-break:break-all}
.dl-row .l{color:#4ade80;font-weight:700;white-space:nowrap}
.dl-empty{padding:18px;text-align:center;font-size:12px;color:var(--mut)}
.dl-btns{display:flex;gap:8px;margin-bottom:8px}
.dl-btns a.sb{display:block;text-align:center;text-decoration:none;box-sizing:border-box}
.dl-btns a.off{opacity:.4;pointer-events:none}
.sb.ghost{background:transparent;border:1px solid var(--line2);color:#d0d5dd}
.sb.ghost:hover{box-shadow:none;background:var(--card2)}

</style>
</head>
<body>
<div class="top">
<div class="top-in">
<div class="logo"><span class="lm">G</span><span>NIROB X LEVEL</span></div>
<div class="meta">
<div class="mi"><span class="l">User</span><span class="v" id="ui-u">{{USERNAME}}</span></div>
<div class="mi"><span class="l">Time</span><span class="v" id="ui-t">--</span></div>
<div class="mi"><span class="l">Slots</span><span class="v" id="ui-s">0/0</span></div>
</div>
<div class="act">
<button class="bs bf" id="rf">__ICON_REFRESH__</button>
<button class="bs bw" id="dl-open" onclick="openDl()">Download <span id="dl-n"></span></button>
<a class="bs bw" href="/plans">Buy</a>
<a class="bs bg" href="/logout">Logout</a>
</div>
</div>
</div>
<div class="main"><div class="grid" id="grid"></div></div>

<div class="modal" id="am">
<div class="mc">
<div class="mh"><h3>Add Free Fire Account</h3><button class="mx" onclick="closeAdd()">__ICON_X__</button></div>
<div class="err" id="aer"></div>
<div class="tabs">
<button class="tb on" data-t="guest" onclick="sw('guest')">UID + Password</button>
<button class="tb" data-t="token" onclick="sw('token')">Access Token</button>
<button class="tb" data-t="bulk" onclick="sw('bulk')">Bulk (UID:Pass)</button>
</div>
<form id="af">
<div class="f"><label>System</label>
<div class="modes">
<button type="button" class="mdb on" data-m="unlimited" onclick="setMode('unlimited')"><b>Unlimited XP</b><span>Level 1 &rarr; no limit</span></button>
<button type="button" class="mdb" data-m="limited" onclick="setMode('limited')"><b>Limited</b><span>Level 1 &rarr; <i class="lmax">8</i>, then expires. Finished accounts go to Download.</span></button>
</div></div>
<div id="fg">
<div class="f"><label>Free Fire UID</label><input type="text" id="fu" autocomplete="off"></div>
<div class="f"><label>Password</label><input type="text" id="fp" autocomplete="off"></div>
</div>
<div id="ft" class="hide">
<div class="f"><label>Access Token</label><textarea id="fk" rows="4"></textarea></div>
</div>
<div id="fb" class="hide">
<div class="f"><label>One Account Per Line &mdash; UID:Password</label><textarea id="fbt" rows="8" placeholder="1234567890:password1&#10;1234567891:password2" spellcheck="false" autocomplete="off"></textarea></div>
<div id="fbr" style="font-size:12px;margin:6px 0 10px;color:#9ca3af;white-space:pre-wrap"></div>
</div>
<button type="submit" class="sb" id="ab">Start Bot</button>
</form>
</div>
</div>

<div class="modal" id="dm">
<div class="mc">
<div class="mh"><h3>Completed Accounts</h3><button class="mx" onclick="closeDl()">__ICON_X__</button></div>
<p class="dl-note" id="dl-note"></p>
<div class="dl-list" id="dl-list"></div>
<div class="dl-btns">
<a class="sb" id="dl-txt" href="/api/download/completed?format=txt" download>Download .TXT</a>
<a class="sb" id="dl-csv" href="/api/download/completed?format=csv" download>Download .CSV</a>
</div>
<button type="button" class="sb ghost" id="dl-clear" onclick="clearDone()">Clear list</button>
</div>
</div>

<div class="conf" id="cm">
<div class="conf-box">
<div class="conf-head" id="cm-t">Confirm</div>
<div class="conf-msg" id="cm-m">Are You Sure?</div>
<div class="conf-btns">
<button class="conf-yes" id="cm-y">Yes</button>
<button class="conf-no" id="cm-n">No</button>
</div>
</div>
</div>


<script>
const SVG={
pause:'__SVG_PAUSE__',
play:'__SVG_PLAY__',
trash:'__SVG_TRASH__',
refresh:'__SVG_REFRESH__',
globe:'__SVG_GLOBE__',
id:'__SVG_ID__',
plus:'__SVG_PLUS__',
warn:'__SVG_WARN__'
};
let CT='guest';
let MODE='unlimited';
let DONE=[];
let LMAX=8;
function setMode(m){MODE=m;document.querySelectorAll('.mdb').forEach(b=>b.classList.toggle('on',b.dataset.m===m))}
function openDl(){renderDl();document.getElementById('dm').classList.add('on')}
function closeDl(){document.getElementById('dm').classList.remove('on')}
function renderDl(){
const n=DONE.length;
const guests=DONE.filter(x=>x.type==='guest').length;
const list=document.getElementById('dl-list');
let h='';
if(!n){h='<div class="dl-empty">No finished accounts yet. Accounts added with the Limited system appear here once they reach Level '+LMAX+'.</div>'}
else{DONE.forEach(x=>{h+='<div class="dl-row"><span class="u">'+esc(x.type==='guest'?x.uid:'Token '+x.uid+'...')+'</span><span class="l">Lv.'+esc(x.level||LMAX)+'</span></div>'})}
list.innerHTML=h;
let note=n+' finished account'+(n===1?'':'s')+'. Files contain UID:Password, one per line.';
if(n>guests){note+=' Token accounts have no password, so they are not in the files.'}
document.getElementById('dl-note').textContent=note;
document.getElementById('dl-txt').classList.toggle('off',!guests);
document.getElementById('dl-csv').classList.toggle('off',!guests);
document.getElementById('dl-clear').style.display=n?'':'none';
}
async function clearDone(){
const ok=await showConfirm('Clear List','This removes the finished accounts from this list. Download them first.','Yes, Clear','No, Cancel');
if(!ok)return;
try{await fetch('/api/completed/clear',{method:'POST'})}catch(e){}
await fetchS();renderDl();
}
function sw(t){CT=t;document.querySelectorAll('.tb').forEach(el=>el.classList.toggle('on',el.dataset.t===t));document.getElementById('fg').classList.toggle('hide',t!=='guest');document.getElementById('ft').classList.toggle('hide',t!=='token');document.getElementById('fb').classList.toggle('hide',t!=='bulk');document.getElementById('ab').textContent=(t==='bulk'?'Add All & Start':'Start Bot')}
function openAdd(){document.getElementById('am').classList.add('on');document.getElementById('aer').classList.remove('on')}
function closeAdd(){document.getElementById('am').classList.remove('on');document.getElementById('af').reset();document.getElementById('aer').classList.remove('on')}

/* Confirm — Yes/No */
function showConfirm(title,msg,yesText,noText){
return new Promise(resolve=>{
document.getElementById('cm-t').textContent=title;
document.getElementById('cm-m').textContent=msg;
document.getElementById('cm-y').textContent=yesText||'Yes';
document.getElementById('cm-n').textContent=noText||'No';
document.getElementById('cm-n').style.display='';
document.getElementById('cm').classList.add('on');
const clean=()=>{
document.getElementById('cm').classList.remove('on');
document.getElementById('cm-y').onclick=null;
document.getElementById('cm-n').onclick=null;
};
document.getElementById('cm-y').onclick=()=>{clean();resolve(true)};
document.getElementById('cm-n').onclick=()=>{clean();resolve(false)};
});
}

/* Info — only single Close button */
function showInfo(title,msg,btnText){
return new Promise(resolve=>{
document.getElementById('cm-t').textContent=title;
document.getElementById('cm-m').textContent=msg;
document.getElementById('cm-y').textContent=btnText||'Close';
document.getElementById('cm-n').style.display='none';
document.getElementById('cm').classList.add('on');
document.getElementById('cm-y').onclick=()=>{
document.getElementById('cm').classList.remove('on');
document.getElementById('cm-y').onclick=null;
document.getElementById('cm-n').style.display='';
resolve(true);
};
});
}

document.getElementById('af').addEventListener('submit',async(e)=>{
e.preventDefault();
const err=document.getElementById('aer');
err.classList.remove('on');
const btn=document.getElementById('ab');
if(CT==='bulk'){
const txt=document.getElementById('fbt').value;
const out=document.getElementById('fbr');
if(!txt.trim()){err.textContent='Paste At Least One UID:Password Line';err.classList.add('on');return}
btn.disabled=true;btn.textContent='Adding...';
try{
const r=await fetch('/api/account/bulk',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text:txt,mode:MODE})});
const d=await r.json();
if(d.status!=='ok'){err.textContent=d.error||'Failed';err.classList.add('on')}
else{
let m='Added '+d.added+' account'+(d.added===1?'':'s')+'.';
if(d.skipped){m+=' Skipped '+d.skipped+':';(d.skipped_detail||[]).slice(0,12).forEach(x=>{m+='\\nLine '+x.line+' ('+x.text+'): '+x.error})}
out.textContent=m;
fetchS();
if(!d.skipped){setTimeout(closeAdd,900)}
}
}catch(ex){err.textContent='Network Error';err.classList.add('on')}
btn.disabled=false;btn.textContent='Add All & Start';
return;
}
btn.disabled=true;btn.textContent='Checking...';
let pl={};
if(CT==='guest'){
pl.uid=document.getElementById('fu').value.trim();
pl.password=document.getElementById('fp').value.trim();
if(!pl.uid||!pl.password){err.textContent='UID And Password Required';err.classList.add('on');btn.disabled=false;btn.textContent='Start Bot';return}
}else{
pl.token=document.getElementById('fk').value.trim();
if(!pl.token){err.textContent='Token Required';err.classList.add('on');btn.disabled=false;btn.textContent='Start Bot';return}
}

/* 1) Check account level + region */
let check;
try{
const r=await fetch('/api/account/check',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(pl)});
check=await r.json();
}catch(ex){
err.textContent='Network Error';err.classList.add('on');btn.disabled=false;btn.textContent='Start Bot';return;
}

if(check.status!=='ok'){
err.textContent=check.error||'Login Failed';err.classList.add('on');btn.disabled=false;btn.textContent='Start Bot';return;
}

const lvl=check.level||1;
const reg=(check.region||'').toUpperCase();
const isIND=(reg==='IND'||reg==='IN');

/* 2) Below target level -> GLD plays solo matches first, then LVL takes over */
const lvlMin=check.lvl_min_level||3;
if(MODE==='limited'&&lvl>=(check.limited_max_level||8)){
const okl=await showConfirm('Already Level '+lvl,'This account is already at or above the limit, so it will go straight to your Download list without leveling.','Yes, Continue','No, Cancel');
if(!okl){btn.disabled=false;btn.textContent='Start Bot';return}
}
if(lvl<lvlMin){
const okg=await showConfirm(
'GLD Warm-Up First',
'This Account Is Level '+lvl+'. GLD Will Play Solo Matches Until Level '+lvlMin+', Then Level Up Starts Automatically.',
'Yes, Continue',
'No, Cancel'
);
if(!okg){btn.disabled=false;btn.textContent='Start Bot';return}
}

/* 3) Level ≥ 3 AND IND → IND warning */
if(isIND){
const ok=await showConfirm(
'IND Low Exp',
'You Need To Agree Before Adding IND Account Because IND Accounts Are Getting Low Exp. Max 5K EXP In 5 Minutes.',
'Yes, I Agree',
'No, Cancel'
);
if(!ok){btn.disabled=false;btn.textContent='Start Bot';return}
}

/* 4) Add the account */
btn.textContent='Adding...';
try{
const r=await fetch('/api/account/add',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(Object.assign({},pl,{mode:MODE}))});
const d=await r.json();
if(d.status==='ok'){closeAdd();fetchS()}
else{err.textContent=d.error||'Failed';err.classList.add('on')}
}catch(ex){err.textContent='Network Error';err.classList.add('on')}
btn.disabled=false;btn.textContent='Start Bot';
});

async function delAcc(uid){
const ok=await showConfirm('Delete Account','Please Confirm That You Are Deleting Your Account.','Yes, Delete','No, Cancel');
if(!ok)return;
try{await fetch('/api/account/delete',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({uid})});fetchS()}catch(e){}
}
async function toggleAcc(uid,action){
try{await fetch('/api/account/'+action,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({uid})});fetchS()}catch(e){}
}
async function refreshAcc(uid,btn){
if(btn)btn.classList.add('spin');
try{
await fetch('/api/account/resume',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({uid})});
await fetchS();
}catch(e){}
setTimeout(()=>{if(btn)btn.classList.remove('spin')},700);
}

function esc(s){if(s==null)return'';return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;')}
function ago(ts){
if(!ts)return'--';
const s=Math.floor(Date.now()/1000-ts);
if(s<5)return'Just Now';
if(s<60)return s+'s Ago';
if(s<3600)return Math.floor(s/60)+'m Ago';
if(s<86400)return Math.floor(s/3600)+'h Ago';
return Math.floor(s/86400)+'d Ago'
}
function fmtLeft(s){
if(s<=0)return'Expired';
const h=Math.floor(s/3600);
const m=Math.floor((s%3600)/60);
if(h>0)return h+'h '+m+'m';
return m+'m'
}

function phaseLabel(acc,data){
const t=(data&&data.lvl_min_level)||3;
if(acc.phase==='GLD')return 'GLD &rarr; Lv.'+t;
if(acc.phase==='LVL')return 'LVL Level-Up';
return 'Pending';
}
function render(data){
const g=document.getElementById('grid');
const a=data.accounts||[];
DONE=data.completed||[];
LMAX=data.limited_max_level||8;
document.getElementById('dl-n').textContent=DONE.length?'('+DONE.length+')':'';
document.querySelectorAll('.lmax').forEach(e=>{e.textContent=LMAX});
if(document.getElementById('dm').classList.contains('on'))renderDl();
const unl=!!data.unlimited;
const slots=unl?1e9:(data.slots||0);
if(data.expired){window.location.href='/expired';return}
let h='';

a.forEach(acc=>{
const gained=acc.gained_exp||0;
const isPaused=acc.status==='PAUSED';
const isMatch=acc.status==='IN_MATCH';
const nickname=esc(acc.nickname||'Player');
const initial=nickname.charAt(0).toUpperCase()||'P';
const uid=esc(acc.uid);
const region=esc(acc.region||'IND');

let statusLabel, statusCls;
if(isPaused){statusLabel='PAUSED';statusCls='status-top paused'}
else if(isMatch){statusLabel='IN MATCH';statusCls='status-top match'}
else if(acc.status==='ONLINE'){statusLabel='ONLINE';statusCls='status-top online'}
else if(acc.status==='LOGIN FAILED'){statusLabel='LOGIN FAILED';statusCls='status-top paused'}
else {statusLabel='LIVE';statusCls='status-top'}

h+='<div class="cc">';

h+='<div class="tagline">';
h+='<span class="pill">'+SVG.globe+' '+region+'</span>';
h+='<span class="pill uid">'+SVG.id+' '+uid+'</span>';
h+='<span class="'+statusCls+'"><span class="dot"></span>'+statusLabel+'</span>';
h+='</div>';

h+='<button class="refresh-btn" onclick="refreshAcc(\\''+uid+'\\',this)">'+SVG.refresh+' Refresh</button>';

h+='<div class="acc-head">';
h+='<div class="avatar">'+initial+'</div>';
h+='<div class="hinfo"><h3>'+nickname+'</h3><p>UID: '+uid+'</p></div>';
h+='<div class="lvl-badge">Lv.'+(acc.level||1)+'</div>';
h+='</div>';

h+='<div class="cd">';
h+='<div class="row"><span class="k">Created</span><span class="v">'+ago(acc.created_at)+'</span></div>';
h+='<div class="row"><span class="k">Played</span><span class="v">'+(acc.matches_played||0)+'</span></div>';
h+='<div class="row"><span class="k">Nickname</span><span class="v">'+nickname+'</span></div>';
h+='<div class="row"><span class="k">Region</span><span class="v">'+region+'</span></div>';
h+='</div>';

h+='<div class="timerow"><span class="td"></span> Updated '+ago(acc.last_update)+'</div>';
h+='<div class="lvlrow"><span>Level</span><span class="v">'+(acc.level||1)+'</span></div>';
h+='<div class="lvlrow"><span>Phase</span><span class="v">'+phaseLabel(acc,data)+'</span></div>';
h+='<div class="lvlrow"><span>System</span><span class="v">'+(acc.mode==='limited'?'Limited &rarr; Lv.'+LMAX:'Unlimited XP')+'</span></div>';

h+='<div class="statrow">';
h+='<div class="sc"><div class="l">EXP</div><div class="v">'+(acc.current_exp||0).toLocaleString()+'</div></div>';
h+='<div class="sc"><div class="l">Initial</div><div class="v">'+(acc.initial_exp||0).toLocaleString()+'</div></div>';
h+='<div class="sc"><div class="l">Gained</div><div class="v g">+'+gained.toLocaleString()+'</div></div>';
h+='</div>';

h+='<div class="matchrow"><span>Matches Played</span><span class="v">'+(acc.matches_played||0)+'</span></div>';

h+='<div class="acc-actions">';
h+='<button onclick="toggleAcc(\\''+uid+'\\',\\'pause\\')">'+SVG.pause+' PAUSE</button>';
h+='<button onclick="refreshAcc(\\''+uid+'\\',this)">'+SVG.refresh+' REFRESH</button>';
h+='<button class="danger" onclick="delAcc(\\''+uid+'\\')">'+SVG.trash+' DELETE</button>';
h+='</div>';

h+='</div>';
});

if(a.length<slots){
h+='<button class="add" onclick="openAdd()">';
h+='<div class="plus">'+SVG.plus+'</div>';
h+='<div class="txt">Add Account</div>';
h+='<div class="sub">SLOT '+(a.length+1)+' OF '+(unl?'&infin;':slots)+'</div>';
h+='</button>'
}
if(a.length===0&&slots===0){
h='<div class="empty"><div class="big">'+SVG.warn+'</div><p>No Plan Assigned. Contact @NIROB_BBZ</p></div>'
}

g.innerHTML=h;
document.getElementById('ui-u').textContent=data.username||'{{USERNAME}}';
document.getElementById('ui-t').textContent=fmtLeft(data.seconds_left||0);
document.getElementById('ui-s').textContent=a.length+'/'+(unl?'\u221e':slots)
}

async function fetchS(){
try{
const r=await fetch('/api/stats');
if(r.status===401){window.location.href='/login';return}
const d=await r.json();
render(d)
}catch(e){}
}
document.getElementById('rf').addEventListener('click',async()=>{
const b=document.getElementById('rf');
b.classList.add('sp');
await fetchS();
setTimeout(()=>b.classList.remove('sp'),700)
});


fetchS();
setInterval(fetchS,3000);
</script>
</body>
</html>
"""

DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_PAUSE__", _icon("pause", "currentColor", 13).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_PLAY__", _icon("play", "currentColor", 13).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_TRASH__", _icon("trash", "currentColor", 13).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_REFRESH__", _icon("refresh", "currentColor", 13).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_GLOBE__", _icon("globe", "currentColor", 11).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_ID__", _icon("id", "currentColor", 11).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_PLUS__", _icon("plus", "#fff", 32).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__SVG_WARN__", _icon("warn", "currentColor", 44).replace('"', '\\"'))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__ICON_REFRESH__", _icon("refresh", "currentColor", 14))
DASHBOARD_HTML = DASHBOARD_HTML.replace("__ICON_X__", _icon("x", "currentColor", 18))

# ==================== ADMIN LOGIN ====================
ADMIN_LOGIN_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Admin Access</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{display:flex;align-items:center;justify-content:center;padding:24px;background:radial-gradient(ellipse at top,#1a0a1a 0%,#000 60%)}
.wrap{width:100%;max-width:380px}
.badge{text-align:center;margin-bottom:30px}
.badge .ic{display:inline-flex;width:60px;height:60px;background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.4);border-radius:14px;align-items:center;justify-content:center;margin-bottom:16px;color:var(--red)}
.badge .ic svg{width:26px;height:26px}
.badge h2{font-family:'Orbitron',sans-serif;font-size:17px;font-weight:800;letter-spacing:2px;text-transform:uppercase}
.badge p{font-size:10px;color:var(--red);margin-top:8px;letter-spacing:3px;text-transform:uppercase;opacity:0.8;font-weight:700}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:28px}
.f{margin-bottom:16px}
.f label{display:block;font-size:10px;font-weight:800;color:var(--mut);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:7px}
.f input{width:100%;background:var(--card2);border:1px solid var(--line2);border-radius:10px;padding:12px 14px;color:#fff;font-size:15px;font-family:'Inter',sans-serif;outline:none;transition:border 0.2s}
.f input:focus{border-color:var(--red);box-shadow:0 0 0 3px rgba(239,68,68,0.15)}
.btn{width:100%;background:linear-gradient(135deg,#ef4444,#dc2626);color:#fff;border:none;border-radius:10px;padding:14px;font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;cursor:pointer;transition:all 0.2s}
.btn:hover{box-shadow:0 8px 28px rgba(239,68,68,0.45)}
.err{background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.3);color:var(--red);padding:12px;border-radius:10px;font-size:13px;margin-bottom:16px;display:none}
.err.on{display:block}
</style>
</head>
<body>
<div class="wrap">
<div class="badge">
<div class="ic">""" + _icon("warn", "currentColor", 26) + """</div>
<h2>Admin Access</h2>
<p>Restricted Area</p>
</div>
<div class="card">
<div id="err" class="err"></div>
<form id="f">
<div class="f"><label>Admin Username</label><input type="text" id="u" autocomplete="off" required></div>
<div class="f"><label>Admin Password</label><input type="password" id="p" autocomplete="off" required></div>
<button type="submit" class="btn">Access Panel</button>
</form>
</div>
</div>
<script>
document.getElementById('f').addEventListener('submit',async(e)=>{
e.preventDefault();
const err=document.getElementById('err');
err.classList.remove('on');
const u=document.getElementById('u').value.trim();
const p=document.getElementById('p').value;
try{
const r=await fetch(window.location.pathname,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,password:p})});
const d=await r.json();
if(d.status==='ok')window.location.href=d.redirect;
else{err.textContent=d.error||'Access Denied';err.classList.add('on')}
}catch(ex){err.textContent='Network Error';err.classList.add('on')}
});
</script>
</body>
</html>
"""


# ==================== ADMIN PANEL ====================
ADMIN_PANEL_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Admin Panel - NIROB X LEVEL</title>
""" + _FONTS + """
<style>
""" + _CSS + """
body{background:#000}
.top{background:rgba(0,0,0,0.95);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:50}
.top-in{max-width:1400px;margin:0 auto;padding:14px 24px;display:flex;align-items:center;justify-content:space-between}
.logo{display:flex;align-items:center;gap:10px;font-family:'Orbitron',sans-serif;font-size:12px;font-weight:700;letter-spacing:2px}
.lm{width:30px;height:30px;background:linear-gradient(135deg,#ef4444,#b91c1c);color:#fff;border-radius:8px;display:inline-flex;align-items:center;justify-content:center;font-weight:900;font-size:14px}
.out{background:transparent;border:1px solid var(--line2);color:var(--mut);padding:8px 14px;border-radius:8px;font-family:'Orbitron',sans-serif;font-size:10px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;transition:all 0.2s}
.out:hover{border-color:var(--red);color:var(--red)}
.main{max-width:1400px;margin:0 auto;padding:28px 24px 80px}
.st{font-family:'Orbitron',sans-serif;font-size:14px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:14px;display:flex;align-items:center;gap:10px}
.st::before{content:'';width:3px;height:16px;background:#fff;border-radius:2px}
.panel{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px;margin-bottom:28px}
.grid4{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:14px;margin-bottom:18px}
@media(max-width:900px){.grid4{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.grid4{grid-template-columns:1fr}}
.f label{display:block;font-size:10px;font-weight:800;color:var(--mut);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:6px}
.f input{width:100%;background:var(--card2);border:1px solid var(--line2);border-radius:10px;padding:11px 14px;color:#fff;font-size:14px;font-family:'Inter',sans-serif;outline:none;transition:border 0.2s}
.f input:focus{border-color:#3b82f6}
.btn{background:linear-gradient(135deg,#3b82f6,#2563eb);color:#fff;border:none;padding:12px 26px;border-radius:10px;font-family:'Orbitron',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;cursor:pointer;transition:all 0.2s}
.btn:hover{box-shadow:0 8px 24px rgba(59,130,246,0.4)}
.hint{font-size:11px;color:var(--mut);margin-top:10px}
.tw{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden}
table{width:100%;border-collapse:collapse;font-size:13px}
th{text-align:left;padding:14px 16px;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;color:var(--mut);letter-spacing:1.5px;text-transform:uppercase;border-bottom:1px solid var(--line2);background:var(--card2)}
td{padding:14px 16px;border-bottom:1px solid var(--line);vertical-align:middle;color:#fff}
tbody tr:last-child td{border-bottom:none}
tbody tr:hover{background:rgba(255,255,255,0.02)}
.mono{font-family:'JetBrains Mono',monospace;font-size:12px}
.muted{color:var(--mut)}
.badge{display:inline-block;padding:4px 10px;border-radius:6px;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1px}
.ba{background:rgba(34,197,94,0.15);color:var(--green);border:1px solid rgba(34,197,94,0.3)}
.be{background:rgba(239,68,68,0.15);color:var(--red);border:1px solid rgba(239,68,68,0.3)}
.acts{display:flex;gap:6px;flex-wrap:wrap}
.mini{background:var(--card2);border:1px solid var(--line2);color:var(--mut);padding:7px 11px;font-family:'Orbitron',sans-serif;font-size:9px;font-weight:700;letter-spacing:1px;border-radius:6px;cursor:pointer;transition:all 0.15s}
.mini:hover{border-color:#3b82f6;color:#60a5fa}
.mini.danger:hover{border-color:var(--red);color:var(--red)}
.empty{text-align:center;padding:60px 20px;color:var(--mut);font-size:14px}
.toast{position:fixed;bottom:24px;right:24px;background:var(--card2);border:1px solid #3b82f6;color:#fff;padding:14px 20px;border-radius:10px;font-size:13px;font-weight:700;box-shadow:0 8px 32px rgba(0,0,0,0.6);opacity:0;transform:translateY(20px);transition:all 0.3s;pointer-events:none;z-index:200;max-width:360px}
.toast.on{opacity:1;transform:translateY(0)}
.toast.err{border-color:var(--red)}
</style>
</head>
<body>
<div class="top">
<div class="top-in">
<div class="logo"><span class="lm">A</span><span>NIROB X LEVEL &mdash; ADMIN</span></div>
<a class="out" href="/admin/nirob/levelup/adm-dash/logout">Logout</a>
</div>
</div>
<div class="main">
<div class="st">Create User</div>
<div class="panel">
<div class="grid4">
<div class="f"><label>Username</label><input type="text" id="nu" autocomplete="off"></div>
<div class="f"><label>Password</label><input type="text" id="np" autocomplete="off"></div>
<div class="f"><label>Slots</label><input type="number" id="ns" value="3" min="1" max="20"></div>
<div class="f"><label>Duration (Hours)</label><input type="number" id="nh" value="24" min="1" max="8760"></div>
</div>
<label style="display:flex;align-items:center;gap:8px;margin:0 0 14px;font-size:12px;color:var(--mut)"><input type="checkbox" id="nun" style="width:auto"> Unlimited slots (no account limit for this user)</label>
<button class="btn" onclick="createU()">Create User</button>
<div class="hint">Timer Starts Immediately Upon Creation.</div>
</div>
<div class="st">All Users</div>
<div class="tw" id="tbl"><div class="empty">Loading...</div></div>
<div class="st" style="margin-top:34px">System Settings</div>
<div class="panel">
<div class="grid4" id="cfgGrid"></div>
<label style="display:flex;align-items:center;gap:8px;margin:0 0 14px;font-size:12px;color:var(--mut)"><input type="checkbox" id="cfg_global_unlimited" style="width:auto"> Global unlimited &mdash; remove the slot limit for every user</label>
<button class="btn" onclick="saveCfg()">Save Settings</button>
<div class="hint">Accounts below "GLD From Level" go straight to LVL. Accounts from that level up to (but not including) "LVL From Level" play solo GLD matches until they reach it, then LVL levels them up.</div>
</div>
<div class="st">Live Accounts</div>
<div class="tw" id="accTbl"><div class="empty">Loading...</div></div>
<div class="st" style="margin-top:34px">Live Logs</div>
<div class="panel"><div id="logBox" class="mono" style="max-height:320px;overflow:auto;font-size:11px;line-height:1.6"></div></div>
</div>
<div class="toast" id="toast"></div>
<script>
let CFG={max_slots_cap:20};
function esc(s){if(s==null)return'';return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;')}
function toast(msg,err){const t=document.getElementById('toast');t.textContent=msg;t.classList.toggle('err',!!err);t.classList.add('on');setTimeout(()=>t.classList.remove('on'),2600)}
function fmtLeft(exp){const now=Math.floor(Date.now()/1000);const s=exp-now;if(s<=0)return{t:'Expired',e:true};const h=Math.floor(s/3600);const m=Math.floor((s%3600)/60);return{t:h+'h '+m+'m',e:false}}
function fmtDate(ts){return new Date(ts*1000).toLocaleString()}
async function createU(){
const u=document.getElementById('nu').value.trim();
const p=document.getElementById('np').value.trim();
const s=parseInt(document.getElementById('ns').value);
const unl=document.getElementById('nun').checked;
const h=parseInt(document.getElementById('nh').value);
if(!u||!p){toast('Username And Password Required',true);return}
if(!unl&&(!(s>=1)||s>CFG.max_slots_cap)){toast('Slots Must Be 1-'+CFG.max_slots_cap,true);return}
if(h<1||h>8760){toast('Hours Must Be 1-8760',true);return}
try{
const r=await fetch('/api/admin/create-user',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,password:p,slots:s,hours:h,unlimited:unl})});
const d=await r.json();
if(d.status==='ok'){toast('User Created: '+u);document.getElementById('nu').value='';document.getElementById('np').value='';loadU()}
else{toast(d.error||'Failed',true)}
}catch(e){toast('Network Error',true)}
}
async function loadU(){
try{
const r=await fetch('/api/admin/list-users');
const d=await r.json();
if(d.status!=='ok')return;
const users=d.users||[];
const w=document.getElementById('tbl');
if(users.length===0){w.innerHTML='<div class="empty">No Users Yet</div>';return}
let h='<table><thead><tr>';
h+='<th>Username</th><th>Slots</th><th>Used</th><th>Expires</th><th>Created</th><th>Actions</th>';
h+='</tr></thead><tbody>';
users.forEach(u=>{
const e=fmtLeft(u.expires_at);
const b=e.e?'<span class="badge be">Expired</span>':'<span class="badge ba">'+e.t+'</span>';
h+='<tr>';
h+='<td class="mono">'+esc(u.username)+'</td>';
h+='<td class="mono">'+(u.unlimited?'&infin;':u.slots)+'</td>';
h+='<td class="mono muted">'+(u.used_slots||0)+'</td>';
h+='<td>'+b+'</td>';
h+='<td class="muted">'+fmtDate(u.created_at)+'</td>';
h+='<td><div class="acts">';
h+='<button class="mini" onclick="ext(\\''+esc(u.username)+'\\',24)">+24H</button>';
h+='<button class="mini" onclick="slot(\\''+esc(u.username)+'\\',1)">+1 Slot</button>';
h+='<button class="mini" data-u="'+esc(u.username)+'" data-n="'+(u.unlimited?'0':'1')+'" onclick="unl(this)">'+(u.unlimited?'Set Limited':'Unlimited')+'</button>';
h+='<button class="mini danger" onclick="delU(\\''+esc(u.username)+'\\')">Delete</button>';
h+='</div></td>';
h+='</tr>'
});
h+='</tbody></table>';
w.innerHTML=h
}catch(e){}
}
async function ext(u,h){
try{
const r=await fetch('/api/admin/extend-time',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,hours:h})});
const d=await r.json();
if(d.status==='ok'){toast('Extended '+u+' By '+h+'h');loadU()}
else{toast(d.error||'Failed',true)}
}catch(e){toast('Network Error',true)}
}
async function slot(u,c){
try{
const r=await fetch('/api/admin/add-slot',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,count:c})});
const d=await r.json();
if(d.status==='ok'){toast('Added '+c+' Slot To '+u);loadU()}
else{toast(d.error||'Failed',true)}
}catch(e){toast('Network Error',true)}
}
async function delU(u){
if(!confirm('Delete User '+u+'? This Wipes All Their Data.'))return;
try{
const r=await fetch('/api/admin/delete-user',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u})});
const d=await r.json();
if(d.status==='ok'){toast('Deleted '+u);loadU()}
else{toast(d.error||'Failed',true)}
}catch(e){toast('Network Error',true)}
}
async function unl(b){
const u=b.dataset.u,on=b.dataset.n==='1';
try{
const r=await fetch('/api/admin/set-unlimited',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,unlimited:on})});
const d=await r.json();
if(d.status==='ok'){toast(u+(on?' Is Now Unlimited':' Is Now Limited'));loadU()}else{toast(d.error||'Failed',true)}
}catch(e){toast('Network Error',true)}
}
const CFG_FIELDS=[['gld_min_level','GLD From Level'],['lvl_min_level','LVL From Level (GLD Target)'],['default_slots','Default Slots'],['max_slots_cap','Max Slots Cap'],['bulk_max_lines','Bulk Max Lines (0 = None)'],['level_poll_seconds','Level Poll (Sec)'],['max_parallel_logins','Parallel Logins'],['login_fail_limit','Login Fail Limit'],['limited_max_level','Limited System Max Level']];
async function loadCfg(){
try{
const r=await fetch('/api/admin/config');const d=await r.json();
if(d.status!=='ok')return;
CFG=d.config;
const g=document.getElementById('cfgGrid');
if(!g.dataset.built){
g.innerHTML=CFG_FIELDS.map(f=>'<div class="f"><label>'+f[1]+'</label><input type="number" id="cfg_'+f[0]+'"></div>').join('');
g.dataset.built='1';
CFG_FIELDS.forEach(f=>{document.getElementById('cfg_'+f[0]).value=CFG[f[0]]});
document.getElementById('cfg_global_unlimited').checked=!!CFG.global_unlimited;
}
}catch(e){}
}
async function saveCfg(){
const c={};
CFG_FIELDS.forEach(f=>{c[f[0]]=parseInt(document.getElementById('cfg_'+f[0]).value)});
c.global_unlimited=document.getElementById('cfg_global_unlimited').checked;
try{
const r=await fetch('/api/admin/config',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({config:c})});
const d=await r.json();
if(d.status==='ok'){CFG=d.config;toast('Settings Saved')}else{toast(d.error||'Failed',true)}
}catch(e){toast('Network Error',true)}
}
async function loadAcc(){
try{
const r=await fetch('/api/admin/accounts');const d=await r.json();
if(d.status!=='ok')return;
const w=document.getElementById('accTbl');
const a=d.accounts||[];
if(!a.length){w.innerHTML='<div class="empty">No Live Accounts</div>';return}
let h='<table><thead><tr><th>Owner</th><th>UID</th><th>Name</th><th>Lv</th><th>Phase</th><th>Status</th><th>Matches</th><th>Routing</th></tr></thead><tbody>';
a.forEach(x=>{
h+='<tr><td class="mono">'+esc(x.owner)+'</td><td class="mono">'+esc(x.uid)+'</td><td>'+esc(x.nickname)+'</td><td class="mono">'+x.level+'</td>';
h+='<td><span class="badge '+(x.phase==='GLD'?'be':'ba')+'">'+esc(x.phase)+'</span></td><td class="muted">'+esc(x.status)+'</td><td class="mono muted">'+x.matches_played+'</td>';
h+='<td><div class="acts">';
['auto','gld','lvl'].forEach(m=>{h+='<button class="mini" data-u="'+esc(x.uid)+'" data-m="'+m+'" onclick="force(this)"'+(x.force===m?' style="border-color:#3b82f6;color:#60a5fa"':'')+'>'+m.toUpperCase()+'</button>'});
h+='</div></td></tr>'
});
h+='</tbody></table>';
w.innerHTML=h
}catch(e){}
}
async function force(b){
try{
const r=await fetch('/api/admin/force',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({uid:b.dataset.u,mode:b.dataset.m})});
const d=await r.json();
if(d.status==='ok'){toast('Routing: '+b.dataset.m.toUpperCase());loadAcc()}else{toast(d.error||'Failed',true)}
}catch(e){toast('Network Error',true)}
}
async function loadLogs(){
try{
const r=await fetch('/api/admin/logs');const d=await r.json();
if(d.status!=='ok')return;
const box=document.getElementById('logBox');
const col={success:'#22c55e',error:'#ef4444',warning:'#f59e0b',info:'#9ca3af'};
box.innerHTML=(d.logs||[]).slice().reverse().map(l=>'<div style="color:'+(col[l.level]||'#9ca3af')+'">['+esc(l.time)+'] '+esc(l.message)+'</div>').join('')
}catch(e){}
}
loadCfg();loadU();loadAcc();loadLogs();
setInterval(loadU,5000);setInterval(loadAcc,5000);setInterval(loadLogs,4000);
</script>
</body>
</html>
"""


ALL_TEMPLATES = {
    "home": HOME_HTML,
    "login": LOGIN_HTML,
    "plans": PLANS_HTML,
    "dashboard": DASHBOARD_HTML,
    "expired": EXPIRED_HTML,
    "admin_login": ADMIN_LOGIN_HTML,
    "admin_panel": ADMIN_PANEL_HTML,
}