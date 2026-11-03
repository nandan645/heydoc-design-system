from base import *

def pdf_thumb():
    return ('<div class="hd-pdf"><div class="hd-pdf__sheet"><b style="width:70%;background:#012b44"></b><b></b><b class="r" style="width:80%"></b><b></b><b class="r" style="width:60%"></b><b></b><b class="r" style="width:75%"></b><b style="width:50%"></b><span class="hd-pdf__type">PDF</span></div>'
            '<div style="min-width:0"><div class="hd-pdf__name">Lab_Report_31Oct.pdf</div><div class="hd-pdf__meta">2 pages · 214 KB</div>'
            '<div class="hd-pdf__vals"><span>HbA1c <em>7.8 %</em></span><span>Glucose <em>148 mg/dL</em></span><span>Vitamin D <em>14 ng/mL</em></span></div></div></div>')

def ping(w=None, fs=None):
    st=[]
    if w: st.append(f'--ping-w:{w}')
    if fs: st.append(f'--ping-fs:{fs}')
    return (f'<div class="hd-ping" style="{";".join(st)}"><div class="hd-ping__app">{ic("whatsapp","62%")}<span class="hd-badge">3</span></div>'
            '<div class="hd-ping__main"><div class="hd-ping__top"><span>WhatsApp</span><span>now</span></div>'
            '<div class="hd-ping__title">City Diagnostics</div><div class="hd-ping__text">Your report is ready. 3 values are outside the normal range.</div>'
            f'{pdf_thumb()}</div></div>')

def lock_screen():
    return ('<div class="hd-scr" style="background:linear-gradient(170deg,#eef7fd 0%,#d5ecfd 55%,#c9f1f4 100%)">'
            '<div style="text-align:center;margin-top:1.4em;color:var(--navy)"><div style="font-size:.95em;font-weight:600;opacity:.7">Saturday, 31 October</div>'
            '<div style="font-size:4.6em;font-weight:300;letter-spacing:-.04em;line-height:1.05">9:41</div></div>'
            f'<div style="padding:1.4em .7em 0">{ping(fs="1em")}</div>'
            '<div style="margin-top:auto;display:flex;justify-content:space-between;padding:0 2.2em 2.6em;color:var(--navy)">'
            f'<span class="hd-well hd-well--white" style="--well:3em;opacity:.8">{ic("call","45%")}</span><span class="hd-well hd-well--white" style="--well:3em;opacity:.8">{ic("camera","45%")}</span></div></div>')

def chat_screen():
    rep=('<div class="hd-report"><div class="hd-report__h"><span>Lab report</span><span class="hd-tag hd-tag--rose" style="font-size:.7em">3 flagged</span></div>'
         '<div class="hd-report__r"><span>HbA1c</span><em class="hi">7.8 %</em><span class="hd-report__f">HIGH</span></div>'
         '<div class="hd-report__r"><span>Glucose (fasting)</span><em class="hi">148</em><span class="hd-report__f">HIGH</span></div>'
         '<div class="hd-report__r"><span>Vitamin D</span><em class="hi">14</em><span class="hd-report__f">LOW</span></div>'
         '<div class="hd-report__r" style="border:0"><span>TSH</span><em class="ok">2.1</em><span class="hd-report__f ok">OK</span></div>'
         '<div style="display:flex;gap:.5em;align-items:center;margin-top:.5em;font-size:.85em;color:var(--muted)"><span style="background:var(--rose-ink);color:#fff;font-weight:800;font-size:.75em;padding:.15em .4em;border-radius:.3em">PDF</span>Lab_Report_31Oct.pdf · 214 KB</div></div>')
    return ('<div class="hd-scr" style="background:#0e1d29">'
            f'<div class="hd-appbar" style="border-bottom:1px solid #1d3242">{ic("back","1.3em")}{well("lab","aqua","2.6em")}'
            '<div><div class="hd-appbar__t">City Diagnostics</div><div class="hd-appbar__s">online</div></div></div>'
            '<div class="hd-scr__body" style="padding-top:1em;gap:.7em">'
            '<div style="align-self:center;font-size:.7em;font-weight:700;color:#8fb3cc;background:#16293a;padding:.3em .8em;border-radius:1em">TODAY</div>'
            '<div class="hd-bubble hd-bubble--agent" style="background:#16293a;color:#fff;max-width:88%;padding:.4em">'+rep+'<span class="hd-bubble__meta" style="padding:0 .5em">9:41</span></div>'
            '<div class="hd-bubble hd-bubble--agent" style="background:#16293a;color:#fff">Hi Aarav, your report is ready. Reply to talk to our care team.<span class="hd-bubble__meta">9:41</span></div>'
            '<div style="align-self:center;margin-top:auto"><span class="hd-unread">3 unread messages</span></div>'
            f'<div class="hd-input" style="background:#16293a;color:#8fb3cc">Message{well("send","grad")}</div></div></div>')

