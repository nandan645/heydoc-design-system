"""Act 3 · Pathkind Labs (34–54s): scene 5 (34–44) one phone, four screens + touchpoint agents; scene 6 (44–54) lab panel, 5 agent cards, logistics → route map."""
from base import *
from s3 import pk_book, pk_track, pk_report, pk_chat, AGENTS, agent, route_map

def _track():
    s=pk_track()
    R=[('<path d="M40 70 V200 H150 V240" stroke="url(#pkg)"','<path class="a3-route" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" d="M40 70 V200 H150 V302 H226" stroke="url(#pkg)"'),
       ('x1="40" x2="150"','x1="40" x2="226"'),
       ('<g transform="translate(150 240)"><circle r="24"','<g class="a3-mk" transform="translate(40 70)"><circle r="24"'),
       ('<g transform="translate(188 312)">','<g class="a3-eta" transform="translate(188 312)">'),
       ('>12 min</text>','><tspan class="a3-etaT">12</tspan> min</text>'),
       ('Arriving in 12 min</div>','Arriving in <span class="a3-etaT">12</span> min</div>'),
       ('style="--p:38%"','class="a3-prog" style="--p:10%"')]
    for a,b in R:
        assert a in s,a; s=s.replace(a,b)
    s=s.replace('class="hd-progress__fill" class="a3-prog"','class="hd-progress__fill a3-prog"')
    return s

import json as _json
PKIMG=_json.load(open('../pk/pk.json'))
# first screen: the user's Pathkind 'Tests' mockup (status bar baked in); Add-button highlight sits on the CBC card
TESTS=(f'<div class="a3-shot"><img src="{PKIMG["tests"]}" alt="Pathkind Tests screen"/>'
       '<span class="a3-hl" style="left:33.3%;top:40.9%;width:14.8%;height:4.2%;border-radius:1.1em"></span>'
       '<span class="a3-hl a3-hl--card" style="left:3.5%;top:25.3%;width:47.2%;height:21.2%;border-radius:1.3em"></span></div>')
STACK='<div class="a3-stack">'+''.join(f'<div class="a3-scr">{f}</div>' for f in [TESTS,_track(),pk_report(),pk_chat()])+'</div>'
PANEL=(f'<div class="a3-panel"><div class="a3-ph">{logo("pathkind","Pathkind Labs","","height:44px")}<span class="a3-pt">Lab operations</span>'
       '<span class="hd-tag hd-tag--mint" style="margin-left:auto"><i></i>Live</span></div></div>')

def shell(sid, content, content2='', cls=''):
    return (f'<div class="sh {cls}" id="sh-{sid}"><div class="sh-bg"></div><div class="sh-orb"></div><div class="sh-ring"></div>'
            f'<div class="sh-clip"><div class="sh-content">{content}</div>{"<div class=sh-content2>"+content2+"</div>" if content2 else ""}</div></div>')

def pk_map():
    # film-only Pathkind recolour of the shared route map: yellow routes + hub, warm ground
    m=route_map()
    for a,b in [('<rect width="1100" height="520" fill="#eef7fd"/>','<rect width="1100" height="520" fill="#f7f7f4"/>'),
                ('<stop offset="0" stop-color="#1789f2"/><stop offset="1" stop-color="#3fd4f6"/></linearGradient>','<stop offset="0" style="stop-color:var(--partner2-deep)"/><stop offset="1" style="stop-color:var(--partner2)"/></linearGradient>'),
                ('<stop offset="0" stop-color="#0a84e8"/><stop offset=".55" stop-color="#2ba7f5"/><stop offset="1" stop-color="#43d0f2"/>','<stop offset="0" style="stop-color:var(--partner2-deep)"/><stop offset=".55" style="stop-color:var(--partner2)"/><stop offset="1" style="stop-color:var(--partner2-light)"/>'),
                ('<circle r="46" fill="#eef7fd" opacity=".9"/>','<circle r="46" style="fill:var(--partner2-tint)" opacity=".9"/>'),
                ('stroke="#8fcdf8" stroke-width="5" stroke-dasharray="2 12"','style="stroke:var(--partner2-pale)" stroke-width="5" stroke-dasharray="2 12"'),
                ('fill="#0873ba" font-family="Open Sans">ETA','fill="#012b44" font-family="Open Sans">ETA'),
                ('stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">','style="stroke:var(--partner2-on)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">')]:
        assert a in m,a; m=m.replace(a,b)
    m=m.replace('<circle r="24" fill="#012b44"/><circle r="30" fill="none" stroke="#012b44"','<circle r="24" style="fill:var(--partner2)"/><circle r="30" fill="none" style="stroke:var(--partner2-deep)"')
    return m.replace('#0873ba','#012b44')

