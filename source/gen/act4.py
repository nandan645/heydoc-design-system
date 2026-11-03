"""Act 4 · MAHA-PULSE AI (54–75s): scene 7 (54–65) Kolhapur live dashboard; scene 8 (65–75) camera tiles, amber alert, Maharashtra map + camera counter."""
from base import *
from s4 import kolhapur_map, legend_dot, DOT_TYPES

STATS=[('Hospitals live','214','hospital','sky'),('Patients today','18,420','patient','lav'),('Health camps','36','camp','mint'),('Ambulances on road','58','ambulance','sun')]
side=''.join(f'<div class="hd-stat a4-stat">{well(i,t,"60px")}<div><div class="hd-stat__k" style="font-size:12px">{k}</div><div class="hd-stat__v a4-cv" data-v="{v.replace(",","")}" style="font-size:44px;margin-top:2px">{v}</div></div></div>' for k,v,i,t in STATS)
legend=''.join(legend_dot(n,c) for n,c,_,_ in DOT_TYPES)
DASH=f'''<div class="a4-dash">
  <div class="a4-dh">
    <span class="hd-avatar-orb" style="width:42px;height:42px"><span style="width:12px;height:12px;border-radius:50%;background:#fff"></span></span>
    <span class="a4-brand">MAHA-PULSE</span><span class="a4-sub">Kolhapur district · live</span>
    <span class="hd-govbadge" style="margin-left:auto">{logo("maha","Seal of Maharashtra")}Government of Maharashtra</span>
    <span class="hd-tag" style="background:rgba(59,230,162,.15);color:var(--d-mint)"><i class="a4-live"></i>LIVE</span>
  </div>
  <div class="a4-body">
    <div><div class="a4-plate">{kolhapur_map()}</div><div class="a4-legend">{legend}</div></div>
    <div class="a4-side">{side}<div class="hd-mini a4-alert" id="a4alert">{ic("alert","22px")}Camp #12 needs 2 more staff</div></div>
  </div>
</div>'''

CAMS=[('OPD queue',[('queue','Queue <b>14</b>','')]),('Emergency',[('ambulance','Bay <b>2 of 4</b> free','ok')]),
      ('Pharmacy',[('queue','Queue <b>6</b>',''),('clock','Wait <b>9 min</b>','ok')]),('Lab collection',[('queue','Queue <b>21</b>','')]),
      ('ICU corridor',[('bed','ICU beds <b>91%</b>','')]),('Registration',[('queue','Queue <b>11</b>','')])]
ALERT_CAM=3
# live agent activity feed (fake data): (agent, icon, tone, text, chip, chip-kind)
FEED=[('Vision agent','camera','sky','Watching <b>6 feeds</b> at CPR Hospital','Scanning','sky'),
      ('Queue agent','queue','aqua','OPD queue <b>14</b>, inside normal range','Normal','ok'),
      ('Vision agent','camera','sky','Lab collection: <b>21 waiting</b>, avg wait <b>42 min</b>','Issue','amber'),
      ('Ops agent','agent','lav','Roster check: <b>2 staff</b> free in Pharmacy','Planning','sky'),
      ('Ops agent','bell','lav','Moved 2 staff to Lab · alerted <b>ward in-charge</b>','Escalated','rose'),
      ('Queue agent','clock','aqua','Lab wait dropping <b>42 → 18 min</b>','Resolved','ok')]
def feed_panel():
    rows=''.join(f'<div class="a4-fr" id="a4fr{k}">{well(i,t,"50px")}<div class="a4-fm"><div class="a4-ft"><b>{n}</b><span class="a4-fts">09:41:{12+k*7:02d}</span></div>'
                 f'<div class="a4-fx">{x}</div></div><span class="a4-fc a4-fc--{ck}">{c}</span></div>' for k,(n,i,t,x,c,ck) in enumerate(FEED))
    return (f'<div class="a4-feed"><div class="a4-fh"><span class="a4-fdot"></span><div><div class="a4-fhT">Agents at work</div><div class="a4-fhS">Pulse AI · live log</div></div>'
            f'<span class="a4-fn"><b id="a4fn">3</b> active</span></div><div class="a4-frs">{rows}</div></div>')
