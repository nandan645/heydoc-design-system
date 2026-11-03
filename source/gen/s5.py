"""Board v2: element cards brought in line with the final film (phones, section accents, real app screens,
camera + agent log, company brain window, dot globe + roadmap). Markup is reused from the film modules."""
import math, json, re
import base, iphone
base.phone = iphone.ip_phone
from base import *
import film, act2, act3, act4, act5
from s3 import pk_track, pk_report, pk_chat, AGENTS, agent
from s4 import endcard

# ---------- film CSS the board needs (film-page globals stripped) ----------
_skip = re.compile(r'^\s*(html,body|body\{|#viewport|#stage|#world|#txt|#scrim|#ctl|#edpop|#edtip|body\.editing|\.tb\b|\.t-|\.hidden-forever)')
def _rules(css):
    out, buf, depth = [], '', 0
    for ch in css:
        buf += ch
        if ch == '{': depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0: out.append(buf); buf = ''
    return out
A1 = ''.join(r for r in _rules(re.sub(r'/\*.*?\*/', '', film.A1CSS, flags=re.S)) if not _skip.match(r.strip()))
import brand
FILMCSS = brand.root_css() + A1 + iphone.CSS_IP + act2.CSS2 + act3.CSS3 + act4.CSS4 + act5.CSS5 + r'''
/* ---- board: show the final (static) state of animated parts ---- */
.eb-card .a2-up,.eb-card .a2-upr,.eb-card .a2-av2,.eb-card .a4-fr,.eb-card .a5-sp{opacity:1}
.eb-card .a2-vin{transform:translateY(-16%)}
.eb-card .a2-logo,.eb-card .a3-tp{position:static;opacity:1}
.eb-card .a5-side{position:static;transform:none}
.hd-ip:has(.a3-shot) .hd-ip__ov{display:none}
.eb-cams{display:grid;grid-template-columns:repeat(2,480px) 480px;grid-template-rows:repeat(3,270px);gap:24px}
.eb-cams .a4-feed{grid-column:3;grid-row:1/4;height:auto}
.eb-cams .a4-cam.is-alert{box-shadow:inset 0 0 0 3px var(--d-amber),0 0 0 8px rgba(254,182,79,.3)}
.eb-cams .is-alert .a4-chips .a4-ochip:first-child{display:none}
.eb-up .a2-up{position:relative;left:auto;top:auto;width:440px;font-size:24px;opacity:1}
.eb-acc{display:grid;gap:24px}
.eb-acc__c{border-radius:22px;padding:24px;box-shadow:0 0 0 2px var(--line)}
.eb-acc__k{font-size:13px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--muted);margin-bottom:16px}
.eb-acc__sw{display:flex;gap:10px;margin-bottom:18px}
.eb-acc__sw span{flex:1;height:72px;line-height:1.3;border-radius:12px;display:flex;align-items:flex-end;padding:8px;font:700 12px var(--font);color:#fff}
.eb-acc__sw span.l{color:var(--navy)}
.eb-acc .hd-headline{font-size:40px}
.eb-orb{width:72px;height:72px;border-radius:50%;flex:none}
.eb-pk{--grad:var(--partner2-grad);--shadow-glow:0 12px 30px rgba(var(--partner2-rgb),.32)}
.eb-pk .hd-chip--solid{color:var(--partner2-on)}.eb-pk .hd-chip--solid .hd-well{background:rgba(255,255,255,.6);color:var(--partner2-on)}
.eb-hbcrowd .hd-crowd .d{fill:var(--partner1-dot)}.eb-hbcrowd .hd-crowd .d.is-hit{fill:var(--partner1)}.eb-hbcrowd .hd-crowd .h{stroke:var(--partner1-pale)}
'''

ph = lambda lbl, s, w=340, cls='': spec(lbl, phone(s, 'light', cls=cls, style=f'--phone-w:{w}px'))

