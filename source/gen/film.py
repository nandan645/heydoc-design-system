import sys; sys.path.insert(0,'.')
import base, iphone; base.phone=iphone.ip_phone   # film uses the vector iPhone replica
from base import *
from css import CSS
from s2 import pdf_thumb, sheet, md
import act2, act3, act4, act5, brand

# ---------------------------------------------------------------- markup
# Act 1 lock screen: decluttered, notifications only, arriving one after another (newest on top)
NOTES=[  # icon, colour, sender, message, arrival time (s) — few and calm
 ('whatsapp','mint-ink','City Diagnostics','Your lab report is ready.',1.3),
 ('report','rose-ink','City Diagnostics','Sent a PDF: Lab_Report_31Oct',2.3),
 ('whatsapp','mint-ink','Family','Did the report come? What does it say?',3.5),
 ('bell','sun-ink','City Diagnostics','Reminder: your report is ready',6.6),
 ('wellness','lav-ink','Habuild','Morning class starts in 10 min',8.2)]
def note(i,c,who,msg):
    return (f'<div class="a1-nt"><span class="a1-nt__ic" style="background:var(--{c})">{ic(i,"58%")}</span>'
            f'<div class="a1-nt__m"><div class="a1-nt__top"><b>{who}</b><span>now</span></div><div class="a1-nt__s">{msg}</div></div></div>')
# original wallpaper in the spirit of a dark titanium lock screen: lit S-shaped ridge + fine grain (all vector, no copied image)
WALL=('<svg class="a1-wall" viewBox="0 0 300 650" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><defs>'
 '<linearGradient id="a1w1" x1="0" y1="0" x2="1" y2=".2"><stop offset="0" stop-color="#6b6e74"/><stop offset=".18" stop-color="#3a3c40"/><stop offset=".55" stop-color="#1b1c1f"/><stop offset="1" stop-color="#0d0e10"/></linearGradient>'
 '<radialGradient id="a1w2" cx=".35" cy=".62" r=".55"><stop offset="0" stop-color="#4a4d52" stop-opacity=".55"/><stop offset="1" stop-color="#0b0c0e" stop-opacity="0"/></radialGradient>'
 '<filter id="a1blur" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="6"/></filter>'
 '<filter id="a1grain"><feTurbulence type="fractalNoise" baseFrequency="1.9" numOctaves="2" seed="4" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/>'
 '<feComponentTransfer><feFuncA type="table" tableValues="0 0 .55"/></feComponentTransfer></filter></defs>'
 '<rect width="300" height="650" fill="#0b0c0e"/>'
 '<path d="M300 -10 C150 10 70 90 120 170 S300 300 250 400 S70 520 40 660 L300 660 Z" fill="url(#a1w1)"/>'
 '<path d="M300 -10 C150 10 70 90 120 170 S300 300 250 400 S70 520 40 660" fill="none" stroke="#9a9da3" stroke-opacity=".35" stroke-width="10" filter="url(#a1blur)"/>'
 '<rect width="300" height="650" fill="url(#a1w2)"/>'
 '<rect width="300" height="650" filter="url(#a1grain)" opacity=".55" style="mix-blend-mode:screen"/></svg>')
LOCK=('<div class="hd-scr a1-lock">'+WALL+
      '<div class="a1-date">Saturday, 31 October</div><div class="a1-clock">9:41</div>'
      '<div class="a1-feed" id="a1feed">'+''.join(note(*n[:4]) for n in NOTES)+'</div>'
      '<div class="a1-dock"><span>'+ic("spark","45%")+'</span><span>'+ic("camera","45%")+'</span></div></div>')

def phone_markup():
    return phone(LOCK,'light',cls='hd-ip--dark',style='--phone-w:360px')

SKEL0=('<div class="a1-skel"><div class="sk-top"><i style="width:34%"></i><i style="width:16%;margin-left:auto"></i></div>'
      '<div class="sk-hero"></div><div class="sk-row"><b></b><i></i></div><div class="sk-row"><b></b><i></i></div><div class="sk-row"><b></b><i></i></div>'
      '<div class="sk-btn"></div></div>')
SKEL=phone(SKEL0,'light',style='--phone-w:300px')

NOTIFS=[('call','rose','Missed call','+91 98xxx xx210 · 3rd attempt'),('whatsapp','mint','12 unread chats','Patients asking for reports'),
        ('report','sun','Report delayed','Sample #4471 · 26 hrs'),('bell','lav','Follow-ups overdue','38 patients this week'),
        ('alert','rose','Queue over 40','OPD wing B · now')]
def notif_stack():
    cards=''.join(f'<div class="hd-notif a1-n" data-i="{k}">{well(i,t)}<div><div class="hd-notif__t">{a}</div><div class="hd-notif__s">{b}</div></div><span class="hd-notif__time">now</span></div>'
                  for k,(i,t,a,b) in enumerate(NOTIFS))
    return f'<div class="a1-nstack">{cards}</div>'

def queue_row():
    seq='sss'+'.'*11+'w.w.ww.wl.wl.ll'
    dots=''.join(f'<i class="{c if c!="." else ""}"></i>' for c in seq)
    return (f'<div class="a1-queue"><div class="hd-queue__dots" id="a1q">{dots}</div>'
            f'<div class="hd-queue__lbl" style="margin-top:12px"><span style="color:var(--navy)">{ic("queue","18px")}</span><span style="color:var(--navy)">OPD queue</span>'
            '<span style="margin-left:auto;color:var(--rose-ink)" id="a1qn">46 waiting · avg 38 min</span></div></div>')

# shells: id, content, face icon/tone, pile x,y,rot,scale k, radius, transparent?
SHELLS=[
 ('sheet',  sheet(),        'report','lav',   -760,-330,-3, 1.0, 16, False),
 ('notifs', notif_stack(),  'bell','sun',      720,-320, 2, 1.3, 16, True),
 ('md0',    md(0),          'trend','sky',   -1220, 260, 4, 1.35, 22, False),
 ('md1',    md(1),          'db','aqua',      -640, 330,-5, 1.35, 22, False),
 ('md2',    md(2),          'call','rose',     640, 340, 3, 1.35, 22, False),
 ('md3',    md(3),          'lab','mint',     1220, 240,-4, 1.35, 22, False),
 ('md4',    md(4),          'whatsapp','peach',-1330,-150, 6, 1.35, 22, False),
 ('queue',  queue_row(),    'queue','sky',       0,-650, 0, 1.2, 16, True),
]

def shell(sid, content, face, cls=''):
    return (f'<div class="sh {cls}" id="sh-{sid}"><div class="sh-bg"></div><div class="sh-orb"></div><div class="sh-ring"></div>'
            f'<div class="sh-clip"><div class="sh-content">{content}</div>{face}</div></div>')

shells=''.join(shell(s[0], s[1], f'<div class="sh-face">{well(s[2],s[3],"72px")}</div>') for s in SHELLS)
shells+=shell('phone', phone_markup(), f'<div class="sh-content2">{SKEL}</div><div class="sh-dot"></div>', 'is-phone')

