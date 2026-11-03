# Reference implementation: the explainer film (1:55)

`examples/explainer-film.html` is the most complete use of the system: 115 seconds, 12 scenes, built from the components and motion rules in this repo. Open it, scrub it, and copy patterns from it.

**Controls:** Space play/pause · ←/→ one frame (Shift = 1s) · `?t=34` opens at 34s · *Edit text* lets anyone change on-screen text and *Save copy* / *Export* it (no code).

## Scene map

| # | Time | Scene | Accent | Components | On-screen line |
|---|---|---|---|---|---|
| 1 | 0–5 | Lock screen: a report arrives, calm notifications stack | HeyDoc | iPhone `.hd-ip--dark`, notifications | "Her report arrived. No one explained it." |
| 1b | 5–10 | Data everywhere: sheets, dashboards, queues pile up, then freeze | HeyDoc | `.hd-window`, `.hd-sheet`, `.hd-minidash`, `.hd-queue` | "Data everywhere. Action nowhere." |
| 2 | 10–16 | Everything morphs into the pulse (the company brain), which becomes a phone | HeyDoc → green | Pulse, shell morph, skeleton phone | "What if care could act on its own?" · "HeyDoc AI. Agents that run care." |
| 3 | 16–27 | Habuild: four app screens, an orb hops between them; chat + upsell | Partner 1 (green) | Phone screenshots, ring highlights, HTML upsell card | "5M+ members · Agents for every one" |
| 4 | 27–34 | Dot crowd, 1 in 10 subscribing, ₹300 Cr | Partner 1 | `.hd-crowd`, `.hd-counter` | — |
| 5 | 34–44 | Pathkind: phone grows from a yellow orb; Tests → tracking → report → chat; touchpoint agents | Partner 2 (yellow) | Phone, `.hd-chip`, connector lines | "10M+ patients · Lab agents at every touchpoint" |
| 6 | 44–54 | Lab operations panel, 5 agent cards, logistics expands to a route map | Partner 2 | `.hd-agent`, route map | "[AL] agents live · [RS]% faster reports" |
| 7 | 54–65 | MAHA-PULSE dashboard, Kolhapur live | HeyDoc | Dashboard, Kolhapur map | "MAHA-PULSE AI · Kolhapur, live" |
| 8 | 65–75 | 6 camera feeds + agent log handling an alert; feeds become dots on Maharashtra | HeyDoc | `.hd-cam`, agent log, Maharashtra dot map | "District hospitals, statewide" |
| 9 | 75–84 | Four care segments, then the company brain app in a browser window | HeyDoc | `.hd-seg`, browser window, product screenshot | "4 care segments. One company brain." |
| 10 | 84–94 | Three numbers (last 3 months) | HeyDoc | `.hd-counter` | — |
| 11 | 94–104 | Logo ring | HeyDoc | `.hd-logoring`, `.hd-logotile` | "Powering agentic care for" |
| 12 | 104–115 | India → dot globe (US next, Europe & GCC then) → end card | HeyDoc | Maps, dot globe, roadmap cards, `.hd-end` | "For India, and for the world." |

## Patterns worth copying

- **Pulse → phone → panel → tile → dot:** acts 2, 3, 5, 8 (`source/gen/film.py`, `act3.py`, `act4.py`).
- **Partner hand-off:** skeleton phone blends blue → green at 15.3s; dots blend green → lime → yellow at 33.8s.
- **Screen scroll inside a mockup:** chat thread scrolls up for the upsell (act 2); company-brain window scrolls a tall screenshot (act 5).
- **Agent log:** rows drop in as agents act, with status chips Scanning → Issue → Escalated → Resolved (act 4).
- **Dot globe:** real land points, orthographic projection, great-circle arcs with altitude (act 5).

## Rebuilding

The film is generated from `source/gen/` (`film.py` + `act2.py` … `act5.py`). `./scripts/build.sh --film` writes `examples/explainer-film.html`. Text edits made in the film's Edit mode live in the saved HTML, not in the source: carry them back into `film.py` before rebuilding.

Audio script and voice prompts: Claude Doc "HeyDoc AI Film · Audio Script".
