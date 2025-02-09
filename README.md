# rag_demo


markdown
Copy
Edit
# Product Retrieval System

This project implements a simple product retrieval system. It reads product descriptions from the `descriptions/` folder (each as a `{product name}.txt` file), builds an index using FAISS, and allows you to run queries from the command line.

## Prerequisites

- Python 3.7 or higher

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_folder>

Create and activate a virtual environment:

2. **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt

## Building the Index
Before running any queries, you need to build the FAISS index. Make sure your product descriptions are placed in the descriptions/ folder and named as {product name}.txt.

To build the index, run:

    ```bash 
    python main.py --build-index

This script reads all .txt files in the descriptions/ folder, computes embeddings using the SentenceTransformer, builds a FAISS index, and saves both the index and a mapping of index positions to product names.

## Running a Query
Once the index is built, you can search for products using the command line. To run a query, use:

    ```bash
    python main.py --query "your desired product description" --top_k 5
    Replace "your desired product description" with your search query.
    The --top_k parameter determines the number of top matching products to return (default is 5).

The script will output the matching products along with their similarity distances.

## Summary
1. **Setup Environment & Install Dependencies**
2. **Build the Index:**
    ```bash
    python main.py --build-index

3. **Run a Query:**
    ```bash
    python main.py --query "example query" --top_k 5


Happy searching!