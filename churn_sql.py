# churn_sql.py
# Run this script from the folder that contains dataset.csv
# python3 churn_sql.py

import sqlite3
import pandas as pd
from pathlib import Path

# ---------- Paths ----------
HERE = Path(__file__).resolve().parent
CSV_PATH = HERE / "dataset.csv"      # <-- your file’s actual name
DB_PATH  = HERE / "churn.db"

# ---------- Load & clean ----------
if not CSV_PATH.exists():
    raise FileNotFoundError(f"Could not find {CSV_PATH}. Make sure dataset.csv is in the same folder as this script.")

df = pd.read_csv(CSV_PATH)

# Fix known issue: blank/space TotalCharges -> numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"].astype(str).str.strip().replace({"": None}),
    errors="coerce",
)
# Backfill with MonthlyCharges * tenure (simple proxy)
df["TotalCharges"] = df["TotalCharges"].fillna(df["MonthlyCharges"] * df["tenure"])

# Add numeric churn flag (handy later)
df["ChurnFlag"] = df["Churn"].map({"Yes": 1, "No": 0})

# ---------- Save to SQLite ----------
conn = sqlite3.connect(DB_PATH)
df.to_sql("customers", conn, if_exists="replace", index=False)

def q(sql: str) -> pd.DataFrame:
    return pd.read_sql(sql, conn)

# ---------- Core SQL ----------
print("\n=== Total customers ===")
total_df = q("""
SELECT COUNT(*) AS total_customers
FROM customers;
""")
print(total_df)

print("\n=== Churn counts & rate ===")
churn_rate_df = q("""
SELECT
  Churn,
  COUNT(*) AS cnt,
  ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM customers), 2) AS pct
FROM customers
GROUP BY Churn
ORDER BY Churn DESC;
""")
print(churn_rate_df)

print("\n=== Churn by Contract Type ===")
by_contract_df = q("""
SELECT
  Contract,
  SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS churn_yes,
  COUNT(*) AS total,
  ROUND(100.0 * SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS churn_rate_pct
FROM customers
GROUP BY Contract
ORDER BY churn_rate_pct DESC;
""")
print(by_contract_df)

print("\n=== Churn by Payment Method ===")
by_payment_df = q("""
SELECT
  PaymentMethod AS payment_method,
  ROUND(100.0 * SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) AS churn_rate_pct,
  COUNT(*) AS total
FROM customers
GROUP BY PaymentMethod
ORDER BY churn_rate_pct DESC;
""")
print(by_payment_df)

print("\n=== Avg Monthly/Total Charges by Churn ===")
charges_df = q("""
SELECT
  Churn,
  ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges,
  ROUND(AVG(TotalCharges), 2)  AS avg_total_charges
FROM customers
GROUP BY Churn;
""")
print(charges_df)

print("\n=== Monthly revenue at risk (rough) ===")
revenue_risk_df = q("""
SELECT
  ROUND(SUM(CASE WHEN Churn='Yes' THEN MonthlyCharges ELSE 0 END), 2) AS monthly_revenue_at_risk
FROM customers;
""")
print(revenue_risk_df)

# ---------- Export dashboard-ready CSVs ----------
(out_dir := HERE / "outputs").mkdir(exist_ok=True)
total_df.to_csv(out_dir / "kpi_total_customers.csv", index=False)
churn_rate_df.to_csv(out_dir / "kpi_churn_rate.csv", index=False)
by_contract_df.to_csv(out_dir / "churn_by_contract.csv", index=False)
by_payment_df.to_csv(out_dir / "churn_by_payment_method.csv", index=False)
charges_df.to_csv(out_dir / "charges_by_churn.csv", index=False)
revenue_risk_df.to_csv(out_dir / "kpi_monthly_revenue_at_risk.csv", index=False)

conn.close()
print(f"\n✔ Done. SQLite DB saved at: {DB_PATH}")
print(f"✔ Dashboard CSVs saved in: {out_dir}")
