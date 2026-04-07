import re

def smart_chunking(text: str) -> list[str]:
    """
    Split text into chunks based on lab test entries.
    Each chunk should ideally represent one test result.
    If no test-like pattern is found, falls back to line-based splitting.
    """
    # Pattern to match: Test Name [optional space] Value [optional space] Unit [optional Range]
    # Example: "Hemoglobin 14.5 g/dL 13.5-17.5"
    # Example: "WBC: 4500 cells/µL (4000-11000)"
    
    # We'll split the text into lines first
    lines = text.split('\n')
    chunks = []
    current_chunk = ""

    for line in lines:
        # If the line looks like a header or is empty, we might want to start a new chunk or append
        line = line.strip()
        if not line:
            continue
            
        # Regex to detect a potential test line: starts with text, followed by a number
        # This is a broad heuristic to group related lines
        if re.search(r'^[A-Za-z\s\(\)]+[:\s\t]+[\d\.]+', line):
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = line
        else:
            # If it doesn't look like a new test, it might be a continuation or metadata
            if current_chunk:
                current_chunk += " " + line
            else:
                current_chunk = line
                
    if current_chunk:
        chunks.append(current_chunk.strip())
        
    # If the smart chunking resulted in too few chunks, fallback to simpler line-based
    if len(chunks) < 3:
        return [l.strip() for l in lines if l.strip()]
        
    return chunks

def extract_values_from_chunks(chunks: list[str], reference_ranges: dict) -> list[dict]:
    """
    Extract specific test values from chunks using a dictionary of known tests.
    """
    extracted_results = []
    
    for chunk in chunks:
        for test_name, ref in reference_ranges.items():
            # Search for the test name in the chunk (case insensitive)
            if re.search(rf'\b{test_name}\b', chunk, re.IGNORECASE):
                # Try to extract the number following the name
                # Matches patterns like "Hemoglobin: 14.5" or "Hematocrit 45%"
                match = re.search(rf'{test_name}[:\s\t]+([\d\.]+)', chunk, re.IGNORECASE)
                if match:
                    try:
                        value = float(match.group(1))
                        extracted_results.append({
                            "test_name": test_name,
                            "value": value,
                            "unit": ref["unit"],
                            "min": ref["min"],
                            "max": ref["max"],
                            "context": chunk
                        })
                        # Once we find a match for this test name, move to the next chunk
                        break
                    except ValueError:
                        continue
                        
    return extracted_results