def e03():
    body=f'''
<div class="eb-row" style="justify-content:space-between;align-items:flex-start">
  {spec('Phone · light (empty)', phone('<div class="hd-scr" style="align-items:center;justify-content:center">'+slot("Screen content","","width:80%;height:60%")+'</div>','light'))}
  {spec('Phone · dark (empty)', phone('<div class="hd-scr" style="align-items:center;justify-content:center">'+slot("Screen content","hd-slot--dark","width:80%;height:60%")+'</div>','dark'))}
  {spec('Light · incoming ping on lock screen', phone(lock_screen(),'light'))}
  {spec('Dark · opened chat with PDF', phone(chat_screen(),'dark'))}
</div>
<div class="eb-row" style="justify-content:space-around;align-items:center;margin-top:40px;padding-top:32px;border-top:2px dashed var(--grey)">
    {spec('Ping · standalone (.hd-ping)', ping(w='480px',fs='18px'))}
    {spec('PDF thumbnail · fake values in red', '<div style="font-size:20px;width:400px">'+pdf_thumb()+'</div>')}
    {spec('Unread badge · count / pill', '<div style="display:flex;gap:18px;align-items:center"><span class="hd-badge">3</span><span class="hd-badge" style="min-width:40px;height:40px;border-radius:20px;font-size:20px">12</span><span class="hd-unread" style="font-size:16px">3 unread messages</span></div>')}
</div>'''
    return card('E-03','Phone frame + WhatsApp-style ping','1, 3, 5',
        'phone: rise 40px + fade, 600ms ease-out. Ping drops from top 400ms ease-spring; badge pops scale 0 → 1, 300ms ease-spring, 200ms after ping. PDF values flash red once (300ms).', body)

# ---------------- E-04 ----------------
def sheet():
    cols=['','A','B','C','D','E','F','G']
    hdr=['ID','Patient','Test','Date','Status','Amount','Notes']
    rows=[
      ['Pt-0412','R. Sharma','CBC','12/10','Pending','₹450','call back??'],
      ['Pt-0413','—','HbA1c','Oct 13','<r>Delayed','₹ 450.00','<e>#REF!'],
      ['Pt-0413','A. Khan','HbA1c','2026-10-13','<y>Collected','450','dup?'],
      ['pt 415','S. Iyer','Lipid','13 Oct','Report sent','<e>#VALUE!','WhatsApp sent x3'],
      ['Pt-0416','M. Das','Vit D','14/10/26','<r>No show','₹899',''],
      ['','N. Rao','','','<y>??','','ask Priya'],
      ['Pt-0418','K. Patel','Thyroid','15/10','Pending','₹600','<ov>rescheduled twice, pickup missed again, check with lab'],
      ['Pt-0419','V. Gupta','CBC','16.10','<y>Pending','₹450',''],
      ['Pt-0420','T. Bose','Full body','16/10','<r>Delayed','₹1,499','<e>#N/A'],
      ['Pt-0421','J. Mehta','HbA1c','Oct 17','Collected','₹450','old sheet'],
    ]
    out=''.join(f'<div class="h">{c}</div>' for c in cols)
    out+='<div class="n">1</div>'+''.join(f'<div style="font-weight:700;color:var(--navy)">{h}</div>' for h in hdr)
    for i,r in enumerate(rows):
        out+=f'<div class="n">{i+2}</div>'
        for j,v in enumerate(r):
            cls=''
            for tag,c in [('<r>','r'),('<y>','y'),('<e>','e'),('<ov>','ov')]:
                if v.startswith(tag): v=v[len(tag):]; cls=c
            if i==4 and j==4: cls+=' sel'
            out+=f'<div class="{cls}">{v}</div>'
    return (f'<div class="hd-window" style="--win-w:860px"><div class="hd-window__bar"><i></i><i></i><i></i><span>patients_FINAL_v7 (2).xlsx</span>'
            f'<span style="margin-left:auto;color:var(--rose-ink);display:flex;gap:6px;align-items:center">{ic("alert","16px")}4 errors</span></div>'
            '<div style="display:flex;gap:6px;padding:8px 14px;border-bottom:1px solid var(--line)">'+''.join(f'<span style="width:{w}px;height:12px;border-radius:4px;background:var(--grey)"></span>' for w in [40,26,60,30,30,80,44])+'</div>'
            f'<div class="hd-sheet">{out}</div></div>')

