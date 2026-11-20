# Descriptives Agent — Instructions

This folder contains data visualizations and descriptive figures built from LinkedIn career history and job posting data.

---

## Two Modes

### 1. Idea Generation
- Focus on insights that would be broadly interesting to a professional LinkedIn audience
- Ideas should be specific and concrete (clear x-axis, clear comparison)
- Target roles: management consulting, product management, strategy & operations, TPM
- Add to IDEAS.md as bullet points — short and clear, tagged `[LinkedIn]`

### 2. Output Drafting
When given a finished figure:
- Draft a post following the LinkedIn Post Format spec below
- Save output to `outputs/posts/` with the matching figure slug

---

## LinkedIn Post Format

Mirror the structure and formatting of the examples in `descriptives/examples/` — not the content or tone. These posts are data-driven; the examples are personal/narrative. Adapt the format, not the voice.

### Structure
- **Opening line**: One punchy sentence that states the key finding directly. No preamble.
- **Data context**: 1–2 sentences explaining what the data is — source, time period, sample size if relevant. Keep it brief.
- **Key observations**: 2–4 short paragraphs or a numbered list. One idea per paragraph. Short sentences.
- **Closing**: A genuine open-ended question, a thought-provoking observation, or a plain declarative statement. Nothing else.

### Rules
- Short paragraphs — one idea per paragraph, often just one or two sentences
- No engagement bait of any kind: no "comment X to get Y", no "drop a 🙋 below", no "share this if you agree"
- No self-promotion, no "I'm hiring", no "link in bio", no asks
- No excessive emoji — zero is fine; one is the max if it fits naturally
- Do not mirror the *content* or *tone* of the examples — mirror the formatting only, applied to the data insight at hand
- The post should stand on its own as something worth reading regardless of who posted it

### Length
Roughly 100–180 words. Long enough to give context; short enough to read in 30 seconds.

---

## Figure Style

Governed by the `descriptives` skill (`~/.claude/skills/descriptives/SKILL.md`). When generating a figure for this folder, invoke that skill rather than hand-rolling the style rules below from scratch — this section mirrors it so the spec is visible without opening the skill file.

Reference examples: the skill's own references at `~/Desktop/research/formatting-examples/linkedin-descriptive-example-{1..7}.png`, plus any local additions in `descriptives/examples/`.

### Layout & Size
- Output format: **PNG**, 300 dpi (no fixed pixel target — size follows figsize × dpi, e.g. 8×5in ≈ 2400×1500px)
- Generous padding/margins — figures should never feel cramped
- White background (`#ffffff`), no chart border or outer box

### Background & Grid
- Background: white
- No gridlines
- Remove top and right axis spines always; for horizontal bar charts also remove the left spine

### Typography
- Font family: sans-serif (**Inter**, fallback: Helvetica Neue, then Arial)
- Title: bold, 14–16pt, top-left aligned. Declarative/factual — states what the figure shows, no stats, no p-values, no "Figure N" label
- Subtitle: one line below the title, 9–10pt, regular weight, `#555555` — describes what's measured, sample, time period; no statistics
- Axis labels: skip where possible — no axis labels that repeat the title/subtitle; label directly on the chart when possible

### Color Palette
1–3 muted colors maximum — never bright, saturated, or extravagant. For a single series use navy or dark gray; for a two-group comparison use navy + coral, or light/dark of one hue; for a ranked list use a single color.

| Use | Color | Hex |
|-----|-------|-----|
| Navy | Primary / single series | `#2c5f8a` |
| Coral | Second series | `#c0392b` |
| Steel | Third series | `#5b9ec9` |
| Sand | Fourth series | `#e8b84b` |
| Sage | Fifth series | `#6aab8e` |
| Light gray / dark gray | Neutral / reference | `#a6a6a6` / `#404040` |

Avoid: bright/saturated colors, more than 3 colors in one figure, blue+green+purple combos that clash — when in doubt, use fewer colors.

### Chart Types
Prefer: horizontal bar charts, vertical bar charts, line plots. Avoid pie charts. No border/edge on bars.

### Labels & Annotations
- For line charts: label series directly at the end of the line rather than using a legend; legend only when >4 overlapping lines, no border box
- For bar charts: data labels on or above bars are preferred over a separate legend
- Arrows (→/←) and Δ/change values are appropriate for before/after comparisons; keep annotation text small (8pt) and uncluttered
- Source attribution always present, bottom of figure, 7.5pt plain text (e.g., "Source: Revelio Labs")
- No logos, watermarks, confidence intervals, R², or significance stars on the figure

---

## Sample Size & Coverage

Every script must print sample size diagnostics before producing any figure. For each key variable used in the analysis, print:
- Total N in the dataset
- N with non-null values for that variable
- Coverage rate (% non-null)

If coverage for any variable central to the figure is below **70%**, flag it explicitly in the console output and add a warning note to the figure title or subtitle (e.g., "Note: based on X% coverage of [variable]").

Do not suppress or hide sparse data — flag it visibly so a posting decision can be made with full information.

## Notes
- All markdown files in this folder use ALL CAPS filenames
- Figures should be clean and publication-quality
- Keep `outputs/INDEX.md` updated for every new figure