cards=''
for k,a in enumerate(AGENTS):
    c=f'<div class="a3-ag" style="--agent-w:270px"><div class="a3-idle">{agent(*a,False)}</div><div class="a3-act">{agent(*a,True)}</div></div>'
    cards+=shell(f'ag{k}', c, f'<div class="a3-map">{pk_map()}</div>' if k==4 else '', 'a3-agsh')

TP=[('Booking agent','cal','peach'),('Collection agent','route','sun'),('Report agent','report','aqua'),('Care agent','chat','lav')]
chips=''.join(f'<div class="a3-tp" id="a3tp{k}"><span class="hd-chip">{well(i,t)}{n}</span></div>' for k,(n,i,t) in enumerate(TP))

WORLD=shell('pk', phone(STACK,'light',style='--phone-w:340px'), PANEL, 'a3-pk')+'<svg id="fx3" width="1" height="1" style="position:absolute;left:0;top:0;overflow:visible"></svg>'+cards+chips
OVER=f'<div class="a2-logo" id="a3logo">{logo("pathkind","Pathkind Labs","","height:46px")}</div>'

CSS3=r'''
.a3-pk .hd-phone--light{box-shadow:inset 0 0 0 2px var(--line)}
.a3-stack{position:relative;flex:1;min-height:0}
.a3-scr{position:absolute;inset:0;display:flex;flex-direction:column}
.a3-scr>.hd-scr{height:100%}
.a3-shot{position:absolute;left:0;right:0;top:-3.2em;bottom:0;background:#fff}
.a3-shot img{position:absolute;inset:0;width:100%;height:100%;display:block}
.a3-hl{position:absolute;pointer-events:none}
/* ---- Partner 2 accent (Act 3): every shade comes from --partner2 (see brand.py) ---- */
.a3-tp,.a3-agsh{--grad:var(--partner2-grad);--shadow-glow:0 12px 30px rgba(var(--partner2-rgb),.32)}
.a3-tp .hd-chip--solid{color:var(--partner2-on)}.a3-tp .hd-chip--solid .hd-well{background:rgba(255,255,255,.6);color:var(--partner2-on)}
.a3-agsh .hd-well--grad{color:var(--partner2-on)}
#t6 em,#t7 em,#t7 .a2-var{color:var(--partner2-ink)}
#t7 .a2-var{border-color:var(--partner2-pale);background:var(--partner2-tint)}
#sh-pk .sh-orb{background:var(--partner2-orb);box-shadow:0 14px 40px rgba(var(--partner2-rgb),.45)}
.a3-panel{width:1560px;height:780px;padding:30px 40px}
.a3-ph{display:flex;align-items:center;gap:22px;padding-bottom:26px;border-bottom:2px solid var(--grey)}
.a3-pt{font-size:26px;font-weight:700;color:var(--navy);padding-left:22px;border-left:2px solid var(--line)}
.a3-ag{position:relative;width:270px}
.a3-act{position:absolute;left:0;top:0;width:100%;opacity:0}
.a3-agsh .sh-bg{border-radius:24px}
.a3-map{width:1100px;height:520px}
.a3-map .hd-routemap{display:block}
.a3-tp{position:absolute;left:0;top:0;opacity:0;will-change:transform}
.a3-tp .hd-chip{font-size:24px;padding:10px 26px 10px 10px;box-shadow:var(--shadow-layered)}
.a3-tp .hd-well{--well:46px}
'''

