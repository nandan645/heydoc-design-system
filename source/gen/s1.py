from base import *

# ---------------- E-01 ----------------
def e01():
    core = [('Primary','--blue','#0873ba'),('Primary deep','--navy','#012b44'),('Secondary','--sky','#139bf5'),('Pale step','--pale','#8fcdf8'),
            ('Accent','--cyan','#3fd4f6'),('Success','--mint-ink','#1f8a43'),('Success data','--d-mint','#3be6a2'),('Alert amber','--d-amber','#feb64f'),('Alert red','--d-rose','#ea5c72')]
    neut = [('Tint','--tint','#eef7fd'),('Line','--line','#d6e7f4'),('Grey','--grey','#f4f6f8'),('Muted text','--muted','#5b6b78'),('Faint text','--c-text-3','#9aabb8'),
            ('White','--white','#ffffff'),('Amber ink','--sun-ink','#a87508'),('Red ink','--rose-ink','#c8394f')]
    sw = lambda a: ''.join(f'<div class="f-sw"><div class="f-sw__c" style="background:var({v})"></div><div class="f-sw__t"><b>{n}</b><code>{v} · {h}</code></div></div>' for n,v,h in a)
    past = ''.join(f'<div class="f-pastel" style="background:var(--{p});color:var(--{p}-ink)">{ic(i,"24px")}{p} / {p}-ink</div>'
                   for p,i in [('aqua','lab'),('sun','alert'),('peach','megaphone'),('mint','wellness'),('rose','report'),('lav','hospital')])
    bgs = ''.join(f'<div class="f-bg" style="background:{b};color:{c}">{n}</div>' for n,b,c in [
        ('Light · --bg-light','var(--bg-light)','var(--muted)'),('Light 2 · --tint','var(--tint)','var(--muted)'),('Title wash · --bg-wash','var(--bg-wash)','var(--muted)')])
    grads = ''.join(f'<div class="f-bg" style="background:{b};color:#fff">{n}</div>' for n,b in [('--grad · agent highlight','var(--grad)'),('--grad-teal · feature','var(--grad-teal)'),('--orb · pulse core','var(--orb)')])
    type_rows = [
      ('Headline · 56/700','<div class="hd-headline">One brain for <em>every care team</em></div>'),
      ('Headline XL · 88/700','<div class="hd-headline hd-headline--xl">The Agentic <em>Care OS</em></div>'),
      ('Subline · 30/400','<div class="hd-subline">Agents that run the everyday work of hospitals, labs and wellness apps.</div>'),
      ('Bold number + text · 84/800 + 28/400','<div class="hd-statline"><span class="hd-statline__num">85K+</span><span class="hd-statline__txt">patient conversations handled every week</span></div>'),
      ('Kicker · 19/700 caps','<div class="hd-kicker">Scene 06 · The agent team</div>'),
      ('Caption · 22/600','<div class="hd-caption">Fake data for illustration</div>'),
    ]
    typ = ''.join(f'<div class="f-type__row"><span class="f-type__meta">{m}</span>{h}</div>' for m,h in type_rows)
    space = ''.join(f'<div><div style="width:{v}px;height:{v}px"></div><span>{v}</span></div>' for v in [4,8,12,16,24,32,48,64,96,120])
    rad = ''.join(f'<div style="border-radius:{v}"></div>' for v in ['8px','12px','16px','22px','24px','28px','999px'])
    radl = ''.join(f'<span style="width:92px;text-align:center;font-size:12px;font-weight:700;color:var(--muted)">{n}</span>' for n in ['xs 8','sm 12','inner 16','plate 22','card 24','panel 28','pill'])
    sh = ''.join(f'<div style="box-shadow:var({v})">{v}</div>' for v in ['--shadow','--shadow-layered','--shadow-float','--shadow-glow'])
    eases = [('ease-out','.22,1,.36,1','enter, count-up'),('ease-in','.55,0,1,.45','exit'),('ease-in-out','.65,0,.35,1','move, swap'),('ease-spring','.34,1.56,.64,1','pop, pins, badges'),('linear','0,0,1,1','orbit, loops')]
    def curve(p):
        a,b,c,d = map(float,p.split(','))
        X=lambda v:10+v*140; Y=lambda v:90-v*70
        return (f'<svg viewBox="0 0 160 100" style="width:100%;height:90px"><rect x="10" y="20" width="140" height="70" fill="none" stroke="#d6e7f4" stroke-dasharray="3 4"/>'
                f'<path d="M{X(0)} {Y(0)}C{X(a)} {Y(b)} {X(c)} {Y(d)} {X(1)} {Y(1)}" fill="none" stroke="#0873ba" stroke-width="3" stroke-linecap="round"/>'
                f'<circle cx="{X(0)}" cy="{Y(0)}" r="4" fill="#0873ba"/><circle cx="{X(1)}" cy="{Y(1)}" r="4" fill="#3fd4f6"/></svg>')
    ease = ''.join(f'<div class="f-ease">{curve(p)}<b>--{n}</b><code>cubic-bezier({p})<br>{u}</code></div>' for n,p,u in eases)
    durs = ''.join(f'<div class="f-dur"><span>--dur-{k}</span><i style="width:{w}%"></i><span style="color:var(--muted)">{v}</span></div>' for k,v,w in [('xs','150ms',6),('s','300ms',12.5),('m','600ms',25),('l','1200ms',50),('xl','2400ms',100)])
    body = f'''
<div class="eb-block"><div class="eb-sub">Colour · core and status</div><div class="f-swatches">{sw(core)}</div></div>
<div class="eb-block"><div class="eb-sub">Colour · neutrals and inks</div><div class="f-swatches">{sw(neut)}</div><div class="f-pastels">{past}</div></div>
<div class="eb-block" style="display:grid;grid-template-columns:5fr 3fr;gap:32px">
  <div><div class="eb-sub">Backgrounds</div><div class="f-bgs">{bgs}</div></div>
  <div><div class="eb-sub">Gradients</div><div class="f-bgs" style="grid-template-columns:repeat(3,1fr)">{grads}</div></div>
</div>
<div class="eb-block" style="display:grid;grid-template-columns:7fr 5fr;gap:48px">
  <div><div class="eb-sub">Type scale · Open Sans</div><div class="f-type">{typ}</div></div>
  <div>
    <div class="eb-sub">Spacing · 8pt</div><div class="f-space">{space}</div>
    <div class="eb-sub" style="margin-top:36px">Radius</div><div class="f-radius">{rad}</div><div style="display:flex;gap:18px;margin-top:8px">{radl}</div>
    <div class="eb-sub" style="margin-top:36px">Shadow</div><div class="f-shadow">{sh}</div>
    <div class="eb-sub" style="margin-top:36px">Stroke</div>
    <div style="display:flex;gap:28px;align-items:center;font-size:12px;font-weight:700;color:var(--muted)">
      <span style="display:flex;gap:8px;align-items:center;color:var(--blue)">{ic("agent","32px")}<span style="color:var(--muted)">icon 2.2</span></span>
      <svg width="90" height="10"><path d="M3 5h84" stroke="#139bf5" stroke-width="3" stroke-linecap="round"/></svg>line 3
      <svg width="90" height="10"><path d="M3 5h84" stroke="#139bf5" stroke-width="6" stroke-linecap="round"/></svg>route 6
      <span style="width:60px;height:30px;border:2px solid var(--line);border-radius:999px"></span>border 2
    </div>
  </div>
</div>
<div class="eb-block" style="display:grid;grid-template-columns:7fr 5fr;gap:48px">
  <div><div class="eb-sub">Motion · easing</div><div class="f-motion">{ease}</div></div>
  <div><div class="eb-sub">Motion · durations</div><div style="display:flex;flex-direction:column;gap:14px">{durs}
    <div class="f-dur"><span>--stagger</span><i style="width:2.5%"></i><span style="color:var(--muted)">60ms</span></div></div>
    <p class="hd-caption" style="font-size:14px;margin-top:18px">Default enter: rise 24px + fade, --dur-m, --ease-out. Default exit: fade, --dur-s, --ease-in.</p></div>
</div>'''
    return card('E-01','Brand foundations','all',
        'Tokens only, nothing moves. Default enter: rise 24px + fade, 600ms ease-out. Default exit: fade, 300ms ease-in. Stagger siblings by 60ms.', body)

