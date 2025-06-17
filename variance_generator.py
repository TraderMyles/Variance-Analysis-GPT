import pandas as pd
from openai import OpenAI
import os
from dotenv import load_dotenv

# === Load .env ===
load_dotenv()

# === Load your OpenAI API key ===
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Load from .env or environment

# === Load Excel ===
df = pd.read_excel("data/financials.xlsx")

# === Calculate variance ===
df["Variance"] = df["Actual"] - df["Budget"]
df["% Variance"] = round((df["Variance"] / df["Budget"]) * 100, 2)

# === Define GPT Commentary Function ===
def generate_commentary(row):
    prompt = (
        f"Account: {row['Account']}\n"
        f"Actual: {row['Actual']}\n"
        f"Budget: {row['Budget']}\n"
        f"Variance: {row['Variance']} ({row['% Variance']}%)\n\n"
        f"Write a short financial analysis commentary in plain English."
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a financial analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=100
    )

    return response.choices[0].message.content.strip()

# === Apply GPT commentary to each row ===
df["Commentary"] = df.apply(generate_commentary, axis=1)

# === Export to Excel ===
output_path = "outputs/commentary_output.xlsx"
os.makedirs("outputs", exist_ok=True)
df.to_excel(output_path, index=False)

print(f"✅ Commentary file saved to: {output_path}")
