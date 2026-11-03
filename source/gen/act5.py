"""Act 5 · Scale and vision (75–115s): 9 segments around the pulse, 10 three numbers, 11 logo ring, 12 India → globe → end card."""
from base import *
from s4 import endcard

SEGS=[('Hospitals','hospital','lav','Beds, queues, follow-ups'),('Labs','lab','aqua','Bookings, pickups, reports'),
      ('Wellness','wellness','mint','Habits, coaching, streaks'),('Insurance','insurance','sun','Claims, renewals, care')]
segs=''.join(f'<div class="a5-seg" id="a5s{k}"><div class="hd-seg hd-seg--{t}">{well(i,"white")}<div class="hd-seg__t">{n}</div><div class="hd-seg__s">{s}</div></div></div>' for k,(n,i,t,s) in enumerate(SEGS))
RING=[('pathkind','Pathkind'),('habuild','Habuild'),('maha','Government of Maharashtra'),('nha','NHA'),('clearmedi','ClearMedi'),('onemg','1mg'),('redcliffe','Redcliffe'),('drlal','Dr. B. Lal Clinical Laboratory'),(None,'and more')]
ring=''.join(f'<div class="a5-lt" id="a5l{k}"><div class="hd-logotile{" hd-logotile--navy" if key=="clearmedi" else ""}">'
             + (logo(key,n) if key else '<span class="a5-more">& more</span>') + '</div></div>' for k,(key,n) in enumerate(RING))
CORE=f'<div class="a5-core" id="a5core">{logo("heydoc","HeyDoc AI")}</div>'
import json as _json
CBIMG=_json.load(open('../cb/cb.json'))['brain']
# company brain app (user's screenshot, client branding painted out) in a browser window; cards = the 9 agent tiles, in % of the image
CBCARDS=[(x0,y0) for y0 in (793,952,1110) for x0 in (602,878,1153,1429)][:9]
cards_hl=''.join(f'<i class="a5-cbhl" style="left:{x/20:.2f}%;top:{y/16.55:.2f}%;width:{255/20:.2f}%;height:{137/16.55:.2f}%"></i>' for x,y in CBCARDS)
WIN=(f'<div class="a5-win"><div class="a5-wbar"><i style="background:#ff5f57"></i><i style="background:#febc2e"></i><i style="background:#28c840"></i>'
     f'<span class="a5-url">{ic("search","12px")}heydoc.co.in/company-brain</span></div>'
     f'<div class="a5-wvp"><div class="a5-wpg"><img src="{CBIMG}" alt="HeyDoc company brain">'
     f'<span class="a5-cblogo">{logo("heydoc","HeyDoc AI")}</span><span class="a5-cbname">Admin</span>'
     f'<span class="a5-cbans">Two programs slipped this week; vendor follow-ups assigned.</span>{cards_hl}</div></div></div>')
cbsh=(f'<div class="sh a5-cbsh" id="sh-cb"><div class="sh-bg"></div><div class="sh-orb"></div><div class="sh-ring"></div>'
      f'<div class="sh-clip"><div class="sh-content">{WIN}</div></div></div>')
WORLD='<svg id="fx5" width="1" height="1" style="position:absolute;left:0;top:0;overflow:visible"></svg>'+segs+ring+CORE+cbsh

NUMS=[('35','+','agents live'),('15','M+','agentic interactions a month'),('15','M+','people reached')]
nums=''.join(f'<div class="a5-n" id="a5n{k}"><div class="hd-counter a5-part" style="--cnt-fs:280px"><span class="hd-counter__num">0</span><span class="hd-counter__unit">{u}</span></div><div class="a5-lab a5-part">{l}</div></div>' for k,(v,u,l) in enumerate(NUMS))
OVER=f'''<div class="a5-nums" id="a5nums"><div class="hd-kicker a5-part" id="a5k">Last 3 months</div>{nums}</div>
<div class="a5-side a5-side--l" id="a5sl"><div class="hd-kicker a5-sp">Where we're going</div><div class="hd-headline a5-sp">For India, <em>and for the world.</em></div><div class="hd-subline a5-sp">Proven in India.<br>The US next, then global.</div></div>
<div class="a5-side a5-side--r" id="a5sr">
 <div class="a5-step a5-sp" id="a5m0"><span class="a5-step__n">01</span><div><div class="a5-step__t">India</div><div class="a5-step__s">Live today</div></div><span class="a5-chip a5-chip--live">Live</span></div>
 <div class="a5-step a5-sp" id="a5m1"><span class="a5-step__n">02</span><div><div class="a5-step__t">United States</div><div class="a5-step__s">Our next market</div></div><span class="a5-chip a5-chip--next">Next</span></div>
 <div class="a5-step a5-sp" id="a5m2"><span class="a5-step__n">03</span><div><div class="a5-step__t">Europe &amp; GCC</div><div class="a5-step__s">Then global</div></div><span class="a5-chip">Then</span></div>
</div>
<div class="a5-end" id="a5end">{endcard(False)}<svg class="a5-endrip" viewBox="-400 -400 800 800"><circle id="a5er0" fill="#139bf5"/><circle id="a5er1" fill="#139bf5"/></svg></div>'''