# ---------------- E-02 ----------------
def pulse(state, size=240):
    rings = {'idle':[(1.35,.18)], 'firing':[(1.55,.55),(2.0,.3),(2.4,.12)], 'linked':[(1.35,.25)]}[state]
    r = ''.join(f'<span class="hd-pulse__ring" style="--sc:{s};--op:{o}"></span>' for s,o in rings)
    return f'<div class="hd-pulse is-{state}" style="--pulse-size:{size}px"><span class="hd-pulse__glow"></span>{r}<span class="hd-pulse__core"></span></div>'

def netlink(w=560,h=300):
    cx,cy=w/2,h/2
    nodes=[(70,60),(80,240),(490,70),(500,235),(280,22)]
    lines=''.join(f'<path class="hd-net__link" d="M{cx} {cy}L{x} {y}" stroke="url(#nlg)" stroke-width="3" stroke-linecap="round"/>' for x,y in nodes[:4])
    lines+=f'<path class="hd-net__link hd-net__link--dashed" d="M{cx} {cy}L{nodes[4][0]} {nodes[4][1]}" stroke="#8fcdf8" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>'
    lines+='<path d="M70 60L80 240M490 70L500 235" stroke="#d6e7f4" stroke-width="2" stroke-dasharray="2 8" stroke-linecap="round"/>'
    nd=''.join(f'<g class="hd-net__node is-on" transform="translate({x} {y})"><circle r="22" fill="#eef7fd"/><circle r="13" fill="#fff" stroke="#139bf5" stroke-width="3"/><circle r="5" fill="#0873ba"/></g>' for x,y in nodes[:4])
    nd+=f'<g class="hd-net__node" transform="translate({nodes[4][0]} {nodes[4][1]})"><circle r="13" fill="#fff" stroke="#d6e7f4" stroke-width="3"/></g>'
    pk=f'<circle class="hd-net__packet" cx="{(cx+490)/2}" cy="{(cy+70)/2}" r="6" fill="#3fd4f6" stroke="#fff" stroke-width="2"/>'
    core=(f'<g class="hd-net__core" transform="translate({cx} {cy})"><circle r="70" fill="none" stroke="#139bf5" stroke-width="3" opacity=".25"/>'
          f'<circle r="54" fill="#eef7fd"/><circle r="42" fill="url(#nlo)"/><circle r="11" fill="#fff"/></g>')
    return (f'<svg class="hd-net" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><defs>'
            f'<linearGradient id="nlg" gradientUnits="userSpaceOnUse" x1="0" x2="{w}"><stop offset="0" stop-color="#1789f2"/><stop offset="1" stop-color="#3fd4f6"/></linearGradient>'
            f'<radialGradient id="nlo" cx=".28" cy=".18" r=".9"><stop offset="0" stop-color="#0a84e8"/><stop offset=".55" stop-color="#2ba7f5"/><stop offset="1" stop-color="#43d0f2"/></radialGradient></defs>'
            f'{lines}{pk}{nd}{core}</svg>')

