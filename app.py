import os

from src.data_loader import load_all_documents
from src.embedding import EmbeddingPipeline
from src.vectorstore import FaissVectorStore

if __name__ == "__main__":
    docs = load_all_documents("data")
    store = FaissVectorStore("faiss_store")

    faiss_path = os.path.join("faiss_store", "faiss.index")
    metadata_path = os.path.join("faiss_store", "metadata.pkl")

    if os.path.exists(faiss_path) and os.path.exists(metadata_path):
        store.load()
    else:
        pipeline = EmbeddingPipeline()
        chunks = pipeline.chunk_documents(docs)
        embeddings = pipeline.embed_chunks(chunks)

        store.add_embeddings(
            embeddings,
            [chunk.metadata for chunk in chunks],
        )
        store.save()