def minidash(i):
    if i==0:
        ch='<svg viewBox="0 0 260 90" width="100%" height="90">'+''.join(f'<rect x="{8+k*36}" y="{90-h}" width="24" height="{h}" rx="6" fill="#3fa1f8"/>' for k,h in enumerate([40,62,30,75,52,68,44]))+'</svg>'
        return ('Leads this week','1,204','CRM export',ch)
    if i==1:
        ch=('<svg viewBox="0 0 260 90" width="100%" height="90"><g transform="translate(60 45)"><circle r="34" fill="none" stroke="#feb64f" stroke-width="16"/>'
            '<circle r="34" fill="none" stroke="#7f7be6" stroke-width="16" stroke-dasharray="120 300" transform="rotate(-90)"/></g>'
            '<g font-size="11" font-weight="700" fill="#5b6b78"><rect x="120" y="26" width="10" height="10" rx="3" fill="#7f7be6"/><text x="136" y="35">Organic</text><rect x="120" y="50" width="10" height="10" rx="3" fill="#feb64f"/><text x="136" y="59">Paid</text></g></svg>')
        return ('Leads (sheet)','1,187','Shared Google Sheet',ch)
    if i==2:
        ch=('<svg viewBox="0 0 260 90" width="100%" height="90"><path d="M5 30 C40 20 60 50 90 44 S140 70 170 62 S220 80 255 74" fill="none" stroke="#ea5c72" stroke-width="4" stroke-linecap="round"/>'
            '<path d="M5 60 C50 58 90 40 130 46 S210 30 255 36" fill="none" stroke="#d6e7f4" stroke-width="3" stroke-dasharray="3 6" stroke-linecap="round"/></svg>')
        return ('Leads ↓ 18%','982','Call-centre log',ch)
    if i==3:
        ch=('<svg viewBox="0 0 260 90" width="100%" height="90"><path d="M70 82A60 60 0 0 1 190 82" fill="none" stroke="#d6e7f4" stroke-width="16" stroke-linecap="round"/>'
            '<path d="M70 82A60 60 0 0 1 152 26" fill="none" stroke="#3be6a2" stroke-width="16" stroke-linecap="round"/><text x="130" y="80" text-anchor="middle" font-size="20" font-weight="800" fill="#012b44">61%</text></svg>')
        return ('Reports on time','61%','Lab system',ch)
    ch='<svg viewBox="0 0 260 90" width="100%" height="90">'+''.join(f'<rect x="{6+c*36}" y="{4+r*29}" width="30" height="24" rx="6" fill="{["#fde0da","#fff2cd","#eef7fd","#ea5c72","#cad4f4"][(r*3+c*2)%5]}"/>' for r in range(3) for c in range(7))+'</svg>'
    return ('Pending follow-ups','214 / 238?','WhatsApp export',ch)

