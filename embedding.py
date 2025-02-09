# embedding.py
from sentence_transformers import SentenceTransformer
import numpy as np

# Load the model once when the module is imported.
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(text: str) -> np.ndarray:
    """
    Returns the embedding of the provided text as a numpy array.
    """
    return model.encode(text, convert_to_numpy=True)
