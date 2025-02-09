# main.py
import argparse
import indexer
import retriever

def main():
    parser = argparse.ArgumentParser(description="RAG system for product retrieval")
    parser.add_argument('--build-index', action='store_true', help="Build the FAISS index from product descriptions.")
    parser.add_argument('--query', type=str, help="Query to search for products.")
    parser.add_argument('--top_k', type=int, default=5, help="Number of top results to return.")
    args = parser.parse_args()

    if args.build_index:
        indexer.build_index()

    if args.query:
        results = retriever.search(args.query, k=args.top_k)
        print("Results:")
        for product, distance in results:
            print(f"{product} (distance: {distance:.4f})")

if __name__ == "__main__":
    main()
