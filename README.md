# Medical Report Explainer (RAG-based)

This application allows users to upload a medical lab report (PDF), automatically extracts and analyzes key test values, and provides simple explanations using a Retrieval-Augmented Generation (RAG) pipeline.

## 🚀 Features
- **PDF Extraction:** Uses PyMuPDF for robust text extraction.
- **Smart Chunking:** Line-based splitting to preserve the context of medical test results.
- **Abnormal Value Detection:** Compares results against a dictionary of normal ranges for CBC, Lipid, and BMP tests.
- **RAG-based Q&A:** Uses LangChain, FAISS, and OpenAI to answer patient questions in simple language.
- **Safety First:** Includes clear disclaimers and avoids providing medical diagnoses.

## 🛠️ Architecture
1. **Frontend (Streamlit):** User interface for file upload, results display, and chat.
2. **Backend (FastAPI):** Orchestrates the RAG pipeline and manages temporary storage.
3. **RAG Pipeline:**
   - **Embeddings:** `all-MiniLM-L6-v2` (SentenceTransformers)
   - **Vector Store:** FAISS (Local)
   - **LLM:** OpenAI GPT-4o-mini

## 📥 Setup Instructions

### 1. Prerequisites
- Python 3.9+
- OpenAI API Key

### 2. Installation
```bash
# Clone the repository
cd medical-rag

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the `medical-rag` directory with your OpenAI API key:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Running the Application

**Step 1: Start the Backend (FastAPI)**
```bash
python main.py
```
*The backend will run on http://localhost:8000*

**Step 2: Start the Frontend (Streamlit)**
```bash
streamlit run app.py
```
*The frontend will open in your browser at http://localhost:8501*

## ⚠️ Safety Disclaimer
This is a demonstration project. It is **not** a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
