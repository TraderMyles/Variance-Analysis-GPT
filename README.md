# 📊 Variance Analysis + GPT Commentary Generator

This project automates the process of calculating budget vs. actual variances and generates natural language commentary using OpenAI's GPT-4 model. Ideal for FP&A professionals, analysts, and anyone who wants to save hours writing financial insights.

---

## ✅ Features
- Upload your financials as an Excel file
- Automatically calculate variance and % variance
- GPT generates board-level commentary
- Outputs a polished Excel report with insights

---

## 🧰 Requirements

- Python 3.10+
- OpenAI Python SDK (`openai>=1.0.0`)
- Excel file with columns: `Account`, `Actual`, `Budget`

---

## 🧪 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/variance-gpt.git
cd variance-gpt

### 2. Create a Virtual Environment

# Git Bash or PowerShell (Windows)
python -m venv venv
source venv/Scripts/activate  # or .\venv\Scripts\activate in PowerShell

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Set Your OpenAI API Key
Option A: Use .env file (Recommended)
Create a file named .env in the root directory and add:

OPENAI_API_KEY=sk-your-openai-key-here

The script will automatically load this using python-dotenv.

Option B: Export manually in terminal

# Git Bash
export OPENAI_API_KEY=sk-your-openai-key-here

# PowerShell
$env:OPENAI_API_KEY="sk-your-openai-key-here"

📂 File Structure

variance-gpt/
├── data/
│   └── financials.xlsx         # Your input file
├── outputs/
│   └── commentary_output.xlsx  # Your generated output
├── variance_generator.py       # Main script
├── requirements.txt
└── .env                        # (optional) API key file

🚀 How to Run

📺 Option 1: Run the Streamlit Web App (Recommended)
To launch the web interface:

streamlit run stream.py

Note: Running with python stream.py won't work — use the streamlit run command to launch the app properly.

Once running, you can upload your Excel file directly in the browser and download a final version with GPT-generated commentary.

⚙️ Option 2: Run as a Script
You can also run the generator manually:

1. Place your Excel file in the data/ folder.

2. Run: python variance_generator.py

3. Your processed file will be saved to the outputs/ folder.

📂 File Structure
variance-gpt/
├── data/
│   └── financials.xlsx         # Input file
├── outputs/
│   └── commentary_output.xlsx  # Output with GPT commentary
├── stream.py                   # Streamlit web app
├── variance_generator.py       # Script version
├── requirements.txt
└── .env                        # (optional) API key



🧠 Sample Output

| Account | Actual | Budget | Variance | % Variance | Commentary                         |
| ------- | ------ | ------ | -------- | ---------- | ---------------------------------- |
| Revenue | 95000  | 100000 | -5000    | -5.0%      | Revenue came in 5% below budget... |
| COGS    | 45000  | 40000  | +5000    | +12.5%     | COGS exceeded budget...            |


🙌 Credits
Built by Myles Williams, a finance professional turned automation builder.

🧠 Future Plans
- Streamlit web app version
- Slack/email auto-report delivery
- CSV upload & GPT agent integration