"""Board additions from the discovery deck (Nov 2026): customer journey kept vs lost, and journey agents (today vs with HeyDoc)."""
from base import *

USERX = ('<svg width="54%" height="54%" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">'
         '<circle cx="10" cy="8" r="4"/><path d="M2.5 21c0-4 3.4-6.5 7.5-6.5 1.6 0 3 .4 4.2 1"/><path d="M16.5 15.5l5 5M21.5 15.5l-5 5"/></svg>')

CSS6 = r'''
/* ---- E-21 customer journey: kept vs lost ---- */
.hd-jrny{display:grid;grid-template-columns:repeat(4,1fr);gap:0;background:#fff;border-radius:var(--r-card);box-shadow:var(--shadow-layered);padding:36px 28px 28px}
.hd-jrny__col{position:relative;display:flex;flex-direction:column;align-items:center;gap:22px;padding:0 14px}
.hd-jrny__col:nth-child(-n+3)::after{content:"";position:absolute;top:22px;right:-24px;width:48px;height:2px;background:var(--pale)}
.hd-jrny__col:nth-child(-n+3)::before{content:"";position:absolute;top:17px;right:-26px;border:6px solid transparent;border-left-color:var(--pale)}
.hd-jrny__pp{display:grid;grid-template-columns:repeat(5,40px);gap:8px}
.hd-pp{width:40px;height:40px;border-radius:12px;display:flex;align-items:center;justify-content:center}
.hd-pp--lost{background:#fff;color:#e48a7a;box-shadow:inset 0 0 0 2px #f6c9c1}
.hd-jrny__note{min-height:32px;display:flex;justify-content:center}
.hd-jrny__key{grid-column:1/-1;display:flex;gap:32px;justify-content:center;margin-top:22px;padding-top:18px;border-top:2px solid var(--grey);font-size:15px;font-weight:600;color:var(--muted)}
.hd-jrny__key span{display:flex;align-items:center;gap:10px}.hd-jrny__key .hd-pp{width:26px;height:26px;border-radius:8px}
.hd-ph{background:#ffe9a8;color:#8a6200;border-radius:6px;padding:0 6px;font-weight:800}
/* vertical journey stack */
.hd-jcol{display:flex;flex-direction:column;align-items:flex-start;width:320px}
.hd-jcol .hd-chip{width:100%;box-sizing:border-box}
.hd-jcol__ln{width:2px;height:22px;background:var(--line);margin-left:36px}
/* ---- E-22 journey agents ---- */
.hd-flow{background:#fff;border-radius:var(--r-card);box-shadow:var(--shadow-layered);padding:30px;display:grid;grid-template-columns:150px repeat(5,1fr);gap:16px;align-items:stretch}
.hd-flow__cap{display:flex;align-items:center;font-size:14px;font-weight:800;letter-spacing:2.5px;text-transform:uppercase;color:var(--muted)}
.hd-flow__cap--hd{color:var(--blue)}
.hd-flow__h{display:flex;align-items:center;gap:12px;padding:16px;border-radius:16px;box-shadow:inset 0 0 0 2px var(--line);font-size:17px;font-weight:600;color:var(--muted)}
.hd-flow__h .hd-well{--well:38px}
.hd-flow__a{position:relative;display:flex;flex-direction:column;gap:12px;padding:18px;border-radius:18px}
.hd-flow__a b{font-size:15px;font-weight:800}.hd-flow__a span{font-size:19px;font-weight:700;color:var(--navy);line-height:1.3}
.hd-flow__a .hd-well{--well:40px}
.hd-flow__a:not(:last-child)::after{content:"";position:absolute;right:-16px;top:50%;width:16px;height:2px;background:var(--pale)}
.hd-mods{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.hd-mod{display:flex;gap:16px;align-items:flex-start;padding:22px;border-radius:var(--r-card);background:#fff;box-shadow:var(--shadow-layered)}
.hd-mod__n{font-size:24px;font-weight:700;color:var(--navy);margin-bottom:8px}.hd-mod__n small{font-size:15px;font-weight:600;color:var(--muted);margin-left:6px}
'''

def _pp(tone, kept):
    return (f'<span class="hd-pp" style="background:var(--{tone});color:var(--{tone}-ink)">{ic("user","54%")}</span>' if kept
            else f'<span class="hd-pp hd-pp--lost">{USERX}</span>')

