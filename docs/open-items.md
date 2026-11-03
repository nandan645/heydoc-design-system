# Open items

Things that block a public release or need a decision. Update this file when one is closed.

## Needed from the design owner

| # | Item | Why | Owner |
|---|---|---|---|
| 1 | **Vector logo masters** (HeyDoc colour, white, mark only) as SVG | Current logos are raster extracts; they blur at large sizes | Abhinandan |
| 2 | **Brand fonts licence check**: Open Sans (OFL) and Inter (OFL) are fine; confirm no other brand font is required | Consistency with the deck | Abhinandan |
| 3 | **Figma library link** (if one exists) to record next to these tokens | Single source of truth across design and code | Abhinandan |
| 4 | Remote for this repository (GitHub/GitLab org + access list) | So the team can clone and review changes | Abhinandan |

## Approvals before public release

| # | Item | Status |
|---|---|---|
| 5 | Government of Maharashtra seal and NHA mark: written approval | Pending |
| 6 | Partner use of Habuild and Pathkind screenshots and logos outside the film | Pending |
| 7 | India / Maharashtra map boundaries checked against the official map | Pending |
| 8 | Hospital name "CPR Hospital" in the camera agent log (real hospital) | Decide: keep or anonymise |

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

- No dark theme by design (white-only).
- Phone markup is long HTML; a web-component wrapper (`<hd-phone>`) would make reuse easier.
- No Figma file is generated from `tokens.json` yet (Tokens Studio can import it directly).
