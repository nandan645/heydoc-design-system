"""Act 2 · Habuild (16–34s): scene 3 (16–27) Habuild screens + hopping pulse, scene 4 (27–34) dot crowd + ₹300 Cr."""
from base import *

import json as _j, os as _o
HBIMG=_j.load(open(_o.path.join(SP,'hb','hb.json')))   # Habuild app screenshots supplied by the team (screen area only)
def hl(x0,y0,x1,y1,r,cls=''):
    return f'<i class="a2-hl {cls}" style="left:{x0}%;top:{y0}%;width:{x1-x0}%;height:{y1-y0}%;border-radius:{r}"></i>'
def shot(key, extra=''):
    return f'<div class="a2-shot"><img src="{HBIMG[key]}" alt="Habuild app screen">{extra}</div>'
# chat screen: a scrolling viewport (copy of the screenshot) so a new message can push the thread up
VP_T,VP_B=24.6,80.6
def _vp(inner):
    h=VP_B-VP_T
    return (f'<div class="a2-vp" style="top:{VP_T}%;height:{h}%"><div class="a2-vin" style="top:{-VP_T/h*100:.3f}%;height:{100/h*100:.3f}%">'
            f'<img src="{HBIMG["chat"]}" alt="">'
            f'<div class="a2-fill"><img src="{HBIMG["chat"]}" alt=""></div>{inner}</div></div>')
UPSELL=('<span class="a2-av a2-av2"><span></span></span>'
  '<div class="a2-up">'
  '<div class="a2-uph"><span class="a2-uppill">'+ic('spark','1em')+'You\'re doing great</span>'
  '<div class="a2-upt1">Unlock <b>Habuild Nutrition Plus</b></div><div class="a2-ups">Smarter meal plans, built around your goals.</div>'
  '<span class="a2-upcrown">'+ic('spark','1.5em','1.8')+'</span></div>'
  '<div class="a2-upl">'
  + ''.join(f'<div class="a2-upr"><span class="a2-upck">{ic("check",".8em","3")}</span>{x}</div>' for x in ['Unlimited meal swaps','Weekly plans, ready every Sunday','Priority support from your coach'])
  + '</div><div class="a2-upbtn">Continue · ₹499/month <span>→</span></div><div class="a2-upno">Not now</div><div class="a2-uptime">5:44 AM</div></div>')
CHAT_X=(_vp('<span class="a2-av"><span></span></span>'
  '<div class="a2-tx a2-tx--b" style="left:14.4%;top:31.7%;width:66%">Your back felt stiff yesterday. Try a short desk stretch at 4 pm.</div>'
  '<div class="a2-tx a2-tx--b" style="left:25.3%;top:43%;width:66%">Done! Remind me again tomorrow?</div>'+UPSELL)+
  '<div class="a2-tx a2-tx--c" style="left:4.4%;top:81.55%;width:34.2%">Plan my dinner</div>'
  '<div class="a2-tx a2-tx--c" style="left:40.4%;top:81.55%;width:34.2%">Add a walk</div>'
  '<div class="a2-tx a2-tx--c" style="left:76.3%;top:81.55%;width:30%;text-align:left;padding-left:4%">Track water</div>'
  '<div class="a2-tx a2-tx--i" style="left:7.9%;top:87.35%;width:60%">Ask Habuild anything…</div>')
SCREENS=[shot('goals', hl(5.1,48.6,95,54.5,'.9em')+hl(5.1,91.4,95,97.4,'2em','a2-press')),
         shot('meal',  hl(5.1,23.3,95,46.9,'1.6em')),
         shot('chat',  CHAT_X),
         shot('profile', hl(4.1,49.7,14.9,59.8,'.8em')+hl(70.8,65.8,95.8,68.3,'2em'))]

def shell(sid, content):
    return (f'<div class="sh a2-sh" id="sh-{sid}"><div class="sh-bg"></div><div class="sh-orb"></div><div class="sh-ring"></div>'
            f'<div class="sh-clip"><div class="sh-content">{content}</div></div></div>')

WORLD=''.join(shell(f'hb{k}', phone(s,'light',cls='hd-ip--img',style='--phone-w:340px')) for k,s in enumerate(SCREENS))

