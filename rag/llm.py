from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm(model_name: str = "llama-3.3-70b-versatile"):
    """
    Initialize and return the LLM using Groq (Free Tier).
    Requires GROQ_API_KEY to be set in the environment.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment. Please set it in .env file.")
        
    llm = ChatGroq(
        model=model_name,
        temperature=0.0,
        api_key=api_key
    )
    return llm

def get_vision_llm(model_name: str = "meta-llama/llama-4-scout-17b-16e-instruct"):
    """
    Initialize and return the Vision LLM using Groq.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment.")
        
    llm = ChatGroq(
        model=model_name,
        temperature=0.0,
        api_key=api_key
    )
    return llm

def generate_medical_prompt_template(language: str = "English"):
    """
    Create the prompt template for the medical assistant.
    Supports English and Hindi.
    """
    language_instruction = f"Please provide your explanation in {language}."
    
    template = f"""
    You are a medical assistant. Your job is to explain lab results in simple terms based on the provided context.
    {language_instruction}

    Rules:
    - Do NOT provide medical diagnosis.
    - Clearly explain whether a value is normal or abnormal based on the context.
    - Use simple, non-technical language that a patient can understand.
    - If the answer is not in the context, say you don't know based on the current report.
    - Always include the disclaimer: 'This is not medical advice. Please consult with your doctor for professional diagnosis.'

    Context:
    {{context}}

    User Question:
    {{question}}

    Your Explanation:
    """
    return PromptTemplate(
        input_variables=["context", "question"],
        template=template
    )
