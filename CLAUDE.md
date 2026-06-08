# Portfolio — Agent Guidelines

A showcase repo of my work. Contents:

- `website/` — personal website (static HTML/CSS)
- `descriptives/` — descriptive figures and data visualizations; has its own `CLAUDE.md` with the figure pipeline and conventions
- `docs/` — CV, headshot, and personal documents; **gitignored and local-only** (never pushed, kept out of the public repo)

`causal-forest-side-project/` and `panel/` also sit in this folder but are each **their own git repo**, not part of portfolio — both are listed in `.gitignore` so this repo doesn't track them. The portfolio README links out to both.

## To-Do

- [x] GitHub profile README created (`rylanmiller25/rylanmiller25`, public) — pin repos via the profile UI; swap the portfolio link to a live URL once the site is deployed
- [x] Build `portfolio.html` (project card grid) + stub subpages `causal-forests.html`, `panel.html`
- [ ] Flesh out the project subpages (currently stubs that link to the GitHub repos)
- [x] Footer on all pages (categorized: Explore / Projects / Connect) — replaces the earlier "About Me & Contact" idea
- [ ] Footer is duplicated in each HTML file; if pages multiply, consider a build step / include to avoid drift
- [ ] Add a photo of Rylan to the right side of the About Me page (user will provide a separate image)

## Working Preferences

- **Voice-to-text.** My messages are dictated, not typed. Don't transcribe literally — clean up and summarize in brief, simple language.
- **Be concise.** Short, direct responses over lengthy explanations.
- **No unsolicited refactoring or cleanup.** Do only what is asked.
- **Prefer editing existing files** over creating new ones.
- **Commit and push frequently.** After any meaningful set of changes, commit and push to `origin` without waiting to be asked.

## Figures & Plots

Titles must be simple and descriptive only — no statistics, p-values, coefficients, or interpretations. "Calibration Test" is a good title. "Calibration slope = 0.35, well-calibrated" is not. Subtitles follow the same rule. See `descriptives/CLAUDE.md` for the full figure style spec.
