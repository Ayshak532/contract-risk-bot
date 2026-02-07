# Contract Risk Bot 📄⚖️

## Overview
Contract Risk Bot is a simple AI-powered web application that analyzes legal contracts and highlights potential risk clauses.  
It helps users quickly understand whether a contract contains **LOW, MEDIUM, or HIGH risk** terms based on predefined legal keywords.

This project was built as part of the **GUVI Hackathon** to demonstrate applied logic, text processing, and cloud deployment using Streamlit.

---

## Features
- Upload contracts in **PDF, DOCX, or TXT** format
- Automatically splits contracts into meaningful clauses
- Detects risky clauses such as:
  - Penalties
  - Indemnity
  - Immediate termination
  - Legal jurisdiction and arbitration
- Displays:
  - Clause-level risk (LOW / MEDIUM / HIGH)
  - Overall contract risk summary
- Includes a **sample contract** for demo purposes

---

## Tech Stack
- **Python**
- **Streamlit** (Web UI & deployment)
- **PyPDF2** (PDF text extraction)
- **python-docx** (DOCX parsing)

---

## How It Works
1. User uploads a contract (or a sample contract is used by default)
2. Text is extracted from the document
3. Contract text is split into clauses
4. Each clause is analyzed using rule-based risk logic
5. Risk results are displayed in the UI

---

## Live Demo
🔗 Deployed Application:
https://contract-risk-bot-offy9fc9pug7rzzjecbrhf.streamlit.app/

---

## Demo Video
🎥 Project Walkthrough (Google Drive):
https://drive.google.com/file/d/1gCY-ht93i98RVZVjvJMYj33WPb6AVP9V/view?usp=drive_link

---

## GitHub Repository
🔗 https://github.com/Ayshak532/contract-risk-bot

---

## Note
For deployment stability, all core logic is implemented directly in `app.py`.  
Supporting files (`utils.py`, `risk_rules.py`) are retained for structure and documentation clarity.

---

## Author
**Aysha K**  
GUVI Hackathon Participant