import json
shell_cfg=json.dumps([{'id':s[0],'x':s[4],'y':s[5],'rot':s[6],'k':s[7],'r':s[8],'tr':s[9]} for s in SHELLS])

def words(txt):
    out=[]
    for tok in txt.split(' '):
        if tok.startswith('*'): out.append(f'<span class="w"><em>{tok.strip("*")}</em></span>')
        else: out.append(f'<span class="w">{tok}</span>')
    return ' '.join(out)

TEXTS=[('t1','t-left',  1.00, 4.25, 'Her report arrived. No one *explained* *it.*'),
       ('t2','t-bottom',5.90, 9.80, 'Data everywhere. *Action* *nowhere.*'),
       ('t3','t-bottom',10.30,12.55,'What if care could act on its own?'),
       ('t4','t-bottom',13.25,16.0,'*HeyDoc* *AI.* Agents that run care.'),
       ('t5','t-bottom',19.0,26.2,'*5M+* *members* · Agents for every one'),
       ('t6','t-bottom',35.3,42.6,'*10M+* *patients* · Lab agents at every touchpoint'),
       ('t7','t-bottom',44.8,52.3,'[AL] *agents* *live* · [RS]% *faster* *reports*'),
       ('t8','t-bottom',55.2,63.6,'*MAHA-PULSE* *AI* · Kolhapur, live'),
       ('t9','t-bottom',70.2,73.5,'District hospitals, statewide'),
       ('t10','t-bottom',77.6,83.3,'4 care segments. *One* *company* *brain.*'),
       ('t11','t-top',95.3,103.2,'Powering agentic care for')]
text_html=''.join(f'<div class="tb {c}" id="{i}"><div class="hd-headline">{words(s)}</div></div>' for i,c,a,b,s in TEXTS).replace('<em>5M+</em>','<em><span id="hbN">0</span>M+</em>').replace('<em>10M+</em>','<em><span id="pkN">0</span>M+</em>').replace('[AL]','<span class="a2-var" id="v_agents_live">00</span>').replace('[RS]','<span class="a2-var" id="v_report_speedup_pct">00</span>')
text_cfg=json.dumps([{'id':i,'in':a,'out':b} for i,c,a,b,s in TEXTS])

A1CSS=r'''
html,body{margin:0;height:100%;overflow:hidden;background:#eef1f4;width:auto}
body{font-family:var(--font)}
#viewport{position:fixed;inset:0;display:flex;align-items:center;justify-content:center}
#stage{position:absolute;left:0;top:0;width:1920px;height:1080px;background:#fff;overflow:hidden;transform-origin:0 0;box-shadow:0 20px 60px rgba(1,43,68,.08)}
#world{position:absolute;left:0;top:0;width:0;height:0;transform-origin:0 0}
#fx{position:absolute;left:0;top:0;overflow:visible}
.sh{position:absolute;left:0;top:0;will-change:transform,width,height;transform-origin:center}
.sh-bg{position:absolute;inset:0;border-radius:inherit;background:#fff;box-shadow:var(--shadow-layered)}
.sh-orb{position:absolute;inset:0;border-radius:inherit;background:var(--orb);opacity:0;box-shadow:0 14px 40px rgba(23,137,242,.35)}
.sh-ring{position:absolute;inset:0;border-radius:inherit;pointer-events:none}
.sh-clip{position:absolute;inset:0;border-radius:inherit;overflow:hidden}
.sh-content,.sh-content2{position:absolute;left:50%;top:50%;transform-origin:center}
.sh-face{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);opacity:0}
.sh-dot{position:absolute;left:50%;top:50%;border-radius:50%;background:#fff;transform:translate(-50%,-50%)}
.sh-content .hd-window,.sh-content .hd-minidash{box-shadow:none}
.is-phone .hd-phone--light{box-shadow:inset 0 0 0 2px var(--line)}
/* lock screen: wallpaper, big clock, a few calm notifications */
.a1-lock{position:relative;background:#0b0c0e;color:#fff}
.a1-wall{position:absolute;left:0;right:0;top:-3.2em;bottom:0;width:100%;height:calc(100% + 3.2em)}
.a1-date{position:relative;text-align:center;font-size:1.05em;font-weight:600;color:rgba(255,255,255,.85);margin-top:.9em}
.a1-clock{position:relative;text-align:center;font-family:'Inter',var(--font);font-weight:600;font-size:5.6em;line-height:1;letter-spacing:-.03em;color:rgba(255,255,255,.92);margin-top:.05em}
.a1-feed{position:relative;flex:1;margin:1.6em .75em 0;overflow:hidden}
.a1-nt{position:absolute;left:0;right:0;top:0;display:flex;gap:.7em;align-items:center;background:rgba(245,246,248,.82);backdrop-filter:blur(14px);border-radius:1.15em;padding:.7em .85em;box-shadow:0 .3em 1.2em rgba(0,0,0,.25);will-change:transform,opacity}
.a1-nt__ic{width:2.4em;height:2.4em;border-radius:.65em;color:#fff;display:flex;align-items:center;justify-content:center;flex:none}
.a1-nt__m{flex:1;min-width:0}
.a1-nt__top{display:flex;justify-content:space-between;align-items:baseline;gap:.5em}
.a1-nt__top b{font-size:.95em;font-weight:700;color:#111;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.a1-nt__top span{font-size:.72em;font-weight:600;color:#6b7280;flex:none}
.a1-nt__s{font-size:.86em;color:#2b2f36;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-top:.1em}
.a1-dock{position:relative;display:flex;justify-content:space-between;padding:0 2.3em 2.5em}
.a1-dock span{width:3em;height:3em;border-radius:50%;background:rgba(255,255,255,.14);backdrop-filter:blur(10px);color:#fff;display:flex;align-items:center;justify-content:center}
/* notif stack */
.a1-nstack{position:relative;width:440px;height:330px}
.a1-n{position:absolute;left:10px;top:10px;width:420px}
/* queue */
.a1-queue{width:900px;padding:8px 4px}
.a1-queue .hd-queue__dots{gap:8px}
/* skeleton screen */
.a1-skel{flex:1;padding:.9em 1.1em 2.2em;display:flex;flex-direction:column;gap:.85em}
.a1-skel i,.a1-skel b{display:block;border-radius:8px;background:var(--sk-tint,var(--tint))}
.sk-top{display:flex;gap:.6em}.sk-top i{height:1.4em}
.sk-hero{height:9em;border-radius:1.3em;background:linear-gradient(90deg,var(--sk-g1,#1789f2),var(--sk-g2,#3fd4f6));opacity:.85}
.sk-row{display:flex;gap:.75em;align-items:center;padding:.75em;border-radius:1em;box-shadow:0 0 0 1px var(--sk-line,var(--line))}
.sk-row b{width:2.4em;height:2.4em;border-radius:50%;flex:none}.sk-row i{height:.9em;flex:1}
.sk-btn{margin-top:auto;height:3.1em;border-radius:999px;background:linear-gradient(90deg,var(--sk-g1,#1789f2),var(--sk-g2,#3fd4f6))}
.sh-content2 .hd-ip__screen{background:var(--sk-bg,#fff)}
/* text */
#txt{position:absolute;inset:0;pointer-events:none}
#scrim{position:absolute;left:0;right:0;bottom:0;height:300px;background:linear-gradient(rgba(255,255,255,0),rgba(255,255,255,.92) 55%,#fff);opacity:0}
.tb{position:absolute}
.tb .hd-headline{font-size:60px}
.tb .w{display:inline-block;will-change:transform,opacity,filter}
.t-left{left:150px;top:50%;transform:translateY(-50%);width:660px}
.t-bottom{left:120px;right:120px;bottom:92px;text-align:center}
.t-big .hd-headline{font-size:76px;letter-spacing:-1.4px}
.t-big em{font-weight:800}
/* controls (not part of the film) */
#ctl{position:fixed;left:50%;bottom:18px;transform:translateX(-50%);display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.92);backdrop-filter:blur(10px);
  border-radius:999px;padding:8px 18px 8px 8px;box-shadow:0 10px 30px rgba(1,43,68,.14);font:600 13px var(--font);color:var(--navy);transition:opacity .3s;z-index:10}
#ctl.hide{opacity:0}
#ctl button{width:38px;height:38px;border-radius:50%;border:0;background:var(--grad);color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center}
#ctl .bar{position:relative;width:min(520px,34vw);height:30px;display:flex;align-items:center}
#ctl input{width:100%;accent-color:#139bf5;margin:0}
#ctl .mk{position:absolute;top:-6px;font-size:11px;font-weight:800;color:var(--blue);transform:translateX(-50%)}
#ctl .tc{min-width:92px;font-variant-numeric:tabular-nums}
#ctl select{border:0;background:var(--tint);border-radius:999px;padding:6px 8px;font:inherit;color:inherit}
#ctl label{display:flex;align-items:center;gap:6px}
#ctl .tc{white-space:nowrap}
#ctl .tb2{white-space:nowrap;width:auto;height:34px;border-radius:999px;padding:0 14px;font:700 13px var(--font);background:var(--tint);color:var(--navy)}
#ctl .tb2.on{background:var(--grad);color:#fff}
body.editing #stage *{pointer-events:auto!important}
body.editing [data-ed]{cursor:text}
#edpop{display:none;position:fixed;z-index:20;width:440px;background:#fff;border-radius:16px;padding:14px;box-shadow:0 18px 50px rgba(1,43,68,.25);font:600 13px var(--font);color:var(--navy)}
#edpop .eh{font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:var(--blue);margin-bottom:8px}
#edpop textarea{width:100%;box-sizing:border-box;border:2px solid var(--line);border-radius:10px;padding:10px;font:600 16px var(--font);color:var(--navy);resize:vertical}
#edpop textarea:focus{outline:none;border-color:#139bf5}
#edpop .ef{display:flex;align-items:center;gap:8px;margin-top:10px}#edpop .ef span{flex:1;font-size:11px;color:var(--muted);font-weight:600}
#edpop button{border:0;border-radius:999px;padding:8px 16px;font:700 13px var(--font);cursor:pointer;background:var(--tint);color:var(--navy)}#edpop #edS{background:var(--grad);color:#fff}
#edtip{display:none;position:fixed;top:14px;left:50%;transform:translateX(-50%);z-index:15;background:var(--navy);color:#fff;font:700 13px var(--font);padding:8px 16px;border-radius:999px}
body.editing #edtip{display:block}
#brandP{display:none;position:fixed;right:16px;top:16px;z-index:16;background:#fff;border-radius:16px;padding:12px 14px;box-shadow:0 18px 50px rgba(1,43,68,.22);font:600 13px var(--font);color:var(--navy);flex-direction:column;gap:8px;min-width:220px}
body.editing #brandP{display:flex}
#brandP .bk{font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:var(--blue)}
#brandP label{display:flex;align-items:center;gap:10px;cursor:pointer}#brandP input{width:34px;height:34px;border:0;padding:0;background:none;cursor:pointer}
#brandP span{display:flex;flex-direction:column}#brandP i{font-style:normal;font-size:11px;color:var(--muted);font-weight:600}
#brandP button{align-self:flex-start;border:0;border-radius:999px;padding:6px 12px;font:700 12px var(--font);background:var(--tint);color:var(--navy);cursor:pointer}
'''