JS3=r'''
/* =================== ACT 3 · PATHKIND =================== */
VARS.agents_live=null; VARS.report_speedup_pct=null;
const SC=[35.0,36.6,38.6,40.6], WIDEN=42.9, AT=[44.5,45.2,45.9,46.6,47.3], EXPAND=48.0, ZOOMOUT=52.5;
const PK_K=.92, PKW=340*PK_K, PKH=340*1940/950*PK_K, PKR=157*340/950*PK_K, PNW=1560, PNH=780, PY=HY;
const mkShell=id=>{const el=$('#sh-'+id);return {el,ct:el.querySelector('.sh-content'),c2:el.querySelector('.sh-content2'),bg:el.querySelector('.sh-bg'),orb:el.querySelector('.sh-orb'),ring:el.querySelector('.sh-ring')}};
const fx3=$('#fx3');const mk3=(tag,at)=>{const e=mk(tag,at);fx3.appendChild(e);return e};
const PK=mkShell('pk');const AG=[0,1,2,3,4].map(k=>mkShell('ag'+k));
AG.forEach(o=>{o.idle=o.ct.querySelector('.a3-idle');o.act=o.ct.querySelector('.a3-act');o.fill=o.act.querySelector('.hd-progress__fill');o.p=parseFloat(o.fill.style.getPropertyValue('--p'));o.ct.style.transform='translate(-50%,-50%)'});
const AGW=270, AGX=[0,1,2,3,4].map(k=>(k-2)*298), AGY=40;
let AGH=AG[0].ct.offsetHeight||230;
['agents_live','report_speedup_pct'].forEach(k=>{const e=$('#v_'+k);if(e&&VARS[k]!=null){e.textContent=VARS[k];e.classList.add('is-set')}});
const setC2=(o,op,bl,sc)=>{o.c2.style.opacity=op;o.c2.style.filter=bl>.2?`blur(${bl}px)`:'none';o.c2.style.transform=`translate(-50%,-50%) scale(${sc})`};
/* phone -> panel */
function pkState(t){
  const st={x:0,y:PY,rot:0,s:P(t,34.15,.45,EZ.spring),sat:1,ring:0,ringA:0,bg:1,orb:1,cop:0,cb:12,op:t<34.1?0:1};
  const d=P(t,34.35,.85,EZ.soft);st.w=lerp(20,PKW,d);st.h=lerp(20,PKH,d);st.r=lerp(10,PKR,d);
  st.orb=1-P(t,34.45,.3,EZ.lin);const ci=P(t,34.55,.5,EZ.out);st.cop=ci;st.cb=12*(1-ci);
  st.ringRGB=ACC.partner2.rgb;
  SC.concat([WIDEN]).forEach(f=>{const rp=clamp((t-f)/.8);if(rp>0&&rp<1){st.ring=40*EZ.out(rp);st.ringA=.32*(1-rp)}const b=bump(t,f,.45);st.s*=1+.03*b;st.y-=10*b});
  const w=P(t,WIDEN,.95,EZ.soft);st.w=lerp(st.w,PNW,w);st.h=lerp(st.h,PNH,w);st.r=lerp(st.r,28,w);
  const co=P(t,WIDEN,.3,EZ.in);st.cop*=1-co;st.cb+=10*co;st.c2=P(t,WIDEN+.45,.5,EZ.out);
  st.op*=1-P(t,ZOOMOUT-.2,.6,EZ.lin);
  st.bg=Math.max(1-st.cop,st.c2||0);
  return st;
}
/* phone screens */
const SCR=[...PK.ct.querySelectorAll('.a3-scr')];
const Qs=(k,s)=>[...SCR[k].querySelectorAll(s)];
const pkHL=Qs(0,'.a3-hl'),pkOV=PK.ct.querySelector('.hd-ip__ov');
const route=Qs(1,'.a3-route')[0],mkr=Qs(1,'.a3-mk')[0],eta=Qs(1,'.a3-eta')[0],etaT=Qs(1,'.a3-etaT'),prog=Qs(1,'.a3-prog')[0];
const RPTS=[[40,70],[40,200],[150,200],[150,302],[226,302]];const RLEN=RPTS.slice(1).reduce((s,p,i)=>s+Math.hypot(p[0]-RPTS[i][0],p[1]-RPTS[i][1]),0);
function along(f){let L=f*RLEN;for(let i=1;i<RPTS.length;i++){const a=RPTS[i-1],b=RPTS[i],l=Math.hypot(b[0]-a[0],b[1]-a[1]);if(L<=l){const p=l?L/l:0;return [lerp(a[0],b[0],p),lerp(a[1],b[1],p)]}L-=l}return RPTS[RPTS.length-1]}
const repLi=Qs(2,'.hd-li'),repFill=Qs(2,'.hd-progress__fill').map(e=>({e,p:parseFloat(e.style.getPropertyValue('--p'))})),repTop=Qs(2,'.hd-scr__body > div').slice(0,2);
const chatEls3=[...SCR[3].querySelector('.hd-scr__body').children].filter(e=>!e.classList.contains('hd-input'));
function pkRing(el,t,a){let sp=0,al=0;[a,a+.55].forEach(f=>{const rp=clamp((t-f)/.8);if(rp>0&&rp<1){sp=Math.max(sp,14*EZ.out(rp));al=Math.max(al,.55*(1-rp))}});
  el.style.boxShadow=al>.002?`0 0 0 2.5px rgba(${ACC.partner2.rgb},${Math.min(1,al*2)}),0 0 0 ${sp}px rgba(${ACC.partner2.rgb},${al})`:'none'}
function pkScreens(t){
  SCR.forEach((s,k)=>{const a=SC[k],b=SC[k+1]??99;const i=k===0?1:P(t,a+.12,.5,EZ.out),o=P(t,b,.4,EZ.in);
    s.style.opacity=i*(1-o);s.style.transform=`translateX(${(1-i)*36-o*36}px)`;const bl=(1-i)*10+o*10;s.style.filter=bl>.2?`blur(${bl}px)`:'none';s.style.visibility=i*(1-o)>0.001?'visible':'hidden'});
  pkHL.forEach((e,i)=>pkRing(e,t,i===0?35.85:35.3));pkHL[0].style.background=`rgba(0,0,0,${.16*bump(t,36.25,.25)})`;
  pkOV.style.opacity=1-(parseFloat(SCR[0].style.opacity)||0);
  const f=P(t,36.8,1.6,EZ.io)*.88;route.setAttribute('stroke-dashoffset',1-f);const [mx,my]=along(f);mkr.setAttribute('transform',`translate(${mx} ${my})`);
  eta.setAttribute('transform',`translate(${mx+14} ${my+18})`);const m=Math.round(12-7*f/.88);etaT.forEach(e=>e.textContent=m);prog.style.setProperty('--p',(10+60*f/.88)+'%');
  repTop.forEach((e,i)=>pop(e,t,38.75+i*.1));repLi.forEach((l,i)=>pop(l,t,38.95+i*.1));repFill.forEach((r,i)=>r.e.style.setProperty('--p',(r.p*P(t,39.1+i*.1,.7,EZ.out))+'%'));
  chatEls3.forEach((e,i)=>pop(e,t,40.75+i*.38,14));
}
/* touchpoint chips + links */
const TPX=[-560,560,-560,560],TPY=[-230,-110,110,230];
const TPE=[0,1,2,3].map(k=>$('#a3tp'+k)),TPC=TPE.map(e=>e.querySelector('.hd-chip'));
const tpLines=[0,1,2,3].map(()=>mk3('line',{style:'stroke:var(--partner2)','stroke-width':3,'stroke-linecap':'round',pathLength:1,'stroke-dasharray':1}));
const tpPk=[0,1,2,3].map(()=>mk3('circle',{r:8,fill:'#012b44',stroke:'#fff','stroke-width':3}));
function touchpoints(t,ps){
  TPE.forEach((e,k)=>{const a=SC[k]+.25,side=Math.sign(TPX[k]);const w=e.offsetWidth||260,h=e.offsetHeight||66;
    const ex=ps.x+side*(PKW/2*ps.s+6),ey=TPY[k],cx=TPX[k]-side*w/2;
    const lp=P(t,a,.35,EZ.out),fade=1-P(t,WIDEN-.3,.35,EZ.lin);
    setL(tpLines[k],ex,ey,lerp(ex,cx-side*6,lp),ey);tpLines[k].setAttribute('stroke-dashoffset',0);tpLines[k].setAttribute('opacity',lp>0?.85*fade:0);
    const pk=P(t,a+.05,.35,EZ.io);setC(tpPk[k],lerp(ex,cx,pk),ey,8,pk>0&&pk<1?fade:0);
    const s=P(t,a+.3,.5,EZ.spring),o=clamp((t-a-.3)/.15)*fade;
    e.style.transform=`translate(${TPX[k]+side*(1-s)*-60}px,${ey}px) translate(-50%,-50%) scale(${.8+.2*s})`;e.style.opacity=o;
    const bl=(1-clamp((t-a-.3)/.3))*8+(1-fade)*8;e.style.filter=bl>.2?`blur(${bl}px)`:'none';
    TPC[k].classList.toggle('hd-chip--solid',t>=a+.3&&t<(SC[k+1]??WIDEN)+.25)});
}
/* agent cards */
const hub=mk3('g',{});hub.innerHTML='<defs><radialGradient id="pkorb" cx=".28" cy=".18" r=".9"><stop offset="0" style="stop-color:var(--partner2-deep)"/><stop offset=".55" style="stop-color:var(--partner2)"/><stop offset="1" style="stop-color:var(--partner2-light)"/></radialGradient></defs><circle r="40" style="fill:var(--partner2)" opacity=".2"/><circle r="32" style="fill:var(--partner2-tint)"/><circle r="24" fill="url(#pkorb)"/><circle r="6.5" fill="#fff"/>';
const HUBY=-215;const agLines=AG.map(()=>mk3('line',{style:'stroke:var(--partner2)','stroke-width':3,'stroke-linecap':'round',pathLength:1,'stroke-dasharray':1}));
const agPk=AG.map(()=>mk3('circle',{r:8,fill:'#012b44',stroke:'#fff','stroke-width':3}));const hubRip=AT.map(()=>mk3('circle',{style:'fill:var(--partner2)'}));
fx3.insertBefore(hub,null);
function agState(k,t){
  const st={x:AGX[k],y:AGY,rot:0,w:AGW,h:AGH,r:24,sat:1,ring:0,ringA:0,bg:0,orb:0,cop:1,cb:0,ringRGB:ACC.partner2.rgb};
  const a=43.55+k*.08;st.s=lerp(.8,1,P(t,a,.55,EZ.spring));st.op=clamp((t-a)/.2);st.cb=8*(1-P(t,a,.4));
  const rp=clamp((t-AT[k])/.8);if(rp>0&&rp<1){st.ring=40*EZ.out(rp);st.ringA=.3*(1-rp)}st.s*=1+.04*bump(t,AT[k],.45);st.y-=10*bump(t,AT[k],.45);
  if(k<4){const x=P(t,EXPAND-.05+k*.03,.35,EZ.in);st.op*=1-x;st.cb+=8*x;st.s*=1-.08*x}
  else{const m=P(t,EXPAND,.95,EZ.soft);st.x=lerp(st.x,0,m);st.y=lerp(st.y,30,m);st.w=lerp(AGW,1320,m);st.h=lerp(AGH,624,m);st.r=lerp(24,28,m);
    st.bg=P(t,EXPAND,.3);const co=P(t,EXPAND,.3,EZ.in);st.cop=1-co;st.cb+=10*co;st.c2=P(t,EXPAND+.4,.5,EZ.out)}
  return st;
}
const MAP=AG[4].c2.querySelector('svg');const mRoutes=[...MAP.querySelectorAll('.hd-route')];mRoutes.forEach(r=>{r.setAttribute('pathLength',1);r.setAttribute('stroke-dasharray',1)});
const mPins=[...MAP.querySelectorAll('.hd-pin')].map(g=>{const m=g.getAttribute('transform').match(/translate\(([-\d.]+) ([-\d.]+)\)/);return {g,x:+m[1],y:+m[2]}});
const mVan=MAP.querySelector('.hd-van'),mEta=[...MAP.querySelectorAll('text')].find(e=>e.textContent.includes('ETA')).parentNode,mPlan=MAP.querySelector('path[stroke-dasharray="2 12"]');
const vanPath=mRoutes[1],VL=vanPath.getTotalLength();
function mapAnim(t){
  mRoutes.forEach((r,i)=>r.setAttribute('stroke-dashoffset',1-P(t,48.8+i*.5,1.0,EZ.io)));mPlan.setAttribute('opacity',P(t,49.8,.5));
  mPins.forEach((p,i)=>{const s=P(t,48.6+i*.12,.45,EZ.spring);p.g.setAttribute('transform',`translate(${p.x} ${p.y-(1-clamp(s))*30}) scale(${Math.max(.001,s)})`);p.g.setAttribute('opacity',clamp((t-48.6-i*.12)/.1))});
  const v=lerp(.05,1,P(t,49.5,2.9,EZ.io)),pt=vanPath.getPointAtLength(v*VL);mVan.setAttribute('transform',`translate(${pt.x} ${pt.y})`);mEta.setAttribute('transform',`translate(${pt.x+18} ${pt.y-50})`);
  mVan.setAttribute('opacity',P(t,49.4,.3));mEta.setAttribute('opacity',P(t,49.6,.3));
}
const cityG=mk('g',{});cityG.innerHTML='<defs><pattern id="a3grid" width="40" height="40" patternUnits="userSpaceOnUse"><circle cx="20" cy="20" r="2.2" fill="#d6e7f4"/></pattern></defs><rect x="-3200" y="-1900" width="6400" height="3800" fill="url(#a3grid)"/>';
fx.insertBefore(cityG,fx.firstChild);
const a3logo=$('#a3logo'),pkN=$('#pkN');
function camA3(t,c){
  if(t<33.85)return c;
  const a=P(t,33.85,1.2,EZ.io),b=P(t,WIDEN,1.1,EZ.io),e=P(t,ZOOMOUT,1.5,EZ.io);
  let z=lerp(c.z,1.0,a),cx=lerp(c.cx,0,a),cy=lerp(c.cy,10,a);
  z=lerp(z,.9,b);cy=lerp(cy,36.7,b);z=lerp(z,.5,e);cy=lerp(cy,30,e);
  return {z,cx,cy};
}
function act3(t){
  if(t<33.9){PK.el.style.opacity=0;AG.forEach(o=>o.el.style.opacity=0);TPE.forEach(e=>e.style.opacity=0);cityG.setAttribute('opacity',0);hub.setAttribute('opacity',0);
    [...tpLines,...tpPk,...agLines,...agPk,...hubRip].forEach(e=>e.setAttribute('opacity',0));a3logo.style.opacity=0;return}
  const ps=pkState(t);applyShell(PK,ps,pkState(t-1/60),false);
  PK.ct.style.transform=`translate(-50%,-50%) scale(${PK_K*clamp(Math.min(ps.w/PKW,ps.h/PKH),.05,1)})`;setC2(PK,ps.c2,8*(1-ps.c2),ps.w/PNW);
  if(t<WIDEN+1)pkScreens(t);touchpoints(t,ps);
  if(t>43.4){AG.forEach((o,k)=>{const s=agState(k,t);applyShell(o,s,agState(k,t-1/60),false);
      const ap=P(t,AT[k],.35,EZ.out);o.idle.style.opacity=1-ap;o.act.style.opacity=ap;const bl=ap>0&&ap<1?6*Math.sin(ap*Math.PI):0;o.act.style.filter=bl>.2?`blur(${bl}px)`:'none';
      o.fill.style.setProperty('--p',(o.p*P(t,AT[k]+.1,.7,EZ.out))+'%');
      if(k===4){setC2(o,s.c2||0,8*(1-(s.c2||0)),s.w/1100);o.c2.style.visibility=s.c2>0.001?'visible':'hidden'}})}
  else AG.forEach(o=>o.el.style.opacity=0);
  if(t>48.3)mapAnim(t);
  const hs=P(t,44.0,.5,EZ.spring)*(1-P(t,EXPAND-.1,.3,EZ.in));let hb=0;AT.forEach(a=>hb+=bump(t,a-.4,.3));
  hub.setAttribute('transform',`translate(0 ${HUBY}) scale(${hs*(1+.12*hb)})`);hub.setAttribute('opacity',hs>0.01?1:0);
  AG.forEach((o,k)=>{const top=AGY-AGH/2-8,lp=P(t,AT[k]-.55,.3,EZ.out),fade=1-P(t,EXPAND-.1,.3,EZ.lin);
    setL(agLines[k],0,HUBY+34,AGX[k],top);agLines[k].setAttribute('stroke-dashoffset',1-lp);agLines[k].setAttribute('opacity',lp>0?.8*fade:0);
    const pk=P(t,AT[k]-.3,.3,EZ.io);setC(agPk[k],lerp(0,AGX[k],pk),lerp(HUBY+34,top,pk),8,pk>0&&pk<1?1:0);
    const rp=clamp((t-AT[k]+.4)/.8);setC(hubRip[k],0,HUBY,30+60*EZ.out(rp),rp>0&&rp<1?.3*(1-rp):0)});
  cityG.setAttribute('opacity',P(t,ZOOMOUT,.9));
  a3logo.style.opacity=P(t,34.8,.6)*(1-P(t,WIDEN-.2,.4));a3logo.style.transform=`translateY(${(1-P(t,34.8,.6))*-12}px)`;
  if(pkN)pkN.textContent=Math.round(10*P(t,35.4,1.3,EZ.out));
}
document.fonts&&document.fonts.ready.then(()=>{AGH=AG[0].ct.offsetHeight||230});
'''
