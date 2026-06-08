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

Inspired by Peter Walker's Carta charts — clean, modern, and professional. Do not copy exactly; use as a reference aesthetic.

Reference images are in `descriptives/examples/`. When new examples are added, read them and update this spec accordingly.

### Layout & Size
- Output format: **PNG**
- Output size: **1200 × 900px** (suitable for LinkedIn)
- Generous padding/margins — figures should never feel cramped
- No chart border or outer box

### Background & Grid
- Background: light cream (`#FAF7F2`) — matches website background
- Gridlines: horizontal only, warm gray (`#E8E2D9`), no vertical gridlines
- No axis spines except the x-axis baseline (bottom); remove top, right, and left spines

### Typography
- Font family: **Inter** (fallback: DM Sans, then sans-serif)
- Title: bold, ~18–20pt, near-black (`#1A1A1A`)
- Subtitle or annotation: regular, ~13pt, dark gray (`#2D2D2D`)
- Axis labels and tick labels: ~11pt, dark gray (`#2D2D2D`)
- No axis titles unless absolutely necessary — label directly on the chart when possible

### Color Palette
For single-series figures, use the primary crimson. For multi-series, use the full warm palette in order — each color is clearly distinct while staying within the same warm family.

| Use | Color | Hex |
|-----|-------|-----|
| Primary / single series | Panel red | `#BE4342` |
| Second series | Burnt orange | `#D35400` |
| Third series | Amber | `#E67E22` |
| Fourth series | Gold | `#F0A500` |
| Reference line / neutral | Warm gray | `#9E8E7E` |

Avoid: blue, green, purple, rainbow palettes, or anything that clashes with the warm cream background.

### Chart Types
Prefer: horizontal bar charts, vertical bar charts, line plots, and small multiples. Avoid pie charts. For bar charts, use clean rectangular bars with no border stroke and slight rounding only if it looks natural in the library being used.

### Labels & Annotations
- For line charts: label series directly at the end of the line rather than using a legend
- For bar charts: data labels on or above bars are preferred over a separate legend when there are few series
- Call out the key insight with a short in-chart annotation when it adds clarity
- Source attribution in small text at the bottom of the figure (e.g., "Source: Revelio Labs")

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
