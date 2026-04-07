import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF file using PyMuPDF.
    """
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def clean_text(text: str) -> str:
    """
    Basic text cleaning to remove extra whitespace and non-printable characters.
    """
    # Remove excessive newlines
    text = re.sub(r'\n+', '\n', text)
    # Remove excessive spaces
    text = re.sub(r' +', ' ', text)
    return text.strip()
