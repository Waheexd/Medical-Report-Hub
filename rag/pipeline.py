import os
from rag.embeddings import get_embedding_model
from rag.vector_store import create_vector_store, load_vector_store
from rag.retriever import retrieve_documents
from rag.llm import get_llm, generate_medical_prompt_template
from utils.pdf_parser import extract_text_from_pdf, clean_text
from utils.chunking import smart_chunking, extract_values_from_chunks
from utils.normal_ranges import NORMAL_RANGES, check_value

class MedicalRAGPipeline:
    def __init__(self, use_local_embeddings=True):
        self.embeddings = get_embedding_model()
        self.vector_store = None
        self.current_report_chunks = []
        self.extracted_results = []
        
    def process_new_report(self, pdf_path: str):
        """
        Process a new PDF report: extract, chunk, store, and analyze.
        """
        # 1. Extract Text
        raw_text = extract_text_from_pdf(pdf_path)
        clean_ext_text = clean_text(raw_text)
        
        # 2. Smart Chunking
        self.current_report_chunks = smart_chunking(clean_ext_text)
        
        # 3. Create Vector Store
        self.vector_store = create_vector_store(self.current_report_chunks, self.embeddings)
        
        # 4. Extract Key Values for Analysis
        self.extracted_results = extract_values_from_chunks(self.current_report_chunks, NORMAL_RANGES)
        
        # Add "Normal/High/Low" flags
        for result in self.extracted_results:
            result["status"] = check_value(result["test_name"], result["value"])
            
        return self.extracted_results, self.current_report_chunks

    def answer_question(self, query: str, language: str = "English"):
        """
        Retrieve chunks and generate an explanation using LLM.
        Supports language-specific responses.
        """
        if not self.vector_store:
            return "No medical report has been uploaded yet.", []
            
        # 1. Retrieve top-k chunks
        relevant_docs = retrieve_documents(query, self.vector_store)
        context = "\n\n".join([doc.page_content for doc in relevant_docs])
        
        # 2. Generate Prompt and LLM Response
        llm = get_llm()
        prompt_template = generate_medical_prompt_template(language=language)
        prompt = prompt_template.format(context=context, question=query)
        
        response = llm.invoke(prompt)
        
        return response.content, [doc.page_content for doc in relevant_docs]

    def auto_analyze(self, language: str = "English"):
        """
        Generate an automatic summary of the whole report.
        """
        if not self.extracted_results:
            return "No relevant test values found to analyze automatically.", []
            
        # Create a summary query for the total report
        query = "Provide a comprehensive summary of my lab results and highlight anything abnormal."
        return self.answer_question(query, language=language)

    def generate_glossary(self, language="English"):
        """
        Generate a glossary of medical terms found in the report.
        """
        if not self.extracted_results:
            return "No medical terms identified to create a glossary.", []
            
        terms = [res['test_name'] for res in self.extracted_results]
        query = f"Explain these medical terms in simple, one-sentence definitions for a patient: {', '.join(terms)}."
        return self.answer_question(query, language=language)