def scene_svg():
    c='#d6e7f4'
    lines=''.join(f'<path d="M{x} 360 L{320+(x-320)*0.25} 150" stroke="{c}" stroke-width="1.5"/>' for x in range(-160,820,80))
    lines+=''.join(f'<path d="M0 {y} H640" stroke="{c}" stroke-width="1.5"/>' for y in [170,195,228,275,345])
    lines+=f'<path d="M0 150 H640" stroke="{c}" stroke-width="2"/><rect x="250" y="70" width="140" height="80" rx="6" fill="#fff" stroke="{c}" stroke-width="2"/>'
    corners=''.join(f'<path d="{p}" stroke="#9aabb8" stroke-width="3" fill="none" stroke-linecap="round"/>' for p in ['M12 28V12H28','M628 28V12H612','M12 332V348H28','M628 332V348H612'])
    return f'<svg class="a4-scene" viewBox="0 0 640 360" preserveAspectRatio="xMidYMid slice">{lines}{corners}</svg>'
def ochip(icon,txt,kind):
    return f'<span class="a4-ochip {"a4-ochip--"+kind if kind else ""}"><span class="ic">{ic(icon,"16px")}</span><span>{txt}</span></span>'
def cam(k,lbl,chips):
    ch=''.join(ochip(*c) for c in chips)
    alert=ochip('alert','Waiting <b>42 min</b>, staff alerted','amber') if k==ALERT_CAM else ''
    return (f'<div class="a4-cam">{scene_svg()}<span class="a4-cic">{ic("camera","64px","1.6")}</span>'
            f'<div class="a4-lbl"><i></i>CAM {k+1:02d} · {lbl}</div><div class="a4-ts">09:41:12</div><div class="a4-chips">{ch}{alert}</div></div>')

def shell(sid, content, cls=''):
    return (f'<div class="sh {cls}" id="sh-{sid}"><div class="sh-bg"></div><div class="sh-orb"></div><div class="sh-ring"></div>'
            f'<div class="sh-clip"><div class="sh-content">{content}</div></div></div>')

WORLD=('<svg id="fx4" width="1" height="1" style="position:absolute;left:0;top:0;overflow:visible"></svg>'
       + shell('mp', DASH, 'a4-mpsh') + ''.join(shell(f'cm{k}', cam(k,l,c), 'a4-camsh') for k,(l,c) in enumerate(CAMS)) + shell('ap', feed_panel(), 'a4-apsh'))
OVER=f'''<div class="a2-logo a4-gov" id="a4gov"><span class="hd-govbadge" style="color:var(--navy);font-size:18px">{logo("maha","Seal of Maharashtra")}Government of Maharashtra</span></div>
<div class="a4-cnt" id="a4cnt">
  <div class="hd-kicker a4-part" id="a4k">Pulse AI · district hospitals</div>
  <div class="a4-stack">
    <div class="hd-counter a4-part" id="a4A" style="--cnt-fs:128px"><span class="hd-counter__num" id="a4An">0</span><span class="hd-counter__unit">+</span></div>
    <div class="hd-counter hd-counter--to a4-part" id="a4B" style="--cnt-fs:128px"><span class="hd-counter__from">1,500+</span><span class="hd-counter__arrow">→</span><span class="hd-counter__num" id="a4Bn">1,500</span></div>
  </div>
  <div class="a4-lab a4-part" id="a4l">cameras live</div>
</div>'''

