# Open items

Things that block a public release or need a decision. Update this file when one is closed.

## Needed from the design owner

| # | Item | Why | Owner |
|---|---|---|---|
| 1 | **Brand fonts licence check**: Open Sans (OFL) and Inter (OFL) are fine; confirm no other brand font is required | Consistency with the deck | Abhinandan |
| 2 | **Figma library link** (if one exists) to record next to these tokens | Single source of truth across design and code | Abhinandan |
| 3 | Remote for this repository (GitHub/GitLab org + access list) | So the team can clone and review changes | Abhinandan |

## Approvals before public release

| # | Item | Status |
|---|---|---|
| 4 | Government of Maharashtra seal and NHA mark: written approval | Pending |
| 5 | Partner use of Habuild and Pathkind screenshots and logos outside the film | Pending |
| 6 | India / Maharashtra map boundaries checked against the official map | Pending |
| 7 | Hospital name "CPR Hospital" in the camera agent log (real hospital) | Decide: keep or anonymise |

## Placeholders still in the work

| Where | Placeholder |
|---|---|
| Film act 3 | `[AL]` agents live, `[RS]%` faster reports |
| Film act 2 | "00,000 agent conversations a day"; ₹300 Cr framing |
| Film acts 2–5 | 5M+ members, 10M+ patients, 35+ agents, 15M+ interactions (confirm sources) |
| Film act 2 | Habuild Nutrition Plus · ₹499/month (confirm product name and price) |
| Board E-21 | `[X%]` never book, `[Y%]` booked ≠ collected |
| Deck (discovery) | `[date]`, `[N]`, `[₹]`, `[metric]` throughout |

## Known gaps in the system

- No dark theme by design (white-only), so there is no white/reversed HeyDoc logo.
- HeyDoc logo exists only as a raster (900×542 WebP); no SVG master. If a vector is ever made, add it to `assets/logos/`.
- Phone markup is long HTML; a web-component wrapper (`<hd-phone>`) would make reuse easier.
- No Figma file is generated from `tokens.json` yet (Tokens Studio can import it directly).
