# Portfolio — Agent Guidelines

A showcase repo of my work. Contents:

- `descriptives/` — descriptive figures and data visualizations; has its own `CLAUDE.md` with the figure pipeline and conventions
- `docs/` — CV, headshot, and personal documents; **gitignored and local-only** (never pushed, kept out of the public repo)

Panel lives in its own repo (`rylanmiller25/panel-side-project`), not in this one. The portfolio README links out to it.

**Website** — lives in its own repo, `rylanmiller25/rylanmiller25.github.io` (static HTML/CSS, served by GitHub Pages at https://rylanmiller25.github.io/). Local clone: `~/Desktop/GitHub Docs/rylanmiller25.github.io/`. Edit the website there — pushing to `main` updates the live site, so ask before pushing.

## To-Do

- [x] GitHub profile README created (`rylanmiller25/rylanmiller25`, public) — still need to pin repos via the profile UI
- [x] Build `portfolio.html` (project card grid)
- [x] Panel beta pages (`panel.html`, `panel-beta.html`, `panel-analytics.html`) — first-draft betas, merged via PR #1
- [ ] **Review and refine Panel** — the beta pages are first drafts and need a pass
- [x] Website deployed (GitHub Pages) — still need to swap the profile README "Portfolio" link from the repo to the live URL
- [ ] Add a photo of Rylan to the right side of the About Me page (user will provide a separate image)
- [ ] Footer is duplicated in each HTML file; if pages multiply, consider a build step / include to avoid drift

## Working Preferences

- **Voice-to-text.** My messages are dictated, not typed. Don't transcribe literally — clean up and summarize in brief, simple language.
- **Be concise.** Short, direct responses over lengthy explanations.
- **No unsolicited refactoring or cleanup.** Do only what is asked.
- **Prefer editing existing files** over creating new ones.
- **Always ask before committing or pushing.** Never commit or push without my explicit go-ahead each time.

## Figures & Plots

Titles must be simple and descriptive only — no statistics, p-values, coefficients, or interpretations. "Calibration Test" is a good title. "Calibration slope = 0.35, well-calibrated" is not. Subtitles follow the same rule. See `descriptives/CLAUDE.md` for the full figure style spec.
