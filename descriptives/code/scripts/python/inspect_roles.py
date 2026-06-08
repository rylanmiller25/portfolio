import duckdb

REPO = "/scratch/zt1/project/estarr-prj/user/rylan/portfolio"
BASE = "/scratch/zt1/project/estarr-prj/user/rylan/revelio-pitchbook-uspto/rpb-data/revelio/individual_positions_parquet"
POSITIONS = f"{BASE}/year=2023/*.parquet"

con = duckdb.connect()
con.execute("SET threads=8")

# Broad keyword search to find all role values containing 'product', 'program', or 'manager'
result = con.execute(f"""
    SELECT role_k17000_v3, COUNT(*) AS n
    FROM read_parquet('{POSITIONS}')
    WHERE LOWER(role_k17000_v3) LIKE '%product%'
       OR (LOWER(role_k17000_v3) LIKE '%program%' AND LOWER(role_k17000_v3) LIKE '%manager%')
    GROUP BY role_k17000_v3
    ORDER BY n DESC
""").df()

print(result.to_string())
result.to_csv(f"{REPO}/code/output/target_roles.csv", index=False)
print("\nDone.")
