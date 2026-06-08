# Data Paths & Variables

All data lives on Zaratan HPC. All input files are Parquet format.

---

## Root Paths

| Name | Path |
|------|------|
| Data root | `/scratch/zt1/project/estarr-prj/user/rylan/revelio-pitchbook-uspto/rpb-data` |
| Revelio | `/scratch/zt1/project/estarr-prj/user/rylan/revelio-pitchbook-uspto/rpb-data/revelio` |
| PitchBook | `/scratch/zt1/project/estarr-prj/user/rylan/revelio-pitchbook-uspto/rpb-data/pitchbook` |
| Code | `/scratch/zt1/project/estarr-prj/user/rylan/geographic-expansion/code` |
| Slurm scripts | `/scratch/zt1/project/estarr-prj/user/rylan/geographic-expansion/slurm` |
| Slurm out/err | `/scratch/zt1/project/estarr-prj/user/rylan/geographic-expansion/slurm/out_err` |

## Input Files

| Table | Path | Grain |
|-------|------|-------|
| `company_mapping` | `.../revelio/company_mapping.parquet` | One row per company |
| `job_postings` | `.../revelio/job_postings.parquet` | One row per job posting |
| `raw_positions_subset` | `.../revelio/raw_positions_subset.parquet` | One row per individual career position; raw position titles for every career history |
| `individual_positions` | `.../revelio/individual_positions_parquet/year=*/` | Hive-partitioned by year (1950–2026); one row per individual career position |
| `rpb_bridge` | `.../rpb-bridge.parquet` | Links Revelio companies to PitchBook companies |
| `pitchbook_companies` | `.../pitchbook/pitchbook_companies.parquet` | One row per company (subset of fields retained) |
| `pitchbook_deals` | `.../pitchbook/pitchbook_deals.parquet` | One row per deal |
| `pitchbook_investors` | `.../pitchbook/pitchbook_investors.parquet` | One row per investor |

## Infrastructure

| Name | Path |
|------|------|
| Conda env | `/scratch/zt1/project/estarr-prj/user/rylan/envs/text-analysis` |
| Python | `/scratch/zt1/project/estarr-prj/user/rylan/envs/text-analysis/bin/python3` |
| Pip cache | `/scratch/zt1/project/estarr-prj/user/rylan/pip_cache` |

---

## Variable Dictionaries

All scripts must select only the columns listed below — drop everything else at load time to keep memory usage low.

### company_mapping

| Column | Type | Description |
|--------|------|-------------|
| `rcid` | DOUBLE | Unique company identifier |
| `company` | VARCHAR | Company name |
| `year_founded` | DOUBLE | Year company was founded |
| `hq_zip_code` | VARCHAR | |
| `hq_city` | VARCHAR | |
| `hq_metro_area` | VARCHAR | |
| `hq_state` | VARCHAR | |
| `hq_country` | VARCHAR | |

### job_postings

| Column | Type | Description |
|--------|------|-------------|
| `job_id` | BIGINT | Unique job posting identifier |
| `rcid` | BIGINT | Identifier of the firm that posted the job (links to `company_mapping.rcid`) |
| `role_k17000_v3` | VARCHAR | Role characterization |
| `country` | VARCHAR | Country where the role is based |
| `state` | VARCHAR | State where the role is based |
| `post_date` | VARCHAR | Date the posting went live |
| `remove_date` | VARCHAR | Date the posting was removed |
| `remote_type` | VARCHAR | Whether the role is listed as remote |
| `expected_hires` | DOUBLE | Number of hires the company aims to make |

### individual_positions

Hive-partitioned by year. Read across all years using a glob pattern. Always exclude the null partition. Drop complete duplicate rows before any analysis.

```python
# Correct pattern for loading
read_parquet('/scratch/zt1/project/estarr-prj/user/rylan/revelio-pitchbook-uspto/rpb-data/revelio/individual_positions_parquet/year=*//*.parquet')

# Always filter out the null partition using the filename virtual column
WHERE NOT contains(filename, 'HIVE_DEFAULT_PARTITION')
```

| Column | Type | Description |
|--------|------|-------------|
| `user_id` | VARCHAR | Unique individual identifier — positions are nested within users |
| `position_id` | VARCHAR | Unique position identifier (links to `raw_positions_subset.position_id`) |
| `country` | VARCHAR | Country where the position was held |
| `state` | VARCHAR | State where the position was held |
| `startdate` | VARCHAR | Position start date |
| `enddate` | VARCHAR | Position end date |
| `role_k17000_v3` | VARCHAR | Role characterization |
| `weight` | VARCHAR | |
| `seniority` | VARCHAR | Seniority level of the position |
| `position_number` | VARCHAR | Order of this position within the individual's career history |
| `rcid` | VARCHAR | Company identifier (links to `company_mapping.rcid`) |
| `year` | BIGINT | Partition year — exclude `__HIVE_DEFAULT_PARTITION__` in all queries |

### raw_positions_subset

Raw position titles for every individual career history. Links to the individual positions file via `position_id`.

| Column | Type | Description |
|--------|------|-------------|
| `position_id` | BIGINT | Unique position identifier (links to individual positions file) |
| `title_raw` | VARCHAR | Raw position title as entered by the individual |

### rpb_bridge

*Not in use for current descriptives. Skip.*

### pitchbook_companies

All column names must be lowercased on load (e.g., `CompanyID` → `company_id`).

| Original Column | Lowercased | Type | Description |
|----------------|------------|------|-------------|
| `CompanyID` | `company_id` | VARCHAR | Unique PitchBook company identifier |
| `CompanyName` | `company_name` | VARCHAR | Company name |
| `CompanyFinancingStatus` | `company_financing_status` | VARCHAR | |
| `TotalRaised` | `total_raised` | VARCHAR | |
| `BusinessStatus` | `business_status` | VARCHAR | |
| `OwnershipStatus` | `ownership_status` | VARCHAR | |
| `YearFounded` | `year_founded` | VARCHAR | |
| `PrimaryIndustrySector` | `primary_industry_sector` | VARCHAR | |
| `PrimaryIndustryGroup` | `primary_industry_group` | VARCHAR | |
| `PrimaryIndustryCode` | `primary_industry_code` | VARCHAR | |
| `AllIndustries` | `all_industries` | VARCHAR | |
| `Verticals` | `verticals` | VARCHAR | |
| `HQAddressLine1` | `hq_address_line1` | VARCHAR | |
| `HQCity` | `hq_city` | VARCHAR | |
| `HQState_Province` | `hq_state_province` | VARCHAR | |
| `HQPostCode` | `hq_post_code` | VARCHAR | |
| `HQCountry` | `hq_country` | VARCHAR | |

### pitchbook_deals

*Not in use for current descriptives. Skip.*

### pitchbook_investors

*Not in use for current descriptives. Skip.*
