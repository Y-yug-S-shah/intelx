import streamlit as st
from parser_core import parse_threat_report

st.set_page_config(page_title="AI-Driven Threat Intel Parser", layout="wide")
st.title("⚡ AI-Driven Threat Intel Parser")

uploaded_file = st.file_uploader("Upload a threat report (.txt)", type=["txt"])

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    result = parse_threat_report(text)

    st.subheader("📄 Extracted Entities")
    st.json({
        "Domains": result["domains"],
        "IPs": result["ips"],
        "Hashes": result["hashes"],
        "CVEs": result["cves"],
        "Organizations": result["organizations"]
    })

    st.subheader("🧠 Generated Splunk Queries")
    for q in result["queries"]:
        st.code(q, language="bash")