CSS5=r'''
.a5-cbsh .sh-content{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%)}
.a5-cbsh .sh-bg{background:#fff}
.a5-win{width:1320px;height:800px;background:#fff;display:flex;flex-direction:column}
.a5-wbar{height:44px;flex:none;display:flex;align-items:center;gap:8px;padding:0 16px;background:#f3f5f8;border-bottom:1px solid #e3e8ee;position:relative}
.a5-wbar i{width:12px;height:12px;border-radius:50%;display:block}
.a5-url{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:flex;align-items:center;gap:8px;background:#fff;border-radius:8px;padding:6px 18px;font-size:13px;font-weight:600;color:var(--muted);box-shadow:0 0 0 1px #e3e8ee;min-width:320px;justify-content:center}
.a5-wvp{position:relative;flex:1;overflow:hidden}
.a5-wpg{position:absolute;left:0;top:0;width:100%;will-change:transform}
.a5-wpg>img{display:block;width:100%;height:auto}
.a5-cblogo{position:absolute;left:4.5%;top:1.5%;height:1.9%;display:flex;align-items:center}
.a5-cblogo .hd-logo,.a5-cblogo img{height:100%;width:auto}
.a5-cbname{position:absolute;left:90.1%;top:1.75%;font:500 9.3px 'Poppins','Open Sans',sans-serif;color:#1b1b1b}
.a5-cbans{position:absolute;left:31.1%;top:91.45%;font:400 8.7px 'Poppins','Open Sans',sans-serif;color:#555}
.a5-cbhl{position:absolute;border-radius:8px;pointer-events:none}
.a5-side{position:absolute;top:50%;transform:translateY(-50%);pointer-events:none}
.a5-side--l{left:110px;width:540px;display:flex;flex-direction:column;gap:22px}
.a5-side--l .hd-headline{font-size:60px}.a5-side--l .hd-subline{font-size:26px;max-width:430px}
.a5-side--r{right:110px;width:440px;display:flex;flex-direction:column;gap:18px}
.a5-step{display:flex;align-items:center;gap:20px;padding:22px 26px;border-radius:24px;background:#fff;box-shadow:var(--shadow-layered);border:1px solid var(--line)}
.a5-step>div{flex:1}
.a5-step__n{font-size:20px;font-weight:800;color:var(--pale);letter-spacing:1px}
.a5-step__t{font-size:30px;font-weight:700;color:var(--navy);line-height:1.15}
.a5-step__s{font-size:19px;color:var(--muted);margin-top:4px}
.a5-chip{font-size:17px;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:8px 16px;border-radius:999px;background:var(--tint);color:var(--blue)}
.a5-chip--live{background:var(--blue);color:#fff}
.a5-chip--next{background:#fff;color:var(--blue);box-shadow:inset 0 0 0 2px var(--blue)}
.a5-step.is-on{border-color:var(--pale)}.a5-step.is-on .a5-step__n{color:var(--blue)}
.a5-sp{will-change:transform,opacity,filter;opacity:0}
.a5-seg{position:absolute;left:0;top:0;width:360px;will-change:transform}
.a5-seg .hd-seg{box-shadow:var(--shadow-layered);min-height:280px}.a5-seg .hd-seg__t{font-size:32px}.a5-seg .hd-seg__s{font-size:18px}
.a5-lt{position:absolute;left:0;top:0;width:190px;will-change:transform}
.a5-lt .hd-logotile{height:76px;box-shadow:var(--shadow-layered)}
.a5-more{font-size:20px;font-weight:800;color:var(--blue)}
.a5-core{position:absolute;left:0;top:0;width:250px;height:250px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;
  box-shadow:0 0 0 3px #8fcdf8,0 0 0 22px var(--tint),0 0 0 44px rgba(238,247,253,.55),var(--shadow-glow)}
.a5-core .hd-logo{width:76%;height:auto}.a5-core .hd-logo img{width:100%;height:auto}
.a5-nums{position:absolute;inset:0;pointer-events:none}
.a5-nums .hd-kicker{position:absolute;left:0;right:0;top:395px;text-align:center;font-size:26px;letter-spacing:4px}
.a5-n{position:absolute;left:0;right:0;top:430px;display:flex;flex-direction:column;align-items:center;gap:6px}
.a5-lab{font-size:46px;font-weight:700;color:var(--navy)}
.a5-part{will-change:transform,opacity,filter;opacity:0}
.a5-end{position:absolute;inset:0;opacity:0;pointer-events:none}
.a5-end .hd-end{position:absolute;inset:0}
.a5-endrip{position:absolute;left:960px;top:420px;width:800px;height:800px;transform:translate(-50%,-50%);overflow:visible}
.a5-end .hd-end__lockup,.a5-end .hd-end__tag,.a5-end .hd-end__url,.a5-end .hd-end__bg{will-change:transform,opacity,filter}
.t-top{left:120px;right:120px;top:84px;text-align:center}
'''