def md(i):
    t,v,src,ch=minidash(i)
    return f'<div class="hd-minidash"><div class="hd-minidash__h"><span>{t}</span>{ic("spark","14px")}</div><div class="hd-minidash__v">{v}</div>{ch}<div class="hd-minidash__src">Source: {src}</div></div>'

def notifs():
    items=[('call','rose','Missed call','+91 98xxx xx210 · 3rd attempt','now'),('whatsapp','mint','12 unread chats','Patients asking for reports','2m'),
           ('report','sun','Report delayed','Sample #4471 · 26 hrs','9m'),('bell','lav','Follow-ups overdue','38 patients this week','14m')]
    out=''
    for k,(i,t,a,b,tm) in enumerate(reversed(items)):
        d=3-k
        out+=(f'<div class="hd-notif" style="top:{d*52}px;transform:scale({1-d*0.04});opacity:{1-d*0.12};z-index:{10-d}">{well(i,t)}'
              f'<div><div class="hd-notif__t">{a}</div><div class="hd-notif__s">{b}</div></div><span class="hd-notif__time">{tm}</span></div>')
    return f'<div class="hd-notif-stack" style="--notif-w:420px">{out}</div>'

def queue():
    seq='sss'+'.'*7+'w.w..w.wl.l.w..'
    dots=''.join(f'<i class="{c if c!="." else ""}"></i>' for c in seq)
    return (f'<div class="hd-queue"><div class="hd-queue__dots">{dots}</div><div class="hd-queue__lbl">'
            '<span style="display:flex;gap:6px;align-items:center"><i style="width:12px;height:12px;border-radius:50%;background:var(--blue)"></i>Being served</span>'
            '<span style="display:flex;gap:6px;align-items:center"><i style="width:12px;height:12px;border-radius:50%;background:var(--line)"></i>Waiting</span>'
            '<span style="display:flex;gap:6px;align-items:center"><i style="width:12px;height:12px;border-radius:50%;background:var(--d-amber)"></i>&gt; 30 min</span>'
            '<span style="display:flex;gap:6px;align-items:center"><i style="width:12px;height:12px;border-radius:50%;background:var(--d-rose)"></i>&gt; 60 min</span>'
            '<span style="margin-left:auto;color:var(--navy)">46 waiting · avg 38 min</span></div></div>')

def e04():
    body=f'''
<div style="display:grid;grid-template-columns:auto 1fr;gap:48px;align-items:start">
  {spec('Messy spreadsheet window', sheet(), 'l')}
  <div style="display:flex;flex-direction:column;gap:40px">
    {spec('Stacked notifications', notifs(), 'l')}
    {spec('Queue dots', queue(), 'l')}
  </div>
</div>
<div class="eb-block" style="margin-top:44px">{spec('Five mini dashboards · same metric, five answers', '<div style="display:flex;gap:24px">'+''.join(md(i) for i in range(5))+'</div>', 'l')}</div>'''
    return card('E-04','Chaos elements','1b',
        'windows pop in staggered 80ms (scale .92 → 1, ease-spring) and settle at random ±3° tilt; notifications stack in 150ms each from top; queue dots fill left to right 40ms each, amber/red ones last.', body)

# ---------------- E-05 Habuild ----------------
def hb_bar(sub):
    return f'<div class="hd-appbar">{logo("habuild","Habuild","","height:1.7em")}<span style="margin-left:auto" class="hd-appbar__s">{sub}</span></div>'