OVER=f'''
<div class="a2-logo" id="a2logo">{logo("habuild","Habuild")}</div>
<div class="a2-big" id="a2big"><div class="a2-veil" id="a2veil"></div>
  <div class="a2-inner">
    <div class="hd-kicker a2-part" id="a2k">1 in 10 subscribing</div>
    <div class="hd-counter a2-part" id="a2cnt" style="--cnt-fs:250px"><span class="hd-counter__pre">₹</span><span class="hd-counter__num" id="a2num">0</span><span class="hd-counter__unit" id="a2unit">&nbsp;Cr</span></div>
    <div class="a2-line a2-part" id="a2line"><span class="w">product</span><span class="w a2-dot">·</span><span class="w"><span class="a2-var" id="a2var">00,000</span></span><span class="w">agent</span><span class="w">conversations</span><span class="w">a</span><span class="w">day</span></div>
  </div>
</div>'''

CSS2=r'''
.a2-sh .hd-phone--light{box-shadow:inset 0 0 0 2px var(--line)}
.hd-ip--img .hd-ip__ov{display:none}
.a2-shot{position:absolute;inset:0;background:#faf8f3}
.a2-shot img{position:absolute;inset:0;width:100%;height:100%;display:block}
.a2-hl{position:absolute;pointer-events:none}
.a2-tx{position:absolute;font-family:'Inter',var(--font);color:#1b1b1b;will-change:transform,opacity}
.a2-tx--b{font-size:.74em;line-height:1.4;font-weight:500}
.a2-tx--c{font-size:.72em;line-height:2.3em;text-align:center;color:#555;font-weight:500}
.a2-tx--i{font-size:.8em;line-height:2.3em;color:#666}
.a2-av{position:absolute;left:2.6%;top:30.15%;width:6%;aspect-ratio:1;border-radius:50%;background:var(--orb);display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 2px #fff}
.a2-av span{width:30%;height:30%;border-radius:50%;background:#fff}
.a2-vp{position:absolute;left:0;right:0;overflow:hidden}
.a2-vin{position:absolute;left:0;right:0;will-change:transform}
.a2-shot .a2-vin>img{position:absolute;inset:0;width:100%;height:100%}
.a2-fill{position:absolute;left:0;right:0;top:80.6%;height:26%;overflow:hidden}
.a2-shot .a2-fill img{position:absolute;left:0;width:100%;height:384.6%;top:-203.8%}
.a2-av2{top:52.6%;opacity:0}
.a2-up{position:absolute;left:11%;top:52%;width:80%;background:#fff;border-radius:1.15em;padding:.5em .5em .35em;box-shadow:0 .25em .9em rgba(var(--partner1-rgb),.14);transform-origin:0 0;opacity:0;font-family:'Inter',var(--font);color:#1b1b1b;will-change:transform,opacity}
.a2-uph{position:relative;border-radius:.85em;padding:.75em .8em .8em;background:linear-gradient(135deg,var(--partner1-deep) 0%,var(--partner1) 60%,var(--partner1-light) 100%);color:var(--partner1-on);overflow:hidden}
.a2-uppill{display:inline-flex;align-items:center;gap:.3em;font-size:.48em;font-weight:700;letter-spacing:.08em;text-transform:uppercase;background:rgba(255,255,255,.18);border-radius:2em;padding:.35em .75em}
.a2-upt1{font-size:.98em;font-weight:500;line-height:1.2;margin-top:.45em;padding-right:1.6em}.a2-upt1 b{font-weight:700;display:block}
.a2-ups{font-size:.58em;line-height:1.35;opacity:.85;margin-top:.35em;padding-right:2em}
.a2-upcrown{position:absolute;right:.55em;top:.55em;width:2.3em;height:2.3em;border-radius:50%;background:#ffcd05;color:#012b44;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 .3em rgba(255,255,255,.18)}
.a2-upl{display:flex;flex-direction:column;gap:.4em;padding:.7em .3em .6em}
.a2-upr{display:flex;align-items:center;gap:.5em;font-size:.66em;font-weight:500;color:#26332b;opacity:0}
.a2-upck{width:1.5em;height:1.5em;border-radius:50%;background:var(--partner1-tint);color:var(--partner1-ink);display:flex;align-items:center;justify-content:center;flex:none}
.a2-upbtn{position:relative;display:flex;align-items:center;justify-content:center;gap:.4em;background:var(--partner1);color:var(--partner1-on);border-radius:2em;font-size:.74em;font-weight:600;padding:.75em 1em}
.a2-upno{text-align:center;font-size:.64em;font-weight:500;color:#5b6b60;padding:.55em 0 .1em}
.a2-uptime{font-size:.48em;color:#666;text-align:right;padding:.1em .3em 0}
.a2-logo{position:absolute;left:72px;top:56px;height:46px;opacity:0}
.a2-logo .hd-logo{height:46px}
.a2-big{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;pointer-events:none}
.a2-veil{position:absolute;inset:0;background:radial-gradient(60% 55% at 50% 50%,rgba(255,255,255,.96) 0%,rgba(255,255,255,.85) 55%,rgba(255,255,255,0) 100%);opacity:0}
.a2-inner{position:relative;display:flex;flex-direction:column;align-items:center;gap:26px;text-align:center}
.a2-big .hd-kicker{font-size:26px;letter-spacing:4px}
.a2-big .hd-counter__unit{font-size:.42em}
.a2-line{display:flex;gap:.28em;align-items:center;font-size:40px;font-weight:700;color:var(--navy)}
.a2-line .w{display:inline-block}
.a2-dot{color:var(--c-text-3)}
.a2-var{display:inline-block;color:var(--blue);font-weight:800;border:3px dashed var(--pale);border-radius:14px;padding:0 14px;background:var(--tint)}
.a2-var.is-set{border:0;background:none;padding:0}
.a2-part{will-change:transform,opacity,filter}
/* ---- Partner 1 accent (Act 2): every shade comes from --partner1 (see brand.py) ---- */
#t5 .hd-headline em,#t5 em,#hbN{color:var(--partner1-ink)}
#a2big .hd-counter,#a2big .hd-counter__unit,#a2big .hd-kicker,#a2big .a2-var{color:var(--partner1-ink)}
#a2big .a2-var{border-color:var(--partner1-pale);background:var(--partner1-tint)}
[id^="sh-hb"] .sh-orb{background:var(--partner1-orb);box-shadow:0 14px 40px rgba(var(--partner1-rgb),.35)}
[id^="sh-hb"] .a2-av,.hd-ip--img .a2-av{background:var(--partner1-orb)}
'''

