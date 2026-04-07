from langchain_community.embeddings import SentenceTransformerEmbeddings

def get_embedding_model():
    """
    Initialize and return the sentence-transformer model.
    Using 'all-MiniLM-L6-v2' for local efficiency.
    """
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings
