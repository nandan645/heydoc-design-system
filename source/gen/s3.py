from base import *

# ---------------- E-06 ----------------
def crowd(cols=25, rows=10, gap=26, r=8, dark=False):
    rnd=random.Random(7)
    n=cols*rows; idx=list(range(n)); rnd.shuffle(idx)
    hits=set(idx[k*10+rnd.randrange(10)] for k in range(n//10))
    w,h=cols*gap,rows*gap
    out=''
    for k in range(n):
        x=gap/2+(k%cols)*gap; y=gap/2+(k//cols)*gap
        if k in hits: out+=f'<circle class="h" cx="{x}" cy="{y}" r="{r+4}"/>'
        out+=f'<circle class="d{" is-hit" if k in hits else ""}" cx="{x}" cy="{y}" r="{r}"/>'
    return f'<svg class="hd-crowd{" hd-crowd--dark" if dark else ""}" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{out}</svg>'

def e06():
    legend=('<div style="display:flex;gap:28px;align-items:center;margin-top:8px">'
            '<span style="display:flex;gap:8px;align-items:center;font-size:15px;font-weight:700;color:var(--muted)"><svg width="18" height="18"><circle cx="9" cy="9" r="8" fill="#d6e7f4"/></svg>1 person</span>'
            '<span style="display:flex;gap:8px;align-items:center;font-size:15px;font-weight:700;color:var(--blue)"><svg width="26" height="26"><circle cx="13" cy="13" r="12" fill="none" stroke="#8fcdf8" stroke-width="2"/><circle cx="13" cy="13" r="8" fill="#0873ba"/></svg>highlighted · 1 in 10</span></div>')
    body=f'''<div style="display:grid;grid-template-columns:auto 1fr;gap:48px;align-items:start">
{spec('Light · 480 dots, 48 highlighted (exactly 1 in each group of 10)', crowd(40,12)+legend, 'l')}
<div style="display:flex;flex-direction:column;gap:32px">
{spec('Paired stat', '<div class="hd-statline"><span class="hd-statline__num">1 in 10</span><span class="hd-statline__txt" style="font-size:24px">fake sample line, replace with script</span></div>', 'l')}
</div></div>'''
    return card('E-06','Dot crowd','4',
        'dots fade in row by row, 30ms stagger, 300ms ease-out; then highlighted dots scale 1 → 1.6 → 1.2 and colour to --blue, 400ms ease-spring, random order within 600ms; halo ring fades in last.', body)

# ---------------- E-07 ----------------
def counter(num, pre='', unit='', fs=None, frm=None, to=None):
    st=f' style="--cnt-fs:{fs}"' if fs else ''
    p=f'<span class="hd-counter__pre">{pre}</span>' if pre else ''
    u=f'<span class="hd-counter__unit">{unit}</span>' if unit else ''
    if frm:
        return (f'<div class="hd-counter hd-counter--to"{st}><span class="hd-counter__from">{frm}</span><span class="hd-counter__arrow">→</span>'
                f'{p}<span class="hd-counter__num" data-to="{to}">{num}</span>{u}</div>')
    return f'<div class="hd-counter"{st}>{p}<span class="hd-counter__num" data-to="{to or num}">{num}</span>{u}</div>'

def e07():
    big_l=('<div class="hd-bignum hd-bignum--light"><div class="hd-kicker">Wellness app · members</div>'
           f'{counter("12","","M+")}<div class="hd-bignum__lbl">people building a daily health habit</div></div>')
    big_d=('<div class="hd-bignum hd-bignum--light"><div class="hd-kicker">Lab partner · reports explained</div>'
           f'{counter("5,000","","",frm="1,500+",to="5000")}<div class="hd-bignum__lbl">reports explained by agents every day</div></div>')
    units=''.join(spec(l,c) for l,c in [('M+',counter("12","","M+")),('₹ Cr',counter("48","₹","Cr")),('%',counter("92","","%")),
                                         ('“to” transition',counter("5,000","","",frm="1,500+",to="5000")),('K+ with prefix label',counter("85","","K+"))])
    chips=(f'<span class="hd-statchip">{well("whatsapp","mint")}<b>85K+</b> chats a week</span>'
           f'<span class="hd-statchip">{well("lab","aqua")}<b>₹ 48 Cr</b> lab revenue served</span>'
           f'<span class="hd-statchip">{well("trend","sky")}<b>92%</b> reports on time</span>'
           f'<span class="hd-statchip">{well("hospital","lav")}<b>214</b> hospitals live</span>')
    body=f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:32px">
  {spec('Full-screen big number · light · true 1920×1080, shown at 44%', scaled(big_l))}
  {spec('Full-screen big number · “to” transition · shown at 44%', scaled(big_d))}
</div>
<div class="eb-block" style="margin-top:40px"><div class="eb-sub">Unit variants · 84px</div><div class="eb-row" style="justify-content:space-between;align-items:flex-end">{units}</div></div>
<div class="eb-block"><div class="eb-sub">Inline stat chips</div><div class="eb-row" style="gap:20px;align-items:center;background:var(--tint);padding:24px;border-radius:var(--r-card)">{chips}</div></div>'''
    return card('E-07','Counters','3, 4, 5, 6, 8, 10',
        'count up 1.2s ease-out on .hd-counter__num (tabular numbers keep width); unit fades in over the last 200ms. “to” variant: old value holds 400ms, slides up 16px + fades, arrow draws, new value counts from old to new in 1.2s.', body)

# ---------------- E-08 Pathkind ----------------
def pk_bar(sub=''):
    return f'<div class="hd-appbar">{logo("pathkind","Pathkind Labs","","height:1.85em")}<span class="hd-appbar__s" style="margin-left:auto">{sub}</span></div>'

def pk_book():
    tests=''.join(f'<div class="hd-li">{well(i,t)}<div><div class="hd-li__t">{n}</div><div class="hd-li__s">{s}</div></div><div class="hd-li__r" style="font-weight:800;font-size:.9em">{p}</div></div>'
                  for n,s,p,i,t in [('HbA1c','Report in 12 hrs','₹450','lab','aqua'),('Vitamin D','Report in 24 hrs','₹899','spark','sun')])
    slots=''.join(f'<span class="hd-tag {"hd-tag--grad" if s else "hd-tag--sky"}" style="font-size:.72em">{t}</span>' for t,s in [('7–8 am',1),('8–9 am',0),('9–10 am',0)])
    return (f'<div class="hd-scr">{pk_bar("Book a test")}<div class="hd-scr__body" style="gap:.7em">'
            f'<div class="hd-input">{ic("search","1.2em")}Search tests or packages</div>'
            '<div style="border-radius:1.2em;padding:1em;background:var(--grad);color:#fff;box-shadow:var(--shadow-glow)">'
            '<div style="display:flex;justify-content:space-between;align-items:flex-start"><div><div style="font-size:.7em;font-weight:700;letter-spacing:.12em;opacity:.85">RECOMMENDED</div><div style="font-weight:800;font-size:1.15em;margin-top:.2em">Full Body Checkup</div><div style="font-size:.78em;opacity:.9">72 tests · home collection</div></div>'
            f'<span class="hd-well hd-well--white" style="--well:1.9em">{ic("check","60%")}</span></div>'
            '<div style="display:flex;align-items:baseline;gap:.5em;margin-top:.6em"><span style="font-size:1.5em;font-weight:800">₹1,499</span><s style="opacity:.7;font-size:.8em">₹3,200</s></div></div>'
            f'{tests}<div style="font-size:.78em;font-weight:700;color:var(--muted);margin-top:.2em">Tomorrow · pick a slot</div><div style="display:flex;gap:.4em">{slots}</div>'
            '<div style="margin-top:auto"><span class="hd-btn hd-btn--primary">Book home collection</span></div></div></div>')

def pk_track():
    blocks=''.join(f'<rect x="{x}" y="{y}" width="62" height="54" rx="8" fill="#fff"/>' for x in [8,82,156,230] for y in range(8,620,66))
    m=('<svg viewBox="0 0 300 620" preserveAspectRatio="xMidYMin slice" style="width:100%;height:100%;position:absolute;inset:0">'
       '<rect width="300" height="620" fill="#eef7fd"/>'+blocks+
       '<rect x="82" y="206" width="62" height="54" rx="8" fill="#cbefd1"/><rect x="230" y="74" width="62" height="54" rx="8" fill="#cbefd1"/>'
       '<path d="M0 352 C80 330 160 380 300 340" stroke="#d5ecfd" stroke-width="18" fill="none"/>'
       '<path d="M40 70 V200 H150 V302 H226" stroke="#d6e7f4" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
       '<path d="M40 70 V200 H150 V240" stroke="url(#pkg)" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
       '<defs><linearGradient id="pkg" gradientUnits="userSpaceOnUse" x1="40" x2="150"><stop offset="0" stop-color="#1789f2"/><stop offset="1" stop-color="#3fd4f6"/></linearGradient></defs>'
       '<circle cx="40" cy="70" r="7" fill="#fff" stroke="#0873ba" stroke-width="3"/>'
       '<g transform="translate(150 240)"><circle r="24" fill="#139bf5" opacity=".18"/><circle r="15" fill="#0873ba" stroke="#fff" stroke-width="3"/>'
       '<g transform="translate(-8 -8) scale(.66)" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">'+ICONS['lab']+'</g></g>'
       '<g transform="translate(226 302)"><path d="M0 0c-9-9-15-15-15-23a15 15 0 0 1 30 0c0 8-6 14-15 23z" fill="#012b44"/><circle cy="-23" r="5.5" fill="#fff"/></g>'
       '<g transform="translate(188 312)"><rect width="76" height="24" rx="12" fill="#012b44"/><text x="38" y="16" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">12 min</text></g></svg>')
    steps=''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:.3em;flex:1"><i style="width:1.1em;height:1.1em;border-radius:50%;display:block;background:{c};{b}"></i><span style="font-size:.62em;font-weight:700;color:{tc}">{t}</span></div>'
                  for t,c,b,tc in [('Booked','var(--blue)','','var(--navy)'),('On the way','#fff','box-shadow:0 0 0 .25em var(--sky) inset,0 0 0 .3em rgba(19,155,245,.2)','var(--blue)'),('Collected','var(--line)','','var(--c-text-3)'),('Report','var(--line)','','var(--c-text-3)')])
    return ('<div class="hd-scr"><div style="position:absolute;inset:0">'+m+'</div>'
            '<div style="position:relative;z-index:2;padding:.2em 1.1em"><span class="hd-tag hd-tag--white" style="font-size:.75em">● Live tracking</span></div>'
            '<div style="margin-top:auto;position:relative;z-index:2;background:#fff;border-radius:1.6em 1.6em 0 0;box-shadow:0 -6px 24px rgba(1,43,68,.08);padding:1.1em 1.1em 2em;display:flex;flex-direction:column;gap:.75em">'
            '<div style="width:2.6em;height:.3em;border-radius:.2em;background:var(--line);align-self:center"></div>'
            f'<div class="hd-row">{well("lab","aqua")}<div><div style="font-weight:800;font-size:1.05em">Arriving in 12 min</div><div class="hd-li__s">Sample collector · ID PK-2291</div></div>'
            f'<span class="hd-well hd-well--sky" style="margin-left:auto">{ic("call","50%")}</span></div>'
            '<div class="hd-progress"><div class="hd-progress__fill" style="--p:38%"></div></div>'
            f'<div style="display:flex">{steps}</div></div></div>')

def pk_report():
    rows=[('HbA1c','7.8 %','High','rose',78),('LDL cholesterol','162 mg/dL','High','rose',70),('Vitamin D','14 ng/mL','Low','sun',22),('Haemoglobin','13.6 g/dL','Normal','mint',55)]
    r=''.join(f'<div class="hd-li" style="flex-direction:column;align-items:stretch;gap:.4em"><div style="display:flex;justify-content:space-between;align-items:center"><span class="hd-li__t">{n}</span><span class="hd-tag hd-tag--{t}">{s}</span></div>'
              f'<div style="display:flex;align-items:center;gap:.6em"><span style="font-weight:800;font-size:.95em;color:{"var(--rose-ink)" if t=="rose" else ("var(--sun-ink)" if t=="sun" else "var(--navy)")};min-width:5.4em">{v}</span>'
              f'<div class="hd-progress hd-progress--{"rose" if t=="rose" else ("amber" if t=="sun" else "mint")}"><div class="hd-progress__fill" style="--p:{p}%"></div></div></div></div>' for n,v,s,t,p in rows)
    return (f'<div class="hd-scr">{pk_bar("Report")}<div class="hd-scr__body" style="gap:.6em">'
            '<div style="font-size:1.35em;font-weight:700;line-height:1.2">Your report is ready</div>'
            '<div style="display:grid;grid-template-columns:1fr 1fr;gap:.5em">'
            '<div style="background:var(--rose);border-radius:1em;padding:.7em"><div style="font-size:1.6em;font-weight:800;color:var(--rose-ink);line-height:1">3</div><div style="font-size:.72em;font-weight:700;color:var(--rose-ink)">need attention</div></div>'
            '<div style="background:var(--mint);border-radius:1em;padding:.7em"><div style="font-size:1.6em;font-weight:800;color:var(--mint-ink);line-height:1">69</div><div style="font-size:.72em;font-weight:700;color:var(--mint-ink)">in normal range</div></div></div>'
            f'{r}<div style="margin-top:auto"><span class="hd-btn hd-btn--primary">{ic("chat","1.2em")}Ask about my report</span></div></div></div>')

def pk_chat():
    return ('<div class="hd-scr" style="background:var(--tint)">'
            f'<div class="hd-appbar" style="background:#fff;padding-top:.3em"><span class="hd-avatar-orb" style="width:2.4em;height:2.4em">{ic("agent","50%")}</span><div><div class="hd-appbar__t">Care agent</div><div class="hd-appbar__s">Pathkind · powered by HeyDoc</div></div></div>'
            '<div class="hd-scr__body" style="padding-top:1em;gap:.6em">'
            '<div class="hd-bubble hd-bubble--user">What does HbA1c 7.8% mean?</div>'
            '<div class="hd-bubble hd-bubble--agent" style="background:#fff">It shows your average blood sugar over 3 months. <b style="color:var(--rose-ink)">7.8%</b> is above the normal range of <b>under 5.7%</b>.</div>'
            '<div class="hd-bubble hd-bubble--agent" style="background:#fff">A doctor should review this. Shall I book a consult for tomorrow?</div>'
            '<div style="display:flex;gap:.4em;flex-wrap:wrap"><span class="hd-tag hd-tag--grad" style="font-size:.78em;padding:.45em .9em">Book consult</span><span class="hd-tag hd-tag--white" style="font-size:.78em;padding:.45em .9em">What should I eat?</span></div>'
            f'<div class="hd-input" style="margin-top:auto;background:#fff">Type a question…{well("send","grad")}</div></div></div>')

def e08():
    ph=lambda lbl,s: spec(lbl, phone(s,'light',style='--phone-w:340px'))
    body=f'''<div class="eb-row" style="justify-content:space-between">
  {ph('1 · Book a test', pk_book())}{ph('2 · Sample collector tracking', pk_track())}{ph('3 · Report card', pk_report())}{ph('4 · Agent explains the result', pk_chat())}
</div>'''
    return card('E-08','Pathkind flow','5',
        'phones swap 500ms ease-in-out slide-left; tracking marker moves along the route 2.4s ease-in-out while the gradient line draws; report rows reveal 80ms stagger with bars filling 600ms ease-out; chat bubbles pop 300ms ease-spring.', body)

# ---------------- E-09 agents ----------------
AGENTS=[('Sales','trend','mint','Converts leads to bookings','Following up <b>128 leads</b> on WhatsApp',62),
        ('Marketing','megaphone','peach','Runs campaigns and nudges','Sending <b>4,200 reminders</b> for Sunday camp',40),
        ('Management','briefcase','lav','Reports and decisions','Writing the <b>8 am ops brief</b>',80),
        ('Lab Ops','lab','aqua','Samples, TAT, reports','Tracking <b>312 samples</b>, 4 at risk',55),
        ('Logistics','truck','sun','Pickups and routes','Routing <b>6 collectors</b> across 22 pickups',70)]
def agent(n,i,t,role,task,p,active):
    st=('<div class="hd-agent__status"><span class="hd-agent__dot"></span>Active</div>' if active else '<div class="hd-agent__status"><span class="hd-agent__dot"></span>Idle</div>')
    tk=(task if active else 'Waiting for a trigger')
    bar=f'<div class="hd-progress hd-progress--thin"><div class="hd-progress__fill" style="--p:{p if active else 0}%"></div></div>'
    return (f'<div class="hd-agent {"is-active" if active else "is-idle"}"><div class="hd-agent__head">{well(i,t)}<div><div class="hd-agent__name">{n} agent</div><div class="hd-agent__role">{role}</div></div></div>'
            f'{st}<div class="hd-agent__task">{tk}</div>{bar}</div>')
def e09():
    idle=''.join(agent(*a,False) for a in AGENTS); act=''.join(agent(*a,True) for a in AGENTS)
    body=f'''<div class="eb-sub">Idle</div><div style="display:flex;gap:24px;justify-content:space-between">{idle}</div>
<div class="eb-sub" style="margin-top:36px">Active</div><div style="display:flex;gap:24px;justify-content:space-between">{act}</div>'''
    return card('E-09','Agent cards','6',
        'idle → active in 300ms ease-out: border fills with --grad, glow fades in, icon re-saturates, bar fills 600ms; status dot pulses (scale 1 → 1.6, fade) 1.2s loop while active. Cards enter staggered 100ms.', body)

# ---------------- E-10 route map ----------------
def route_map(w=1100,h=520):
    out=f'<svg class="hd-routemap" viewBox="0 0 {w} {h}" width="100%" style="border-radius:22px"><rect width="{w}" height="{h}" fill="#eef7fd"/>'
    parks={(2,1),(7,3)}
    for i in range(10):
        for j in range(5):
            x=20+i*110; y=20+j*100
            fill='#cbefd1' if (i,j) in parks else '#fff'
            out+=f'<rect x="{x}" y="{y}" width="90" height="80" rx="12" fill="{fill}"/>'
    out+='<path d="M-20 470 C200 420 330 520 560 455 S900 380 1120 430" stroke="#d5ecfd" stroke-width="34" fill="none"/>'
    out+='<defs><linearGradient id="rmg" gradientUnits="userSpaceOnUse" x1="0" x2="1100"><stop offset="0" stop-color="#1789f2"/><stop offset="1" stop-color="#3fd4f6"/></linearGradient></defs>'
    r1='M560 310 H340 V110 H120'; r2='M560 310 V210 H780 V110 H1000'; r3='M560 310 V410 H890'
    out+=f'<path d="{r3}" stroke="#8fcdf8" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round" fill="none"/>'
    for r in (r1,r2): out+=f'<path class="hd-route" d="{r}" stroke="url(#rmg)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
    pins=[(340,110,1,'done'),(120,110,2,'done'),(780,210,3,'done'),(1000,110,4,'next'),(890,410,5,'todo'),(230,310,6,'todo')]
    for x,y,n,s in pins: out+=pin_svg(x,y,n,s)
    out+=('<g transform="translate(560 310)"><circle r="46" fill="#eef7fd" opacity=".9"/><circle r="34" fill="url(#rmo)"/>'
          '<g transform="translate(-13 -13) scale(1.08)" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">'+ICONS['lab']+'</g></g>'
          '<defs><radialGradient id="rmo" cx=".28" cy=".18" r=".9"><stop offset="0" stop-color="#0a84e8"/><stop offset=".55" stop-color="#2ba7f5"/><stop offset="1" stop-color="#43d0f2"/></radialGradient></defs>')
    out+=van_svg(890,210)
    out+='<g transform="translate(588 250)"><rect width="126" height="34" rx="17" fill="#012b44"/><text x="63" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="#fff" font-family="Open Sans">Lab hub</text></g>'
    out+='<g transform="translate(906 166)"><rect width="128" height="34" rx="17" fill="#fff" stroke="#d6e7f4" stroke-width="2"/><text x="64" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="#0873ba" font-family="Open Sans">ETA 6 min</text></g>'
    return out+'</svg>'

def pin_svg(x,y,n,state):
    fill={'done':'#1f8a43','next':'#0873ba','todo':'#fff'}[state]; tc='#fff' if state!='todo' else '#0873ba'
    stroke='' if state!='todo' else ' stroke="#0873ba" stroke-width="3"'
    ring='<circle cy="-30" r="24" fill="#139bf5" opacity=".18"/>' if state=='next' else ''
    lab=('<path d="M-6 -30l4 4 8-8" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' if state=='done'
         else f'<text y="-25" text-anchor="middle" font-size="15" font-weight="800" fill="{tc}" font-family="Open Sans">{n}</text>')
    return (f'<g class="hd-pin is-{state}" transform="translate({x} {y})"><ellipse rx="9" ry="3.5" fill="#012b44" opacity=".15"/>{ring}'
            f'<path d="M0 0C-12-12-18-20-18-30a18 18 0 0 1 36 0c0 10-6 18-18 30z" fill="{fill}"{stroke}/>{lab}</g>')

def van_svg(x,y):
    return (f'<g class="hd-van" transform="translate({x} {y})"><circle r="24" fill="#012b44"/><circle r="30" fill="none" stroke="#012b44" stroke-width="2" opacity=".2"/>'
            '<g transform="translate(-12 -12)" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">'+ICONS['truck']+'</g></g>')

def e10():
    pins=''.join(f'<svg viewBox="-24 -56 48 64" width="48" height="64">{pin_svg(0,0,n,s)}</svg>' for n,s in [(1,'done'),(4,'next'),(5,'todo')])
    parts=f'''<div style="display:flex;flex-direction:column;gap:28px;min-width:300px">
  {spec('Pickup pin · collected / next / pending', '<div style="display:flex;gap:18px;align-items:flex-end">'+pins+'</div>','l')}
  {spec('Collector van', '<svg viewBox="-32 -32 64 64" width="64" height="64">'+van_svg(0,0)+'</svg>','l')}
  {spec('Route · driven / planned', '<svg width="260" height="50"><defs><linearGradient id="rlg" gradientUnits="userSpaceOnUse" x1="6" x2="254"><stop offset="0" stop-color="#1789f2"/><stop offset="1" stop-color="#3fd4f6"/></linearGradient></defs><path d="M6 14H254" stroke="url(#rlg)" stroke-width="6" stroke-linecap="round"/><path d="M6 38H254" stroke="#8fcdf8" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/></svg>','l')}
  {spec('Map legend chip', '<div style="display:flex;gap:10px;flex-wrap:wrap"><span class="hd-tag hd-tag--navy">Lab hub</span><span class="hd-tag hd-tag--white">ETA 6 min</span><span class="hd-tag hd-tag--mint">22 pickups · 14 done</span></div>','l')}
</div>'''
    body=f'<div style="display:grid;grid-template-columns:1fr auto;gap:40px;align-items:start">{spec("Flat city map · 1100×520, fake geography", route_map(), "l")}{parts}</div>'
    return card('E-10','Route map','6',
        'map fades in 600ms; routes draw 1.2s ease-in-out via stroke-dashoffset, one after another; pins drop 300ms ease-spring staggered 120ms; van follows the route path (offset-path) 2.4s ease-in-out; collected pins flip to green with a 150ms tick.', body)