CSS4=r'''
.a4-dash{width:1600px;background:#fff}
.a4-dh{display:flex;align-items:center;gap:16px;padding:20px 28px;background:var(--navy);color:#fff}
.a4-brand{font-size:24px;font-weight:800;letter-spacing:2px}.a4-sub{opacity:.7;font-size:17px;font-weight:600}
.a4-dh .hd-govbadge{font-size:16px}
.a4-live{width:8px;height:8px;border-radius:50%;background:currentColor;display:block}
.a4-body{display:grid;grid-template-columns:1fr 340px;gap:28px;padding:28px}
.a4-plate{background:var(--grey);border-radius:var(--r-plate);padding:12px;display:flex;justify-content:center}
.a4-plate .hd-kmap{width:100%;height:640px}
.a4-legend{display:flex;gap:28px;margin-top:16px;color:var(--navy)}
.a4-side{display:flex;flex-direction:column;gap:16px}
.a4-stat{display:flex;gap:18px;align-items:center;box-shadow:0 0 0 2px var(--line)}
.a4-alert{background:var(--sun);font-size:15px;display:flex;gap:10px;align-items:center;color:var(--sun-ink);font-weight:700}
.hd-kdot{transform-box:fill-box;transform-origin:center}
.a4-mpsh .sh-bg{border-radius:28px}
.a4-cam{position:relative;width:480px;height:270px;background:linear-gradient(160deg,#f7f9fb 0%,#eef1f4 100%);overflow:hidden;border-radius:16px}
.a4-scene{position:absolute;inset:0;width:100%;height:100%}
.a4-cic{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);color:#b9c8d4}
.a4-lbl{position:absolute;left:30px;top:18px;display:flex;align-items:center;gap:8px;font-size:12px;font-weight:700;letter-spacing:.6px;text-transform:uppercase;color:var(--navy)}
.a4-lbl i{width:8px;height:8px;border-radius:50%;background:var(--d-rose);display:block;box-shadow:0 0 0 3px rgba(234,92,114,.2)}
.a4-ts{position:absolute;right:30px;top:18px;font-size:12px;font-weight:700;color:var(--muted)}
.a4-chips{position:absolute;left:26px;bottom:24px;right:26px;display:flex;gap:8px;flex-wrap:wrap}
.a4-ochip{display:inline-flex;align-items:center;gap:8px;background:#fff;color:var(--navy);border-radius:999px;padding:6px 14px 6px 6px;font-size:14px;font-weight:600;white-space:nowrap;box-shadow:0 4px 14px rgba(1,43,68,.12)}
.a4-ochip b{font-weight:800}
.a4-ochip .ic{width:26px;height:26px;border-radius:50%;background:#d5ecfd;color:var(--blue);display:flex;align-items:center;justify-content:center}
.a4-ochip--ok .ic{background:var(--mint);color:var(--mint-ink)}
.a4-ochip--amber{background:var(--d-amber);color:#3d2a00}.a4-ochip--amber .ic{background:rgba(255,255,255,.45);color:#3d2a00}
.a4-cam.is-alert{box-shadow:inset 0 0 0 3px var(--d-amber)}
.a4-cam.is-alert .a4-cic{color:#f3c27a}
.a4-camsh .sh-bg{border-radius:16px}
.a4-apsh .sh-bg{border-radius:20px}
.a4-feed{width:480px;height:858px;background:#fff;border-radius:20px;padding:24px 20px;display:flex;flex-direction:column;gap:16px;box-shadow:inset 0 0 0 2px var(--line)}
.a4-fh{display:flex;align-items:center;gap:14px;padding:4px 4px 16px;border-bottom:2px solid var(--grey)}
.a4-fdot{width:12px;height:12px;border-radius:50%;background:var(--d-mint);box-shadow:0 0 0 5px rgba(59,230,162,.22);flex:none}
.a4-fhT{font-size:26px;font-weight:800;color:var(--navy)}.a4-fhS{font-size:16px;font-weight:600;color:var(--muted);margin-top:2px}
.a4-fn{margin-left:auto;font-size:15px;font-weight:700;color:var(--blue);background:var(--tint);border-radius:999px;padding:6px 14px}
.a4-frs{display:flex;flex-direction:column;gap:12px}
.a4-fr{display:flex;gap:14px;align-items:flex-start;padding:16px 14px;border-radius:16px;background:#fff;box-shadow:0 0 0 1.5px var(--line);opacity:0;will-change:transform,opacity}
.a4-fr .hd-well{flex:none}
.a4-fm{flex:1;min-width:0}
.a4-ft{display:flex;justify-content:space-between;align-items:baseline;font-size:19px;color:var(--navy)}.a4-ft b{font-weight:800}
.a4-fts{font-size:13px;font-weight:700;color:var(--muted)}
.a4-fx{font-size:17px;line-height:1.35;color:#2c4252;margin-top:4px}.a4-fx b{color:var(--navy)}
.a4-fc{align-self:center;flex:none;font-size:12.5px;font-weight:800;letter-spacing:.6px;text-transform:uppercase;padding:6px 11px;border-radius:999px;background:#d5ecfd;color:var(--blue)}
.a4-fc--ok{background:var(--mint);color:var(--mint-ink)}.a4-fc--amber{background:var(--d-amber);color:#3d2a00}.a4-fc--rose{background:var(--rose);color:var(--rose-ink)}
.a4-fr.is-hot{box-shadow:0 0 0 2.5px var(--d-amber),0 10px 26px rgba(254,182,79,.25)}
.a4-fr.is-done{box-shadow:0 0 0 2.5px var(--d-mint),0 10px 26px rgba(59,230,162,.18)}
.a4-gov{left:72px}
.a4-cnt{position:absolute;left:120px;top:50%;transform:translateY(-55%);display:flex;flex-direction:column;gap:18px;pointer-events:none}
.a4-cnt .hd-kicker{font-size:24px;letter-spacing:4px}
.a4-stack{position:relative;height:140px}
.a4-stack .hd-counter{position:absolute;left:0;top:0;white-space:nowrap}
.a4-lab{font-size:44px;font-weight:700;color:var(--navy)}
.a4-part{will-change:transform,opacity,filter;opacity:0}
'''