JS5=r'''
/* =================== ACT 5 · SCALE & VISION =================== */
const INDIA_D=__INDIA__;
const S9=75, S10=84, S11=94, S12=104, GLOBE=106.9, ENDC=111.4;
const fx5=$('#fx5');const mk5=(tag,at)=>{const e=document.createElementNS(NS,tag);for(const k in at)e.setAttribute(k,at[k]);fx5.appendChild(e);return e};
/* India dot map + globe (built first so they sit under everything else in fx5) */
const IS=10.5,MHU={x:21,y:47},IC={x:(33.5-MHU.x)*IS,y:(37-MHU.y)*IS};
const indG=mk5('g',{});indG.innerHTML=`<path d="${INDIA_D}" fill="#eef7fd" stroke="#0873ba" stroke-width=".28" stroke-linejoin="round"/>`;
const indDots=document.createElementNS(NS,'g');indG.appendChild(indDots);const ID=[];
(function(){const ctx=document.createElement('canvas').getContext('2d'),path=new Path2D(INDIA_D);
  for(let v=.6;v<74;v+=1.15)for(let u=.6;u<67;u+=1.15){const x=u+(Math.round(v/1.15)%2)*.57;if(ctx.isPointInPath(path,x,v)){const c=document.createElementNS(NS,'circle');c.setAttribute('cx',x);c.setAttribute('cy',v);c.setAttribute('fill','#139bf5');indDots.appendChild(c);ID.push({c,d:Math.hypot(x-MHU.x,v-MHU.y)})}}})();
const GR=380,GC={x:IC.x,y:IC.y},D2R=Math.PI/180;
/* dot globe: real land points, orthographic projection, rotates India -> the world */
const GL=__GLAND__,GD=[];for(let i=0;i<GL.length;i+=3)GD.push({la:GL[i]/10*D2R,lo:GL[i+1]/10*D2R,g:GL[i+2]});
const V0={lo:80,la:18},V1={lo:2,la:27};               // view centre: India first, then the world
function gview(t){const r=P(t,GLOBE+.95,1.5,EZ.io);return {lo:lerp(V0.lo,V1.lo,r)-1.2*Math.max(0,t-GLOBE-2.45),la:lerp(V0.la,V1.la,r)}}
function gproj(la,lo,v,h=1){const l0=v.lo*D2R,p0=v.la*D2R,dl=lo-l0,cl=Math.cos(la);
  return {x:GR*h*cl*Math.sin(dl),y:-GR*h*(Math.cos(p0)*Math.sin(la)-Math.sin(p0)*cl*Math.cos(dl)),z:Math.sin(p0)*Math.sin(la)+Math.cos(p0)*cl*Math.cos(dl)}}
const gvec=(la,lo)=>[Math.cos(la)*Math.cos(lo),Math.cos(la)*Math.sin(lo),Math.sin(la)];
const gang=(a,b)=>Math.acos(Math.max(-1,Math.min(1,a[0]*b[0]+a[1]*b[1]+a[2]*b[2])));
const globeG=mk5('g',{});
globeG.innerHTML=`<circle r="${GR+34}" fill="none" stroke="#eef7fd" stroke-width="40"/><circle r="${GR}" fill="url(#a5glg)" stroke="#8fcdf8" stroke-width="3"/>
<defs><radialGradient id="a5glg" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#fff"/><stop offset=".6" stop-color="#f4faff"/><stop offset="1" stop-color="#ddeffc"/></radialGradient></defs>`;
const gpath=(st,w)=>{const p=document.createElementNS(NS,'path');p.setAttribute('fill','none');p.setAttribute('stroke',st);p.setAttribute('stroke-width',w);p.setAttribute('stroke-linecap','round');globeG.appendChild(p);return p};
const LP={rim:gpath('#e1eef8',7),base:gpath('#c3dcef',7.5),lit:gpath('#139bf5',8),ind:gpath('#0873ba',8)};
const GIN_LL=[21.5*D2R,78.5*D2R];
const ROUTES=[{to:[39.0,-77.0],g:4,t0:GLOBE+1.55,d:1.05,lab:'US · next',main:1},{to:[50.1,8.7],g:3,t0:GLOBE+2.35,d:.75,lab:'Europe'},{to:[24.7,46.7],g:2,t0:GLOBE+2.55,d:.65,lab:'GCC'}];
const GHOME={g:1,lab:'India · live',t0:GLOBE+.75};
ROUTES.forEach(r=>{r.la=r.to[0]*D2R;r.lo=r.to[1]*D2R;r.v=gvec(r.la,r.lo);r.land=r.t0+r.d;r.ang=gang(gvec(...GIN_LL),r.v)});
GD.forEach(d=>{d.v=gvec(d.la,d.lo);const r=ROUTES.find(r=>r.g===d.g);d.lt=r?r.land+gang(d.v,r.v)*2.2:0});
ROUTES.forEach(r=>{r.path=gpath(r.main?'#0873ba':'#139bf5',r.main?4.5:3.5);
  r.head=document.createElementNS(NS,'circle');r.head.setAttribute('fill','#fff');r.head.setAttribute('stroke',r.main?'#0873ba':'#139bf5');r.head.setAttribute('stroke-width',4);globeG.appendChild(r.head)});
const gpin=()=>{const g=document.createElementNS(NS,'g');g.innerHTML='<circle class="rp" fill="#139bf5"/><circle class="pn" fill="#0873ba" stroke="#fff" stroke-width="4"/>';globeG.appendChild(g);return g};
const glabel=(txt,main)=>{const g=document.createElementNS(NS,'g');const w=txt.length*(main?14:12.5)+34,h=main?46:40;
  g.innerHTML=`<rect x="${-w/2}" y="${-h/2}" width="${w}" height="${h}" rx="${h/2}" fill="${main?'#0873ba':'#fff'}" stroke="${main?'#0873ba':'#d6e7f4'}" stroke-width="2"/><text text-anchor="middle" dy=".35em" font-size="${main?24:21}" font-weight="700" fill="${main?'#fff':'#012b44'}">${txt}</text>`;globeG.appendChild(g);return g};
[GHOME,...ROUTES].forEach(r=>{r.pin=gpin();r.lb=glabel(r.lab,r.main)});
GHOME.la=GIN_LL[0];GHOME.lo=GIN_LL[1];
const _g0=gproj(19*D2R,75*D2R,V0);const GIN={x:GC.x+_g0.x,y:GC.y+_g0.y};   // Maharashtra on the globe = where the India map lands
const A5SL=[...$$('#a5sl .a5-sp')],A5S=[0,1,2].map(k=>$('#a5m'+k));
function sides(t){const o=P(t,ENDC-.2,.5,EZ.in);
  A5SL.forEach((e,j)=>inout(e,t,GLOBE+.5+j*.18,ENDC-.25+j*.04));
  const on=[GLOBE+.85,ROUTES[0].t0+ROUTES[0].d,ROUTES[1].t0+ROUTES[1].d];
  A5S.forEach((e,k)=>{inout(e,t,on[k]-.15,ENDC-.2+k*.05);e.classList.toggle('is-on',t>=on[k]);
    if(t>on[k]-.15&&t<ENDC)e.style.transform+=` scale(${1+.03*bump(t,on[k]+.1,.35)})`})}
/* links, packets, ripples, pulse */
const SEGP=[{x:-540,y:-170},{x:540,y:-170},{x:-540,y:200},{x:540,y:200}];
const sLines=SEGP.map(()=>mk5('line',{stroke:'#139bf5','stroke-width':3.5,'stroke-linecap':'round',pathLength:1,'stroke-dasharray':1}));
const sPk=SEGP.map(()=>mk5('circle',{r:9,fill:'#3fd4f6',stroke:'#fff','stroke-width':3}));
const rip5=[...Array(8)].map(()=>mk5('circle',{fill:'#139bf5'}));
const core5=mk5('g',{});core5.innerHTML='<circle r="80" fill="#139bf5" opacity=".12"/><circle r="64" fill="#eef7fd"/><circle r="50" fill="url(#hdorb)"/><circle r="13" fill="#fff"/>';
const SEG=SEGP.map((p,k)=>({el:$('#a5s'+k),seg:$('#a5s'+k+' .hd-seg')}));
const LT=[...Array(9).keys()].map(k=>$('#a5l'+k));const CORE5=$('#a5core');
const FIRE9=[76.7,77.05,77.4,77.75],REFIRE=79.05,LAND=[85.3,88.5,91.7];
/* pulse position/scale over the act */
/* scene 9b · company brain window: pulse -> browser window -> scroll -> back to pulse */
const CB=(()=>{const el=$('#sh-cb');return {el,ct:el.querySelector('.sh-content'),bg:el.querySelector('.sh-bg'),orb:el.querySelector('.sh-orb'),ring:el.querySelector('.sh-ring')}})();
const CBPG=$('#sh-cb .a5-wpg'),CBHL=[...$$('#sh-cb .a5-cbhl')];const WO=79.35,WC=82.85,WW=1320,WH=800,WY=-30;
function cbState(t){const e=P(t,WO,.85,EZ.soft),c=P(t,WC,.55,EZ.io);
  const st={x:0,y:lerp(0,WY,e*(1-c)),rot:0,s:1,sat:1,ring:0,ringA:0,op:t<WO||t>WC+.6?0:1};
  const m=e*(1-c);st.w=lerp(100,WW,m);st.h=lerp(100,WH,m);st.r=lerp(50,18,m);
  st.orb=1-P(t,WO+.1,.35,EZ.lin)+P(t,WC+.2,.3,EZ.lin);st.bg=1;st.cop=P(t,WO+.35,.45,EZ.out)*(1-P(t,WC,.25,EZ.in));st.cb=8*(1-st.cop);
  return st}
function cbWin(t){if(t<WO-.1||t>WC+.7){CB.el.style.opacity=0;return}
  applyShell(CB,cbState(t),cbState(t-1/60),false);
  const y=lerp(0,255,P(t,80.45,.9,EZ.io))+lerp(0,80,P(t,82.0,.6,EZ.io));CBPG.style.transform=`translateY(${-y}px)`;
  CBHL.forEach((h,k)=>{const f=81.25+k*.07,rp=clamp((t-f)/.8);h.style.boxShadow=rp>0&&rp<1?`0 0 0 2px rgba(19,155,245,${.9*(1-rp)}),0 0 0 ${10*EZ.out(rp)}px rgba(19,155,245,${.3*(1-rp)})`:'none'})}
function pulse5(t){
  let x=0,y=0,s=1;
  const up=P(t,83.5,.9,EZ.io),dn=P(t,93.3,.9,EZ.io);y=lerp(0,-235,up);s=lerp(1,.55,up);y=lerp(y,0,dn);s=lerp(s,1,dn);
  let fire=0;FIRE9.forEach(f=>fire+=bump(t,f-.4,.3));fire+=bump(t,REFIRE,.4);LAND.forEach(f=>fire+=bump(t,f,.35));fire+=.6*bump(t,104.5,.4);
  s*=1+.08*fire+.025*Math.sin(t*2.6)*(t>94&&t<104?1:0);
  const toCore=P(t,94.25,.5,EZ.out),back=P(t,103.6,.5,EZ.out);const vis=(1-toCore)+back;
  const outG=P(t,GLOBE,.6,EZ.in);
  const win=t>WO+.05&&t<WC+.6?1:0;s*=1-win;
  return {x,y,s:s*clamp(vis)*(1-outG),core:toCore*(1-back)};
}
function ripplesAt(t){
  // [time, x, y, r0, grow, alpha]
  const R=[];const p0=pulse5(t);
  FIRE9.forEach((f,k)=>R.push([f+.35,SEGP[k].x,SEGP[k].y,40,170,.25]));
  [REFIRE,REFIRE+.35].forEach(f=>R.push([f,0,0,50,260,.22]));
  LAND.forEach(f=>R.push([f,0,-235,30,220,.25]));
  [104.5,104.9,105.3].forEach(f=>R.push([f,0,0,50,1100,.18]));
  return R;
}
function act5(t){
  if(t<74.8){[indG,globeG,core5,...sLines,...sPk,...rip5].forEach(e=>e.setAttribute('opacity',0));SEG.forEach(s=>s.el.style.opacity=0);LT.forEach(e=>e.style.opacity=0);CORE5.style.opacity=0;CB.el.style.opacity=0;$('#a5end').style.opacity=0;return}
  // hand-off: hide act 4 pulse (same place/size as ours)
  pulseG.setAttribute('opacity',0);pRip.forEach(c=>c.setAttribute('opacity',0));
  const p=pulse5(t);core5.setAttribute('transform',`translate(${p.x} ${p.y}) scale(${Math.max(.001,p.s)})`);core5.setAttribute('opacity',p.s>.01?1:0);
  /* scene 9 · segment tiles */
  SEG.forEach((s,k)=>{const a=75.5+k*.15,P0=SEGP[k],e=P(t,a,.9,EZ.soft),cl=P(t,79.25+k*.05,.5,EZ.in);
    const x=lerp(0,P0.x,e),y=lerp(0,P0.y,e),sc=lerp(.3,1,P(t,a,.7,EZ.spring))*(1-.15*cl)*(1+.05*bump(t,FIRE9[k]+.35,.45)+.04*bump(t,REFIRE+.3,.45));
    const bl=8*(1-P(t,a,.45))+10*cl;s.el.style.transform=`translate(${x}px,${y}px) translate(-50%,-50%) scale(${sc})`;s.el.style.opacity=clamp((t-a)/.15)*(1-cl);s.el.style.filter=bl>.2?`blur(${bl}px)`:'none';
    const lp=P(t,FIRE9[k]-.45,.35,EZ.out),fade=1-P(t,79.1,.4,EZ.lin);const D=Math.hypot(P0.x,P0.y),ux=P0.x/D,uy=P0.y/D;
    setL(sLines[k],ux*70,uy*70,P0.x-ux*200,P0.y-uy*150);sLines[k].setAttribute('stroke-dashoffset',1-lp);sLines[k].setAttribute('opacity',lp>0?.85*fade:0);
    const pk=P(t,FIRE9[k],.35,EZ.io);setC(sPk[k],lerp(ux*70,P0.x-ux*200,pk),lerp(uy*70,P0.y-uy*150,pk),9,pk>0&&pk<1?1:0);
    s.seg.style.boxShadow=t>FIRE9[k]+.35&&t<79.3?`0 0 0 ${30*EZ.out(clamp((t-FIRE9[k]-.35)/.8))}px rgba(19,155,245,${.3*(1-clamp((t-FIRE9[k]-.35)/.8))}),var(--shadow-layered)`:'var(--shadow-layered)'});
  /* ripples */
  const R=ripplesAt(t);rip5.forEach((c,j)=>{const r=R.filter(q=>t>=q[0]&&t<q[0]+1.2).slice(0,8)[j];if(!r){c.setAttribute('opacity',0);return}const rp=(t-r[0])/1.2;setC(c,r[1],r[2],r[3]+r[4]*EZ.out(rp),r[5]*(1-rp))});
  /* scene 10 · three numbers */
  inout($('#a5k'),t,84.1,93.2);
  NUMS.forEach((n,k)=>{const a=LAND[k]-1.1,b=k<2?LAND[k+1]-1.35:93.25;const parts=n.el.querySelectorAll('.a5-part');
    inout(parts[0],t,a,b,40);inout(parts[1],t,a+.3,b+.03);
    const sh=P(t,93.25,.6,EZ.in);if(k===2&&t>93.2){parts[0].style.transform=`translateY(${-235*sh*.0}px) scale(${1-.9*sh})`;parts[0].style.opacity=1-sh;parts[0].style.filter=`blur(${6*sh}px)`}
    n.num.textContent=Math.round(n.v*P(t,a+.05,1.05,EZ.out));parts[0].style.transform+=` scale(${1+.05*bump(t,LAND[k],.35)})`});
  /* scene 11 · logo ring */
  const RR=340,cy=0,rot=(t-94)*7*Math.PI/180;
  LT.forEach((e,k)=>{const a=94.6+k*.07,base=-Math.PI/2+k*2*Math.PI/9,ent=P(t,a,1.0,EZ.soft),ex=P(t,103.4+k*.03,.8,EZ.in);
    const ang=base+rot-(1-ent)*.6+ex*1.2,r=RR*ent*(1-ex);
    const x=Math.cos(ang)*r,y=cy+Math.sin(ang)*r,sc=lerp(.5,1,ent)*(1-.7*ex);
    e.style.transform=`translate(${x}px,${y}px) translate(-50%,-50%) scale(${sc})`;e.style.opacity=clamp((t-a)/.2)*(1-P(t,103.9+k*.03,.3,EZ.lin));
    const bl=8*(1-P(t,a,.5))+8*ex;e.style.filter=bl>.2?`blur(${bl}px)`:'none'});
  const cs=p.core;CORE5.style.transform=`translate(0px,0px) translate(-50%,-50%) scale(${.4+.6*cs*(1+.02*Math.sin(t*2.2))})`;CORE5.style.opacity=cs;CORE5.style.filter=cs<.98?`blur(${8*(1-cs)}px)`:'none';
  /* scene 12 · India, then globe */
  const iA=P(t,104.4,.8,EZ.out),iO=P(t,GLOBE,1.0,EZ.io);
  if(t>104.2){const sc=IS*lerp(.9,1,iA)*lerp(1,.25,iO),tx=lerp(0,GIN.x,iO),ty=lerp(0,GIN.y,iO);
    indG.setAttribute('transform',`translate(${tx} ${ty}) scale(${sc}) translate(${-MHU.x} ${-MHU.y})`);indG.setAttribute('opacity',iA*(1-P(t,GLOBE+.6,.45,EZ.lin)));
    ID.forEach(d=>{const th=104.6+d.d/60*1.6,s=P(t,th,.35,EZ.spring);d.c.setAttribute('r',Math.max(0,.36*s));d.c.setAttribute('opacity',clamp((t-th)/.1))})}
  else indG.setAttribute('opacity',0);
  globeFrame(t);sides(t);cbWin(t);
  /* end card */
  const E=$('#a5end');E.style.opacity=P(t,ENDC+.3,.6,EZ.out);
  const lk=E.querySelector('.hd-end__lockup'),tg=E.querySelector('.hd-end__tag'),ur=E.querySelector('.hd-end__url'),bg=E.querySelector('.hd-end__bg');
  const l=P(t,ENDC+.6,1.2,EZ.out);lk.style.transform=`scale(${.96+.04*l})`;lk.style.opacity=l;lk.style.filter=l<.98?`blur(${8*(1-l)}px)`:'none';
  inout(tg,t,ENDC+1.0,999);inout(ur,t,ENDC+1.4,999);bg.style.opacity=P(t,ENDC+.4,.8);
  ['#a5er0','#a5er1'].forEach((id,j)=>{const rp=clamp((t-ENDC-.8-j*.35)/1.4);const c=$(id);c.setAttribute('r',120+260*EZ.out(rp));c.setAttribute('opacity',rp>0&&rp<1?.18*(1-rp):0)});
}
const NUMS=[35,15,15].map((v,k)=>({v,el:$('#a5n'+k),num:$('#a5n'+k+' .hd-counter__num')}));
function globeFrame(t){
  const gA=P(t,GLOBE,.7,EZ.out),gO=P(t,ENDC,.9,EZ.in);
  if(gA<=0||gO>=1){globeG.setAttribute('opacity',0);return}
  globeG.setAttribute('transform',`translate(${GC.x} ${GC.y}) scale(${lerp(.94,1,gA)*(1-.5*gO)})`);globeG.setAttribute('opacity',gA*(1-gO));
  const v=gview(t),B={rim:'',base:'',lit:'',ind:''},iOn=P(t,GLOBE+.45,.5);
  for(const d of GD){const p=gproj(d.la,d.lo,v);if(p.z<.04)continue;
    const k=(d.g===1&&iOn>.5)?'ind':(d.g>1&&t>d.lt)?'lit':(p.z<.32?'rim':'base');B[k]+=`M${p.x.toFixed(1)} ${p.y.toFixed(1)}h0`}
  for(const k in B)LP[k].setAttribute('d',B[k]);
  const sa=gvec(...GIN_LL);
  ROUTES.forEach(r=>{const pr=P(t,r.t0,r.d,EZ.io);let d='',hd=null,pen=0;
    if(pr>0){const N=44,n=Math.ceil(N*pr),A=r.ang,sA=Math.sin(A),lift=.1+.22*A/Math.PI;
      for(let i=0;i<=n;i++){const u=Math.min(i/N,pr),f0=Math.sin((1-u)*A)/sA,f1=Math.sin(u*A)/sA,w=[sa[0]*f0+r.v[0]*f1,sa[1]*f0+r.v[1]*f1,sa[2]*f0+r.v[2]*f1];
        const q=gproj(Math.asin(w[2]),Math.atan2(w[1],w[0]),v,1+lift*Math.sin(Math.PI*u));const hid=q.z<0&&Math.hypot(q.x,q.y)<GR;
        if(hid){pen=0;hd=null;continue}d+=(pen?'L':'M')+q.x.toFixed(1)+' '+q.y.toFixed(1);pen=1;hd=q}}
    r.path.setAttribute('d',d||'M0 0');r.path.setAttribute('opacity',pr>0?.95:0);
    const hv=pr>0&&pr<1;r.head.setAttribute('r',hv?7:0);if(hd){r.head.setAttribute('cx',hd.x);r.head.setAttribute('cy',hd.y)}});
  [GHOME,...ROUTES].forEach(r=>{const a=r.land||r.t0,q=gproj(r.la,r.lo,v),vis=q.z>.05?1:0,ps=P(t,a,.45,EZ.spring),rp=clamp((t-a)/1.1);
    r.pin.setAttribute('transform',`translate(${q.x} ${q.y})`);r.pin.setAttribute('opacity',vis);
    const pn=r.pin.querySelector('.pn'),rpE=r.pin.querySelector('.rp');pn.setAttribute('r',Math.max(0,(r.main?11:9)*ps));
    rpE.setAttribute('r',12+(r.main?90:60)*EZ.out(rp));rpE.setAttribute('opacity',rp>0&&rp<1?.28*(1-rp):0);
    const lp=P(t,a+.15,.5,EZ.out),pulse=r.main?1+.04*Math.sin((t-a)*5)*(t>a+.6?1:0):1;
    r.lb.setAttribute('transform',`translate(${q.x} ${q.y-(r.main?52:44)-10*(1-lp)}) scale(${pulse})`);r.lb.setAttribute('opacity',lp*vis)});
}
function camA5(t,c){
  if(t<74.8)return c;
  const a=P(t,74.8,.8,EZ.io);let z=lerp(c.z,1,a),cx=lerp(c.cx,0,a),cy=lerp(c.cy,70,a);
  const r=P(t,S11-.4,1.0,EZ.io);cy=lerp(cy,-40,r);z=lerp(z,.98,r);
  const i=P(t,S12,1.6,EZ.io);z=lerp(z,.8,i);cx=lerp(cx,IC.x,i);cy=lerp(cy,IC.y+25,i);
  return {z,cx,cy};
}
'''
