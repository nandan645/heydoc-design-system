"""Vector replica of the supplied 'iPhone 15 Pro Max.png' mockup (950×1940 px source).
All geometry is in source pixels: 1em on .hd-ip = 1 source px, so it scales cleanly with --phone-w.
Measured: body 926×1926 at (12,7) r145 · titanium rim bands · black bezel · screen 856×1856 at (35,35) r110
· buttons L 353–424 / 485–618 / 656–789, R 578–789 · island 247×72 · home bar 267×10."""
import re

STATUS=('<svg class="hd-ip__ov" viewBox="0 0 856 1856" aria-hidden="true">'
  '<text x="126" y="68" font-size="41" font-weight="600" letter-spacing="-0.4" fill="currentColor" class="hd-ip__time">9:41</text>'
  '<g fill="currentColor"><rect x="610" y="54" width="8.5" height="10" rx="2.2"/><rect x="621.5" y="49" width="8.5" height="15" rx="2.2"/>'
  '<rect x="633" y="44" width="8.5" height="20" rx="2.2"/><rect x="644.5" y="39" width="8.5" height="25" rx="2.2"/></g>'
  '<g fill="none" stroke="currentColor" stroke-width="6.4" stroke-linecap="round"><path d="M667.9 44.9A27 27 0 0 1 706.1 44.9"/><path d="M675.7 52.7A16 16 0 0 1 698.3 52.7"/></g><circle cx="687" cy="61" r="4.6" fill="currentColor"/>'
  '<rect x="722" y="43.5" width="52" height="24" rx="7.5" fill="none" stroke="currentColor" stroke-opacity=".38" stroke-width="2.6"/>'
  '<rect x="726" y="47.5" width="44" height="16" rx="4.5" fill="currentColor"/>'
  '<path d="M777.5 51.5h1.5a2.5 2.5 0 0 1 2.5 2.5v3a2.5 2.5 0 0 1-2.5 2.5h-1.5z" fill="currentColor" fill-opacity=".38"/>'
  '<rect x="304" y="22" width="247" height="72" rx="36" fill="#000"/>'
  '<circle cx="516" cy="58" r="11" fill="#0a0c16"/><circle cx="516" cy="58" r="5.5" fill="#141c36"/><circle cx="513.5" cy="55.5" r="1.6" fill="#3b4a7a"/>'
  '<rect x="295" y="1832" width="267" height="10" rx="5" fill="currentColor"/></svg>')

def ip_phone(screen, theme='light', cls='', style='', label=None):
    return (f'<div class="hd-ip {cls}" style="{style}">'
            '<i class="hd-ip__btn" style="left:6.5em;top:353em;height:72em"></i><i class="hd-ip__btn" style="left:6.5em;top:485em;height:134em"></i>'
            '<i class="hd-ip__btn" style="left:6.5em;top:656em;height:134em"></i><i class="hd-ip__btn hd-ip__btn--r" style="right:6.5em;top:578em;height:212em"></i>'
            f'<div class="hd-ip__body"><div class="hd-ip__screen"><div class="hd-ip__inner"><div class="hd-ip__sb"></div>{screen}</div>{STATUS}</div></div></div>')

CSS_IP=r'''
/* ===== iPhone mockup (vector replica of the supplied PNG) ===== */
.hd-ip{--phone-w:360px;position:relative;width:var(--phone-w);height:calc(var(--phone-w) * 1940 / 950);font-size:calc(var(--phone-w) / 950);flex:none;color:var(--navy)}
.hd-ip__btn{position:absolute;width:6em;border-radius:3em;background:linear-gradient(90deg,#3f3a33 0%,#625d55 45%,#4b463f 75%,#35322c 100%)}
.hd-ip__btn--r{background:linear-gradient(270deg,#3f3a33 0%,#625d55 45%,#4b463f 75%,#35322c 100%)}
.hd-ip__body{position:absolute;left:12em;top:7em;width:926em;height:1926em;border-radius:145em;background:#000;
  box-shadow:inset 0 0 0 2.5em #2e2924,inset 0 0 0 4.5em #433e37,inset 0 0 0 6.5em #6a655d,inset 0 0 0 8.5em #8c877d,inset 0 0 0 10.5em #625d55,
  inset 0 0 0 12.5em #24221f,inset 0 0 0 14.5em #313132,inset 0 0 0 16.5em #0c0c0c,0 18px 48px rgba(1,43,68,.16),0 3px 10px rgba(1,43,68,.08)}
.hd-ip__screen{position:absolute;left:35em;top:35em;width:856em;height:1856em;border-radius:110em;overflow:hidden;background:#fff}
.hd-ip__inner{position:absolute;inset:0;display:flex;flex-direction:column;font-size:calc(var(--phone-w) * 856 / 950 / 21.24)}
.hd-ip__sb{height:3.2em;flex:none}
.hd-ip__ov{position:absolute;left:0;top:0;width:100%;height:100%;pointer-events:none;z-index:6;overflow:visible;color:#000}
.hd-ip--dark .hd-ip__ov{color:#fff}
.hd-ip--dark .hd-ip__screen{background:#0b0c0e}
.hd-ip__time{font-family:'Inter','SF Pro Text',-apple-system,system-ui,sans-serif}
'''