JS4=r'''
/* =================== ACT 4 · MAHA-PULSE =================== */
const MAHA_D=__MAHA__;
const KOL=54.0, DOTS7=55.4, LIVE=57.4, TOTILES=63.8, ALERT=66.8, TOMAP=69.0, FILL2=71.6, TOPULSE=73.6;
const fx4=$('#fx4');const mk4=(tag,at)=>{const e=document.createElementNS(NS,tag);for(const k in at)e.setAttribute(k,at[k]);fx4.appendChild(e);return e};
const MP=mkShell('mp');MP.ct.style.transform='translate(-50%,-50%)';
let MPW=MP.ct.offsetWidth||1600,MPH=MP.ct.offsetHeight||860;
const NCAM=6,AC=3;const CM=[...Array(NCAM).keys()].map(k=>{const o=mkShell('cm'+k);o.ct.style.transform='translate(-50%,-50%)';o.cam=o.ct.querySelector('.a4-cam');o.chips=[...o.ct.querySelectorAll('.a4-ochip')];return o});
const TW=480,TH=270,TXY=[...Array(NCAM).keys()].map(k=>({x:(k%2-1)*504,y:(Math.floor(k/2)-1)*294}));
const AP=mkShell('ap');AP.ct.style.transform='translate(-50%,-50%)';const APX=504,APY=0,APW=480,APH=858;
const FR=[...Array(6).keys()].map(k=>$('#a4fr'+k)),a4fn=$('#a4fn');
const FT=[64.75,65.6,ALERT+.05,ALERT+.75,ALERT+1.35,ALERT+1.95];   // feed row arrival times
function apState(t){
  const st={x:APX,y:APY,rot:0,w:APW,h:APH,r:20,sat:1,ring:0,ringA:0,bg:1,orb:0,cop:1,cb:0,s:1,op:clamp((t-TOTILES-.7)/.1)};
  [ALERT+.05,ALERT+1.35].forEach((f,j)=>{const rp=clamp((t-f)/.8);if(rp>0&&rp<1){st.ring=30*EZ.out(rp);st.ringA=.3*(1-rp);st.ringRGB=j?'234,92,114':'254,182,79'}});
  const x=P(t,TOMAP-.15,.45,EZ.in);st.op*=1-x;st.cb=10*x;st.s=1-.06*x;
  return st;
}
function feed(t){
  FR.forEach((e,k)=>{const a=FT[k],p=P(t,a,.5,EZ.spring),o=clamp((t-a)/.15);e.style.opacity=o;e.style.transform=`translateY(${(1-p)*-18}px) scale(${.96+.04*p})`;
    e.classList.toggle('is-hot',k===2&&t>=a&&t<FT[5]);e.classList.toggle('is-done',k===5&&t>=a)});
  a4fn.textContent=t<FT[3]?2:t<FT[5]?3:2;
}
/* dashboard internals */
const KM=MP.ct.querySelector('.hd-kmap'),KOUT=KM.querySelector('.hd-kmap__outline');
const KD={};['hospitals','camps','ambulances','patients'].forEach(c=>KD[c]=[...KM.querySelectorAll('.hd-kdot--'+c)]);
KD.ambulances.forEach(e=>e.halo=e.nextElementSibling);
const kpos=e=>e.tagName==='rect'?[+e.getAttribute('x')+7,+e.getAttribute('y')+7]:e.tagName==='circle'?[+e.getAttribute('cx'),+e.getAttribute('cy')]:(m=>[+m[1],+m[2]+8])(e.getAttribute('d').match(/M([\d.]+) ([\d.]+)/));
const KRIP=[...Array(6)].map(()=>{const c=document.createElementNS(NS,'circle');c.setAttribute('fill','#139bf5');KM.appendChild(c);return c});
const ALLK=[...KD.hospitals,...KD.camps,...KD.ambulances,...KD.patients];
const CV=[...MP.ct.querySelectorAll('.a4-cv')].map(e=>({e,v:+e.dataset.v})),a4alert=$('#a4alert'),a4live=MP.ct.querySelector('.a4-live');
const fmt=n=>Math.round(n).toLocaleString('en-IN');
function dash(t){
  KOUT.style.opacity=P(t,54.6,.6);KOUT.setAttribute('stroke-dashoffset',-t*24);
  const order={hospitals:DOTS7,camps:DOTS7+.5,ambulances:DOTS7+.9,patients:DOTS7+1.3},stag={hospitals:.03,camps:.03,ambulances:.03,patients:.005};
  for(const c in KD)KD[c].forEach((e,i)=>{const a=order[c]+i*stag[c],s=P(t,a,.4,EZ.spring);let tr=`scale(${Math.max(.001,s)})`;
    if(c==='ambulances'){const ph=i*1.7,m=clamp((t-LIVE)/1);const dx=m*14*Math.sin((t-LIVE)*.9+ph),dy=m*10*Math.cos((t-LIVE)*.7+ph);tr=`translate(${dx}px,${dy}px) `+tr;e.halo.style.transform=`translate(${dx}px,${dy}px)`;e.halo.style.opacity=clamp((t-a)/.2)*.35*(.6+.4*Math.sin(t*4+i))}
    e.style.transform=tr;e.style.opacity=clamp((t-a)/.12)});
  // live updates: a ripple fires on a dot every .42s
  KRIP.forEach((c,j)=>{const per=.42*6,base=LIVE+j*.42;if(t<base){c.setAttribute('opacity',0);return}const n=Math.floor((t-base)/per),tt=(t-base)-n*per,rp=clamp(tt/1.1);
    const e=ALLK[Math.floor(hash(n*6+j+1)*ALLK.length)],[x,y]=kpos(e);c.setAttribute('cx',x);c.setAttribute('cy',y);c.setAttribute('r',8+38*EZ.out(rp));c.setAttribute('opacity',rp<1?.35*(1-rp):0)});
  const cu=P(t,55.6,1.4,EZ.out);
  CV.forEach((c,i)=>{let v=c.v*cu;if(t>LIVE){if(i===1)v=c.v+Math.floor((t-LIVE)*7);if(i===3)v=c.v+Math.round(2*Math.sin((t-LIVE)*1.3));if(i===2&&t>60)v=c.v+1}
    c.e.textContent=fmt(v)});
  a4alert.style.transform=`translateY(${(1-P(t,59.5,.5,EZ.spring))*20}px)`;a4alert.style.opacity=clamp((t-59.5)/.2);
  a4live.style.opacity=.5+.5*Math.sin(t*6);
}
function mpState(t){
  const st={x:0,y:30,rot:0,s:1,sat:1,ring:0,ringA:0,bg:1,orb:0,op:t<53.95?0:1};
  const g=P(t,KOL,1.0,EZ.soft);st.w=lerp(1320,MPW,g);st.h=lerp(624,MPH,g);st.r=28;st.y=lerp(30,0,g);
  const ci=P(t,KOL+.2,.5,EZ.out);st.cop=ci;st.cb=10*(1-ci);
  const m=P(t,TOTILES,.95,EZ.soft);st.w=lerp(st.w,APW,m);st.h=lerp(st.h,APH,m);st.r=lerp(28,20,m);st.x=lerp(0,APX,m);st.y=lerp(st.y,APY,m);
  const co=P(t,TOTILES,.3,EZ.in);st.cop*=1-co;st.cb+=10*co;st.op*=1-P(t,TOTILES+.75,.2,EZ.lin);
  return st;
}
/* camera tiles */
function camState(k,t){
  const T=TXY[k],d=Math.hypot(T.x,T.y)/600,a=TOTILES+.65+d*.25;
  const st={x:T.x,y:T.y,rot:0,w:TW,h:TH,r:16,sat:1,ring:0,ringA:0,bg:1,orb:0,cop:1,cb:0};
  {const p=P(t,a,.7,EZ.soft);st.x=lerp(APX,T.x,p);st.y=lerp(APY,T.y,p);st.s=lerp(.6,1,P(t,a,.6,EZ.spring));st.op=clamp((t-a)/.15);st.cb=8*(1-P(t,a,.45))}
  if(k===AC){const pl=t>ALERT&&t<TOMAP?.5+.5*Math.sin((t-ALERT)*5.2):0;st.ring=10+16*pl;st.ringA=t>ALERT&&t<TOMAP?.45*(1-.5*pl)*P(t,ALERT,.3):0;st.ringRGB='254,182,79';st.s*=1+.04*bump(t,ALERT,.45)}
  else{const sp=ALERT+1.1+Math.hypot(T.x-TXY[AC].x,T.y-TXY[AC].y)/1000*.6,rp=clamp((t-sp)/.8);if(rp>0&&rp<1){st.ring=36*EZ.out(rp);st.ringA=.3*(1-rp)}}
  const S=TOMAP+k*.04,m=P(t,S,.9,EZ.soft),ms=P(t,S,.6,EZ.soft);
  st.w=lerp(TW,16,ms);st.h=lerp(TH,16,ms);st.r=lerp(16,8,ms);st.x=lerp(st.x,MPTS[k].x,m);st.y=lerp(st.y,MPTS[k].y,m);
  const co=P(t,S,.25,EZ.in);st.cop=1-co;st.cb+=10*co;st.orb=P(t,S+.15,.35);st.bg=1-P(t,S+.2,.3);st.op*=1-P(t,S+.85,.2,EZ.lin);
  return st;
}
function camInner(t){
  CM.forEach((o,k)=>{const T=TXY[k],a=TOTILES+1.0+Math.hypot(T.x,T.y)/600*.25;
    o.chips.forEach((c,j)=>{if(k===AC&&j===1){const s=P(t,ALERT+.3,.5,EZ.spring);c.style.transform=`translateY(${(1-s)*14}px) scale(${.85+.15*s})`;c.style.opacity=clamp((t-ALERT-.3)/.15);return}
      if(k===AC&&j===0){pop(c,t,a+.25,12);c.style.opacity=+c.style.opacity*(1-P(t,ALERT+.1,.25,EZ.lin));c.style.display=t>ALERT+.35?'none':'';return}
      pop(c,t,a+.25+j*.12,12)});
    o.cam.classList.toggle('is-alert',k===AC&&t>=ALERT&&t<TOMAP)});
}
/* Maharashtra map (dot fill) */
const MS=13.2,MCX=57.2,MCY=47;const mapG=mk4('g',{});
mapG.innerHTML=`<path d="${MAHA_D}" fill="#eef7fd" stroke="#0873ba" stroke-width=".3" stroke-linejoin="round"/>`;
const mapDots=document.createElementNS(NS,'g');mapG.appendChild(mapDots);
const MD=[];(function(){const ctx=document.createElement('canvas').getContext('2d'),path=new Path2D(MAHA_D),R=rng(7);
  for(let v=1;v<94;v+=1.45)for(let u=1;u<114;u+=1.45){const x=u+(Math.floor(v/1.45)%2)*.72;if(ctx.isPointInPath(path,x,v)){const c=document.createElementNS(NS,'circle');c.setAttribute('cx',x);c.setAttribute('cy',v);c.setAttribute('fill','#139bf5');mapDots.appendChild(c);MD.push({c,x,v,o:R()})}}})();
MD.sort((a,b)=>a.o-b.o);MD.forEach((d,i)=>d.rank=i/MD.length);
const kolG=document.createElementNS(NS,'g');kolG.innerHTML='<circle r="5" fill="#3fd4f6" opacity=".25"/><circle r="2.6" fill="#0873ba" stroke="#fff" stroke-width=".8"/><g transform="translate(5 -3)"><rect width="22" height="6" rx="3" fill="#012b44"/><text x="11" y="4.3" text-anchor="middle" font-size="3.4" font-weight="700" fill="#fff">Kolhapur</text></g>';
kolG.setAttribute('transform','translate(22 81)');mapG.appendChild(kolG);
const toW=(u,v)=>({x:(u-MCX)*MS,y:(v-MCY)*MS});
const MPTS=[0,1,2,3,4,5].map(k=>{const d=MD[Math.floor((k+.5)/6*MD.length*.3)];return toW(d.x,d.v)});
const pulseG=mk4('g',{});pulseG.innerHTML='<circle r="80" fill="#139bf5" opacity=".12"/><circle r="64" fill="#eef7fd"/><circle r="50" fill="url(#hdorb)"/><circle r="13" fill="#fff"/>';
const pRip=[0,1,2].map(()=>mk4('circle',{fill:'#139bf5'}));
function mahaMap(t){
  if(t<TOMAP-.2){mapG.setAttribute('opacity',0);return}
  const a=P(t,TOMAP+.1,.7,EZ.out),sh=P(t,TOPULSE,.9,EZ.in);
  const sc=MS*lerp(.94,1,a)*lerp(1,.04,sh);mapG.setAttribute('transform',`scale(${sc}) translate(${-MCX} ${-MCY})`);mapG.setAttribute('opacity',a*(1-P(t,TOPULSE+.6,.3,EZ.lin)));
  MD.forEach(d=>{const th=d.rank<.3?TOMAP+.9+d.rank/.3*1.0:FILL2+.2+(d.rank-.3)/.7*1.4;const s=P(t,th,.35,EZ.spring);d.c.setAttribute('r',Math.max(0,.55*s));d.c.setAttribute('opacity',clamp((t-th)/.1))});
  kolG.setAttribute('opacity',P(t,TOMAP+.7,.4));
}
function pulseEnd(t){
  const s=P(t,TOPULSE+.45,.6,EZ.spring);pulseG.setAttribute('transform',`scale(${Math.max(.001,s*(1+.06*bump(t,74.5,.4)))})`);pulseG.setAttribute('opacity',s>0.01?1:0);
  pRip.forEach((c,j)=>{const rp=clamp((t-74.2-j*.3)/1.1);setC(c,0,0,50+180*EZ.out(rp),rp>0&&rp<1?.25*(1-rp):0)});
}
/* big camera counter */
const a4k=$('#a4k'),a4A=$('#a4A'),a4An=$('#a4An'),a4B=$('#a4B'),a4Bn=$('#a4Bn'),a4l=$('#a4l'),a4gov=$('#a4gov');
function camCounter(t){
  inout(a4k,t,TOMAP+.8,TOPULSE);inout(a4l,t,TOMAP+1.0,TOPULSE+.05);
  inout(a4A,t,TOMAP+.9,FILL2,40);a4An.textContent=fmt(1500*P(t,TOMAP+.9,1.0,EZ.out));
  inout(a4B,t,FILL2+.1,TOPULSE+.02,40);a4Bn.textContent=fmt(lerp(1500,5000,P(t,FILL2+.25,1.4,EZ.out)));a4B.style.transform+=` scale(${1+.04*bump(t,73.0,.35)})`;
}
function camA4(t,c){
  if(t<53.8)return c;
  const a=P(t,53.8,1.2,EZ.io);let z=lerp(c.z,.8,a),cx=lerp(c.cx,0,a),cy=lerp(c.cy,85,a);
  const b=P(t,TOTILES,1.0,EZ.io);z=lerp(z,.78,b);cy=lerp(cy,88,b);
  const m=P(t,TOMAP,1.1,EZ.io);z=lerp(z,.55,m);cx=lerp(cx,-570,m);cy=lerp(cy,70,m);
  const e=P(t,TOPULSE,1.2,EZ.io);z=lerp(z,1.0,e);cx=lerp(cx,0,e);cy=lerp(cy,50,e);
  return {z,cx,cy};
}
function act4(t){
  if(t<53.8){MP.el.style.opacity=0;AP.el.style.opacity=0;CM.forEach(o=>o.el.style.opacity=0);mapG.setAttribute('opacity',0);pulseG.setAttribute('opacity',0);pRip.forEach(c=>c.setAttribute('opacity',0));a4gov.style.opacity=0;return}
  // hand-off from act 3
  const ho=1-P(t,54.05,.3,EZ.lin);AG[4].el.style.opacity=(+AG[4].el.style.opacity)*ho;cityG.setAttribute('opacity',(+cityG.getAttribute('opacity'))*(1-P(t,54.0,.8,EZ.lin)));
  if(t<TOTILES+1.2){applyShell(MP,mpState(t),mpState(t-1/60),false);dash(t)}else MP.el.style.opacity=0;
  if(t>TOTILES+.5){CM.forEach((o,k)=>applyShell(o,camState(k,t),camState(k,t-1/60),false));camInner(t)}else CM.forEach(o=>o.el.style.opacity=0);
  if(t>TOTILES+.5&&t<TOMAP+.4){applyShell(AP,apState(t),apState(t-1/60),false);feed(t)}else AP.el.style.opacity=0;
  mahaMap(t);pulseEnd(t);camCounter(t);
  a4gov.style.opacity=P(t,TOTILES+.8,.6)*(1-P(t,TOPULSE,.4));
}
document.fonts&&document.fonts.ready.then(()=>{MPW=MP.ct.offsetWidth||MPW;MPH=MP.ct.offsetHeight||MPH});
'''
