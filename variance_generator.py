import pandas as pd

# Load Excel
df = pd.read_excel("data/financials.xlsx")

# Calculate variance
df["Variance"] = df["Actual"] - df["Budget"]
df["% Variance"] = round((df["Variance"] / df["Budget"]) * 100, 2)

print(df)
