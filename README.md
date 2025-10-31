# INTELX - AI-Driven Threat Intelligence Parser

**INTELX** is a lightweight Streamlit-based demo project that uses AI (via spaCy NLP) to parse unstructured threat intelligence reports and automatically generate actionable Splunk hunting and detection queries.

---

## 🚀 Features
- Parses **unstructured threat reports** in `.txt` format  
- Extracts key threat indicators: **domains, IPs, hashes, CVEs, and organizations**  
- Generates **Splunk-compatible hunting queries** automatically  
- Uses **spaCy NLP pipelines** for named entity recognition  
- Simple **Streamlit UI** for quick demo and interaction  

---

## 🧠 How It Works
1. Upload a `.txt` threat report.  
2. The app extracts threat entities using regex and NLP.  
3. INTELX generates Splunk detection and hunting queries dynamically.  
4. Entities and queries are displayed in an interactive Streamlit dashboard.

---

## ⚙️ Installation & Usage

```bash
# Clone the repository
git clone https://github.com/<your-username>/intelx.git
cd intelx

# Install dependencies
pip install -r requirements.txt

# Download spaCy language model
python -m spacy download en_core_web_sm

# Run the app
streamlit run app.py
