# retriever.py
import faiss
import pickle
import numpy as np
from embedding import embed_text

def load_index(index_file="faiss.index", product_file="product_names.pkl"):
    """
    Loads the FAISS index and the corresponding product names.
    """
    index = faiss.read_index(index_file)
    with open(product_file, "rb") as f:
        product_names = pickle.load(f)
    return index, product_names

def search(query: str, k=5, index_file="faiss.index", product_file="product_names.pkl"):
    """
    Given a query, returns the top k matching products as a list of tuples:
    (product_name, distance).
    """
    index, product_names = load_index(index_file, product_file)
    query_embedding = embed_text(query).reshape(1, -1).astype('float32')
    distances, indices = index.search(query_embedding, k)

    # Map search results to product names.
    results = []
    for dist, idx in zip(distances[0], indices[0]):
        if idx < len(product_names):
            results.append((product_names[idx], float(dist)))
    return results

if __name__ == "__main__":
    query = input("Enter your query: ")
    results = search(query)
    print("Results:")
    for product, distance in results:
        print(f"{product} (distance: {distance:.4f})")