def e21():
    cols = [('Enquiry', 'chat', 'aqua', 10, '<span class="hd-tag hd-tag--sky">Paid to acquire</span>'),
            ('Booking', 'cal', 'sun', 6, '<span class="hd-tag hd-tag--rose"><span class="hd-ph">[X%]</span>&nbsp;of enquiries never book</span>'),
            ('Report', 'report', 'lav', 4, '<span class="hd-tag hd-tag--rose"><span class="hd-ph">[Y%]</span>&nbsp;booked ≠ collected</span>'),
            ('Retest', 'lab', 'mint', 2, '<span class="hd-tag hd-tag--mint">Where the revenue is</span>')]
    grid = ''.join(f'<div class="hd-jrny__col"><span class="hd-chip">{well(i, t)}{n}</span>'
                   f'<div class="hd-jrny__pp">{"".join(_pp(t, k < kept) for k in range(10))}</div><div class="hd-jrny__note">{note}</div></div>'
                   for n, i, t, kept, note in cols)
    key = (f'<div class="hd-jrny__key"><span>{_pp("aqua", True)}Customer still in the journey</span><span>{_pp("aqua", False)}Customer lost</span></div>')
    stack = '<div class="hd-jcol">' + '<div class="hd-jcol__ln"></div>'.join(
        f'<span class="hd-chip{" hd-chip--solid" if s else ""}">{well(i, "white" if s else t)}{n}</span>'
        for n, i, t, s in [('First question', 'chat', 'aqua', 0), ('Test', 'lab', 'sun', 0), ('Report', 'report', 'lav', 0), ('Follow-up', 'bell', 'peach', 0), ('Retest', 'cal', 'sky', 1)]) + '</div>'
    body = f'''<div style="display:grid;grid-template-columns:1fr auto;gap:48px;align-items:start">
  {spec('Kept vs lost, step by step · 10 → 6 → 4 → 2 (illustrative)', '<div class="hd-jrny">' + grid + key + '</div>', 'l')}
  {spec('Journey stack · current step solid', stack)}
</div>
<p class="hd-caption" style="font-size:15px;margin-top:20px">From the discovery deck (slides 1 and 3). Yellow <span class="hd-ph">[X%]</span> marks are placeholders for real numbers.</p>'''
    return card('E-21', 'Customer journey · kept vs lost', '1b (problem), 2',
        'columns reveal left to right 150ms apart; in each, kept people pop in 40ms stagger (spring) and the lost ones flip from pastel to the rose outline 300ms later; arrows draw between columns; notes slide up last.', body)

def e22():
    steps = [('Answer', 'chat'), ('Recommend a test', 'lab'), ('Book', 'cal'), ('Explain the report', 'report'), ('Follow up', 'call')]
    agents = [('Care agent', 'chat', 'lav', 'Answers questions 24/7'), ('Advisor agent', 'lab', 'aqua', 'Recommends the right test'),
              ('Booking agent', 'cal', 'peach', 'Books the test'), ('Report agent', 'report', 'sky', 'Explains the result'),
              ('Follow-up agent', 'call', 'mint', 'Checks in after the visit')]
    today = ''.join(f'<div class="hd-flow__h">{well("user", "white")}{n}</div>' for n, i in steps)
    tone = lambda t: ('#d5ecfd', 'var(--blue)') if t == 'sky' else (f'var(--{t})', f'var(--{t}-ink)')
    withh = ''.join(f'<div class="hd-flow__a" style="background:{tone(t)[0]}">{well(i, "white")}<b style="color:{tone(t)[1]}">{n}</b><span>{d}</span></div>' for n, i, t, d in agents)
    flow = (f'<div class="hd-flow"><div class="hd-flow__cap">Today</div>{today}'
            f'<div class="hd-flow__cap hd-flow__cap--hd">With HeyDoc</div>{withh}</div>')
    mods = ('<div class="hd-mods">'
            f'<div class="hd-mod">{well("chat", "aqua")}<div><div class="hd-mod__n">Text</div><span class="hd-tag hd-tag--mint">Live, recurring</span></div></div>'
            f'<div class="hd-mod">{well("phone", "sun")}<div><div class="hd-mod__n">Voice</div><span class="hd-tag hd-tag--mint">Live, recurring</span></div></div>'
            f'<div class="hd-mod">{well("camera", "lav")}<div><div class="hd-mod__n">Vision<small>on existing cameras</small></div><span class="hd-tag hd-tag--sun">Paid POC · state programme</span></div></div></div>')
    body = f'''{spec('Today vs with HeyDoc · each human step becomes an agent', flow, 'l')}
<div style="margin-top:36px">{spec('Three ways in · one SOP engine', mods, 'l')}</div>'''
    return card('E-22', 'Journey agents · today vs with HeyDoc', '2, 6, 9',
        'the grey “Today” steps hold, then each one drops 12px and is replaced from below by its agent tile (pastel fill, 400ms spring), 120ms stagger left to right; connector lines draw between tiles; channel cards fade up after.', body)