# ---------- E-01b accent system: HeyDoc + Partner ----------
EXAMPLES=[('Any company · e.g. #6A3FD0', '#6A3FD0'), ('Any company · e.g. #E4572E', '#E4572E')]
def _partner_col(title, hexv):
    T = brand.derive(hexv)
    sw = ''.join(f'<span class="{"l" if brand.contrast(T[k]) < 3 else ""}" style="background:{T[k]}">{k}<br>{T[k]}</span>' for k in ('base', 'deep', 'light', 'pale', 'tint'))
    orb = f'radial-gradient(circle at 30% 22%,{T["deep"]} 0%,{T["base"]} 55%,{T["light"]} 100%)'
    return (f'<div class="eb-acc__c"><div class="eb-acc__k">{title}</div><div class="eb-acc__sw">{sw}</div>'
            f'<div style="display:flex;gap:16px;align-items:center"><span class="eb-orb" style="background:{orb}"></span>'
            f'<div><div class="hd-headline" style="font-size:34px"><em style="color:{T["ink"]}">5M+ members</em> · agents</div>'
            f'<div style="display:flex;gap:10px;align-items:center;margin-top:10px"><span style="background:{T["base"]};color:{T["on"]};border-radius:999px;padding:8px 16px;font-weight:700;font-size:14px">Button · on-colour</span>'
            f'<span style="font-size:13px;font-weight:700;color:var(--muted)">text ink {T["ink"]}</span></div></div></div></div>')
def e01b():
    hd = ('<div class="eb-acc__c" style="grid-column:1/-1;display:flex;gap:28px;align-items:center"><div class="eb-acc__k" style="margin:0;min-width:180px">State 1 · HeyDoc</div>'
          '<div class="eb-acc__sw" style="margin:0;flex:1">' + ''.join(f'<span class="{"l" if l else ""}" style="background:{c}">{c}</span>' for c, l in [('#0873ba', 0), ('#139bf5', 0), ('#8fcdf8', 1), ('#eef7fd', 1)]) + '</div>'
          '<span class="eb-orb" style="background:radial-gradient(circle at 30% 22%,#0a84e8,#2ba7f5 55%,#43d0f2)"></span>'
          '<div class="hd-headline" style="font-size:34px">One <em>company brain.</em></div></div>')
    rules = ('<div class="eb-acc__c" style="grid-column:1/-1"><div class="eb-acc__k">State 2 · Partner — one brand hex in, every shade out</div>'
             '<p class="hd-caption" style="font-size:15px;line-height:1.6;margin:0">base = brand colour · deep = 20% toward black · light = +16 lightness (same hue) · pale = 62% toward white · line = 80% · tint = 90% · '
             'dot (unlit crowd) = 14% brand on grey · <b>ink</b> (text on white) = brand darkened in 5% steps until ≥ 3:1 contrast · <b>on</b> (text on a brand fill) = white if the brand passes 3:1, else navy · '
             'orb = radial deep → base → light · hand-offs between any two colours blend along the hue wheel. '
             'Film: CSS custom properties <code>--partner1-*</code>, <code>--partner2-*</code>; change one colour in <code>brand.py</code> or live in Edit mode → Partner brand colours.</p></div>')
    body = '<div class="eb-acc" style="grid-template-columns:repeat(2,1fr)">' + hd + rules + ''.join(_partner_col(t, h) for t, h in EXAMPLES) + '</div>'
    return card('E-01b', 'Accent system · HeyDoc + Partner', '3–6 (any partner section)',
        'a partner section takes over the accent as its brand appears and hands back to HeyDoc blue when it ends; every hand-off blends over ~0.6s on the hue wheel.', body)

# ---------- E-03 phone ----------
def lock_static():
    n = len(film.NOTES)
    notes = ''.join(film.note(*nt[:4]).replace('class="a1-nt"', f'class="a1-nt" style="transform:translateY({(n-1-k)*4.4}em)"') for k, nt in enumerate(film.NOTES))
    notes = notes.replace('<b>Habuild</b>', '<b>Wellness app</b>')
    return film.LOCK.split('<div class="a1-feed"')[0] + f'<div class="a1-feed">{notes}</div>' + '<div class="a1-dock">' + film.LOCK.split('<div class="a1-dock">')[1]

def e03():
    empty = '<div class="hd-scr" style="align-items:center;justify-content:center">' + slot("Screen content", "", "width:80%;height:60%") + '</div>'
    skel = film.SKEL0
    body = f'''<div class="eb-row" style="justify-content:space-between;align-items:flex-start">
  {ph('iPhone replica · light (empty)', empty, 330)}
  {ph('Lock screen · wallpaper, big clock, 5 calm notifications', lock_static(), 330, 'hd-ip--dark')}
  {ph('Skeleton · core → phone hand-off', skel, 330)}
</div>'''
    return card('E-03', 'Phone · iPhone replica + lock screen', '1, 3, 5',
        'vector replica of the supplied iPhone mockup (all em units, scales with --phone-w). Notifications arrive one at a time, newest on top, 550ms spring; the clock never moves. Skeleton is the core → phone hand-off screen.', body)

