import streamlit as st
import pandas as pd
from openai import OpenAI
import os
from dotenv import load_dotenv
from io import BytesIO

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- Streamlit UI ---
st.set_page_config(page_title="Variance + GPT Commentary", layout="centered")
st.title("📊 Variance Analysis + GPT Commentary Generator")
st.write("Upload an Excel file with `Account`, `Actual`, and `Budget` columns.")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)

        # Validate required columns
        required_columns = {"Account", "Actual", "Budget"}
        if not required_columns.issubset(df.columns):
            st.error(f"❌ Missing columns. Your file must include: {required_columns}")
        else:
            # Calculate variances
            df["Variance"] = df["Actual"] - df["Budget"]
            df["% Variance"] = round((df["Variance"] / df["Budget"]) * 100, 2)

            st.success("✅ Variance calculated!")
            st.dataframe(df)

            if st.button("🧠 Generate GPT Commentary"):
                with st.spinner("Asking GPT for insights..."):
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

                    df["Commentary"] = df.apply(generate_commentary, axis=1)
                    st.success("✅ GPT Commentary added!")
                    st.dataframe(df)

                    # Download
                    
                    output = BytesIO()
                    df.to_excel(output, index=False, engine='openpyxl')
                    st.download_button(
                        label="📥 Download Excel with Commentary",
                        data=output.getvalue(),
                        file_name="variance_with_commentary.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
    except Exception as e:
        st.error(f"⚠️ Error processing file: {e}")
