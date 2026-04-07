def retrieve_documents(query: str, vector_store, k: int = 4):
    """
    Retrieve the top-k relevant chunks based on the query.
    """
    if vector_store:
        results = vector_store.similarity_search(query, k=k)
        return results
    return []