# ---------- E-05 Habuild ----------
def e05():
    lab = ['1 · Health goals', '2 · Daily meal plan', '3 · Chat + upsell (after scroll)', '4 · Profile + streak']
    phones = ''.join(ph(l, s, 330, 'hd-ip--img') for l, s in zip(lab, act2.SCREENS))
    up = '<div class="eb-up">' + act2.UPSELL[act2.UPSELL.index('<div class="a2-up">'):] + '</div>'
    body = f'''<div class="eb-row" style="justify-content:space-between">{phones}</div>
<div class="eb-row" style="gap:56px;align-items:center;margin-top:40px;padding-top:32px;border-top:2px dashed var(--grey)">
  {spec('Upsell card · Habuild Nutrition Plus (HTML, all text editable)', up)}
  <p class="hd-caption" style="font-size:15px;max-width:620px">Screens 1, 2, 4 are the team's app screenshots. Screen 3 chat text is HTML over a cleaned screenshot; when the upsell arrives the thread scrolls up 16%, benefits pop 120ms apart, the button gets a partner-accent ring and a tap.</p>
</div>'''
    return card('E-05', 'Habuild app screens', '3',
        'orb hops phone to phone (arc + squash); each landing rings the screen in the partner accent and pops its content. Upsell: card springs in 550ms, chat scrolls 700ms soft.', body)

# ---------- E-06 crowd (Habuild green) ----------
def e06():
    from s3 import crowd, counter
    legend = ('<div style="display:flex;gap:28px;align-items:center;margin-top:8px">'
              '<span style="display:flex;gap:8px;align-items:center;font-size:15px;font-weight:700;color:var(--muted)"><svg width="18" height="18"><circle cx="9" cy="9" r="8" style="fill:var(--partner1-dot)"/></svg>1 person</span>'
              '<span style="display:flex;gap:8px;align-items:center;font-size:15px;font-weight:700;color:var(--partner1-ink)"><svg width="26" height="26"><circle cx="13" cy="13" r="12" fill="none" style="stroke:var(--partner1-pale)" stroke-width="2"/><circle cx="13" cy="13" r="8" style="fill:var(--partner1)"/></svg>subscribing · 1 in 10</span></div>')
    big = ('<div style="display:flex;flex-direction:column;align-items:center;gap:14px;text-align:center"><div class="hd-kicker" style="color:var(--partner1-ink);font-size:22px;letter-spacing:4px">1 in 10 subscribing</div>'
           '<div class="hd-counter" style="--cnt-fs:150px;color:var(--partner1-ink)"><span class="hd-counter__pre">₹</span><span class="hd-counter__num">300</span><span class="hd-counter__unit" style="font-size:.42em">&nbsp;Cr</span></div></div>')
    body = f'''<div class="eb-hbcrowd" style="display:grid;grid-template-columns:auto 1fr;gap:48px;align-items:center">
{spec('Dot crowd · 480 dots, 1 in 10 lit in the Partner accent', crowd(40, 12) + legend, 'l')}
{spec('Big counter over the crowd', big)}</div>'''
    return card('E-06', 'Dot crowd', '4',
        'dots fade in row by row; lit dots spring to the Partner 1 accent with a breathing halo; crowd dims under the ₹ counter, then converges to the centre and blends (hue wheel) into the Partner 2 orb.', body)

# ---------- E-08 Pathkind ----------
def e08():
    tests = act3.TESTS.replace('<span class="a3-hl a3-hl--card"', '<span class="a3-hl a3-hl--card" data-x').replace(
        'class="a3-hl" style="', 'class="a3-hl" style="box-shadow:0 0 0 2.5px var(--partner2),0 0 0 8px rgba(var(--partner2-rgb),.35);')
    tp = ''.join(f'<span class="hd-chip{" hd-chip--solid" if k == 1 else ""}">{well(i, t)}{n}</span>' for k, (n, i, t) in enumerate(act3.TP))
    body = f'''<div class="eb-row" style="justify-content:space-between">
  {ph('1 · Tests (team mockup)', tests)}{ph('2 · Sample collector tracking', pk_track())}{ph('3 · Report card', pk_report())}{ph('4 · Agent explains the result', pk_chat())}
</div>
<div class="eb-pk eb-row" style="gap:16px;margin-top:32px;padding-top:28px;border-top:2px dashed var(--grey)">{spec('Touchpoint chips · idle / active (partner accent)', '<div style="display:flex;gap:16px">'+tp+'</div>')}</div>'''
    return card('E-08', 'Pathkind flow', '5',
        'phone grows from the partner orb; first screen rings the CBC card then taps Add; screens swap 500ms slide-left; touchpoint chips link in with partner-accent lines and navy packets.', body)

