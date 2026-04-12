# 🩺 Medical Report Hub

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://medical-report-app.streamlit.app/)

An advanced AI-powered laboratory report analyzer that helps users understand their medical results using Retrieval-Augmented Generation (RAG).

**Live Demo:** [medical-report-app.streamlit.app](https://medical-report-app.streamlit.app/)

---

## 🚀 Features
- **Multi-Format Support:** Extracts data from both **PDFs** and **Images** (JPG/PNG) using Groq's Vision capabilities.
- **Abnormal Value Detection:** Automatically flags results outside normal ranges for common tests (CBC, Lipid Panel, Metabolic Panel, etc.).
- **AI-Powered Analysis:** Generates a professional summary and deep insights into your report.
- **Interactive AI Assistant:** A specialized chatbot to answer your questions about the report's findings in simple language.
- **Multi-Language Support:** Generate summaries and chat in **English** or **Hindi**.
- **Personalized Medical Glossary:** Defines complex medical terms found specifically in *your* report.
- **Downloadable Reports:** Export the AI analysis and results into a clean PDF format.

---

## 🛠️ Architecture
- **Frontend/Backend:** Standalone **Streamlit** application (Python).
- **RAG Pipeline:**
  - **Text Extraction:** PyMuPDF (for PDFs) and Groq Llama-3-70b-vision (for images).
  - **Embeddings:** `all-MiniLM-L6-v2` (HuggingFace) for efficient local vector search.
  - **Vector Store:** **FAISS** (Local) for context retrieval.
  - **LLM:** **Groq Llama-3** (70B/8B) for fast, high-quality reasoning.
- **Styling:** Custom Vanilla CSS for a premium medical-grade UI.

---

## 📥 Local Setup Instructions

### 1. Prerequisites
- Python 3.10+
- [Groq API Key](https://console.groq.com/)

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/Waheexd/Medical-Report-Hub.git
cd Medical-Report-Hub

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory with your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Running the Application
```bash
streamlit run app.py
```
*The app will open in your browser at http://localhost:8501*

---

## ⚠️ Safety Disclaimer
This application is for **educational and informational purposes only**. It is **not** a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition. Never disregard professional medical advice or delay in seeking it because of something you have read here.
