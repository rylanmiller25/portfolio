# Descriptives — Agent Guidelines

## About This Subproject

This is the `descriptives/` subproject of the `portfolio` repo — descriptive figures and data visualizations built from labor-market and startup datasets. The CV, website, and other portfolio pieces live in sibling folders of the same repo (`docs/`, `website/`).

The goal is to present a clear picture of my work, interests, and approach to anyone viewing externally.

## Data Sources

The primary data underlying figures and descriptives:

- **Revelio Labs** — Full LinkedIn dataset: individual career histories and job postings
- **PitchBook** — Data on venture-backed and high-growth startups and private companies
- **USPTO Patents** — Patent filings data

These datasets are linkable via a bridge I maintain. Analysis will draw on combinations of these sources to produce insights about labor markets, career trajectories, and startup ecosystems.

## Goals for Figures and Descriptives

Figures should be interesting and accessible to a professional audience. Good topics include:

- Trends in job postings and labor demand
- Career path patterns across industries and geographies
- Startup growth and hiring dynamics
- Cross-dataset insights (e.g., patent activity + hiring + career histories)

The bar is: would a smart, non-academic professional find this interesting and share-worthy?

## TODO

Items needed before the descriptives pipeline can be fully automated. Each item is tagged by owner.

### User
- [x] Provide figure formatting preferences: a reference figure or describe preferred style (colors, font, size, chart style) (User)
- [x] Provide LinkedIn post examples or describe preferred tone, length, and format (User)
- [x] Provide file paths for all datasets — documented in `DATA.md` (User)
- [x] Provide variable dictionaries for each dataset: column names, types, and descriptions — documented in `DATA.md` (User)
- [x] Confirm preferred coding language: Python (User)
- [ ] Review and prioritize ideas in `descriptives/IDEAS.md` — flag which to build first (User)
### Claude
- [x] Write figure formatting spec into `descriptives/CLAUDE.md` (Claude)
- [x] Write LinkedIn post formatting spec into `descriptives/CLAUDE.md` (Claude)
- [ ] Write analysis and figure-generation code for each idea in `descriptives/IDEAS.md` (Claude)
- [ ] Draft LinkedIn posts for each completed figure (Claude)
- [ ] Keep `outputs/INDEX.md` up to date, linking each figure to its output and source idea (Claude)

---

## Compute & Workflow

All analysis code is written locally but runs on **Zaratan** (UMD HPC cluster), where the data lives. All data paths, file locations, and variable dictionaries are documented in `DATA.md`.

The workflow is:

1. I write both a `.py` script and a corresponding `.slurm` file
2. You transfer both to Zaratan (`code/` and `slurm/` respectively) and submit via `sbatch`
3. Logs go to `slurm/out_err/`; figures are saved to a specified output path
4. You pull the output PNGs back to your local machine and place them in `outputs/`

**Implications for code I write:**
- I cannot run or verify the code — paths and variable names must be exact
- Scripts should be fully self-contained and runnable as-is on Zaratan
- Always include an output path variable at the top of each script so it is easy to redirect
- Create output directories within the script if they don't exist (`os.makedirs(..., exist_ok=True)`)
- Save all figures as PNG at 1200×900px, 150 dpi
- Every `.py` script gets a paired `.slurm` file using this template:

```bash
#!/bin/bash
#SBATCH --job-name=<job_name>
#SBATCH --output=/scratch/zt1/project/estarr-prj/user/rylan/portfolio/code/output/%x_%j.out
#SBATCH --error=/scratch/zt1/project/estarr-prj/user/rylan/portfolio/code/err/%x_%j.err
#SBATCH --time=01:00:00
#SBATCH --mem=32G
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4

/scratch/zt1/project/estarr-prj/user/rylan/envs/text-analysis/bin/python3 \
    /scratch/zt1/project/estarr-prj/user/rylan/geographic-expansion/code/<script_name>.py
```

Adjust `--mem` and `--time` based on the size of data being loaded. The `individual_positions` glob across all years will require more memory than single-file jobs.

### Confirmed libraries
- Data: `pandas`, `pyarrow`, `duckdb`, `numpy`, `scipy`
- Plotting: `matplotlib`, `seaborn`
- No `plotly` — all figures use matplotlib/seaborn only

### DuckDB for data loading
Use `duckdb` to query Parquet files rather than loading them fully into pandas. The datasets are large; DuckDB reads Parquet efficiently and supports SQL directly on the files without loading everything into memory. Pattern:
```python
import duckdb
con = duckdb.connect()
df = con.execute("SELECT ... FROM read_parquet('/path/to/file.parquet') WHERE ...").df()
```

### Font note
Inter is specified in the figure style guide but may not be available on Zaratan. Each script should attempt to load Inter, then fall back gracefully:
```python
from matplotlib import font_manager
try:
    font_manager.findfont("Inter", fallback_to_default=False)
    plt.rcParams["font.family"] = "Inter"
except:
    plt.rcParams["font.family"] = "DejaVu Sans"
```

---

## Agent Behavior Rules

- **I use voice-to-text (Wispr Flow).** My messages are dictated, not typed. Do not transcribe my phrasing literally — summarize, clean up, and make it coherent.
- **Be concise.** Short, direct responses are preferred over lengthy explanations.
- **No unsolicited refactoring or cleanup.** Do only what is asked.
- **No unnecessary comments in code.** Only add comments when the reason behind something is non-obvious.
- **Prefer editing existing files** over creating new ones.
- **Commit and push frequently.** After any meaningful set of changes, commit and push to `origin/main` without waiting to be asked.