JS2=r'''
/* =================== ACT 2 · HABUILD =================== */
const VARS={agent_conversations_per_day:null};
const UPSCROLL=16;   // % of the chat thread scrolled when the upsell arrives   // set a number/string here when final
const HX=[-630,-210,210,630], HY=-30, HL=[18.0,19.8,21.6,23.4], ALLFIRE=23.9, SHRINK=26.4, HK=300/340;
const HB=[0,1,2,3].map(k=>{const el=$('#sh-hb'+k);const o={el,ct:el.querySelector('.sh-content'),bg:el.querySelector('.sh-bg'),orb:el.querySelector('.sh-orb'),ring:el.querySelector('.sh-ring')};
  o.ct.style.transform=`translate(-50%,-50%) scale(${HK})`;return o});
/* dot crowd grid (E-06) */
const COLS=48,ROWS=20,GAP=32,GX0=-(COLS-1)*GAP/2,GY0=HY-(ROWS-1)*GAP/2;
const SRC=HX.map(x=>{const c=Math.round((x-GX0)/GAP),r=Math.round((HY-GY0)/GAP);return {c,r,i:r*COLS+c,x:GX0+c*GAP,y:GY0+r*GAP}});
function rng(a){return()=>{a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
const crowdG=mk('g',{});const DOTS=[];
(function(){const R=rng(42),n=COLS*ROWS,idx=[...Array(n).keys()];for(let i=n-1;i>0;i--){const j=Math.floor(R()*(i+1));[idx[i],idx[j]]=[idx[j],idx[i]]}
  const lit=new Set();for(let g=0;g<n/10;g++)lit.add(idx[g*10+Math.floor(R()*10)]);SRC.forEach(s=>lit.add(s.i));
  for(let i=0;i<n;i++){const c=i%COLS,r=Math.floor(i/COLS),x=GX0+c*GAP,y=GY0+r*GAP,d=Math.min(...SRC.map(s=>Math.hypot(s.x-x,s.y-y)));
    const isL=lit.has(i),isS=SRC.some(s=>s.i===i);let h=null;
    if(isL){h=document.createElementNS(NS,'circle');h.setAttribute('fill','none');h.setAttribute('style','stroke:var(--partner1-pale)');h.setAttribute('stroke-width',2.5);crowdG.appendChild(h)}
    const e=document.createElementNS(NS,'circle');crowdG.appendChild(e);
    DOTS.push({x,y,e,h,isL,isS,ta:27.2+d/1500,tl:isS?0:28.35+R()*1.1,ph:R()*6.28,hr:R()})}
})();
fx.appendChild(crowdG);
/* hopping pulse */
const defs=mk('defs',{});defs.innerHTML='<radialGradient id="a2orb" cx=".28" cy=".18" r=".9"><stop offset="0" style="stop-color:var(--partner1-deep)"/><stop offset=".55" style="stop-color:var(--partner1)"/><stop offset="1" style="stop-color:var(--partner1-light)"/></radialGradient><radialGradient id="hdorb" cx=".28" cy=".18" r=".9"><stop offset="0" stop-color="#0a84e8"/><stop offset=".55" stop-color="#2ba7f5"/><stop offset="1" stop-color="#43d0f2"/></radialGradient>';
const arcs=[0,1,2].map(k=>mk('path',{fill:'none',style:'stroke:var(--partner1)','stroke-width':3,'stroke-linecap':'round',pathLength:1,'stroke-dasharray':1,opacity:0}));
const landRip=HL.map(()=>mk('circle',{style:'fill:var(--partner1)'}));
const orbG=mk('g',{});orbG.innerHTML='<circle r="40" style="fill:var(--partner1)" opacity=".14"/><circle r="32" style="fill:var(--partner1-tint)"/><circle r="24" fill="url(#a2orb)"/><circle r="6.5" fill="#fff"/>';
const OTOP=HY-312-46;
arcs.forEach((a,k)=>a.setAttribute('d',`M${HX[k]} ${OTOP} Q${(HX[k]+HX[k+1])/2} ${OTOP-240} ${HX[k+1]} ${OTOP}`));

function hbState(k,t){
  const st={sat:1,ring:0,ringA:0,bg:1,orb:0,cop:1,cb:0,op:1,rot:0,s:1,r:157*300/950,w:300,h:300*1940/950,x:0,y:HY,ringRGB:ACC.partner1.rgb};
  if(k===0){const ci=P(t,16.0,.5,EZ.out);st.cop=ci;st.cb=10*(1-ci);st.op=t<16?0:1;st.x=lerp(0,HX[0],P(t,16.9,.95,EZ.soft))}
  else{const a=16.95+k*.1;st.op=clamp((t-a)/.2);const p=P(t,a,.95,EZ.soft);st.x=lerp(0,HX[k],p);st.s=lerp(.82,1,P(t,a,.7,EZ.spring));st.cb=8*(1-P(t,a,.5))}
  const dim=k===0?P(t,17.0,.4):1,act=P(t,HL[k],.5,EZ.out);st.sat=lerp(1,lerp(.2,1,act),dim);st.op*=lerp(1,lerp(.7,1,act),dim);
  [HL[k],ALLFIRE+k*.06].forEach(f=>{const rp=clamp((t-f)/.8);if(rp>0&&rp<1){st.ring=46*EZ.out(rp);st.ringA=.3*(1-rp)}const b=bump(t,f,.5);st.s*=1+.035*b;st.y-=12*b});
  const S=SHRINK+k*.08,m=P(t,S,.9,EZ.soft),ms=P(t,S,.7,EZ.soft);
  st.w=lerp(300,20,ms);st.h=lerp(300*1940/950,20,ms);st.r=lerp(157*300/950,10,ms);st.x=lerp(st.x,SRC[k].x,m);st.y=lerp(st.y,SRC[k].y,m);st.s=lerp(st.s,1,m);
  const co=P(t,S,.3,EZ.in);st.cop*=1-co;st.cb+=10*co;st.orb=P(t,S+.2,.4);st.bg=1-P(t,S+.3,.4);if(t>S)st.sat=1;
  st.op*=1-P(t,27.45,.15,EZ.lin);
  st.bg=Math.min(st.bg,1-st.cop);
  if(k===0&&t<17)st.bg=0;
  return st;
}
function orbState(t){
  let x=HX[0],y=OTOP;
  for(let k=0;k<3;k++){const h0=HL[k]+1.2,h1=HL[k+1];if(t>=h0){const p=P(t,h0,h1-h0,EZ.io);x=lerp(HX[k],HX[k+1],p);y=OTOP-120*4*p*(1-p)}}
  let sq=0;HL.forEach(L=>sq+=bump(t,L-.05,.3));let st=0;HL.slice(0,3).forEach(L=>st+=bump(t,L+1.15,.25));
  if(t>HL[3]+.3)y+=7*Math.sin((t-HL[3]-.3)*3.6);
  const s=P(t,17.65,.55,EZ.spring)*(1-P(t,26.05,.3,EZ.in));
  return {x,y,s,sx:1+.28*sq-.12*st,sy:1-.24*sq+.18*st};
}
/* in-screen animations, keyed to each landing */
const Q=(k,s)=>[...HB[k].ct.querySelectorAll(s)];
const HLS=[0,1,2,3].map(k=>Q(k,'.a2-hl:not(.a2-press)')),PRESS=Q(0,'.a2-press')[0],CTX=Q(2,'.a2-tx'),AV=Q(2,'.a2-av')[0],AV2=Q(2,'.a2-av2')[0],UP=Q(2,'.a2-up')[0],UPB=Q(2,'.a2-upbtn')[0],UPR=Q(2,'.a2-upr'),VIN=Q(2,'.a2-vin')[0];
const pop=(el,t,a,dy=12)=>{const p=P(t,a,.45,EZ.spring),o=clamp((t-a)/.15);el.style.transform=`translateY(${(1-p)*dy}px) scale(${.92+.08*p})`;el.style.opacity=o};
function ringHL(el,t,a){let sp=0,al=0;[a,a+.55].forEach(f=>{const rp=clamp((t-f)/.8);if(rp>0&&rp<1){sp=Math.max(sp,14*EZ.out(rp));al=Math.max(al,.4*(1-rp))}});
  el.style.boxShadow=al>.002?`0 0 0 2px rgba(${ACC.partner1.rgb},${Math.min(1,al*2.2)}),0 0 0 ${sp}px rgba(${ACC.partner1.rgb},${al})`:'none'}
function screens(t){
  HLS.forEach((arr,k)=>arr.forEach((el,i)=>ringHL(el,t,HL[k]+.15+i*.45)));
  const b=bump(t,HL[0]+1.05,.3);PRESS.style.background=`rgba(0,0,0,${.14*b})`;
  const a2=HL[2]+.1;AV.style.opacity=1;CTX.forEach((e,i)=>pop(e,t,a2+(i<2?i*.45:.9+(i-2)*.08),i<2?10:6));
  {const u=a2+1.0,p=P(t,u,.55,EZ.spring),sc=P(t,u+.05,.7,EZ.soft);
    VIN.style.transform=`translateY(${-sc*UPSCROLL}%)`;
    UP.style.opacity=clamp((t-u)/.15);UP.style.transform=`translateY(${(1-p)*18}px) scale(${.92+.08*p})`;AV2.style.opacity=clamp((t-u)/.15);
    UPR.forEach((r,i)=>pop(r,t,u+.35+i*.12,6));
    ringHL(UPB,t,u+.95);UPB.style.transform=`scale(${1-.05*bump(t,u+1.6,.25)})`}
}
/* colour helper */
const mix=(a,b,p)=>{const A=[parseInt(a.slice(1,3),16),parseInt(a.slice(3,5),16),parseInt(a.slice(5),16)],B=[parseInt(b.slice(1,3),16),parseInt(b.slice(3,5),16),parseInt(b.slice(5),16)];return `rgb(${A.map((v,i)=>Math.round(v+(B[i]-v)*p)).join(',')})`};
function crowd(t){
  if(t<27.0||t>34.9){crowdG.style.display='none';return}crowdG.style.display='';
  crowdG.setAttribute('opacity',1-.8*P(t,29.3,.5,EZ.io)+.8*P(t,32.55,.6,EZ.io));
  const dr=P(t,33.0,1.0,EZ.in),dn=P(t,33.0,.6);
  DOTS.forEach((d,i)=>{const s=d.isS?(t>=27.4?1:0):P(t,d.ta,.45,EZ.spring);
    let x=d.x+dr*150*(.6+.4*d.hr)+dn*8*nz(i,t),y=d.y+dn*8*nz(i+3,t*.8);
    const cv=P(t,33.8+d.hr*.35,.6,EZ.in);x=lerp(x,0,cv);y=lerp(y,HY,cv);
    let r=8*s*(1-.75*cv),fill=mix(ACC.partner1.dot,ACC.partner2.dot,cv),hop=0,hr=0;
    if(d.isL){const lp=d.isS?1:P(t,d.tl,.45,EZ.spring);fill=cv>0?hueMix(ACC.partner1.base,ACC.partner2.base,cv):mix(ACC.partner1.dot,ACC.partner1.base,clamp(lp));r*=1+.25*lp;
      const br=t>29.6?.5+.5*Math.sin((t-29.6)*4.2+d.ph):0;hr=13+4*br;hop=s*clamp(lp)*(.85-.4*br)*(1-cv)}
    d.e.setAttribute('cx',x);d.e.setAttribute('cy',y);d.e.setAttribute('r',Math.max(0,r));d.e.setAttribute('fill',fill);
    if(d.h){d.h.setAttribute('cx',x);d.h.setAttribute('cy',y);d.h.setAttribute('r',hr);d.h.setAttribute('opacity',hop)}});
}
const a2logo=$('#a2logo'),a2veil=$('#a2veil'),a2k=$('#a2k'),a2cnt=$('#a2cnt'),a2num=$('#a2num'),a2unit=$('#a2unit'),a2line=[...$$('#a2line .w')],a2var=$('#a2var'),hbN=$('#hbN');
if(VARS.agent_conversations_per_day!=null){a2var.textContent=VARS.agent_conversations_per_day;a2var.classList.add('is-set')}
const inout=(el,t,a,b,dy=24)=>{const p=P(t,a,.6,EZ.out),q=P(t,b,.4,EZ.in);el.style.transform=`translateY(${24*(1-p)*dy/24-16*q}px)`;el.style.opacity=p*(1-q);const bl=8*(1-p)+8*q;el.style.filter=bl>.2?`blur(${bl}px)`:'none'};
function bigCounter(t){
  a2veil.style.opacity=P(t,29.3,.5)*(1-P(t,32.6,.5));
  inout(a2k,t,29.4,32.45);
  const c=P(t,29.55,1.4,EZ.out);a2num.textContent=Math.round(300*c);a2unit.style.opacity=P(t,30.75,.25);
  inout(a2cnt,t,29.5,32.5,40);a2cnt.style.transform+=` scale(${1+.045*bump(t,30.95,.35)})`;
  a2line.forEach((w,j)=>inout(w,t,30.7+j*.06,32.55+j*.02));
}
function act2(t){
  HB.forEach((o,k)=>{if(t<15.9){o.el.style.opacity=0;return}applyShell(o,hbState(k,t),hbState(k,t-1/60),false)});
  const o=orbState(t);orbG.setAttribute('transform',`translate(${o.x} ${o.y}) scale(${o.s*o.sx} ${o.s*o.sy})`);orbG.setAttribute('opacity',o.s>0.01?1:0);
  arcs.forEach((a,k)=>{const h0=HL[k]+1.2;const p=P(t,h0,HL[k+1]-h0,EZ.io);a.setAttribute('stroke-dashoffset',1-p);a.setAttribute('opacity',p>0?.45*(1-P(t,25.8,.4,EZ.lin)):0)});
  landRip.forEach((c,k)=>{const rp=clamp((t-HL[k])/.9);setC(c,HX[k],OTOP,26+70*EZ.out(rp),rp>0&&rp<1?.3*(1-rp):0)});
  if(t>15.9&&t<27)screens(t);
  crowd(t);bigCounter(t);
  a2logo.style.opacity=P(t,16.6,.6)*(1-P(t,26.2,.4));a2logo.style.transform=`translateY(${(1-P(t,16.6,.6))*-12}px)`;
  if(hbN)hbN.textContent=Math.round(5*P(t,19.1,1.2,EZ.out));
}
'''
