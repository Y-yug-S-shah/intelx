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
git clone https://github.com/Y-yug-S-shah/intelx.git
cd intelx

# Install dependencies
pip install -r requirements.txt

# Download spaCy language model
python -m spacy download en_core_web_sm

# Run the app
streamlit run app.py

```

## 🔮 Future Scope

- Validate and de-duplicate IOCs  
- Filter out internal or non-relevant IP ranges  
- Integrate threat enrichment from public feeds  
- Add contextual scoring and risk tagging  
- Explore true AI-based text summarization and report correlation  

*(Open to contributions - feel free to fork, enhance, and build upon it!)*

## Sample Output
<img width="1920" height="1005" alt="cli" src="https://github.com/user-attachments/assets/419dc637-d4aa-4847-a1c4-bf31ae239499" />
<img width="1920" height="1005" alt="gui 1st part" src="https://github.com/user-attachments/assets/788e73f6-ea17-4bff-a611-ba554f0556d7" />
<img width="1920" height="1005" alt="splunk queries" src="https://github.com/user-attachments/assets/311028fb-c49a-49d5-8f5c-c3abf9b1147f" />

