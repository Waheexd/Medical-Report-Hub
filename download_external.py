import requests
import os

def download_file(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded: {save_path}")
    else:
        print(f"Failed: {response.status_code}")

if __name__ == "__main__":
    download_file("https://www.labtestingapi.com/sample-report.pdf", "c:\\Users\\mohdw\\OneDrive\\Documents\\RAG\\medical-rag\\data\\external_sample_report.pdf")