JS=r'''
const DUR=115;
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];

/* ---------- text edits: capture source + apply saved edits before anything reads the DOM ---------- */
const SCR_O='<scr'+'ipt',SCR_C='</scr'+'ipt>',ED_TAG=SCR_O+' id="hd-edits">';
const __SRC='<!DOCTYPE html>\n'+document.documentElement.outerHTML.replace(new RegExp(ED_TAG+'[\\s\\S]*?'+SCR_C),'');
const ED=Object.assign({h:{},s:{},j:{},brand:{}},window.__EDITS||{}),EXPORTED=!!window.__EXPORT;
__BRANDJS__
applyBrand();
const directTN=e=>[...e.childNodes].filter(n=>n.nodeType===3&&n.nodeValue.trim());
const isCand=e=>!e.closest('script,style,defs,.tb')&&directTN(e).length>0;
const ID_EL={},ID_HOME={};document.querySelectorAll('#txt .tb [id]').forEach(e=>{ID_EL[e.id]=e;ID_HOME[e.id]=e.closest('.tb').id});
function hlSer(n){let o='';n.childNodes.forEach(c=>{if(c.nodeType===3)o+=c.nodeValue;else if(c.id)o+='[['+c.id+']]';else if(c.tagName==='EM')o+='*'+hlSer(c)+'*';else o+=hlSer(c)});return o}
const hlGet=h=>[...h.querySelectorAll(':scope>.w')].map(hlSer).join(' ');
function hlSet(h,txt){h.innerHTML='';txt.trim().split(/\s+/).forEach((tok,i)=>{if(i)h.appendChild(document.createTextNode(' '));
  const w=document.createElement('span');w.className='w';let host=w;const m=tok.match(/^\*(.+)\*$/);if(m){host=document.createElement('em');w.appendChild(host);tok=m[1]}
  tok.split(/(\[\[[\w-]+\]\])/).forEach(part=>{if(!part)return;const id=part.match(/^\[\[([\w-]+)\]\]$/);host.appendChild(id&&ID_EL[id[1]]&&ID_HOME[id[1]]===h.closest('.tb').id?ID_EL[id[1]]:document.createTextNode(part))});h.appendChild(w)})}
const setTN=(e,vals)=>directTN(e).forEach((n,i)=>{if(vals[i]!=null)n.nodeValue=vals[i]});
for(const id in ED.h){const h=document.querySelector('#'+id+' .hd-headline');if(h)hlSet(h,ED.h[id])}
const SCAND=[...document.querySelectorAll('#stage *')].filter(isCand);
SCAND.forEach((e,i)=>{if(ED.s[i])setTN(e,ED.s[i]);e.dataset.ed='s'+i});
document.querySelectorAll('#txt .tb').forEach(b=>b.querySelector('.hd-headline').dataset.ed='h'+b.id);
const clamp=(v,a=0,b=1)=>Math.min(b,Math.max(a,v)), lerp=(a,b,p)=>a+(b-a)*p;
function bez(x1,y1,x2,y2){const cx=3*x1,bx=3*(x2-x1)-cx,ax=1-cx-bx,cy=3*y1,by=3*(y2-y1)-cy,ay=1-cy-by;
  const X=t=>((ax*t+bx)*t+cx)*t,Y=t=>((ay*t+by)*t+cy)*t,dX=t=>(3*ax*t+2*bx)*t+cx;
  return x=>{if(x<=0)return 0;if(x>=1)return 1;let t=x;for(let i=0;i<8;i++){const d=dX(t);if(Math.abs(d)<1e-6)break;t-=(X(t)-x)/d}return Y(clamp(t))}}
function springF(z,w){const wd=w*Math.sqrt(1-z*z);return p=>{if(p<=0)return 0;if(p>=1)return 1;
  const v=1-Math.exp(-z*w*p)*(Math.cos(wd*p)+z*w/wd*Math.sin(wd*p));return v+(1-v)*Math.pow(p,6)}}
/* easing = design-system motion tokens */
const EZ={lin:x=>x,out:bez(.22,1,.36,1),in:bez(.55,0,1,.45),io:bez(.65,0,.35,1),spring:springF(.5,12),soft:springF(.78,10)};
const P=(t,t0,d,e=EZ.out)=>e(clamp((t-t0)/d));
const nz=(s,t)=>Math.sin(t*13.1+s*7.3)*.5+Math.sin(t*23.7+s*3.1)*.3+Math.sin(t*7.9+s*11)*.2;
const bump=(t,t0,d)=>{const p=(t-t0)/d;return p>0&&p<1?Math.sin(p*Math.PI):0};

/* ---------- timing (seconds) ---------- */
const FREEZE=9.75, LIFT0=10.25, MORPH0=11.0, LINK0=11.85, FIRE=12.7, CONTRACT=14.7, TOPHONE=15.25;
const NODE=132, CORE=220, PW=360, PH=360*1940/950, PR=157*360/950, EW=300, EH=300*1940/950, ER=157*300/950;
const CFG=__SHELLS__, TXT=__TEXTS__;
const ORDER=['notifs','sheet','md0','md3','md1','md2','md4','queue'];
CFG.forEach(c=>{c.appear=4.95+ORDER.indexOf(c.id)*.14});

/* ---------- camera ---------- */
function cam(t){const c=cam1(t);if(t>16){c.z*=lerp(1,1.05,P(t,16.4,9.6,EZ.lin));c.cy=lerp(c.cy,-56,P(t,16.3,1.1,EZ.io));c.z=lerp(c.z,1.05,P(t,26.3,1.2,EZ.io));c.cy=lerp(c.cy,HY,P(t,26.3,1.2,EZ.io));c.cx+=70*P(t,33,1,EZ.in);c.z*=1+.04*P(t,33,1,EZ.in)}return camA5(t,camA4(t,camA3(t,c)))}
function cam1(t){
  const z = t<5.4 ? (t<4.3? lerp(1.12,1.19,P(t,1.2,3.1,EZ.lin)) : lerp(1.19,.6,P(t,4.3,1.1,EZ.io)))
          : t<11 ? lerp(.6,.63,P(t,5.4,4.3,EZ.lin))
          : t<14.6 ? lerp(.63,.8,P(t,11,1.5,EZ.io))+ .03*P(t,12.5,2.1,EZ.lin)
          : lerp(.83,.95,P(t,14.6,1.4,EZ.io));
  const cx = t<4.3 ? lerp(0,-300,P(t,.85,.9,EZ.soft)) : lerp(-300,0,P(t,4.3,1.1,EZ.io));
  const cy = lerp(0,-30,P(t,11,1.4,EZ.io)) + lerp(0,74,P(t,TOPHONE,.75,EZ.io));
  return {z,cx,cy};
}

/* ---------- network layout ---------- */
const RX=640, RY=340, NC={x:0,y:-30};
(function assign(){
  const els=CFG.map(c=>({c,a:Math.atan2(c.y,c.x)})).sort((a,b)=>a.a-b.a);
  const slots=[...Array(8)].map((_,k)=>{const a=-Math.PI/2+Math.PI/8+k*Math.PI/4;return {x:NC.x+RX*Math.cos(a),y:NC.y+RY*Math.sin(a),a:Math.atan2(Math.sin(a),Math.cos(a))}}).sort((a,b)=>a.a-b.a);
  let best=1e18,bo=0;for(let o=0;o<8;o++){let s=0;els.forEach((e,i)=>{const n=slots[(i+o)%8];s+=Math.hypot(n.x-e.c.x,n.y-e.c.y)});if(s<best){best=s;bo=o}}
  els.forEach((e,i)=>{const n=slots[(i+bo)%8];e.c.nx=n.x;e.c.ny=n.y;e.c.na=n.a});
  CFG.sort((a,b)=>a.na-b.na); CFG.forEach((c,i)=>c.ring=i);
})();

/* ---------- state functions (pure in t) ---------- */
function phoneState(t){
  const st={x:0,y:0,rot:0,s:1,w:56,h:56,r:28,orb:1,cop:0,cb:12,c2:0,dot:1,bg:1,sat:1,ring:0,ringA:0};
  st.s=P(t,0,.55,EZ.spring);
  const d=P(t,.35,.85,EZ.soft);
  st.w=lerp(56,PW,d);st.h=lerp(56,PH,d);st.r=lerp(28,PR,d);
  st.orb=1-P(t,.38,.3,EZ.lin);st.dot=1-P(t,.35,.25,EZ.lin);
  const ci=P(t,.55,.5,EZ.out);st.cop=ci;st.cb=12*(1-ci);
  // ping buzz
  NTT.forEach(b=>{const k=t-b;if(k>0&&k<.45)st.rot+=1.6*Math.exp(-k*9)*Math.sin(k*70)});
  // idle soft ripple, scene 1
  if(t>1.8&&t<4.3){const ph=((t-1.8)%1.6)/1.6;st.ring=70*EZ.out(ph);st.ringA=.14*Math.pow(1-ph,1.6)}
  // pile jitter
  const ja=clamp((t-5.6)/.4)*(t<FREEZE?1:0);st.x+=ja*2*nz(21,t);st.y+=ja*2*nz(22,t);st.rot+=ja*.4*nz(23,t);
  // freeze -> grey -> light up
  satRipple(st,t,LIFT0);
  // morph to core
  const m=P(t,MORPH0,.9,EZ.soft);
  st.w=lerp(st.w,CORE,m);st.h=lerp(st.h,CORE,m);st.r=lerp(st.r,CORE/2,m);
  st.x=lerp(st.x,NC.x,P(t,MORPH0,1,EZ.soft));st.y=lerp(st.y,NC.y,P(t,MORPH0,1,EZ.soft));st.rot*=1-m;
  const co=P(t,MORPH0,.32,EZ.in);st.cop*=1-co;st.cb+=10*co;
  st.orb=Math.max(st.orb,P(t,MORPH0+.1,.5,EZ.out));st.dot=Math.max(st.dot,P(t,MORPH0+.35,.4,EZ.out));
  // core heartbeat
  st.s*=1+.07*bump(t,13.3,.45)+.04*bump(t,13.9,.4)+.04*bump(t,14.8,.4)+.06*bump(t,15.05,.35);
  // core -> phone screen
  const e=P(t,TOPHONE,.75,EZ.soft);
  if(t>TOPHONE){st.w=lerp(CORE,EW,e);st.h=lerp(CORE,EH,e);st.r=lerp(CORE/2,ER,e);st.orb*=1-P(t,TOPHONE,.45,EZ.lin);st.dot*=1-P(t,TOPHONE,.25,EZ.lin);
    const c2=P(t,TOPHONE+.3,.5,EZ.out);st.c2=c2;st.c2b=8*(1-c2)}
  st.op=1-P(t,16.05,.25,EZ.lin);
  st.bg=Math.max(0,(1-st.cop))*(1-(st.c2||0));
  return st;
}
function satRipple(st,t,L){
  if(t>=FREEZE){const g=P(t,FREEZE,.12,EZ.lin);const back=P(t,L,.5,EZ.out);st.sat=lerp(1,lerp(.12,1,back),g)}
  const rp=clamp((t-L)/.8);if(rp>0&&rp<1){st.ring=46*EZ.out(rp);st.ringA=.35*(1-rp)}
  const lift=P(t,L,.45,EZ.out)*(1-P(t,MORPH0,.6,EZ.out));st.s*=1+.05*lift;st.y-=12*lift;st.lift=lift;
}
function shellState(c,i,t){
  const a=c.appear, st={sat:1,ring:0,ringA:0,bg:c.tr?0:1,orb:0,dot:0,c2:0};
  const p=P(t,a,.95,EZ.soft);
  st.x=lerp(0,c.x,p);st.y=lerp(0,c.y,p);st.rot=lerp(0,c.rot,p);
  st.s=lerp(.3,1,P(t,a,.75,EZ.spring));st.op=clamp((t-a)/.22);
  st.w=c.w;st.h=c.h;st.r=c.r;st.cop=1;st.cb=0;st.fop=0;st.fb=8;
  const ja=clamp((t-a-.6)/.4)*(t<FREEZE?1:0);
  st.x+=ja*4*nz(i,t);st.y+=ja*4*nz(i+5,t*1.1);st.rot+=ja*.8*nz(i+9,t*.9);
  if(c.id==='notifs')NB.forEach(b=>{const k=t-b;if(k>0&&k<.5)st.x+=8*Math.exp(-k*8)*Math.sin(k*62)});
  const L=LIFT0+(i+1)*.07; satRipple(st,t,L);
  const M=MORPH0+(i+1)*.05, m=P(t,M,1.0,EZ.soft), ms=P(t,M,.8,EZ.soft);
  st.x=lerp(st.x,c.nx,m);st.y=lerp(st.y,c.ny,m);st.rot=lerp(st.rot,0,m);
  st.w=lerp(c.w,NODE,ms);st.h=lerp(c.h,NODE,ms);st.r=lerp(c.r,NODE/2,ms);
  st.bg=Math.max(st.bg,P(t,M,.35,EZ.out));
  const co=P(t,M,.3,EZ.in);st.cop=1-co;st.cb=10*co;
  st.fop=P(t,M+.32,.4,EZ.out);st.fb=8*(1-st.fop);
  st.s*=1+.06*bump(t,FIRE+.55,.4);
  // contract
  const C=CONTRACT+c.ring*.03, k=P(t,C,.7,EZ.in);
  st.x=lerp(st.x,NC.x,k);st.y=lerp(st.y,NC.y,k);st.s*=lerp(1,.25,k);st.op*=1-P(t,C+.45,.25,EZ.lin);
  return st;
}
const NB=[5.0,6.1,6.9,7.6,8.4]; // notification arrivals

/* ---------- DOM ---------- */
const stage=$('#stage'),world=$('#world'),fx=$('#fx');
const SH={};CFG.forEach(c=>{const el=$('#sh-'+c.id);const ct=el.querySelector('.sh-content');
  c.w=ct.offsetWidth*c.k;c.h=ct.offsetHeight*c.k;ct.style.transform=`translate(-50%,-50%) scale(${c.k})`;SH[c.id]={el,ct,bg:el.querySelector('.sh-bg'),orb:el.querySelector('.sh-orb'),ring:el.querySelector('.sh-ring'),face:el.querySelector('.sh-face')}});
const PH_={el:$('#sh-phone')};['bg','orb','ring'].forEach(k=>PH_[k]=PH_.el.querySelector('.sh-'+k));
PH_.ct=PH_.el.querySelector('.sh-content');PH_.c2=PH_.el.querySelector('.sh-content2');PH_.dot=PH_.el.querySelector('.sh-dot');
PH_.ct.style.transform='translate(-50%,-50%)';
const NS='http://www.w3.org/2000/svg';const mk=(tag,at)=>{const e=document.createElementNS(NS,tag);for(const k in at)e.setAttribute(k,at[k]);fx.appendChild(e);return e};
const halo=mk('circle',{fill:'#eef7fd'});
const ringL=CFG.map(()=>mk('line',{stroke:'#8fcdf8','stroke-width':3,'stroke-dasharray':'2 10','stroke-linecap':'round'}));
const coreRip=[0,1,2,3,4,5].map(()=>mk('circle',{fill:'#139bf5'}));
const nodeRip=CFG.map(()=>[mk('circle',{fill:'#139bf5'}),mk('circle',{fill:'#139bf5'})]);
const links=CFG.map(()=>mk('line',{stroke:'#139bf5','stroke-width':3.5,'stroke-linecap':'round',pathLength:1,'stroke-dasharray':1}));
const packets=CFG.map(()=>mk('circle',{r:8,fill:'#3fd4f6',stroke:'#fff','stroke-width':3}));
const dotRip=mk('circle',{fill:'#139bf5'});
/* blue -> Habuild green hand-off on the skeleton phone (15.45-16.0s) */
const mixH=(a,b,p)=>{const f=h=>[1,3,5].map(i=>parseInt(h.slice(i,i+2),16)),A=f(a),B=f(b);return '#'+A.map((v,i)=>Math.round(v+(B[i]-v)*p).toString(16).padStart(2,'0')).join('')};
const SKC=$('#sh-phone .sh-content2');let skLast=-1;
function skelTint(t){const p=P(t,15.3,.6,EZ.io)*(t<17?1:0);if(p===skLast)return;skLast=p;const v=SKC.style;
  const A=ACC.partner1;v.setProperty('--sk-g1',mixH('#1789f2',A.base,p));v.setProperty('--sk-g2',mixH('#3fd4f6',A.light,p));
  v.setProperty('--sk-tint',mixH('#eef7fd',A.tint,p));v.setProperty('--sk-line',mixH('#d6e7f4',A.line,p));v.setProperty('--sk-bg',mixH('#ffffff','#faf8f3',p));
  coreRip.forEach(c=>c.setAttribute('fill',t<17?mixH('#139bf5',ACC.partner1.base,p):'#139bf5'))}

function applyShell(o,st,prev,isPhone){
  const v=prev?Math.hypot(st.x-prev.x,st.y-prev.y):0, mb=clamp(v*.14,0,9);
  o.el.style.width=st.w+'px';o.el.style.height=st.h+'px';o.el.style.borderRadius=st.r+'px';
  o.el.style.transform=`translate(${st.x}px,${st.y}px) translate(-50%,-50%) rotate(${st.rot}deg) scale(${st.s})`;
  o.el.style.opacity=st.op==null?1:st.op;
  const f=[];if(mb>.3)f.push(`blur(${mb.toFixed(2)}px)`);if(st.sat<.995)f.push(`saturate(${st.sat.toFixed(3)})`);o.el.style.filter=f.length?f.join(' '):'none';
  o.bg.style.opacity=st.bg;o.orb.style.opacity=st.orb;
  o.ring.style.boxShadow=st.ringA>0.002?`0 0 0 ${st.ring}px rgba(${st.ringRGB||'19,155,245'},${st.ringA})`:'none';
  o.ct.style.opacity=st.cop;o.ct.style.filter=st.cb>.2?`blur(${st.cb}px)`:'none';
  if(o.face){o.face.style.opacity=st.fop;o.face.style.filter=st.fb>.2?`blur(${st.fb}px)`:'none';o.face.style.transform=`translate(-50%,-50%) scale(${.7+.3*st.fop})`}
  if(isPhone){const ds=st.w*.26;o.dot.style.width=o.dot.style.height=ds+'px';o.dot.style.opacity=st.dot;
    o.c2.style.opacity=st.c2;o.c2.style.filter=st.c2b>.2?`blur(${st.c2b}px)`:'none';o.c2.style.transform=`translate(-50%,-50%) scale(${st.w/EW})`;
    o.ct.style.transform=`translate(-50%,-50%) scale(${clamp(st.w/PW,.3,1)})`}
}

/* phone screen: notifications arrive one by one, newest on top, older ones slide down */
const NT=$$('#a1feed .a1-nt'),NTT=__NTT__,NSTEP=4.4; // em per card slot
function phoneScreen(t){
  NT.forEach((el,i)=>{const a=NTT[i];if(t<a-.02){el.style.opacity=0;return}
    let off=0;for(let j=i+1;j<NTT.length;j++)off+=P(t,NTT[j],.5,EZ.soft);
    const e=P(t,a,.55,EZ.spring);
    el.style.transform=`translateY(${off*NSTEP-(1-e)*2.2}em) scale(${.94+.06*e})`;el.style.opacity=clamp((t-a)/.15);el.style.zIndex=100+i;
    const bl=(1-P(t,a,.3))*8;el.style.filter=bl>.2?`blur(${bl}px)`:'none'});
}
/* chaos internals */
const nCards=$$('.a1-n');
function notifStack(t){
  nCards.forEach((el,i)=>{const a=NB[i];const vis=clamp((t-a)/.18);let off=0,n=0;
    for(let j=i+1;j<NB.length;j++){const q=P(t,NB[j],.55,EZ.spring);off+=72*q;n+=q}
    const e=P(t,a,.55,EZ.spring);
    el.style.transform=`translateY(${off-(1-e)*40}px) scale(${1-.04*n})`;el.style.opacity=vis*clamp(1-.22*n)*(n>3.2?0:1);el.style.zIndex=10+i;
    el.style.filter=t-a<.3&&t>a?`blur(${(1-P(t,a,.3))*8}px)`:'none'});
}
const qd=$$('#a1q i'),qn=$('#a1qn');
function queueRow(t,a){
  qd.forEach((d,k)=>{const at=a+.25+k*.15;const s=P(t,at,.4,EZ.spring);d.style.transform=`scale(${s})`;d.style.opacity=clamp((t-at)/.1)});
  const shown=qd.filter((d,k)=>t>=a+.25+k*.15).length;qn.textContent=`${16+shown*2} waiting · avg ${20+shown} min`;
}
const mdv=CFG.filter(c=>c.id.startsWith('md')).map(c=>{const e=$('#sh-'+c.id+' .hd-minidash__v');return {e,o:e.textContent,a:c.appear}});
function hash(n){n=Math.sin(n*127.1)*43758.5453;return n-Math.floor(n)}
function scramble(t){mdv.forEach((m,i)=>{if(t<m.a+.4||t>=FREEZE){m.e.textContent=m.o;return}
  const f=Math.floor(t*14);m.e.textContent=m.o.replace(/\d/g,(d,j)=>hash(f*13+i*7+j)<.45?String(Math.floor(hash(f+i+j*3)*10)):d)})}
const errs=$$('#sh-sheet .e, #sh-sheet .r');
function sheetFlash(t){const on=t>5.4&&t<FREEZE;errs.forEach((e,i)=>{e.style.opacity=on?.55+.45*Math.abs(Math.sin(t*5+i)):1})}

/* text */
const TB=TXT.map(o=>({...o,ws:$$('#'+o.id+' .w')}));
function texts(t){TB.forEach(b=>{b.ws.forEach((w,j)=>{const p=P(t,b.in+j*.06,.6,EZ.out),q=P(t,b.out+j*.03,.4,EZ.in);
  const y=24*(1-p)-16*q,op=p*(1-q),bl=8*(1-p)+8*q;w.style.transform=`translateY(${y}px)`;w.style.opacity=op;w.style.filter=bl>.2?`blur(${bl}px)`:'none'})})}

/* fx layer */
function setC(c,x,y,r,op){c.setAttribute('cx',x);c.setAttribute('cy',y);c.setAttribute('r',Math.max(0,r));c.setAttribute('opacity',op)}
function setL(l,x1,y1,x2,y2){l.setAttribute('x1',x1);l.setAttribute('y1',y1);l.setAttribute('x2',x2);l.setAttribute('y2',y2)}
function fxLayer(t,ps,ss){
  {const rp=clamp((t-.05)/.8);setC(dotRip,0,0,28+70*EZ.out(rp),rp>0&&rp<1?.35*(1-rp):0)}
  skelTint(t);
  setC(halo,ps.x,ps.y,ps.w/2*ps.s+20,ps.orb*(ps.w<CORE+40?1:0)*(1-P(t,TOPHONE,.3,EZ.lin)));
  const cr=[FIRE,FIRE+.35,13.9,14.8,99,99];
  coreRip.forEach((c,k)=>{const rp=clamp((t-cr[k])/1.2);setC(c,ps.x,ps.y,CORE/2*ps.s+190*EZ.out(rp),rp>0&&rp<1?.2*(1-rp):0)});
  CFG.forEach((c,i)=>{const s=ss[i];const nr=NODE/2*s.s;
    const dx=s.x-ps.x,dy=s.y-ps.y,D=Math.hypot(dx,dy)||1,ux=dx/D,uy=dy/D,cr=CORE/2*ps.s+6;
    const lp=P(t,LINK0+c.ring*.05,.55,EZ.out)*(t<CONTRACT+.9?1:0);
    setL(links[i],ps.x+ux*cr,ps.y+uy*cr,s.x-ux*(nr+6),s.y-uy*(nr+6));
    links[i].setAttribute('stroke-dashoffset',1-lp);links[i].setAttribute('opacity',D>cr+nr+8?1:0);
    const j=CFG.findIndex(o=>o.ring===(c.ring+1)%8),s2=ss[j];
    setL(ringL[c.ring],s.x,s.y,s2.x,s2.y);ringL[c.ring].setAttribute('opacity',P(t,12.2+c.ring*.04,.4)*(1-P(t,CONTRACT-.1,.3,EZ.lin))*.9);
    [FIRE,FIRE+.6].forEach((w,k)=>{const rp=clamp((t-w-c.ring*.015)/1);setC(nodeRip[i][k],s.x,s.y,nr+52*EZ.out(rp),rp>0&&rp<1?.24*(1-rp):0)});
    const pk=P(t,FIRE+.05+c.ring*.02,.6,EZ.io);const pv=pk>0&&pk<1;
    setC(packets[i],lerp(s.x-ux*nr,ps.x+ux*cr,pk),lerp(s.y-uy*nr,ps.y+uy*cr,pk),8,pv?1:0);
  });
}

/* ---------- render ---------- */
let prevStates=null;
function render(t){
  const c=cam(t);world.style.transform=`translate(960px,540px) scale(${c.z}) translate(${-c.cx}px,${-c.cy}px)`;
  const ps=phoneState(t),pp=phoneState(t-1/60);
  const ss=CFG.map((cf,i)=>shellState(cf,i,t)),sp=CFG.map((cf,i)=>shellState(cf,i,t-1/60));
  applyShell(PH_,ps,pp,true);CFG.forEach((cf,i)=>applyShell(SH[cf.id],ss[i],sp[i],false));
  phoneScreen(t);notifStack(t);queueRow(t,CFG.find(c=>c.id==='queue').appear);scramble(t);sheetFlash(t);
  fxLayer(t,ps,ss);texts(t);act2(t);act3(t);act4(t);act5(t);
  $('#scrim').style.opacity=P(t,5.2,.6)*(1-P(t,TOPHONE+.2,.6))+P(t,TOPHONE+.2,.6)*.0;
}

__JS2__
/* ---------- player ---------- */
let T=0,playing=true,last=null,speed=1,loop=true;
const range=$('#seek'),tc=$('#tc'),pb=$('#pp');
function fit(){const k=Math.min(innerWidth/1920,innerHeight/1080);stage.style.transform=`translate(${(innerWidth-1920*k)/2}px,${(innerHeight-1080*k)/2}px) scale(${k})`}
addEventListener('resize',fit);fit();
function setT(v){T=clamp(v,0,DUR);render(T);range.value=T;tc.textContent=T.toFixed(2).padStart(5,'0')+' / '+DUR.toFixed(2);}
function frame(now){if(last==null)last=now;const dt=(now-last)/1000;last=now;
  if(playing){let n=T+dt*speed;if(n>=DUR){if(loop)n=0;else{n=DUR;playing=false;icon()}}setT(n)}requestAnimationFrame(frame)}
function icon(){pb.innerHTML=playing?'<svg width="14" height="14" viewBox="0 0 14 14"><rect x="2" y="1" width="3.5" height="12" rx="1" fill="#fff"/><rect x="8.5" y="1" width="3.5" height="12" rx="1" fill="#fff"/></svg>':'<svg width="14" height="14" viewBox="0 0 14 14"><path d="M3 1.5v11l9-5.5z" fill="#fff"/></svg>'}
pb.onclick=()=>{playing=!playing;if(playing&&T>=DUR)T=0;icon()};
range.oninput=()=>{playing=false;icon();setT(+range.value)};
$('#spd').onchange=e=>speed=+e.target.value;$('#lp').onchange=e=>loop=e.target.checked;
addEventListener('keydown',e=>{if(e.target.closest&&e.target.closest('textarea,input'))return;if(e.code==='Space'){e.preventDefault();pb.click()}
  if(e.key==='ArrowRight'){playing=false;icon();setT(T+(e.shiftKey?1:1/30))}
  if(e.key==='ArrowLeft'){playing=false;icon();setT(T-(e.shiftKey?1:1/30))}
  if(e.key==='r'||e.key==='R'){setT(0);playing=true;icon()}
  if(e.key==='h'||e.key==='H')$('#ctl').classList.toggle('hidden-forever')});
let idle;addEventListener('mousemove',()=>{$('#ctl').classList.remove('hide');clearTimeout(idle);idle=setTimeout(()=>$('#ctl').classList.add('hide'),2200)});
const q=new URLSearchParams(location.search);if(q.has('t')){T=+q.get('t');playing=q.get('play')==='1'}
window.__render=t=>{playing=false;setT(t)}; // hook for frame capture later
icon();setT(T);document.fonts&&document.fonts.ready.then(()=>{CFG.forEach(c=>{const ct=SH[c.id].ct;c.w=ct.offsetWidth*c.k;c.h=ct.offsetHeight*c.k});setT(T)});

/* ---------- text editor · save · export ---------- */
(function(){
  // JS-built text (labels drawn by the animation) gets its own stable index
  const JC=[...document.querySelectorAll('#stage *')].filter(e=>isCand(e)&&!e.dataset.ed);
  JC.forEach((e,i)=>{if(ED.j[i])setTN(e,ED.j[i]);e.dataset.ed='j'+i});
  // anything the animation rewrites over time (counters, clocks) is not editable
  const all=[...document.querySelectorAll('[data-ed]')].filter(e=>e.dataset.ed[0]!=='h'),snap=()=>all.map(e=>directTN(e).map(n=>n.nodeValue).join('|'));
  const base=snap();[2,8,14,20,26,31,38,46,52,58,64,70,76,82,90,98,106,112].forEach(t=>{render(t);snap().forEach((v,i)=>{if(v!==base[i])all[i].dataset.dyn=1})});
  all.forEach(e=>{if(e.dataset.dyn)delete e.dataset.ed});render(T);
  const ctl=$('#ctl');
  if(EXPORTED){['#spd','#lp'].forEach(s=>{const e=$(s);(e.closest('label')||e).remove()});return}
  ctl.insertAdjacentHTML('beforeend','<button class="tb2" id="edB">Edit text</button><button class="tb2" id="svB">Save copy</button><button class="tb2" id="exB">Export</button>');
  document.body.insertAdjacentHTML('beforeend','<div id="edpop"><div class="eh" id="edH"></div><textarea id="edT" rows="2"></textarea><div class="ef"><span id="edN"></span><button id="edC">Cancel</button><button id="edS">Save</button></div></div><div id="edtip">Edit mode · click any text on screen · scrub to find it</div><div id="brandP"><div class="bk">Partner brand colours</div>'+PARTNERS.map(p=>`<label><input type="color" data-slot="${p.slot}" value="${ACC[p.slot].base}"><span><b>${p.name}</b><i>${p.section}</i></span></label>`).join('')+'<button id="brandR">Reset</button></div>');
  $$('#brandP input').forEach(inp=>inp.addEventListener('input',()=>{ED.brand[inp.dataset.slot]=inp.value;applyBrand();skLast=-1;render(T)}));
  $('#brandR').onclick=()=>{ED.brand={};applyBrand();skLast=-1;$$('#brandP input').forEach(i=>i.value=ACC[i.dataset.slot].base);render(T)};
  const edB=$('#edB'),pop=$('#edpop'),edT=$('#edT');let editing=false,cur=null;
  edB.onclick=()=>{editing=!editing;document.body.classList.toggle('editing',editing);edB.classList.toggle('on',editing);edB.textContent=editing?'Done editing':'Edit text';if(editing){playing=false;icon()}else pop.style.display='none'};
  const shown=e=>{if(e.dataset.ed[0]==='h'&&![...e.querySelectorAll('.w')].some(w=>+getComputedStyle(w).opacity>.05))return false;for(let n=e;n&&n.nodeType===1;n=n.parentNode){const c=getComputedStyle(n);if(c.display==='none'||c.visibility==='hidden'||+c.opacity<.05||n.getAttribute('opacity')==='0')return false}return true};
  addEventListener('click',ev=>{if(!editing||ev.target.closest('#ctl,#edpop'))return;
    const hit=document.elementsFromPoint(ev.clientX,ev.clientY).map(e=>e.closest('[data-ed]')).find(e=>e&&shown(e));if(!hit)return;
    ev.preventDefault();cur=hit;const k=hit.dataset.ed,isH=k[0]==='h';
    $('#edH').textContent=isH?'Headline':'Text';$('#edN').textContent=isH?'Wrap a word in *stars* to colour it. Keep [[…]] tags, they are live numbers.':(directTN(hit).length>1?'Parts are separated by ¦':'');
    edT.value=isH?hlGet(hit):directTN(hit).map(n=>n.nodeValue).join('¦');
    pop.style.display='block';const r=hit.getBoundingClientRect();pop.style.left=Math.max(12,Math.min(innerWidth-452,r.left))+'px';pop.style.top=(r.bottom+10+170>innerHeight?Math.max(12,r.top-180):r.bottom+10)+'px';edT.focus();edT.select()},true);
  function commit(){if(!cur)return;const k=cur.dataset.ed,v=edT.value;
    if(k[0]==='h'){const id=k.slice(1);hlSet(cur,v);ED.h[id]=v;const b=TB.find(b=>b.id===id);if(b)b.ws=$$('#'+id+' .w')}
    else{const vals=v.split('¦');setTN(cur,vals);ED[k[0]][k.slice(1)]=directTN(cur).map(n=>n.nodeValue)}
    pop.style.display='none';cur=null;render(T)}
  $('#edS').onclick=commit;$('#edC').onclick=()=>{pop.style.display='none';cur=null};
  edT.addEventListener('keydown',e=>{e.stopPropagation();if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();commit()}if(e.key==='Escape')$('#edC').click()});
  function download(exp){const js=JSON.stringify(ED).replace(/</g,'\\u003c');
    const html=__SRC.replace(SCR_O+'>',ED_TAG+'window.__EDITS='+js+';'+(exp?'window.__EXPORT=1;':'')+SCR_C+SCR_O+'>');
    const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([html],{type:'text/html'}));a.download=exp?'heydoc-film-export.html':'heydoc-film-edited.html';document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},1500)}
  $('#svB').onclick=()=>download(false);$('#exB').onclick=()=>download(true);
})();
requestAnimationFrame(frame);
'''
JS=JS.replace('__BRANDJS__',brand.DERIVE_JS.replace('__PARTNERS__',json.dumps(brand.PARTNERS)));
JS=JS.replace('__NTT__',json.dumps([n[4] for n in NOTES])).replace('__SHELLS__',shell_cfg).replace('__TEXTS__',text_cfg).replace('__JS2__',act2.JS2+act3.JS3+act4.JS4.replace('__MAHA__',json.dumps(MAHA_D))+act5.JS5.replace('__INDIA__',json.dumps(INDIA_D)).replace('__GLAND__',open('globe_land.json').read()))

