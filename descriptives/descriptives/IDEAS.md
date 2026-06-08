# Descriptive Ideas — LinkedIn Data Only

Data: `individual_positions` (career histories), `job_postings`, `company_mapping`, `raw_positions_subset`. All linkable via `rcid` and `position_id`.

**Feasibility notes:**
- Industry-level analysis requires the RPB bridge + PitchBook — not available from Revelio alone
- Education/school-based analysis: no education variables in any dataset
- Skills analysis: no skills column in `job_postings`
- Role identification: `role_k17000_v3` in `individual_positions` is a standardized classification and may lack the granularity needed to identify specific roles (e.g., TPM vs. PM vs. Strategy). Where needed, join `raw_positions_subset` on `position_id` and use `title_raw` with keyword/text matching to identify target roles. Both approaches may be used depending on the analysis.

---

## Derived Variables

These can be constructed from the raw data and unlock most of the interesting analyses below.

**From `individual_positions`:**
- `tenure` — `enddate` - `startdate` per position (days or years)
- `career_gap` — time between `enddate` of position N and `startdate` of position N+1 for the same `user_id`
- `years_of_experience` — cumulative tenure across all prior positions up to a given point
- `years_before_target_role` — total years of experience before first occurrence of a target `role_k17000_v3`
- `positions_before_target_role` — `position_number` at first target role minus 1
- `career_start_year` — year extracted from the first `startdate` per `user_id` (enables cohort analysis)
- `time_to_seniority_level` — years from first position to first reaching a given seniority level
- `seniority_change` — whether seniority increased, decreased, or stayed flat between consecutive positions
- `cross_state_move` / `cross_country_move` — boolean, whether location changed between consecutive positions
- `is_current` — whether `enddate` is null (position is ongoing)
- `cohort` — decade or 5-year bin of `career_start_year`

**From `job_postings`:**
- `posting_duration` — `remove_date` - `post_date` in days (proxy for difficulty-to-fill)
- `post_year`, `post_month` — extracted from `post_date` (enables trend and seasonality analysis)
- `is_remote` — boolean from `remote_type`

---

## Career Path Patterns

- **What jobs do people have before becoming a PM, TPM, or strategy professional?** — role sequences from `role_k17000_v3` ordered by `position_number`, filtered to users whose first target role is observed
- **Has the path to PM or TPM gotten harder over time?** — same as above, segmented by `cohort` (people who reached the role in 2010 vs. 2015 vs. 2020)
- **Does the road to PM look different at Google vs. Amazon vs. Microsoft?** — prior role sequences filtered by `rcid` of target company
- **Where do people go after leaving McKinsey, BCG, or Bain?** — next `role_k17000_v3` and company after consulting firm `rcid`, ranked by frequency
- **What backgrounds do people come from before joining a top consulting firm?** — prior roles filtered to users whose first consulting firm position is observed
- **At what seniority level do people typically break into PM, TPM, or strategy?** — distribution of `seniority` at first occurrence of target `role_k17000_v3`

## Experience & Time to Role

- **How many years of experience does it take to land a PM or TPM role — and is that number growing?** — `years_before_target_role` by `cohort`
- **How many jobs does it take before someone lands their first PM or TPM role?** — `positions_before_target_role` distribution
- **Do more experienced hires enter target roles at higher seniority?** — `years_before_target_role` vs. `seniority` at entry
- **Once someone lands a PM or TPM role, how long do they stay?** — `tenure` filtered to target `role_k17000_v3`
- **Are people job-hopping more than they used to?** — average `tenure` by role over time
- **How long do people stick around at FAANG companies — and has that changed since 2020?** — `tenure` filtered by `rcid` of FAANG companies, split pre/post 2020

## Seniority Progression

- **How fast do people climb the ladder at top tech companies?** — `time_to_seniority_level` by `rcid` of target company
- **Do most people break into PM or TPM at a junior or senior level?** — distribution of `seniority` at entry into target role, by company
- **Is it getting harder to reach a senior-level role than it used to be?** — `time_to_seniority_level` by `cohort`
- **How often do career moves actually result in a step up — vs. a lateral or step down?** — distribution of `seniority_change` across all observed job transitions

## Career Gaps

- **How common are employment gaps, and are they becoming more or less stigmatized over time?** — frequency and length of `career_gap` by year
- **Does taking a career gap hurt your next role's seniority?** — `career_gap` length vs. `seniority` of the next position
- **At what career stage are people most likely to take a gap?** — `career_gap` frequency by `position_number` or seniority level

## Job Market Trends

- **Is demand for PM, TPM, and strategy roles growing or shrinking?** — posting volume by `post_year` and `role_k17000_v3`
- **When do companies actually hire? Is there a best time of year to apply?** — posting volume by `post_month` for target roles
- **Which roles are hardest to fill — and is that changing?** — `posting_duration` by `role_k17000_v3` over time
- **Are companies trying to hire more people per posting than they used to?** — `expected_hires` by role over `post_year`
- **Which cities are becoming hubs for PM and strategy roles — and which are fading?** — posting volume by metro area over time
- **How has the shift to remote work played out differently across roles?** — `is_remote` share by `role_k17000_v3` over `post_year`
- **Which cities are going most remote — and which are holding the line on in-office?** — `is_remote` share by metro area over time

## Geographic Mobility

- **How often does a career move require a physical move — and is that declining?** — `cross_state_move` rate by year
- **Where do PM and TPM professionals tend to cluster early in their careers — and does that change as they advance?** — state/metro distribution by `seniority` level
- **Which cities are gaining the most career migrants in knowledge work roles?** — net inflow by metro area, derived from `cross_state_move` + location fields

## Timely / News-Reactive

Ideas tied to current events. These should be built and posted quickly — within a few days of the news — to maximize relevance. Flag with approximate news date.

- **Where do Meta employees land after leaving — and are AI companies absorbing them?** *(Meta layoffs, May 2026)* — next company and role after Meta `rcid`, ranked by frequency; highlight share going to Anthropic, OpenAI, Google DeepMind vs. other FAANG vs. startups — `[LinkedIn]`
- **How long does it take Meta alumni to find their next role — and has that gotten harder?** *(Meta layoffs, May 2026)* — `career_gap` length for people whose last position was at Meta `rcid`, compared across layoff waves (2022, 2023, 2026) — `[LinkedIn]`
- **Which roles is Meta still actively hiring for despite the layoffs?** *(Meta layoffs, May 2026)* — Meta `rcid` job posting volume by `role_k17000_v3` in recent months vs. same period last year — `[LinkedIn]`
- **How has tenure at Meta trended — are people leaving faster than they used to?** *(Meta layoffs, May 2026)* — `tenure` at Meta `rcid` by `cohort`, line chart over time — `[LinkedIn]`

