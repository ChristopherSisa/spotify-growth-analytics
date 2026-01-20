import sqlite3
import pandas as pd

DB_PATH = "marketing.db"

tables = {
    "users": "data/users.csv",
    "touchpoints": "data/touchpoints.csv",
    "conversions": "data/conversions.csv",
    "geo_experiment": "data/geo_experiment.csv",
}

conn = sqlite3.connect(DB_PATH)

for table, path in tables.items():
    df = pd.read_csv(path)
    df.to_sql(table, conn, if_exists="replace", index=False)
    print(f"Loaded {table}: {len(df)} rows")

conn.close()
print(f"Done! Created {DB_PATH}")
