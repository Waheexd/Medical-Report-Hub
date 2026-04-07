import os
from utils.pdf_parser import extract_text_from_pdf, clean_text
from utils.chunking import smart_chunking, extract_values_from_chunks
from utils.normal_ranges import NORMAL_RANGES, check_value

def analyze_report(pdf_path):
    print(f"\n--- Standalone Analysis: {os.path.basename(pdf_path)} ---")
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    # 1. Extract Text
    text = extract_text_from_pdf(pdf_path)
    clean_ext_text = clean_text(text)
    
    # 2. Smart Chunking
    chunks = smart_chunking(clean_ext_text)
    
    # 3. Extract Values
    results = extract_values_from_chunks(chunks, NORMAL_RANGES)
    
    print(f"Extracted {len(results)} test values.")
    for res in results:
        status = check_value(res['test_name'], res['value'])
        print(f" - {res['test_name']}: {res['value']} {res['unit']} ({status})")
    
    if not results:
        print("No specific values found. Full text preview:")
        print(clean_ext_text[:200] + "...")

if __name__ == "__main__":
    base_path = "data/"
    analyze_report(base_path + "sample_report.pdf")
    analyze_report(base_path + "external_sample_report.pdf")
