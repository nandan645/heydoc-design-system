CSS = r'''
/* =====================================================================
   HEYDOC FILM TOKENS — change colours, type, radius, shadow and motion here.
   Source of truth: HeyDoc design system deck (ppt.html).
   ===================================================================== */
:root{
  /* --- brand palette (from the deck) --- */
  --navy:#012b44;  --blue:#0873ba;  --sky:#139bf5;  --pale:#8fcdf8;
  --tint:#eef7fd;  --line:#d6e7f4;  --muted:#5b6b78; --grey:#f4f6f8; --white:#ffffff;
  --cyan:#3fd4f6;  --teal:#2ce9d5;
  /* pastel surfaces + their inks (icon/text placed ON a pastel uses its ink) */
  --aqua:#caf4f3; --sun:#fff2cd; --peach:#ffdeaf; --mint:#cbefd1; --rose:#fde0da; --lav:#cad4f4;
  --aqua-ink:#0f8a85; --sun-ink:#a87508; --peach-ink:#bd6512; --mint-ink:#1f8a43; --rose-ink:#c8394f; --lav-ink:#4a5bc4;
  /* data accents */
  --d-rose:#ea5c72; --d-mint:#3be6a2; --d-blue:#3fa1f8; --d-violet:#7f7be6; --d-amber:#feb64f;

  /* --- semantic roles --- */
  --c-primary:var(--blue);       /* key numbers, highlights */
  --c-primary-deep:var(--navy);  /* headings, text, dark surfaces */
  --c-secondary:var(--sky);      /* lines, nodes */
  --c-accent:var(--cyan);        /* gradient end, glow */
  --c-success:var(--mint-ink);   --c-success-soft:var(--mint);  --c-success-data:var(--d-mint);
  --c-amber:var(--d-amber);      --c-amber-ink:var(--sun-ink);  --c-amber-soft:var(--sun);
  --c-red:var(--d-rose);         --c-red-ink:var(--rose-ink);   --c-red-soft:var(--rose);
  --c-text:var(--navy); --c-text-2:var(--muted); --c-text-3:#9aabb8;

  /* --- backgrounds --- */
  --bg-page:#eef1f4;             /* this board */
  --bg-light:#ffffff;  --bg-light-2:var(--tint);
  --bg-wash:linear-gradient(160deg,#fff 0%,#fff 45%,#e9f8fb 70%,#c9f1f4 100%); /* title-slide aqua wash */
  --bg-dark:#0b1620;   --bg-dark-2:#012b44; --bg-dark-3:#0f2433;
  --bg-dark-grad:radial-gradient(120% 90% at 70% 10%,#0a3350 0%,#0b1620 60%);

  /* --- gradients --- */
  --grad:linear-gradient(90deg,#1789f2,#3fd4f6);                          /* agent highlight */
  --grad-teal:linear-gradient(135deg,#72c2ff 0%,#5adcfd 55%,#2ce9d5 100%); /* feature card */
  --orb:radial-gradient(circle at 28% 18%,#0a84e8 0%,#2ba7f5 55%,#43d0f2 100%); /* hub / pulse core */

  /* --- type --- */
  --font:'Open Sans',system-ui,sans-serif;
  --t-hero:84px; --t-title:56px; --t-lead:30px; --t-body:28px; --t-small:22px; --t-kicker:19px; --t-cap:20px;
  --t-mega:280px;  /* full-screen counter */
  --w-regular:400; --w-semi:600; --w-bold:700; --w-black:800;

  /* --- spacing (8pt) --- */
  --s-1:4px; --s-2:8px; --s-3:12px; --s-4:16px; --s-5:24px; --s-6:32px; --s-7:48px; --s-8:64px; --s-9:96px; --s-10:120px;

  /* --- shape --- */
  --r-pill:999px; --r-panel:28px; --r-card:24px; --r-plate:22px; --r-inner:16px; --r-sm:12px; --r-xs:8px;
  --border:2px; --stroke-icon:2.2; --stroke-line:3; --stroke-route:6;

  /* --- shadow (deck: one soft shadow; layered variant for floating elements) --- */
  --shadow:0 10px 32px rgba(1,43,68,.07);
  --shadow-layered:0 1px 2px rgba(1,43,68,.05),0 4px 12px rgba(1,43,68,.05),0 10px 32px rgba(1,43,68,.07);
  --shadow-float:0 2px 6px rgba(1,43,68,.06),0 18px 48px rgba(1,43,68,.14);
  --shadow-glow:0 12px 30px rgba(23,137,242,.30);
  --shadow-amber:0 0 0 3px var(--d-amber),0 0 40px rgba(254,182,79,.45);

  /* --- motion --- */
  --ease-out:cubic-bezier(.22,1,.36,1);
  --ease-in:cubic-bezier(.55,0,1,.45);
  --ease-in-out:cubic-bezier(.65,0,.35,1);
  --ease-spring:cubic-bezier(.34,1.56,.64,1);
  --ease-linear:linear;
  --dur-xs:150ms; --dur-s:300ms; --dur-m:600ms; --dur-l:1200ms; --dur-xl:2400ms; --stagger:60ms;

  /* --- board chrome --- */
  --eb-card-r:var(--r-panel); --eb-card-pad:32px; --eb-card-shadow:var(--shadow-layered); --eb-gutter:32px;
}

*{margin:0;padding:0;box-sizing:border-box}
html{background:var(--bg-page)}
body{width:1920px;margin:0 auto;background:var(--bg-page);font-family:var(--font);color:var(--c-text);-webkit-font-smoothing:antialiased;font-variant-numeric:tabular-nums}
svg{display:block}
svg text{font-family:var(--font)}
.hd-icon{stroke-width:var(--stroke-icon);flex:none}

/* =====================================================================
   BOARD CHROME (eb-*) — not part of any scene
   ===================================================================== */
.eb-top{padding:72px 64px 40px;display:flex;justify-content:space-between;align-items:flex-end}
.eb-top h1{font-size:56px;font-weight:700;letter-spacing:-.8px;line-height:1.1}
.eb-top h1 em{font-style:normal;color:var(--blue)}
.eb-top .k{font-size:var(--t-kicker);font-weight:700;letter-spacing:3px;text-transform:uppercase;color:var(--blue);margin-bottom:14px}
.eb-top .meta{display:flex;gap:12px}
.eb-top .meta span{background:#fff;border-radius:999px;padding:10px 20px;font-size:16px;font-weight:600;color:var(--muted);box-shadow:var(--shadow)}
.eb-grid{display:grid;grid-template-columns:repeat(12,1fr);gap:var(--eb-gutter);padding:0 64px 96px;align-items:start}
.eb-card{background:#fff;border-radius:var(--eb-card-r);box-shadow:var(--eb-card-shadow);padding:var(--eb-card-pad);min-width:0}
.eb-card__head{display:flex;align-items:center;gap:16px;flex-wrap:wrap}
.eb-id{font-size:15px;font-weight:800;letter-spacing:1.5px;color:#fff;background:var(--navy);border-radius:999px;padding:6px 14px}
.eb-name{font-size:28px;font-weight:700;letter-spacing:-.3px}
.eb-scenes{margin-left:auto;font-size:15px;font-weight:700;color:var(--blue);background:var(--tint);border-radius:999px;padding:7px 16px}
.eb-motion{margin-top:12px;font-size:15px;color:var(--muted);line-height:1.5;display:flex;gap:10px;align-items:baseline}
.eb-motion b{font-size:12px;letter-spacing:1.5px;text-transform:uppercase;color:var(--sky);flex:none}
.eb-card__body{margin-top:28px;padding-top:28px;border-top:2px solid var(--grey)}
.eb-spec{display:flex;flex-direction:column;align-items:center;gap:14px;min-width:0}
.eb-spec.l{align-items:flex-start}
.eb-label{font-size:13px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;color:var(--c-text-3);text-align:center}
.eb-row{display:flex;gap:40px;align-items:flex-start;flex-wrap:wrap}
.eb-sub{font-size:13px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:var(--blue);margin:0 0 16px}
.eb-block+.eb-block{margin-top:40px}
.eb-dark{background:var(--bg-dark);border-radius:var(--r-card);padding:32px}

/* =====================================================================
   SHARED ATOMS (hd-*) — reusable in any scene
   ===================================================================== */
/* icon well: pastel background + its ink */
.hd-well{--well:52px;width:var(--well);height:var(--well);border-radius:50%;display:inline-flex;align-items:center;justify-content:center;flex:none;background:var(--tint);color:var(--blue)}
.hd-well--sky{background:#d5ecfd;color:var(--blue)}
.hd-well--aqua{background:var(--aqua);color:var(--aqua-ink)} .hd-well--sun{background:var(--sun);color:var(--sun-ink)}
.hd-well--peach{background:var(--peach);color:var(--peach-ink)} .hd-well--mint{background:var(--mint);color:var(--mint-ink)}
.hd-well--rose{background:var(--rose);color:var(--rose-ink)} .hd-well--lav{background:var(--lav);color:var(--lav-ink)}
.hd-well--white{background:#fff;color:var(--blue)} .hd-well--grad{background:var(--grad);color:#fff}
.hd-well--navy{background:var(--navy);color:#fff} .hd-well--ghost{background:var(--grey);color:var(--muted)}
.hd-well--sq{border-radius:28%}

/* placeholder slot for supplied logos / screenshots */
.hd-slot{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;text-align:center;border:2px dashed var(--pale);border-radius:var(--r-sm);
  background:repeating-linear-gradient(135deg,rgba(143,205,248,.10) 0 8px,rgba(143,205,248,0) 8px 16px),#fff;color:var(--blue);padding:8px 12px;min-height:40px}
.hd-slot__tag{font-size:9px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:var(--c-text-3)}
.hd-slot__label{font-size:13px;font-weight:700;line-height:1.2}
.hd-slot--dark{background:repeating-linear-gradient(135deg,rgba(143,205,248,.08) 0 8px,transparent 8px 16px),rgba(255,255,255,.04);border-color:rgba(143,205,248,.4);color:#fff}

/* brand logos (supplied files, embedded) */
.hd-logo{display:inline-flex;align-items:center;justify-content:center;flex:none;line-height:0}
.hd-logo img{display:block;height:100%;width:auto;max-width:100%;object-fit:contain}
.hd-logotile{height:62px;background:#fff;border-radius:var(--r-sm);box-shadow:var(--shadow);padding:9px 14px;display:flex;align-items:center;justify-content:center}
.hd-logotile .hd-logo{height:100%;max-width:100%}
.hd-logotile--navy{background:var(--navy)}
.hd-govbadge{display:inline-flex;align-items:center;gap:12px;color:#fff;font-size:15px;font-weight:700}
.hd-govbadge .hd-logo{width:44px;height:44px;border-radius:50%;background:#fff;padding:3px}

/* chip (deck node shape) */
.hd-chip{display:inline-flex;align-items:center;gap:12px;background:#fff;border:var(--border) solid var(--line);border-radius:var(--r-pill);padding:8px 22px 8px 8px;font-size:20px;font-weight:600;white-space:nowrap;color:var(--navy)}
.hd-chip .hd-well{--well:40px}
.hd-chip--solid{background:var(--grad);border-color:transparent;color:#fff;box-shadow:var(--shadow-glow)} .hd-chip--solid .hd-well{background:rgba(255,255,255,.18);color:#fff}
.hd-chip--ghost{background:var(--grey);border-color:var(--grey);color:var(--muted)} .hd-chip--ghost .hd-well{background:#fff;color:var(--muted)}
.hd-chip--text{padding:10px 22px}
.hd-chip--dark{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.14);color:#fff} .hd-chip--dark .hd-well{background:rgba(255,255,255,.12);color:#fff}

/* tag / badge */
.hd-tag{display:inline-flex;align-items:center;gap:8px;font-size:16px;font-weight:700;padding:6px 14px;border-radius:var(--r-pill);white-space:nowrap;line-height:1.3}
.hd-tag--sky{background:#d5ecfd;color:var(--blue)} .hd-tag--aqua{background:var(--aqua);color:var(--aqua-ink)} .hd-tag--mint{background:var(--mint);color:var(--mint-ink)}
.hd-tag--sun{background:var(--sun);color:var(--sun-ink)} .hd-tag--rose{background:var(--rose);color:var(--rose-ink)} .hd-tag--lav{background:var(--lav);color:var(--lav-ink)}
.hd-tag--navy{background:var(--navy);color:#fff} .hd-tag--white{background:#fff;color:var(--blue);box-shadow:var(--shadow)} .hd-tag--grad{background:var(--grad);color:#fff}
.hd-tag i{width:8px;height:8px;border-radius:50%;background:currentColor;display:block}
.hd-badge{min-width:26px;height:26px;padding:0 8px;border-radius:13px;background:var(--d-rose);color:#fff;font-size:14px;font-weight:800;display:inline-flex;align-items:center;justify-content:center;box-shadow:0 0 0 3px #fff}

/* buttons */
.hd-btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;font-family:var(--font);font-size:18px;font-weight:700;border-radius:var(--r-pill);padding:14px 28px;border:var(--border) solid transparent;white-space:nowrap}
.hd-btn--primary{background:var(--grad);color:#fff;box-shadow:var(--shadow-glow)}
.hd-btn--navy{background:var(--navy);color:#fff}
.hd-btn--secondary{background:#fff;color:var(--blue);border-color:var(--line)}
.hd-btn--ghost{background:var(--tint);color:var(--blue)}
.hd-btn--sm{font-size:14px;padding:9px 18px}
/* gradient fills run under the (transparent) border too, so no repeated colour slice shows at the pill ends */
.hd-btn,.hd-chip,.hd-tag,.hd-toggle{background-origin:border-box}

/* toggle */
.hd-toggle{width:56px;height:32px;border-radius:16px;background:var(--line);position:relative;flex:none}
.hd-toggle::after{content:"";position:absolute;left:4px;top:4px;width:24px;height:24px;border-radius:50%;background:#fff;box-shadow:0 2px 6px rgba(1,43,68,.18)}
.hd-toggle.is-on{background:var(--grad)} .hd-toggle.is-on::after{left:28px}

/* progress */
.hd-progress{height:12px;border-radius:6px;background:var(--line);overflow:hidden;width:100%}
.hd-progress__fill{height:100%;border-radius:6px;background:var(--grad);width:var(--p,50%)}
.hd-progress--mint .hd-progress__fill{background:var(--d-mint)} .hd-progress--amber .hd-progress__fill{background:var(--d-amber)} .hd-progress--rose .hd-progress__fill{background:var(--d-rose)}
.hd-progress--thin{height:6px}

/* chat bubbles */
.hd-bubble{font-size:20px;line-height:1.45;padding:16px 22px;border-radius:24px;max-width:480px}
.hd-bubble--agent{background:var(--tint);color:var(--navy);border-bottom-left-radius:8px}
.hd-bubble--user{background:var(--blue);color:#fff;border-bottom-right-radius:8px;margin-left:auto}
.hd-bubble__meta{display:block;font-size:.65em;font-weight:600;opacity:.6;margin-top:6px;text-align:right}
.hd-msg{display:flex;gap:12px;align-items:flex-end}
.hd-avatar-orb{width:40px;height:40px;border-radius:50%;background:var(--orb);flex:none;display:flex;align-items:center;justify-content:center;color:#fff}
.hd-typing{align-self:flex-start;display:inline-flex;gap:6px;padding:16px 20px;background:var(--tint);border-radius:24px;border-bottom-left-radius:8px}
.hd-typing i{width:9px;height:9px;border-radius:50%;background:var(--pale);display:block}
.hd-typing i:nth-child(2){background:var(--sky)}

/* cards */
.hd-panel{background:#fff;border-radius:var(--r-panel);box-shadow:var(--shadow);padding:32px 36px}
.hd-mini{border-radius:var(--r-plate);padding:22px 26px;font-size:20px;line-height:1.35}
.hd-stat{background:#fff;border-radius:var(--r-card);box-shadow:var(--shadow);padding:24px 28px}
.hd-stat__k{font-size:14px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--blue)}
.hd-stat__v{font-size:48px;font-weight:800;letter-spacing:-1px;line-height:1.1;margin-top:8px}
.hd-stat__s{font-size:16px;color:var(--muted);margin-top:4px}

/* text styles */
.hd-kicker{font-size:var(--t-kicker);font-weight:700;letter-spacing:3px;text-transform:uppercase;color:var(--blue)}
.hd-headline{font-size:var(--t-title);font-weight:700;line-height:1.18;letter-spacing:-.8px;color:var(--navy);text-wrap:balance}
.hd-headline em,.hd-subline em,.hd-caption em{font-style:normal;color:var(--blue)}
.hd-headline--xl{font-size:88px;line-height:1.08;letter-spacing:-1.5px}
.hd-subline{font-size:var(--t-lead);line-height:1.4;color:var(--muted);text-wrap:balance}
.hd-statline{display:flex;align-items:baseline;gap:20px}
.hd-statline__num{white-space:nowrap;font-size:var(--t-hero);font-weight:800;line-height:1;letter-spacing:-2px;color:var(--blue)}
.hd-statline__txt{font-size:var(--t-body);line-height:1.35;color:var(--navy);max-width:520px}
.hd-lower{display:inline-flex;align-items:center;gap:16px;background:#fff;border-radius:var(--r-pill);padding:12px 28px 12px 12px;box-shadow:var(--shadow-float);font-size:24px;font-weight:600}
.hd-lower .hd-well{--well:44px}
.hd-caption{font-size:var(--t-small);font-weight:600;color:var(--muted);letter-spacing:.2px}
.on-dark .hd-headline,.on-dark .hd-statline__txt{color:#fff} .on-dark .hd-subline,.on-dark .hd-caption{color:#a9c3d6}
.on-dark .hd-headline em,.on-dark .hd-statline__num,.on-dark .hd-caption em,.on-dark .hd-subline em{color:var(--cyan)}
.on-dark .hd-kicker{color:var(--cyan)}
.on-dark .hd-lower{background:rgba(255,255,255,.08);color:#fff;box-shadow:none;border:1px solid rgba(255,255,255,.14)}

/* =====================================================================
   E-01 brand foundations
   ===================================================================== */
.f-swatches{display:grid;grid-template-columns:repeat(9,1fr);gap:16px}
.f-sw{border-radius:var(--r-inner);overflow:hidden;box-shadow:inset 0 0 0 1px rgba(1,43,68,.06)}
.f-sw__c{height:96px}
.f-sw__t{padding:10px 12px;font-size:13px;line-height:1.4;background:#fff}
.f-sw__t b{display:block;font-size:14px}
.f-sw__t code{font-family:var(--font);color:var(--muted);font-size:12px}
.f-pastels{display:grid;grid-template-columns:repeat(6,1fr);gap:16px;margin-top:16px}
.f-pastel{border-radius:var(--r-inner);padding:16px;display:flex;align-items:center;gap:12px;font-size:13px;font-weight:700}
.f-bgs{display:grid;grid-template-columns:repeat(5,1fr);gap:16px}
.f-bg{height:150px;border-radius:var(--r-inner);display:flex;align-items:flex-end;padding:14px;font-size:13px;font-weight:700;box-shadow:inset 0 0 0 1px rgba(1,43,68,.06)}
.f-type{display:flex;flex-direction:column;gap:22px}
.f-type__row{display:grid;grid-template-columns:180px 1fr;align-items:baseline;gap:24px}
.f-type__meta{font-size:13px;color:var(--c-text-3);font-weight:700;letter-spacing:.5px}
.f-space{display:flex;align-items:flex-end;gap:18px}
.f-space div{background:var(--pale);border-radius:4px}
.f-space span{display:block;font-size:12px;color:var(--muted);font-weight:700;margin-top:6px;text-align:center}
.f-radius{display:flex;gap:18px;align-items:flex-end}
.f-radius div{width:92px;height:92px;background:var(--tint);border:2px solid var(--pale)}
.f-shadow{display:flex;gap:28px}
.f-shadow div{width:150px;height:96px;border-radius:var(--r-card);background:#fff;display:flex;align-items:flex-end;padding:12px;font-size:12px;font-weight:700;color:var(--muted)}
.f-motion{display:grid;grid-template-columns:repeat(5,1fr);gap:16px}
.f-ease{background:var(--tint);border-radius:var(--r-inner);padding:16px}
.f-ease b{font-size:14px;display:block} .f-ease code{font-family:var(--font);font-size:11px;color:var(--muted)}
.f-dur{display:grid;grid-template-columns:110px 1fr 70px;gap:14px;align-items:center;font-size:13px;font-weight:700}
.f-dur i{height:10px;border-radius:5px;background:var(--grad);display:block}

/* =====================================================================
   E-02 pulse
   ===================================================================== */
.hd-pulse{position:relative;width:var(--pulse-size,280px);height:var(--pulse-size,280px);display:flex;align-items:center;justify-content:center}
.hd-pulse__core{position:relative;z-index:2;width:36%;height:36%;border-radius:50%;background:var(--orb);box-shadow:0 0 0 calc(var(--pulse-size,280px)*.05) var(--tint);display:flex;align-items:center;justify-content:center}
.hd-pulse__core::after{content:"";width:26%;height:26%;border-radius:50%;background:#fff;opacity:.95}
.hd-pulse__ring{position:absolute;left:50%;top:50%;width:36%;height:36%;border-radius:50%;border:3px solid var(--sky);transform:translate(-50%,-50%) scale(var(--sc,1));opacity:var(--op,0)}
.hd-pulse__glow{position:absolute;inset:18%;border-radius:50%;background:radial-gradient(circle,rgba(63,212,246,.55) 0%,rgba(19,155,245,.18) 45%,rgba(19,155,245,0) 70%);opacity:0}
.hd-pulse.is-firing .hd-pulse__glow{opacity:1}
.hd-pulse.is-firing .hd-pulse__core{box-shadow:0 0 0 calc(var(--pulse-size,280px)*.05) rgba(63,212,246,.25),0 0 40px rgba(63,212,246,.6)}
.hd-pulse.is-idle .hd-pulse__core{filter:saturate(.85)}
.hd-net{overflow:visible}

/* =====================================================================
   E-03 phone
   ===================================================================== */
.hd-phone{--phone-w:320px;width:var(--phone-w);height:calc(var(--phone-w)*2.08);font-size:calc(var(--phone-w)/22.5);border-radius:3.4em;padding:.62em;flex:none;position:relative}
.hd-phone--light{background:#fff;box-shadow:inset 0 0 0 2px var(--line),var(--shadow-float);color:var(--navy)}
.hd-phone--dark{background:#0b1620;box-shadow:inset 0 0 0 2px #1d3242,var(--shadow-float);color:#fff}
.hd-phone__screen{position:relative;width:100%;height:100%;border-radius:2.8em;overflow:hidden;display:flex;flex-direction:column}
.hd-phone--light .hd-phone__screen{background:#fff;box-shadow:inset 0 0 0 1px var(--line)}
.hd-phone--dark .hd-phone__screen{background:#0e1d29}
.hd-phone__status{height:3.2em;flex:none;display:flex;align-items:center;justify-content:space-between;padding:0 1.6em 0 2em;font-size:.95em;font-weight:700;position:relative;z-index:3}
.hd-phone__island{position:absolute;left:50%;top:.75em;transform:translateX(-50%);width:6.6em;height:1.85em;border-radius:1em;background:#05090d}
.hd-phone__sys{width:3.6em;height:.95em}
.hd-phone__home{position:absolute;left:50%;bottom:.6em;transform:translateX(-50%);width:8.5em;height:.32em;border-radius:.2em;background:currentColor;opacity:.85;z-index:5}
/* in-screen app parts (em-based: everything scales with --phone-w) */
.hd-scr{flex:1;display:flex;flex-direction:column;min-height:0;position:relative}
.hd-appbar{display:flex;align-items:center;gap:.7em;padding:.5em 1.15em .9em}
.hd-appbar .hd-slot{min-height:0;height:2.3em;padding:0 .7em;border-radius:.7em;flex-direction:row;gap:.4em}
.hd-appbar .hd-slot__tag{display:none} .hd-appbar .hd-slot__label{font-size:.75em}
.hd-appbar__t{font-weight:700;font-size:1.05em;line-height:1.2} .hd-appbar__s{font-size:.75em;color:var(--muted);font-weight:600}
.hd-phone--dark .hd-appbar__s{color:#8fb3cc}
.hd-scr__body{flex:1;padding:0 1.15em 1.6em;display:flex;flex-direction:column;gap:.8em;min-height:0}
.hd-scr .hd-btn{font-size:1em;padding:.85em 1.2em;width:100%}
.hd-scr .hd-tag{font-size:.75em;padding:.3em .75em}
.hd-scr .hd-bubble{font-size:.92em;padding:.7em .95em;border-radius:1.15em;max-width:84%}
.hd-scr .hd-bubble--agent{border-bottom-left-radius:.35em} .hd-scr .hd-bubble--user{border-bottom-right-radius:.35em}
.hd-scr .hd-well{--well:2.5em}
.hd-scr .hd-progress{height:.45em}
.hd-row{display:flex;align-items:center;gap:.7em}
.hd-li{display:flex;align-items:center;gap:.75em;padding:.7em .8em;border-radius:1em;background:#fff;box-shadow:0 0 0 1px var(--line)}
.hd-li__t{font-weight:700;font-size:.92em;line-height:1.25} .hd-li__s{font-size:.75em;color:var(--muted)}
.hd-li__r{margin-left:auto;text-align:right}
.hd-input{display:flex;align-items:center;gap:.6em;border-radius:2em;padding:.6em .6em .6em 1em;background:var(--grey);color:var(--muted);font-size:.85em}
.hd-input .hd-well{--well:2.2em;margin-left:auto}

/* WhatsApp-style ping + PDF */
.hd-ping{display:flex;gap:.8em;background:rgba(255,255,255,.92);border-radius:1.35em;padding:.85em .9em;box-shadow:var(--shadow-float);color:var(--navy);font-size:var(--ping-fs,14px);width:var(--ping-w,auto);backdrop-filter:blur(12px)}
.hd-ping__app{position:relative;width:2.7em;height:2.7em;border-radius:.75em;background:var(--mint-ink);color:#fff;display:flex;align-items:center;justify-content:center;flex:none}
.hd-ping__app .hd-badge{position:absolute;right:-.55em;top:-.55em;min-width:1.5em;height:1.5em;font-size:.72em;padding:0 .35em;box-shadow:0 0 0 .18em #fff}
.hd-ping__main{flex:1;min-width:0}
.hd-ping__top{display:flex;justify-content:space-between;font-size:.72em;font-weight:700;color:var(--muted);letter-spacing:.3px;text-transform:uppercase}
.hd-ping__title{font-weight:700;font-size:.98em;margin-top:.2em}
.hd-ping__text{font-size:.86em;line-height:1.35;color:#2c4252;margin-top:.15em}
.hd-pdf{display:flex;gap:.7em;align-items:center;margin-top:.6em;background:#fff;border-radius:.8em;padding:.5em;box-shadow:0 0 0 1px var(--line)}
.hd-pdf__sheet{width:4.4em;height:5.6em;border-radius:.35em;background:#fff;box-shadow:0 0 0 1px var(--line),0 2px 6px rgba(1,43,68,.08);padding:.4em .35em;display:flex;flex-direction:column;gap:.22em;position:relative;flex:none;overflow:hidden}
.hd-pdf__sheet b{display:block;height:.28em;border-radius:.14em;background:var(--line)}
.hd-pdf__sheet .r{background:var(--d-rose)}
.hd-pdf__type{position:absolute;right:0;bottom:0;background:var(--rose-ink);color:#fff;font-size:.5em;font-weight:800;padding:.2em .45em;border-top-left-radius:.4em;letter-spacing:.5px}
.hd-pdf__name{font-size:.82em;font-weight:700} .hd-pdf__meta{font-size:.7em;color:var(--muted)}
.hd-pdf__vals{margin-top:.3em;display:flex;flex-direction:column;gap:.1em;font-size:.72em}
.hd-pdf__vals span{display:flex;justify-content:space-between;gap:.8em;white-space:nowrap} .hd-pdf__vals em{font-style:normal;color:var(--rose-ink);font-weight:800}
/* large report preview (chat attachment) */
.hd-report{background:#fff;color:var(--navy);border-radius:.8em;padding:.9em;font-size:.82em}
.hd-report__h{display:flex;justify-content:space-between;align-items:center;font-weight:800;font-size:.95em;padding-bottom:.5em;border-bottom:1px solid var(--line)}
.hd-report__r{display:grid;grid-template-columns:1fr auto auto;gap:.6em;padding:.38em 0;border-bottom:1px dashed var(--line);font-size:.9em;align-items:center}
.hd-report__r em{font-style:normal;font-weight:800}
.hd-report__r .hi{color:var(--rose-ink)} .hd-report__r .ok{color:var(--navy)}
.hd-report__f{font-size:.65em;font-weight:800;padding:.15em .45em;border-radius:.4em;background:var(--rose);color:var(--rose-ink)}
.hd-report__f.ok{background:var(--mint);color:var(--mint-ink)}
.hd-unread{display:inline-flex;align-items:center;gap:.5em;background:var(--mint-ink);color:#fff;border-radius:2em;padding:.35em .9em;font-size:.78em;font-weight:700}

/* =====================================================================
   E-04 chaos
   ===================================================================== */
.hd-window{background:#fff;border-radius:var(--r-inner);box-shadow:var(--shadow-float);overflow:hidden;width:var(--win-w,820px);font-size:13px}
.hd-window__bar{height:38px;background:var(--grey);display:flex;align-items:center;gap:8px;padding:0 14px;border-bottom:1px solid var(--line)}
.hd-window__bar i{width:12px;height:12px;border-radius:50%;background:#d3dde5;display:block}
.hd-window__bar span{margin-left:12px;font-weight:700;color:var(--muted);font-size:13px}
.hd-sheet{display:grid;grid-template-columns:36px 92px 140px 70px 110px 96px 120px 1fr;font-size:12.5px}
.hd-sheet div{border-right:1px solid #e7eef4;border-bottom:1px solid #e7eef4;padding:6px 8px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;height:30px;color:#2c4252}
.hd-sheet .h{background:#f7f9fb;font-weight:700;color:var(--muted);text-align:center}
.hd-sheet .n{background:#f7f9fb;color:var(--c-text-3);text-align:center;font-weight:700}
.hd-sheet .y{background:var(--sun)} .hd-sheet .r{background:var(--rose);color:var(--rose-ink);font-weight:700} .hd-sheet .e{color:var(--rose-ink);font-weight:800}
.hd-sheet .sel{box-shadow:inset 0 0 0 2px var(--sky)} .hd-sheet .ov{overflow:visible;position:relative;z-index:1}
.hd-minidash{width:var(--md-w,300px);background:#fff;border-radius:var(--r-inner);box-shadow:var(--shadow-float);padding:14px 16px;font-size:12px}
.hd-minidash__h{display:flex;justify-content:space-between;align-items:center;font-weight:700;color:var(--muted);font-size:12px}
.hd-minidash__v{font-size:26px;font-weight:800;letter-spacing:-.5px;margin-top:4px}
.hd-minidash__src{font-size:11px;color:var(--c-text-3);font-weight:600;margin-top:6px}
.hd-notif{display:flex;gap:12px;align-items:center;background:#fff;border-radius:var(--r-inner);padding:12px 16px;box-shadow:var(--shadow-float);width:var(--notif-w,420px)}
.hd-notif .hd-well{--well:40px}
.hd-notif__t{font-weight:700;font-size:15px} .hd-notif__s{font-size:13px;color:var(--muted)} .hd-notif__time{margin-left:auto;font-size:12px;color:var(--c-text-3);font-weight:700;align-self:flex-start}
.hd-notif-stack{position:relative;width:var(--notif-w,420px);height:250px}
.hd-notif-stack .hd-notif{position:absolute;left:0;right:0}
.hd-queue{display:flex;flex-direction:column;gap:12px}
.hd-queue__dots{display:flex;gap:10px;align-items:center}
.hd-queue__dots i{width:22px;height:22px;border-radius:50%;background:var(--line);display:block}
.hd-queue__dots .s{background:var(--blue)} .hd-queue__dots .w{background:var(--d-amber)} .hd-queue__dots .l{background:var(--d-rose)}
.hd-queue__lbl{display:flex;gap:16px;font-size:14px;font-weight:700;color:var(--muted);align-items:center}

/* =====================================================================
   E-06 crowd · E-07 counters
   ===================================================================== */
.hd-crowd .d{fill:var(--line)} .hd-crowd .d.is-hit{fill:var(--blue)} .hd-crowd .h{fill:none;stroke:var(--pale);stroke-width:2}
.hd-crowd--dark .d{fill:#1d3242} .hd-crowd--dark .d.is-hit{fill:var(--cyan)} .hd-crowd--dark .h{stroke:rgba(63,212,246,.4)}
.hd-counter{display:inline-flex;align-items:baseline;gap:.06em;font-weight:800;letter-spacing:-.03em;line-height:1;color:var(--blue);font-size:var(--cnt-fs,84px);font-variant-numeric:tabular-nums}
.hd-counter__pre{font-size:.55em;font-weight:700;margin-right:.08em}
.hd-counter__unit{font-size:.5em;font-weight:800;margin-left:.06em;letter-spacing:0}
.hd-counter__from{color:var(--c-text-3);font-size:.6em;font-weight:700}
.hd-counter__arrow{font-size:.45em;color:var(--pale);margin:0 .25em;font-weight:700;align-self:center}
.hd-bignum{width:1920px;height:1080px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:32px;position:relative;overflow:hidden}
.hd-bignum--light{background:var(--bg-wash);box-shadow:inset 0 0 0 1px var(--line)}
.hd-bignum--dark{background:var(--bg-dark-grad)}
.hd-bignum .hd-counter{--cnt-fs:var(--t-mega)}
.hd-bignum .hd-kicker{font-size:28px;letter-spacing:4px}
.hd-bignum--dark .hd-counter{color:#fff} .hd-bignum--dark .hd-counter__unit{color:var(--cyan)}
.hd-bignum__lbl{font-size:40px;color:var(--muted);max-width:900px;line-height:1.35} .hd-bignum--dark .hd-bignum__lbl{color:#a9c3d6}
.hd-statchip{display:inline-flex;align-items:center;gap:12px;background:#fff;border-radius:var(--r-pill);padding:10px 22px 10px 10px;box-shadow:var(--shadow);font-size:20px;color:var(--navy);font-weight:600}
.hd-statchip b{font-weight:800;color:var(--blue);font-size:1.15em}
.hd-statchip .hd-well{--well:40px}
.hd-statchip--dark{background:rgba(255,255,255,.08);color:#fff;box-shadow:none;border:1px solid rgba(255,255,255,.14)} .hd-statchip--dark b{color:var(--cyan)}

/* =====================================================================
   E-09 agents
   ===================================================================== */
.hd-agent{width:var(--agent-w,300px);background:#fff;border:var(--border) solid var(--line);border-radius:var(--r-card);padding:22px;display:flex;flex-direction:column;gap:16px}
.hd-agent__head{display:flex;align-items:center;gap:14px}
.hd-agent__head .hd-well{--well:56px}
.hd-agent__name{font-size:21px;font-weight:700;line-height:1.2} .hd-agent__role{font-size:14px;color:var(--muted)}
.hd-agent__status{display:flex;align-items:center;gap:8px;font-size:14px;font-weight:700;color:var(--muted)}
.hd-agent__dot{width:10px;height:10px;border-radius:50%;background:#c3d0da}
.hd-agent__task{font-size:15px;color:var(--muted);line-height:1.4;min-height:42px}
.hd-agent__task b{color:var(--navy)}
.hd-agent.is-active{border-color:transparent;background:linear-gradient(#fff,#fff) padding-box,var(--grad) border-box;box-shadow:var(--shadow-glow)}
.hd-agent.is-active .hd-agent__dot{background:var(--d-mint);box-shadow:0 0 0 4px rgba(59,230,162,.25)}
.hd-agent.is-active .hd-agent__status{color:var(--mint-ink)}
.hd-agent.is-idle .hd-well{filter:grayscale(.6);opacity:.75}

/* =====================================================================
   E-12 camera tiles
   ===================================================================== */
.hd-cam{position:relative;aspect-ratio:16/9;border-radius:var(--r-inner);overflow:hidden;background:linear-gradient(160deg,#10283a 0%,#0b1620 70%);color:#fff}
.hd-cam__scene{position:absolute;inset:0;width:100%;height:100%}
.hd-cam__icon{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);color:rgba(143,205,248,.22)}
.hd-cam__lbl{position:absolute;left:32px;top:18px;display:flex;align-items:center;gap:8px;font-size:12px;font-weight:700;letter-spacing:.6px;text-transform:uppercase;color:#cfe3f1}
.hd-cam__lbl i{width:8px;height:8px;border-radius:50%;background:var(--d-rose);display:block;box-shadow:0 0 0 3px rgba(234,92,114,.25)}
.hd-cam__ts{position:absolute;right:32px;top:18px;font-size:12px;font-weight:700;color:#8fb3cc}
.hd-cam__chips{position:absolute;left:28px;bottom:24px;display:flex;gap:8px;flex-wrap:wrap}
.hd-cam__frame{position:absolute;inset:10px;pointer-events:none}
.hd-ochip{display:inline-flex;align-items:center;gap:8px;background:rgba(11,22,32,.55);border:1px solid rgba(255,255,255,.18);backdrop-filter:blur(8px);color:#fff;border-radius:var(--r-pill);padding:6px 14px 6px 8px;font-size:14px;font-weight:600;white-space:nowrap}
.hd-ochip b{font-weight:800}
.hd-ochip .ic{width:26px;height:26px;border-radius:50%;background:rgba(63,212,246,.18);color:var(--cyan);display:flex;align-items:center;justify-content:center}
.hd-ochip--ok .ic{background:rgba(59,230,162,.18);color:var(--d-mint)}
.hd-ochip--amber{background:var(--d-amber);border-color:var(--d-amber);color:#3d2a00} .hd-ochip--amber .ic{background:rgba(255,255,255,.35);color:#3d2a00}
.hd-cam.is-alert{box-shadow:var(--shadow-amber)}
.hd-cam.is-alert .hd-cam__icon{color:rgba(254,182,79,.35)}

/* =====================================================================
   E-14 segments · E-15 logo ring
   ===================================================================== */
.hd-seg{border-radius:var(--r-card);padding:26px;display:flex;flex-direction:column;gap:18px;min-height:250px}
.hd-seg .hd-well{--well:76px;background:#fff}
.hd-seg__t{font-size:28px;font-weight:700;margin-top:auto}
.hd-seg__s{font-size:16px;color:var(--muted);line-height:1.4;margin-top:-10px;min-height:2.8em}
.hd-seg--lav{background:var(--lav)} .hd-seg--lav .hd-well{color:var(--lav-ink)}
.hd-seg--aqua{background:var(--aqua)} .hd-seg--aqua .hd-well{color:var(--aqua-ink)}
.hd-seg--mint{background:var(--mint)} .hd-seg--mint .hd-well{color:var(--mint-ink)}
.hd-seg--sun{background:var(--sun)} .hd-seg--sun .hd-well{color:var(--sun-ink)}
.hd-logoring{position:relative;width:var(--ring-size,680px);height:var(--ring-size,680px)}
.hd-logoring__svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.hd-logoring__core{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:30%;height:30%;border-radius:50%;background:#fff;box-shadow:0 0 0 3px #8fcdf8,0 0 0 18px var(--tint),0 0 0 36px rgba(238,247,253,.5),var(--shadow-glow);display:flex;align-items:center;justify-content:center;padding:16px}
.hd-logoring__core .hd-slot{background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.6);color:#fff;width:100%;border-radius:var(--r-pill)}
.hd-logoring__core .hd-slot__tag{color:rgba(255,255,255,.75)}
.hd-logoring__slot{position:absolute;transform:translate(-50%,-50%);width:150px}
.hd-logoring__core .hd-logo{width:78%;height:auto}.hd-logoring__core .hd-logo img{width:100%;height:auto}
.hd-logoring__slot .hd-slot{height:62px;border-radius:var(--r-sm);box-shadow:var(--shadow)}

/* =====================================================================
   E-19 end card
   ===================================================================== */
.hd-end{width:1920px;height:1080px;position:relative;overflow:hidden;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:26px;text-align:center}
.hd-end--light{background:var(--bg-wash);box-shadow:inset 0 0 0 1px var(--line)}
.hd-end--dark{background:var(--bg-dark-grad);color:#fff}
.hd-end__lockup{height:260px}
.hd-end__lockup .hd-slot__label{font-size:30px}.hd-end__lockup .hd-slot__tag{font-size:14px}
.hd-end__tag{font-size:var(--t-hero);font-weight:700;letter-spacing:-.6px}
.hd-end__tag em{font-style:normal;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.hd-end__url{font-size:var(--t-lead);font-weight:700;color:var(--blue);letter-spacing:.5px;display:flex;align-items:center;gap:10px}
.hd-end--dark .hd-end__url{color:var(--cyan)}
.hd-end__bg{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
'''