# ---------- E-09 agents (Pathkind yellow) ----------
def e09():
    idle = ''.join(agent(*a, False) for a in AGENTS); act = ''.join(agent(*a, True) for a in AGENTS)
    body = f'''<div class="eb-pk"><div class="eb-sub">Idle</div><div style="display:flex;gap:24px;justify-content:space-between">{idle}</div>
<div class="eb-sub" style="margin-top:36px">Active · Partner 2 accent</div><div style="display:flex;gap:24px;justify-content:space-between">{act}</div></div>'''
    return card('E-09', 'Agent cards', '6',
        'idle → active in 300ms: partner-accent border + glow, bar fills 600ms; hub orb above takes the partner accent and fires a ripple per activation.', body)

# ---------- E-10 route map ----------
def e10():
    body = spec('Route map · partner accent (routes, hub and van take --partner2; pins stay navy/green)', act3.pk_map(), 'l')
    return card('E-10', 'Route map', '6',
        'routes draw 1s each; pins drop 450ms spring; van follows the second route over 2.9s; ETA label rides with it.', body)

# ---------- E-12 cameras + agent log ----------
def e12():
    tiles = ''.join(act4.cam(k, l, c).replace('class="a4-cam"', 'class="a4-cam is-alert"' if k == act4.ALERT_CAM else 'class="a4-cam"') for k, (l, c) in enumerate(act4.CAMS))
    body = f'<div class="eb-cams">{tiles}{act4.feed_panel()}</div>'
    body = body.replace('id="a4fr2"', 'id="a4fr2" style="box-shadow:0 0 0 2.5px var(--d-amber),0 10px 26px rgba(254,182,79,.25)"').replace('id="a4fr5"', 'id="a4fr5" style="box-shadow:0 0 0 2.5px var(--d-mint),0 10px 26px rgba(59,230,162,.18)"')
    return card('E-12', 'Camera tiles + agent log', '8',
        'dashboard folds into the log panel, 6 feeds fan out from it. Log rows drop in as agents act: scanning → normal → issue (amber, with the camera alert) → planning → escalated (rose ripple) → resolved (mint).', body)

