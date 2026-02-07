import streamlit as st
import PyPDF2
from docx import Document

# --------------------------------------------------
# Page config (MUST be first Streamlit command)
# --------------------------------------------------
st.set_page_config(page_title="Contract Risk Bot", layout="wide")

# --------------------------------------------------
# Session State Initialization
# --------------------------------------------------
if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

if "results" not in st.session_state:
    st.session_state.results = []

st.title("📄 Contract Analysis & Risk Assessment Bot")

# --------------------------------------------------
# Helper Functions
# --------------------------------------------------
def extract_text(file):
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    if file.name.endswith(".docx"):
        doc = Document(file)
        return "\n".join(p.text for p in doc.paragraphs)

    if file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

    return ""


def split_into_clauses(text):
    clauses = []
    for line in text.split("\n"):
        line = line.strip()
        if len(line) > 40:
            clauses.append(line)
    return clauses


def assess_risk(clause):
    clause_lower = clause.lower()

    if any(word in clause_lower for word in ["penalty", "terminate immediately", "indemnify", "liability"]):
        return "HIGH", "Contains penalty, indemnity, or termination risk"

    if any(word in clause_lower for word in ["arbitration", "jurisdiction", "governing law"]):
        return "MEDIUM", "Legal jurisdiction or arbitration clause"

    return "LOW", "Standard clause"


# --------------------------------------------------
# App Logic
# --------------------------------------------------
uploaded_file = st.file_uploader("Upload Contract (PDF / DOCX / TXT)", type=["pdf", "docx", "txt"])

# Reset analysis when new file is uploaded
if uploaded_file:
    st.session_state.analysis_done = False
    st.session_state.results = []

# Load text
if uploaded_file:
    text = extract_text(uploaded_file)
else:
    with open("sample_contract.txt") as f:
        text = f.read()
    st.info("Using sample contract for demo")

# --------------------------------------------------
# Run analysis ONLY ONCE
# --------------------------------------------------
if not st.session_state.analysis_done:
    clauses = split_into_clauses(text)

    for clause in clauses:
        risk, reason = assess_risk(clause)
        st.session_state.results.append((clause, risk, reason))

    st.session_state.analysis_done = True

# --------------------------------------------------
# Display Clause Risk Analysis
# --------------------------------------------------
st.subheader("🔍 Clause Risk Analysis")

high_risk = 0
medium_risk = 0

for clause, risk, reason in st.session_state.results:

    if risk == "HIGH":
        high_risk += 1
        st.error(f"⚠️ **HIGH RISK**: {reason}\n\n{clause}")

    elif risk == "MEDIUM":
        medium_risk += 1
        st.warning(f"⚠️ **MEDIUM RISK**: {reason}\n\n{clause}")

    else:
        st.success(f"✅ **LOW RISK**\n\n{clause}")

# --------------------------------------------------
# Overall Contract Risk (CORRECT LOGIC)
# --------------------------------------------------
st.subheader("📊 Overall Contract Risk")

if high_risk > 0:
    st.error("Overall Risk: HIGH")
elif medium_risk > 0:
    st.warning("Overall Risk: MEDIUM")
else:
    st.success("Overall Risk: LOW")
