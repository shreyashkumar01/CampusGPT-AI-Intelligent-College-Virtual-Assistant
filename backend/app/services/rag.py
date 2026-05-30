from typing import List, Tuple, Optional
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions
import os

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path=os.getenv("CHROMA_DB_PATH", "./chroma_db"))
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="sentence-transformers/all-MiniLM-L6-v2")
collection = client.get_or_create_collection(name="campusgpt_documents", embedding_function=embedding_fn)


def index_document(source_name: str, raw_bytes: bytes):
    text = raw_bytes.decode("utf-8", errors="ignore")
    chunks = [text[i:i+800] for i in range(0, len(text), 800)]
    for idx, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            metadatas=[{"source": source_name, "chunk_id": idx}],
            ids=[f"{source_name}-{idx}"],
        )


def retrieve_relevant_context(query: str, top_k: int = 4) -> Tuple[List[dict], str]:
    query_embedding = model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    sources = []
    context = []
    if results and results.get("documents"):
        for doc, metadata in zip(results["documents"][0], results["metadatas"][0]):
            sources.append(metadata)
            context.append(doc)
    return sources, "\n\n".join(context)
