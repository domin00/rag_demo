# indexer.py
import os
import glob
import numpy as np
import faiss
import pickle
from embedding import embed_text

def build_index(descriptions_folder="descriptions", index_file="faiss.index", product_file="product_names.pkl"):
    """
    Reads all txt files from the descriptions folder, creates embeddings,
    builds a FAISS index, and saves the index along with product names.
    """
    file_pattern = os.path.join(descriptions_folder, "*.txt")
    files = glob.glob(file_pattern)
    product_names = []
    embeddings = []

    for file_path in files:
        # Extract product name from the filename (without extension)
        product_name = os.path.splitext(os.path.basename(file_path))[0]
        product_names.append(product_name)
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
            embedding = embed_text(text)
            embeddings.append(embedding)

    if not embeddings:
        print("No product descriptions found in the folder.")
        return

    embeddings = np.vstack(embeddings).astype('float32')
    d = embeddings.shape[1]  # embedding dimension
    index = faiss.IndexFlatL2(d)
    index.add(embeddings)

    # Save the FAISS index and product names mapping.
    faiss.write_index(index, index_file)
    with open(product_file, "wb") as f:
        pickle.dump(product_names, f)

    print(f"Index built with {len(product_names)} products and saved to '{index_file}' and '{product_file}'.")

if __name__ == "__main__":
    build_index()
