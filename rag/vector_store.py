from langchain_community.vectorstores import FAISS
import os

def create_vector_store(chunks: list[str], embeddings, save_path: str = "medical-rag/data/faiss_index"):
    """
    Create a FAISS vector store from text chunks.
    """
    vector_store = FAISS.from_texts(chunks, embeddings)
    # Ensure the data directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    vector_store.save_local(save_path)
    return vector_store

def load_vector_store(embeddings, save_path: str = "medical-rag/data/faiss_index"):
    """
    Load a FAISS vector store from local storage.
    """
    if os.path.exists(save_path):
        return FAISS.load_local(save_path, embeddings, allow_dangerous_deserialization=True)
    return None
