# Contributing

## Workflow
1. Branch from `main`: `design/<short-name>` or `fix/<short-name>`.
2. Make the change with tokens and existing components (`AGENTS.md` has the rules).
3. If you changed a token, update **both** `tokens/tokens.json` and `css/tokens.css`, then run `python3 scripts/check_tokens.py`.
4. If you changed a component, rebuild the board (`./scripts/build.sh`) and check it in a browser.
5. Add a line to `CHANGELOG.md` under *Unreleased*.
6. Open a pull request with before/after screenshots. The design owner reviews.

## Versioning (semver)
- **Major:** a token renamed/removed or a component's markup changed in a breaking way.
- **Minor:** new component, token or variant.
- **Patch:** fixes that don't change the API (colour tweak inside a token, spacing bug).

## Commit messages
`<area>: <what changed>`, e.g. `tokens: add --t-scene`, `components: journey stack`, `docs: motion recipes`.

## Large files
Images go in `assets/` (prefer SVG/WebP, under 1 MB each). Generated HTML in `examples/` is committed so the system works without a build; regenerate rather than hand-edit it.
