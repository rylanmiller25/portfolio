# Portfolio — Agent Guidelines

A showcase repo of my work. Contents:

- `website/` — personal website (static HTML/CSS)
- `descriptives/` — descriptive figures and data visualizations; has its own `CLAUDE.md` with the figure pipeline and conventions
- `docs/` — CV, headshot, and personal documents; **gitignored and local-only** (never pushed, kept out of the public repo)

`causal-forest-side-project/` and `panel/` also sit in this folder but are each **their own git repo**, not part of portfolio — both are listed in `.gitignore` so this repo doesn't track them. The portfolio README links out to both.

## Working Preferences

- **Voice-to-text.** My messages are dictated, not typed. Don't transcribe literally — clean up and summarize in brief, simple language.
- **Be concise.** Short, direct responses over lengthy explanations.
- **No unsolicited refactoring or cleanup.** Do only what is asked.
- **Prefer editing existing files** over creating new ones.

## Figures & Plots

Titles must be simple and descriptive only — no statistics, p-values, coefficients, or interpretations. "Calibration Test" is a good title. "Calibration slope = 0.35, well-calibrated" is not. Subtitles follow the same rule. See `descriptives/CLAUDE.md` for the full figure style spec.
