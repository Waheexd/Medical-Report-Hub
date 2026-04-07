import warnings
# Suppress Pydantic V1 warnings for Python 3.14 compatibility
warnings.filterwarnings("ignore", message="Core Pydantic V1 functionality isn't compatible with Python 3.14")

from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from rag.pipeline import MedicalRAGPipeline
import os
import shutil

app = FastAPI()
pipeline = MedicalRAGPipeline()

# Ensure temp data dir exists
os.makedirs("medical-rag/tmp", exist_ok=True)

class QueryRequest(BaseModel):
    query: str

@app.post("/upload")
async def upload_report(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF.")
        
    temp_path = f"medical-rag/tmp/{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    extracted_results, chunks = pipeline.process_new_report(temp_path)
    
    return {
        "message": "File uploaded and processed successfully",
        "results": extracted_results,
        "chunk_count": len(chunks)
    }

@app.post("/query")
async def process_query(request: QueryRequest):
    answer, sources = pipeline.answer_question(request.query)
    return {
        "answer": answer,
        "sources": sources
    }

@app.post("/analyze")
async def auto_analyze():
    summary, sources = pipeline.auto_analyze()
    return {
        "summary": summary,
        "sources": sources
    }

@app.get("/status")
async def get_status():
    if pipeline.vector_store:
        return {"status": "ready", "results": pipeline.extracted_results}
    return {"status": "empty"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
