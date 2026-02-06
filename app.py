import streamlit as st
import PyPDF2
from docx import Document

# Page config
st.set_page_config(page_title="Contract Risk Bot", layout="wide")

st.title("📄 Contract Analysis & Risk Assessment Bot")

# --------- Helper Functions ---------

def extract_text(file):
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    if file.name.endswith(".docx"):
        doc = Document(file)
        return "\n".join(p.text for p in doc.paragraphs)

    if file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        return "\n".join(page.extract_text() for page in reader.pages)

    return ""


def split_into_clauses(text):
    clauses = []
    for line in text.split("\n"):
        if len(line.strip()) > 40:
            clauses.append(line.strip())
    return clauses


def assess_risk(clause):
    clause = clause.lower()

    if any(word in clause for word in ["penalty", "terminate immediately", "indemnify", "liability"]):
        return "HIGH", "Contains penalty, indemnity, or termination risk"

    if any(word in clause for word in ["arbitration", "jurisdiction", "governing law"]):
        return "MEDIUM", "Legal jurisdiction or arbitration clause"

    return "LOW", "Standard clause"


# --------- App Logic ---------

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
