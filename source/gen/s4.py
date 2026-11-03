from base import *
from s3 import counter

# ---------------- E-11 MAHA-PULSE ----------------
def blob(cx,cy,rx,ry,n=14,seed=3,samples=240):
    rnd=random.Random(seed)
    pts=[]
    for k in range(n):
        a=2*math.pi*k/n; f=0.78+rnd.random()*0.3
        pts.append((cx+math.cos(a)*rx*f, cy+math.sin(a)*ry*f))
    dense=[]
    for k in range(n):
        p0,p1,p2,p3=pts[k-1],pts[k],pts[(k+1)%n],pts[(k+2)%n]
        for t in [i/(samples//n) for i in range(samples//n)]:
            t2,t3=t*t,t*t*t
            x=0.5*((2*p1[0])+(-p0[0]+p2[0])*t+(2*p0[0]-5*p1[0]+4*p2[0]-p3[0])*t2+(-p0[0]+3*p1[0]-3*p2[0]+p3[0])*t3)
            y=0.5*((2*p1[1])+(-p0[1]+p2[1])*t+(2*p0[1]-5*p1[1]+4*p2[1]-p3[1])*t2+(-p0[1]+3*p1[1]-3*p2[1]+p3[1])*t3)
            dense.append((x,y))
    d='M'+' L'.join(f'{x:.1f} {y:.1f}' for x,y in dense)+'Z'
    return d,dense

def inside(pt,poly):
    x,y=pt; c=False; j=len(poly)-1
    for i in range(len(poly)):
        xi,yi=poly[i]; xj,yj=poly[j]
        if (yi>y)!=(yj>y) and x<(xj-xi)*(y-yi)/(yj-yi+1e-9)+xi: c=not c
        j=i
    return c

DOT_TYPES=[('Hospitals','#0873ba',7,24),('Patients','#8fcdf8',4,260),('Health camps','#3be6a2',7,14),('Ambulances','#feb64f',7,18)]
def kolhapur_map(w=880,h=600):
    d,poly=blob(w/2,h/2,330,250,seed=11)
    rnd=random.Random(5)
    dots={k:[] for k,_,_,_ in DOT_TYPES}
    for name,col,r,cnt in DOT_TYPES:
        while len(dots[name])<cnt:
            p=(rnd.uniform(60,w-60),rnd.uniform(40,h-40))
            if inside(p,poly): dots[name].append(p)
    out=(f'<svg class="hd-kmap" viewBox="0 0 {w} {h}" width="100%"><defs><pattern id="kgrid" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="12" cy="12" r="1.3" fill="#d6e7f4"/></pattern></defs>'
         f'<rect width="{w}" height="{h}" fill="url(#kgrid)"/>'
         f'<path class="hd-kmap__outline" d="{d}" fill="#eef7fd" stroke="#8fcdf8" stroke-width="3" stroke-dasharray="10 8" stroke-linejoin="round"/>')
    for name,col,r,cnt in DOT_TYPES:
        cls=name.split()[-1].lower()
        for x,y in dots[name]:
            if name=='Hospitals': out+=f'<rect class="hd-kdot hd-kdot--{cls}" x="{x-r}" y="{y-r}" width="{2*r}" height="{2*r}" rx="3" fill="{col}" stroke="#fff" stroke-width="2"/>'
            elif name=='Patients': out+=f'<circle class="hd-kdot hd-kdot--{cls}" cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}"/>'
            elif name=='Health camps': out+=f'<path class="hd-kdot hd-kdot--{cls}" d="M{x:.1f} {y-r-1:.1f}L{x+r+1:.1f} {y+r:.1f}H{x-r-1:.1f}Z" fill="{col}" stroke="#fff" stroke-width="2" stroke-linejoin="round"/>'
            else: out+=f'<circle class="hd-kdot hd-kdot--{cls}" cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}" stroke="#fff" stroke-width="2"/><circle cx="{x:.1f}" cy="{y:.1f}" r="{r+6}" fill="none" stroke="{col}" stroke-width="2" opacity=".35"/>'
    out+=(f'<g transform="translate({w/2-150} {h-50})"><rect width="300" height="34" rx="17" fill="#fff" stroke="#8fcdf8" stroke-width="2" stroke-dasharray="5 5"/>'
          '<text x="150" y="22" text-anchor="middle" font-family="Open Sans" font-size="13" font-weight="700" fill="#0873ba">PLACEHOLDER · Kolhapur district outline</text></g>')
    return out+'</svg>'

def legend_dot(name,col):
    shape={'Hospitals':f'<rect x="2" y="2" width="14" height="14" rx="3" fill="{col}"/>','Patients':f'<circle cx="9" cy="9" r="5" fill="{col}"/>',
           'Health camps':f'<path d="M9 1.5L16.5 15.5H1.5Z" fill="{col}"/>','Ambulances':f'<circle cx="9" cy="9" r="6" fill="{col}"/><circle cx="9" cy="9" r="8.5" fill="none" stroke="{col}" opacity=".4"/>'}[name]
    return f'<span style="display:inline-flex;gap:8px;align-items:center;font-size:15px;font-weight:700"><svg width="18" height="18">{shape}</svg>{name}</span>'

def e11():
    stats=[('Hospitals live','214','hospital','sky','',''),('Patients today','18,420','patient','lav','',''),('Health camps','36','camp','mint','',''),('Ambulances on road','58','ambulance','sun','','')]
    side=''.join(f'<div class="hd-stat" style="display:flex;gap:18px;align-items:center;box-shadow:0 0 0 2px var(--line)">{well(i,t,"60px")}<div><div class="hd-stat__k" style="font-size:12px">{k}</div><div class="hd-stat__v" style="font-size:44px;margin-top:2px">{v}</div></div></div>' for k,v,i,t,_,__ in stats)
    legend=''.join(legend_dot(n,c) for n,c,_,_ in DOT_TYPES)
    dash=f'''<div class="hd-mahapulse" style="background:#fff;border-radius:var(--r-panel);box-shadow:var(--shadow-float);overflow:hidden">
  <div style="display:flex;align-items:center;gap:16px;padding:20px 28px;background:var(--navy);color:#fff">
    <span class="hd-avatar-orb" style="width:40px;height:40px"><span style="width:12px;height:12px;border-radius:50%;background:#fff"></span></span>
    <span style="font-size:22px;font-weight:800;letter-spacing:2px">MAHA-PULSE</span><span style="opacity:.7;font-size:16px;font-weight:600">Kolhapur district · live</span>
    <span class="hd-govbadge" style="margin-left:auto">{logo("maha","Seal of Maharashtra")}Government of Maharashtra</span>
    <span class="hd-tag" style="background:rgba(59,230,162,.15);color:var(--d-mint)"><i></i>LIVE</span>
  </div>
  <div style="display:grid;grid-template-columns:1fr 340px;gap:28px;padding:28px">
    <div><div style="background:var(--grey);border-radius:var(--r-plate);padding:12px">{kolhapur_map()}</div>
      <div style="display:flex;gap:28px;margin-top:16px;color:var(--navy)">{legend}</div></div>
    <div style="display:flex;flex-direction:column;gap:16px">{side}
      <div class="hd-mini" style="background:var(--sun);font-size:15px;display:flex;gap:10px;align-items:center;color:var(--sun-ink);font-weight:700">{ic("alert","22px")}Camp #12 needs 2 more staff</div></div>
  </div></div>'''
    return card('E-11','MAHA-PULSE dashboard','7',
        'panel rises 600ms ease-out; outline draws 1.2s (dashoffset); dots appear by type (hospitals → camps → ambulances → patients), 20ms stagger, 300ms ease-spring; side counters count up 1.2s ease-out; LIVE dot pulses 1.2s loop; ambulances drift slowly along short paths.', dash)

# ---------------- E-12 camera grid ----------------
def cam_scene(alert=False):
    c='rgba(254,182,79,.16)' if alert else 'rgba(143,205,248,.10)'
    lines=''.join(f'<path d="M{x} 360 L{320+(x-320)*0.25} 150" stroke="{c}" stroke-width="1.5"/>' for x in range(-160,820,80))
    lines+=''.join(f'<path d="M0 {y} H640" stroke="{c}" stroke-width="1.5"/>' for y in [170,195,228,275,345])
    lines+=f'<path d="M0 150 H640" stroke="{c}" stroke-width="2"/><rect x="250" y="70" width="140" height="80" rx="6" fill="none" stroke="{c}" stroke-width="2"/>'
    corners=''.join(f'<path d="{p}" stroke="rgba(255,255,255,.45)" stroke-width="3" fill="none" stroke-linecap="round"/>' for p in ['M12 28V12H28','M628 28V12H612','M12 332V348H28','M628 332V348H612'])
    return f'<svg class="hd-cam__scene" viewBox="0 0 640 360" preserveAspectRatio="xMidYMid slice">{lines}{corners}</svg>'

def cam(lbl, ts, chips, alert=False):
    ch=''.join(chips)
    return (f'<div class="hd-cam{" is-alert" if alert else ""}">{cam_scene(alert)}<span class="hd-cam__icon">{ic("camera","64px","1.6")}</span>'
            f'<div class="hd-cam__lbl"><i></i>{lbl}</div><div class="hd-cam__ts">{ts}</div><div class="hd-cam__chips">{ch}</div></div>')

def ochip(icon, txt, kind=''):
    return f'<span class="hd-ochip {kind}"><span class="ic">{ic(icon,"16px")}</span><span>{txt}</span></span>'

def e12():
    tiles=[cam('CAM 01 · OPD queue','09:41:12',[ochip('queue','Queue <b>14</b>')]),
           cam('CAM 02 · Ward B','09:41:12',[ochip('bed','Beds <b>82%</b>')]),
           cam('CAM 03 · Emergency','09:41:12',[ochip('ambulance','Bay <b>2 of 4</b> free','hd-ochip--ok')]),
           cam('CAM 04 · Pharmacy','09:41:12',[ochip('queue','Queue <b>6</b>'),ochip('clock','Wait <b>9 min</b>','hd-ochip--ok')]),
           cam('CAM 05 · Lab collection','09:41:12',[ochip('alert','Waiting <b>42 min</b>, staff alerted','hd-ochip--amber')],True),
           cam('CAM 06 · ICU corridor','09:41:12',[ochip('bed','ICU beds <b>91%</b>')])]
    grid='<div class="hd-camgrid" style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">'+''.join(tiles)+'</div>'
    chips=('<div style="display:flex;gap:12px;flex-wrap:wrap">'+ochip('queue','Queue <b>14</b>')+ochip('bed','Beds <b>82%</b>')+ochip('clock','Wait <b>9 min</b>','hd-ochip--ok')
           +ochip('alert','Waiting <b>42 min</b>, staff alerted','hd-ochip--amber')+'</div>')
    body=f'''<div class="eb-dark" style="padding:28px">{grid}</div>
<div style="display:flex;gap:48px;margin-top:28px;align-items:center">{spec('Overlay chips · default / ok / amber alert', '<div class="eb-dark" style="padding:18px">'+chips+'</div>','l')}
<p class="hd-caption" style="font-size:15px;max-width:640px">Tiles are abstract (perspective grid + camera glyph), no footage or people. Drop real CCTV stills into .hd-cam behind .hd-cam__scene if needed.</p></div>'''
    return card('E-12','Camera tile grid','8',
        'tiles fade in across the grid 60ms stagger, 300ms; chips slide up 12px + fade 300ms ease-out; alert tile: amber ring pulses (glow .45 → .9) 1.2s loop, chip pops 300ms ease-spring; REC dot blinks 1s.', body)

# ---------------- E-13 maps ----------------
def maha_dotfill(w=520):
    return (f'<svg class="hd-map-mh" viewBox="-2 -2 118.4 98" width="{w}"><defs>'
            '<pattern id="mhdots" width="2.6" height="2.6" patternUnits="userSpaceOnUse"><circle cx="1.3" cy="1.3" r=".78" fill="#139bf5"/></pattern>'
            f'<clipPath id="mhclip"><path d="{MAHA_D}"/></clipPath></defs>'
            f'<path d="{MAHA_D}" fill="#eef7fd"/><rect x="0" y="0" width="115" height="94" fill="url(#mhdots)" clip-path="url(#mhclip)"/>'
            f'<path d="{MAHA_D}" fill="none" stroke="#0873ba" stroke-width=".7" stroke-linejoin="round"/>'
            '<g transform="translate(22 81)"><circle r="5" fill="#3fd4f6" opacity=".25"/><circle r="2.6" fill="#0873ba" stroke="#fff" stroke-width=".8"/></g>'
            '<g transform="translate(28 79)"><rect width="22" height="6" rx="3" fill="#012b44"/><text x="11" y="4.3" text-anchor="middle" font-size="3.4" font-weight="700" fill="#fff" font-family="Open Sans">Kolhapur</text></g></svg>')

def maha_solid(w=300):
    return (f'<svg viewBox="-2 -2 118.4 98" width="{w}"><path d="{MAHA_D}" fill="#0873ba"/></svg>')

def india(w=420):
    return (f'<svg class="hd-map-in" viewBox="-2 -2 71 78" width="{w}"><path d="{INDIA_D}" fill="#eef7fd" stroke="#0873ba" stroke-width=".55" stroke-linejoin="round"/>'
            '<g transform="translate(21 47)"><circle r="6" fill="#3fd4f6" opacity=".22"/><circle r="3.4" fill="#3fd4f6" opacity=".35"/><circle r="1.7" fill="#0873ba" stroke="#fff" stroke-width=".5"/></g></svg>')

def globe(w=380):
    lon=''.join(f'<ellipse cx="0" cy="0" rx="{r}" ry="150" fill="none" stroke="#8fcdf8" stroke-width="1.5" opacity=".7"/>' for r in [40,80,120])
    lat=''.join(f'<ellipse cx="0" cy="{y}" rx="{math.sqrt(150**2-y**2):.1f}" ry="{math.sqrt(150**2-y**2)*0.18:.1f}" fill="none" stroke="#8fcdf8" stroke-width="1.5" opacity=".7"/>' for y in [-100,-50,0,50,100])
    return (f'<svg class="hd-globe" viewBox="-180 -180 360 360" width="{w}"><defs><radialGradient id="glg" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#ffffff"/><stop offset=".6" stop-color="#eef7fd"/><stop offset="1" stop-color="#cfe9fb"/></radialGradient></defs>'
            '<circle r="172" fill="none" stroke="#eef7fd" stroke-width="16"/><circle r="150" fill="url(#glg)" stroke="#8fcdf8" stroke-width="2"/>'
            f'<line x1="0" y1="-150" x2="0" y2="150" stroke="#8fcdf8" stroke-width="1.5" opacity=".7"/>{lon}{lat}'
            '<g transform="translate(62 -10)"><circle r="16" fill="#3fd4f6" opacity=".25"/><circle r="7" fill="#0873ba" stroke="#fff" stroke-width="2.5"/></g>'
            '<g transform="translate(-110 -26)"><circle r="6" fill="#139bf5" stroke="#fff" stroke-width="2"/></g><path d="M62 -10 Q-20 -90 -110 -26" stroke="#139bf5" stroke-width="2.5" fill="none" stroke-dasharray="2 7" stroke-linecap="round"/>'
            '<g transform="translate(-120 120)"><rect width="240" height="30" rx="15" fill="#fff" stroke="#8fcdf8" stroke-width="2" stroke-dasharray="5 5"/><text x="120" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0873ba" font-family="Open Sans">PLACEHOLDER · globe with landmasses</text></g></svg>')

def e13():
    body=f'''<div class="eb-row" style="justify-content:space-between;align-items:flex-end">
  {spec('Maharashtra · dot-fill state + Kolhapur pin (approx.)', maha_dotfill(460))}
  {spec('Maharashtra · solid', maha_solid(260))}
  {spec('India outline · Maharashtra glow', india(330))}
  {spec('Globe · placeholder (graticule + US/India arc)', globe(340))}
</div>'''
    return card('E-13','Maps','8, 12',
        'Maharashtra dot-fill reveals radially from the Kolhapur pin over 1.2s ease-out (mask circle grows); zoom-out Maharashtra → India → globe as one 2.4s ease-in-out camera move with cross-fades; globe arc draws 1.2s.', body)

# ---------------- E-14 segments ----------------
def e14():
    segs=[('Hospitals','hospital','lav','Beds, queues, follow-ups'),('Labs','lab','aqua','Bookings, pickups, reports'),
          ('Wellness','wellness','mint','Habits, coaching, streaks'),('Insurance','insurance','sun','Claims, renewals, care')]
    tiles=''.join(f'<div class="hd-seg hd-seg--{t}">{well(i,"white")}<div class="hd-seg__t">{n}</div><div class="hd-seg__s">{s}</div></div>' for n,i,t,s in segs)
    body=f'''<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px">{tiles}</div>
<div style="margin-top:32px;text-align:center">{spec('Caption style · headline 56', '<div class="hd-headline">4 care segments. <em>One company brain.</em></div>')}</div>'''
    return card('E-14','Segment tiles','9',
        'tiles rise 24px + fade, 600ms ease-out, 100ms stagger; icon wells pop 300ms ease-spring; caption appears 600ms later, second sentence in --blue lands last.', body, span=7)

# ---------------- E-15 logo ring ----------------
def e15(size=600):
    names=['Government of Maharashtra','NHA','ClearMedi','1mg','Redcliffe','Dr. B. Lal','Others']
    R=size*0.40; c=size/2
    slots=''
    for k,n in enumerate(names):
        a=-math.pi/2+2*math.pi*k/len(names)
        x=c+R*math.cos(a); y=c+R*math.sin(a)
        key={'Pathkind':'pathkind','Habuild':'habuild','Government of Maharashtra':'maha','NHA':'nha','ClearMedi':'clearmedi','1mg':'onemg','Redcliffe':'redcliffe','Dr. B. Lal':'drlal'}.get(n)
        tile=(f'<div class="hd-logotile{" hd-logotile--navy" if key=="clearmedi" else ""}">{logo(key,n)}</div>' if key else '<div class="hd-logotile"><span class="a5-more">&amp; more</span></div>')
        slots+=f'<div class="hd-logoring__slot" style="left:{x/size*100:.2f}%;top:{y/size*100:.2f}%">{tile}</div>'
    svg=(f'<svg class="hd-logoring__svg" viewBox="0 0 {size} {size}"><circle cx="{c}" cy="{c}" r="{R}" fill="none" stroke="#8fcdf8" stroke-width="2" stroke-dasharray="2 9" stroke-linecap="round"/>'
         f'<circle cx="{c}" cy="{c}" r="{R*0.68:.0f}" fill="none" stroke="#eef7fd" stroke-width="2"/></svg>')
    ring=f'<div class="hd-logoring" style="--ring-size:{size}px">{svg}<div class="hd-logoring__core">{logo("heydoc","HeyDoc AI")}</div>{slots}</div>'
    return card('E-15','Logo ring','11',
        'slots orbit in: rotate −30° → 0 around the core with fade, 1.2s ease-out, 60ms stagger; then the ring drifts 360° over 60s linear (slots counter-rotate to stay upright).', '<div style="display:flex;justify-content:center">'+ring+'</div>', span=5)

# ---------------- E-16 atoms ----------------
def e16():
    bubbles=(f'<div style="display:flex;flex-direction:column;gap:14px;width:520px">'
             f'<div class="hd-msg"><span class="hd-avatar-orb">{ic("agent","20px")}</span><div class="hd-bubble hd-bubble--agent">Your sample is collected. Report by 6 pm today.<span class="hd-bubble__meta">Agent · 9:41</span></div></div>'
             '<div class="hd-bubble hd-bubble--user">Can I get it on WhatsApp?<span class="hd-bubble__meta">9:42 ✓✓</span></div>'
             f'<div class="hd-msg"><span class="hd-avatar-orb">{ic("agent","20px")}</span><div class="hd-typing"><i></i><i></i><i></i></div></div></div>')
    chips=(f'<div style="display:flex;flex-wrap:wrap;gap:14px"><span class="hd-chip">{well("lab","aqua")}Lab reports</span><span class="hd-chip hd-chip--solid">{well("agent","white")}Agent on</span>'
           f'<span class="hd-chip hd-chip--ghost">{well("clock","ghost")}Manual today</span><span class="hd-chip hd-chip--text">Text chip</span></div>')
    btns='<div style="display:flex;flex-wrap:wrap;gap:14px;align-items:center"><span class="hd-btn hd-btn--primary">Book a test</span><span class="hd-btn hd-btn--navy">Talk to us</span><span class="hd-btn hd-btn--secondary">View report</span><span class="hd-btn hd-btn--ghost">Skip</span><span class="hd-btn hd-btn--primary hd-btn--sm">Small</span></div>'
    badges=('<div style="display:flex;flex-wrap:wrap;gap:12px;align-items:center">'+''.join(f'<span class="hd-tag hd-tag--{t}">{n}</span>' for t,n in [('sky','New'),('mint','Normal'),('sun','Pending'),('rose','High'),('lav','Agent'),('aqua','Lab'),('navy','Live'),('grad','Active'),('white','Fake data')])
            +'<span class="hd-tag hd-tag--mint"><i></i>Online</span><span class="hd-badge">3</span></div>')
    toggles='<div style="display:flex;gap:24px;align-items:center;font-size:16px;font-weight:600"><span class="hd-toggle"></span>Off<span class="hd-toggle is-on"></span>On</div>'
    prog=''.join(f'<div style="display:grid;grid-template-columns:150px 1fr 50px;gap:14px;align-items:center;font-size:15px;font-weight:600"><span>{n}</span><div class="hd-progress {c}"><div class="hd-progress__fill" style="--p:{p}%"></div></div><b>{p}%</b></div>'
                 for n,c,p in [('Reports on time','',92),('Beds occupied','hd-progress--amber',82),('Follow-ups done','hd-progress--mint',64),('SLA breached','hd-progress--rose',12)])
    cards=(f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px">'
           f'<div class="hd-panel"><div class="hd-stat__k">Panel</div><div style="font-size:22px;font-weight:700;margin-top:8px">White, radius 28, one soft shadow</div></div>'
           f'<div class="hd-stat"><div class="hd-stat__k">Stat card</div><div class="hd-stat__v">18,420</div><div class="hd-stat__s">patients today</div></div>'
           f'<div class="hd-mini" style="background:var(--mint);display:flex;gap:16px;align-items:center">{well("trend","white","56px")}<div><b style="color:var(--mint-ink)">Pastel card</b><div style="font-size:15px;color:var(--muted)">Ink on its own pastel</div></div></div></div>')
    body=f'''<div style="display:grid;grid-template-columns:auto 1fr;gap:56px">
  {spec('Chat bubbles · agent / user / typing', bubbles, 'l')}
  <div style="display:flex;flex-direction:column;gap:30px">
    {spec('Chips', chips, 'l')}{spec('Buttons', btns, 'l')}{spec('Badges and tags', badges, 'l')}
    <div style="display:grid;grid-template-columns:auto 1fr;gap:48px">{spec('Toggles', toggles, 'l')}{spec('Progress bars', '<div style="display:flex;flex-direction:column;gap:12px;width:100%">'+prog+'</div>', 'l')}</div>
  </div>
</div>
<div style="margin-top:36px">{spec('Cards', cards, 'l')}</div>'''
    return card('E-16','UI atoms','all',
        'bubbles: scale .9 → 1 + fade from the tail corner, 300ms ease-spring; typing dots bounce 4px, 600ms loop, 150ms offset; toggles slide 150ms ease-out; progress fills 600ms ease-out; buttons press scale .96, 150ms.', body)

# ---------------- E-17 icons ----------------
def e17():
    tones=['lav','peach','mint','sky','sun','rose','aqua','sky','aqua','mint','sun','peach','rose','mint','lav']
    core=''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:10px">{well(n,t,"72px")}<span class="eb-label" style="text-transform:none;letter-spacing:0;font-size:14px;color:var(--muted)">{n}</span></div>' for n,t in zip(CORE15,tones))
    raw=''.join(f'<span style="color:var(--navy)">{ic(n,"40px")}</span>' for n in CORE15)
    dark=''.join(f'<span style="color:var(--cyan)">{ic(n,"40px")}</span>' for n in CORE15)
    ext=''.join(f'<span title="{n}" style="color:var(--blue)">{ic(n,"32px")}</span>' for n in ICONS if n not in CORE15)
    sizes=''.join(f'<span style="color:var(--blue)">{ic("agent",f"{s}px")}</span>' for s in [16,24,32,48,64])
    body=f'''<div style="display:grid;grid-template-columns:repeat(15,1fr);gap:12px">{core}</div>
<div style="margin-top:32px">
  {spec('Raw stroke · navy on white', '<div style="display:flex;justify-content:space-between;width:100%">'+raw+'</div>','l')}
</div>
<div style="display:grid;grid-template-columns:2fr 1fr;gap:28px;margin-top:28px">
  {spec('Extended set · same grid (24) and stroke (2.2, round caps/joins)', '<div style="display:flex;gap:22px;flex-wrap:wrap">'+ext+'</div>','l')}
  {spec('Sizes 16 · 24 · 32 · 48 · 64', '<div style="display:flex;gap:22px;align-items:flex-end">'+sizes+'</div>','l')}
</div>'''
    return card('E-17','Icon set','all',
        'icons draw on via stroke-dashoffset (pathLength=1), 600ms ease-in-out; or pop in a well, scale 0 → 1, 300ms ease-spring. Colour via currentColor.', body)

# ---------------- E-18 text ----------------
def e18():
    def block(dark):
        cls='on-dark' if dark else ''
        bg='background:var(--bg-dark-grad);' if dark else 'background:var(--bg-wash);box-shadow:inset 0 0 0 1px var(--line);'
        return f'''<div class="{cls}" style="{bg}border-radius:var(--r-card);padding:48px;display:flex;flex-direction:column;gap:36px">
  <div><div class="eb-label" style="text-align:left;margin-bottom:10px">Kicker + headline</div><div class="hd-kicker">Scene 09</div><div class="hd-headline" style="margin-top:12px">4 care segments. <em>One company brain.</em></div></div>
  <div><div class="eb-label" style="text-align:left;margin-bottom:10px">Headline XL (end card)</div><div class="hd-headline hd-headline--xl">The Agentic <em>Care OS</em></div></div>
  <div><div class="eb-label" style="text-align:left;margin-bottom:10px">Subline</div><div class="hd-subline">[Script line] Agents that run the everyday work of care teams.</div></div>
  <div><div class="eb-label" style="text-align:left;margin-bottom:10px">Bold stat + text</div><div class="hd-statline"><span class="hd-statline__num">1,500+ → 5,000</span><span class="hd-statline__txt">[Script line] reports a day</span></div></div>
  <div><div class="eb-label" style="text-align:left;margin-bottom:10px">Lower caption</div><span class="hd-lower">{well("alert","sun")}Waiting 42 min, staff alerted</span></div>
  <div><div class="eb-label" style="text-align:left;margin-bottom:10px">Caption</div><div class="hd-caption">Fake data for illustration · <em>heydoc.co.in</em></div></div>
</div>'''
    body=f'''<div>{block(False)}</div>
<p class="hd-caption" style="font-size:15px;margin-top:20px">Exact lines used where the brief gave them. Lines marked [Script line] are stand-ins: no full script was supplied.</p>'''
    return card('E-18','On-screen text styles','all',
        'headline: word-by-word rise 24px + fade, 60ms stagger, 600ms ease-out; the &lt;em&gt; phrase colours from navy to --blue 300ms after landing. Subline follows 200ms later as one line. Lower caption slides in from left 40px, 400ms ease-out.', body)

# ---------------- E-19 end card ----------------
def endcard(dark=False):
    bg=('<svg class="hd-end__bg" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice"><g fill="none" stroke="'+('#139bf5' if dark else '#8fcdf8')+'" stroke-width="3" opacity="'+('.25' if dark else '.6')+'">'
        '<circle cx="960" cy="420" r="260" stroke-dasharray="2 12" stroke-linecap="round"/><circle cx="960" cy="420" r="380" opacity=".5"/><circle cx="960" cy="420" r="520" opacity=".25"/></g></svg>')
    lock=logo('heydoc_white' if dark else 'heydoc','HeyDoc AI','hd-end__lockup','position:relative')
    return (f'<div class="hd-end hd-end--{"dark" if dark else "light"}">{bg}{lock}'
            f'<div class="hd-end__tag" style="position:relative">The Agentic <em>Care OS</em></div>'
            f'<div class="hd-end__url" style="position:relative">{ic("globe","1em")}heydoc.co.in</div></div>')

def e19():
    body=f'''<div style="display:flex;justify-content:center">
  {spec('True 1920×1080, shown at 44%', scaled(endcard(False)))}
</div>'''
    return card('E-19','End card','12',
        'rings fade in 600ms; lockup fades + scales .96 → 1, 1.2s ease-out; tagline rises 24px 300ms after; URL fades in last (300ms). Hold 2.4s. Optional: E-02 pulse fires once behind the lockup.', body)
