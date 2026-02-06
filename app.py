import streamlit as st
from utils import extract_text, split_into_clauses
from risk_rules import assess_risk

st.set_page_config(page_title="Contract Risk Bot", layout="wide")

st.title("📄 Contract Analysis & Risk Assessment Bot")

uploaded_file = st.file_uploader("Upload Contract (PDF / DOCX / TXT)")

if uploaded_file:
    text = extract_text(uploaded_file)
else:
    with open("sample_contract.txt") as f:
        text = f.read()
    st.info("Using sample contract for demo")

clauses = split_into_clauses(text)

high_risk = 0
medium_risk = 0

st.subheader("🔍 Clause Risk Analysis")

for clause in clauses:
    risk, reason = assess_risk(clause)

    if risk == "HIGH":
        high_risk += 1
        st.error(f"⚠️ HIGH RISK: {reason}\n\n{clause}")

    elif risk == "MEDIUM":
        medium_risk += 1
        st.warning(f"⚠️ MEDIUM RISK: {reason}\n\n{clause}")

    else:
        st.success(f"✅ LOW RISK\n\n{clause}")

st.subheader("📊 Overall Contract Risk")

if high_risk > 2:
    st.error("Overall Risk: HIGH")
elif medium_risk > 2:
    st.warning("Overall Risk: MEDIUM")
else:
    st.success("Overall Risk: LOW")