def hb_onboard():
    chips=''.join(f'<span class="hd-chip {"hd-chip--solid" if s else ""}" style="font-size:.85em;padding:.35em .9em .35em .35em;gap:.5em">{well(i,"white" if s else t,"2em")}{n}</span>' for n,i,t,s in
                  [('Better sleep','clock','lav',0),('Less stress','wellness','mint',1),('Lose weight','trend','peach',0),('More energy','spark','sun',0)])
    orb=('<svg viewBox="0 0 200 150" style="width:100%;height:9.5em"><circle cx="100" cy="75" r="68" fill="none" stroke="#d6e7f4" stroke-width="2" stroke-dasharray="2 7" stroke-linecap="round"/>'
         '<circle cx="100" cy="75" r="46" fill="#eef7fd"/><circle cx="100" cy="75" r="30" fill="url(#hbo)"/><defs><radialGradient id="hbo" cx=".28" cy=".18" r=".9"><stop offset="0" stop-color="#0a84e8"/><stop offset="1" stop-color="#43d0f2"/></radialGradient></defs>'
         '<circle cx="32" cy="75" r="6" fill="#cbefd1"/><circle cx="168" cy="75" r="6" fill="#fff2cd"/><circle cx="100" cy="7" r="6" fill="#cad4f4"/></svg>')
    return (f'<div class="hd-scr">{hb_bar("Step 1 of 3")}<div class="hd-scr__body">{orb}'
            '<div style="font-size:1.55em;font-weight:700;line-height:1.2;letter-spacing:-.02em">Build a daily habit that <span style="color:var(--blue)">sticks</span></div>'
            '<div style="font-size:.88em;color:var(--muted);line-height:1.4">Pick a goal. Your plan updates every day.</div>'
            f'<div style="display:flex;flex-wrap:wrap;gap:.45em">{chips}</div>'
            '<div style="margin-top:auto"><span class="hd-btn hd-btn--primary">Start my plan</span></div>'
            '<div style="display:flex;gap:.35em;justify-content:center"><i style="width:1.4em;height:.4em;border-radius:.2em;background:var(--blue)"></i><i style="width:.4em;height:.4em;border-radius:50%;background:var(--line)"></i><i style="width:.4em;height:.4em;border-radius:50%;background:var(--line)"></i></div></div></div>')

def hb_plan():
    items=[('06:30','Morning yoga','20 min','wellness','mint',1),('07:00','Breathing','5 min','spark','aqua',1),('13:00','Hydration','6 of 8 glasses','clock','sky',0),
           ('18:30','Evening walk','4,000 steps','route','peach',0),('21:30','Wind down','10 min','layers','lav',0)]
    li=''
    for t,n,s,i,tone,done in items:
        r=(f'<span class="hd-well hd-well--grad" style="--well:1.7em">{ic("check","60%")}</span>' if done else '<span style="width:1.7em;height:1.7em;border-radius:50%;border:.15em solid var(--line);display:block"></span>')
        li+=f'<div class="hd-li" style="{"opacity:.6" if done else ""}">{well(i,tone)}<div><div class="hd-li__t">{n}</div><div class="hd-li__s">{t} · {s}</div></div><div class="hd-li__r">{r}</div></div>'
    return (f'<div class="hd-scr">{hb_bar("Sat, 31 Oct")}<div class="hd-scr__body">'
            '<div style="display:flex;justify-content:space-between;align-items:flex-end"><div><div class="hd-kicker" style="font-size:.7em;letter-spacing:.15em">Day 21</div><div style="font-size:1.4em;font-weight:700">Today\'s plan</div></div>'
            '<svg viewBox="0 0 40 40" style="width:3.2em;height:3.2em"><circle cx="20" cy="20" r="16" fill="none" stroke="#d6e7f4" stroke-width="5"/><circle cx="20" cy="20" r="16" fill="none" stroke="#139bf5" stroke-width="5" stroke-dasharray="40 101" stroke-linecap="round" transform="rotate(-90 20 20)"/><text x="20" y="24" text-anchor="middle" font-size="11" font-weight="800" fill="#012b44">2/5</text></svg></div>'
            f'{li}</div></div>')

