# Open items

Things that block a public release or need a decision. Update this file when one is closed.

## Needed from the design owner

| # | Item | Why | Owner |
|---|---|---|---|
| 1 | **Brand fonts licence check**: Open Sans (OFL) and Inter (OFL) are fine; confirm no other brand font is required | Consistency with the deck | Abhinandan |
| 2 | Access list for the GitHub repository | So the team can clone and review changes | Abhinandan |

## Approvals before public release

| # | Item | Status |
|---|---|---|
| 4 | Government of Maharashtra seal and NHA mark: written approval | Pending |
| 5 | Partner use of Habuild and Pathkind screenshots and logos outside the film | Pending |
| 6 | India / Maharashtra map boundaries checked against the official map | Pending |
| 7 | Hospital name "CPR Hospital" in the camera agent log (real hospital) | Decide: keep or anonymise |

## Illustrative numbers

All numbers in the examples (film, board, starters) are **illustrative by design** and are replaced per use case. Before a piece goes public, swap them for confirmed figures from the source of truth for that piece. Places where the examples show numbers:

| Where | Numbers |
|---|---|
| Film act 2 | 5M+ members, ₹300 Cr, 1 in 10 subscribing, 00,000 conversations a day, Habuild Nutrition Plus ₹499/month |
| Film act 3 | 10M+ patients, `[AL]` agents live, `[RS]%` faster reports |
| Film acts 4–5 | 1,500 → 5,000 cameras, 35+ agents, 15M+ interactions, 15M+ people |
| Board E-21 | `[X%]` never book, `[Y%]` booked ≠ collected |

## Known gaps in the system

- No dark theme by design (white-only), so there is no white/reversed HeyDoc logo.
- HeyDoc logo exists only as a raster (900×542 WebP); no SVG master. If a vector is ever made, add it to `assets/logos/`.
- Phone markup is long HTML; a web-component wrapper (`<hd-phone>`) would make reuse easier.
- There is no Figma library; code (this repo) is the source of truth. `tokens/tokens.json` can be imported into Figma with Tokens Studio if one is ever made.