def e02():
    ripple=('<svg viewBox="0 0 200 200" width="180" height="180" class="hd-ripple">'
            '<circle cx="100" cy="100" r="40" fill="none" stroke="#139bf5" stroke-width="3" opacity=".6"/>'
            '<circle cx="100" cy="100" r="66" fill="none" stroke="#139bf5" stroke-width="3" opacity=".3"/>'
            '<circle cx="100" cy="100" r="92" fill="none" stroke="#139bf5" stroke-width="3" opacity=".12"/></svg>')
    glow='<div class="hd-glow" style="width:180px;height:180px;border-radius:50%;background:radial-gradient(circle,rgba(63,212,246,.6) 0%,rgba(19,155,245,.2) 45%,rgba(19,155,245,0) 70%)"></div>'
    node_on='<svg viewBox="0 0 60 60" width="72" height="72" class="hd-node is-on"><circle cx="30" cy="30" r="26" fill="#eef7fd"/><circle cx="30" cy="30" r="15" fill="#fff" stroke="#139bf5" stroke-width="3"/><circle cx="30" cy="30" r="6" fill="#0873ba"/></svg>'
    node_off='<svg viewBox="0 0 60 60" width="72" height="72" class="hd-node"><circle cx="30" cy="30" r="15" fill="#fff" stroke="#d6e7f4" stroke-width="3"/></svg>'
    links=('<svg viewBox="0 0 300 120" width="300" height="120" class="hd-links"><defs><linearGradient id="lkg" gradientUnits="userSpaceOnUse" x1="10" x2="290"><stop offset="0" stop-color="#1789f2"/><stop offset="1" stop-color="#3fd4f6"/></linearGradient></defs>'
           '<path d="M10 20H290" stroke="url(#lkg)" stroke-width="3" stroke-linecap="round"/>'
           '<path d="M10 60H290" stroke="#8fcdf8" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>'
           '<path d="M10 100H290" stroke="#d6e7f4" stroke-width="3" stroke-linecap="round"/><path d="M10 100H170" stroke="url(#lkg)" stroke-width="3" stroke-linecap="round"/><circle cx="170" cy="100" r="6" fill="#3fd4f6" stroke="#fff" stroke-width="2"/></svg>')
    body=f'''
<div class="eb-row" style="justify-content:space-between;align-items:center">
  {spec('Core · idle', pulse('idle'))}
  {spec('Core · firing (frame at peak)', pulse('firing'))}
  {spec('Linked · core joined to network', netlink())}
</div>
<div class="eb-row" style="justify-content:space-around;align-items:center;margin-top:40px;padding-top:32px;border-top:2px dashed var(--grey)">
  {spec('Ripple rings · .hd-ripple', ripple)}
  {spec('Glow · .hd-glow', glow)}
  {spec('Node · active / dormant', '<div style="display:flex;gap:16px">'+node_on+node_off+'</div>')}
  {spec('Links · live / planned / drawing + packet', links)}
</div>'''
    return card('E-02','The Pulse','1, 2, 6, 7, 11, 12 (recurring motif)',
        'pulse: 1.2s ease-out, ring scale 1 → 2.4, opacity .6 → 0, 3 rings staggered 400ms, loop. Glow fades in 300ms on fire. Links draw 600ms ease-in-out (stroke-dashoffset); packet travels the link in 1.2s.', body)