# ---------- E-13 maps: dot globe + roadmap ----------
def dot_globe(R=300, lo0=2, la0=27):
    D = json.load(open('globe_land.json')); r = math.radians
    def proj(la, lo, h=1):
        dl = r(lo - lo0); cl = math.cos(r(la)); p0 = r(la0)
        x = R*h*cl*math.sin(dl); y = -R*h*(math.cos(p0)*math.sin(r(la)) - math.sin(p0)*cl*math.cos(dl))
        z = math.sin(p0)*math.sin(r(la)) + math.cos(p0)*cl*math.cos(dl); return x, y, z
    col = {0: '#c3dcef', 1: '#0873ba', 2: '#139bf5', 3: '#139bf5', 4: '#139bf5'}
    paths = {}
    for i in range(0, len(D), 3):
        x, y, z = proj(D[i]/10, D[i+1]/10)
        if z < .04: continue
        c = col[D[i+2]] if D[i+2] else ('#e1eef8' if z < .32 else '#c3dcef')
        paths[c] = paths.get(c, '') + f'M{x:.1f} {y:.1f}h0'
    dots = ''.join(f'<path d="{d}" stroke="{c}" stroke-width="5.5" stroke-linecap="round" fill="none"/>' for c, d in paths.items())
    vec = lambda la, lo: (math.cos(r(la))*math.cos(r(lo)), math.cos(r(la))*math.sin(r(lo)), math.sin(r(la)))
    IN = (21.5, 78.5); arcs = ''; pins = ''
    for to, lab, main in [((39.0, -77.0), 'US · next', 1), ((50.1, 8.7), 'Europe', 0), ((24.7, 46.7), 'GCC', 0)]:
        a, b = vec(*IN), vec(*to); A = math.acos(sum(p*q for p, q in zip(a, b))); lift = .1 + .22*A/math.pi; pts = []
        for k in range(45):
            u = k/44; f0 = math.sin((1-u)*A)/math.sin(A); f1 = math.sin(u*A)/math.sin(A); w = [a[j]*f0 + b[j]*f1 for j in range(3)]
            x, y, z = proj(math.degrees(math.asin(w[2])), math.degrees(math.atan2(w[1], w[0])), 1 + lift*math.sin(math.pi*u))
            if z < 0 and math.hypot(x, y) < R: continue
            pts.append(f'{x:.1f} {y:.1f}')
        arcs += f'<path d="M{" L".join(pts)}" fill="none" stroke="{"#0873ba" if main else "#139bf5"}" stroke-width="{3.5 if main else 2.8}" stroke-linecap="round"/>'
    for (la, lo), lab, main in [(IN, 'India · live', 0), ((39.0, -77.0), 'US · next', 1), ((50.1, 8.7), 'Europe', 0), ((24.7, 46.7), 'GCC', 0)]:
        x, y, _ = proj(la, lo); w = len(lab)*(11 if main else 10) + 28; h = 36 if main else 32
        pins += (f'<g transform="translate({x:.1f} {y:.1f})"><circle r="8" fill="#0873ba" stroke="#fff" stroke-width="3"/>'
                 f'<g transform="translate(0 {-(h/2+18)})"><rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="{h/2}" fill="{"#0873ba" if main else "#fff"}" stroke="{"#0873ba" if main else "#d6e7f4"}" stroke-width="2"/>'
                 f'<text text-anchor="middle" dy=".35em" font-size="{18 if main else 16}" font-weight="700" fill="{"#fff" if main else "#012b44"}" font-family="Open Sans">{lab}</text></g></g>')
    return (f'<svg viewBox="{-R-60} {-R-60} {2*R+120} {2*R+120}" width="{2*R+120}"><defs><radialGradient id="ebglg" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#fff"/><stop offset=".6" stop-color="#f4faff"/><stop offset="1" stop-color="#ddeffc"/></radialGradient></defs>'
            f'<circle r="{R+28}" fill="none" stroke="#eef7fd" stroke-width="34"/><circle r="{R}" fill="url(#ebglg)" stroke="#8fcdf8" stroke-width="3"/>{dots}{arcs}{pins}</svg>')

def e13():
    from s4 import maha_dotfill, india
    road = act5.OVER[act5.OVER.index('<div class="a5-side a5-side--l"'):act5.OVER.index('<div class="a5-end"')]
    body = f'''<div class="eb-row" style="justify-content:space-between;align-items:flex-end">
  {spec('Maharashtra · dot-fill + Kolhapur pin (approx.)', maha_dotfill(420))}
  {spec('India outline · shrinks onto its spot on the globe', india(300))}
  {spec('Dot globe · real land points, India first then the world', dot_globe(260))}
</div>
<div style="display:flex;gap:60px;justify-content:center;align-items:center;margin-top:36px;padding-top:32px;border-top:2px dashed var(--grey)">{road}</div>'''
    return card('E-13', 'Maps · Maharashtra, India, dot globe + roadmap', '8, 12',
        'India map shrinks onto Maharashtra on the globe; globe turns west (1.5s); arcs fly US → Europe → GCC, each region lights in a ripple from its pin; roadmap cards light as each arc lands. Boundaries approximate, need checking.', body)

# ---------- E-20 company brain ----------
def e20():
    win = act5.WIN.replace('<div class="a5-wpg">', '<div class="a5-wpg" style="transform:translateY(-255px)">').replace('class="a5-cbhl" style="', 'class="a5-cbhl" style="box-shadow:0 0 0 2px rgba(19,155,245,.8),0 0 0 8px rgba(19,155,245,.18);', 4)
    body = (f'<div style="display:flex;justify-content:center"><div style="width:{1320*.78:.0f}px;height:{800*.78:.0f}px;border-radius:18px;overflow:hidden;box-shadow:var(--shadow-layered)">'
            f'<div style="transform:scale(.78);transform-origin:0 0;width:1320px;height:800px">{win}</div></div></div>'
            '<p class="hd-caption" style="font-size:15px;text-align:center;margin-top:18px">Team screenshot of the company brain app in a browser window. Client logo and user name painted out (HeyDoc logo, "Admin"). Shown mid-scroll at the agent grid.</p>')
    return card('E-20', 'Company brain window', '9',
        'the pulse grows into the window (850ms soft), page scrolls hero → agents → chat history, the 9 agent cards ring one after another (70ms), window folds back into the pulse at 82.85s.', body)
