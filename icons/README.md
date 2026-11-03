# Icons

38 HeyDoc stroke icons on a 24×24 grid, 2.2 stroke, round caps and joins, `currentColor`.

- `svg/<name>.svg`: one file per icon
- `sprite.svg`: inline it once, then `<svg class="hd-icon" width="24" height="24"><use href="#i-lab"/></svg>`
- `icons.json`: `{ name: "<svg inner markup>" }` for code

Put icons in an `.hd-well` (pastel + ink) or use them raw in navy/blue. Sizes: 16, 24, 32, 48, 64. To add one, draw on the same grid and stroke, add it to `source/gen/base.py` (`ICONS`) and re-export.