markers=''.join(f'<span class="mk" style="left:{s/115*100:.2f}%">{n}</span>' for s,n in [(0,'1'),(5,'1b'),(10,'2'),(16,'3'),(27,'4'),(34,'5'),(44,'6'),(54,'7'),(65,'8'),(75,'9'),(84,'10'),(94,'11'),(104,'12')])
html=f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>HeyDoc Film</title>
<!-- HeyDoc AI explainer · Act 1 "Care that doesn't connect" (0–16s). Pure HTML/CSS/JS, deterministic: render(t) is a pure function of time.
     Components from the film element board (E-02, E-03, E-04, E-16, E-18). Controls: Space play/pause · ←/→ frame step (Shift = 1s) · R restart · H hide bar · ?t=10 to open at 10s -->
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Open+Sans:wght@300;400;600;700;800&display=swap" rel="stylesheet">
<style>{brand.root_css()}{CSS}{A1CSS}{iphone.CSS_IP}{act2.CSS2}{act3.CSS3}{act4.CSS4}{act5.CSS5}
.hidden-forever{{display:none!important}}</style></head>
<body>
<div id="viewport"><div id="stage">
  <div id="world"><svg id="fx" width="1" height="1"></svg>{shells}{act2.WORLD}{act3.WORLD}{act4.WORLD}{act5.WORLD}</div>
  <div id="txt"><div id="scrim"></div>{text_html}{act2.OVER}{act3.OVER}{act4.OVER}{act5.OVER}</div>
</div></div>
<div id="ctl"><button id="pp" aria-label="Play or pause"></button><div class="bar">{markers}<input id="seek" type="range" min="0" max="115" step="0.001" value="0"></div>
<span class="tc" id="tc">00.00</span><select id="spd"><option value="0.25">0.25×</option><option value="0.5">0.5×</option><option value="1" selected>1×</option></select>
<label><input type="checkbox" id="lp" checked>Loop</label></div>
<script>{JS}</script>
</body></html>'''
open('../film.html','w').write(html)
print(len(html))
