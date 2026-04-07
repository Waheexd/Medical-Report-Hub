import requests
import os

def test_upload(file_path):
    print(f"\n--- Testing: {os.path.basename(file_path)} ---")
    url = "http://localhost:8000/upload"
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(url, files=files)
        
    if response.status_code == 200:
        data = response.json()
        print("Upload Successful!")
        print(f"Extracted {len(data['results'])} test values.")
        for res in data['results']:
            print(f" - {res['test_name']}: {res['value']} {res['unit']} ({res['status']})")
    else:
        print(f"Upload Failed: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    base_path = "c:\\Users\\mohdw\\OneDrive\\Documents\\RAG\\medical-rag\\data\\"
    test_upload(base_path + "sample_report.pdf")
    test_upload(base_path + "external_sample_report.pdf")