def hb_chat():
    return ('<div class="hd-scr" style="background:var(--tint)">'
            f'<div class="hd-appbar" style="background:#fff;padding-top:.3em"><span class="hd-avatar-orb" style="width:2.4em;height:2.4em">{ic("spark","50%")}</span><div><div class="hd-appbar__t">WellnessGPT</div><div class="hd-appbar__s" style="color:var(--mint-ink)">● online</div></div>{logo("habuild","Habuild","","height:1.25em;margin-left:auto")}</div>'
            '<div class="hd-scr__body" style="padding-top:1em;gap:.6em">'
            '<div class="hd-bubble hd-bubble--user">My back feels stiff after sitting all day.</div>'
            '<div class="hd-bubble hd-bubble--agent" style="background:#fff">Try a 5-minute desk stretch. I\'ve added it to your 4 pm plan.</div>'
            f'<div class="hd-li" style="max-width:84%">{well("wellness","mint")}<div><div class="hd-li__t">Desk stretch</div><div class="hd-li__s">5 min · 16:00</div></div><span class="hd-tag hd-tag--mint" style="margin-left:auto">Added</span></div>'
            '<div class="hd-bubble hd-bubble--user">Thanks. Can you remind me?</div>'
            '<div class="hd-typing" style="font-size:.7em;background:#fff"><i></i><i></i><i></i></div>'
            f'<div class="hd-input" style="margin-top:auto;background:#fff">Ask WellnessGPT…{well("send","grad")}</div></div></div>')

def hb_streak():
    days=''.join(f'<i style="width:1.55em;height:1.55em;border-radius:50%;display:block;background:{"var(--grad)" if k<21 else ("#fff" if k>21 else "var(--sun)")};{"box-shadow:inset 0 0 0 .12em var(--line)" if k>21 else ""}{";box-shadow:0 0 0 .2em rgba(254,182,79,.35)" if k==21 else ""}"></i>' for k in range(28))
    return (f'<div class="hd-scr">{hb_bar("Progress")}<div class="hd-scr__body" style="gap:1em">'
            '<div style="text-align:center;padding:1em 0 .4em;background:var(--tint);border-radius:1.4em">'
            f'<span class="hd-well hd-well--sun" style="--well:3em">{ic("flame","55%")}</span>'
            '<div style="font-size:4.4em;font-weight:800;letter-spacing:-.04em;line-height:1;color:var(--blue);margin-top:.15em">21</div>'
            '<div style="font-weight:700">day streak</div><div style="font-size:.78em;color:var(--muted);margin:.2em 0 .6em">Best so far · keep it going</div></div>'
            '<div style="display:flex;justify-content:space-between;font-size:.65em;font-weight:700;color:var(--c-text-3)"><span>M</span><span>T</span><span>W</span><span>T</span><span>F</span><span>S</span><span>S</span></div>'
            f'<div style="display:grid;grid-template-columns:repeat(7,1fr);gap:.45em;justify-items:center;margin-top:-.5em">{days}</div>'
            '<div style="display:grid;grid-template-columns:1fr 1fr;gap:.6em;margin-top:auto">'
            '<div class="hd-li" style="flex-direction:column;align-items:flex-start;gap:.1em"><span class="hd-li__s">Sessions</span><span style="font-size:1.3em;font-weight:800">58</span></div>'
            '<div class="hd-li" style="flex-direction:column;align-items:flex-start;gap:.1em"><span class="hd-li__s">Minutes</span><span style="font-size:1.3em;font-weight:800">1,140</span></div></div>'
            '<span class="hd-tag hd-tag--sky" style="align-self:center">Top 10% this month</span></div></div>')

def e05():
    ph=lambda lbl,s: spec(lbl, phone(s,'light',style='--phone-w:340px'))
    body=f'''<div class="eb-row" style="justify-content:space-between">
  {ph('1 · Onboarding', hb_onboard())}{ph('2 · Daily plan', hb_plan())}{ph('3 · WellnessGPT chat', hb_chat())}{ph('4 · Progress streak', hb_streak())}
</div>'''
    return card('E-05','Habuild app screens','3',
        'screens swap with 500ms ease-in-out slide (40px) + cross-fade; plan items check off 300ms ease-spring, 120ms apart; streak number counts 0 → 21 in 800ms ease-out; calendar dots fill 20ms each.', body)
