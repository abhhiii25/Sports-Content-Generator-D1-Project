import faiss
import numpy as np
from .embedding_service import get_embedding, model

dimension = 384
index = faiss.IndexFlatL2(dimension)
documents = []

def add_document(text):
    embedding = get_embedding(text)
    index.add(np.array([embedding]).astype("float32"))
    documents.append(text)

def search(query, k=2):
    if len(documents) == 0:
        return []

    query_embedding = model.encode([query])
    D, I = index.search(query_embedding, k)

    results = []

    for idx in I[0]:
        if idx == -1:
            continue
        if 0 <= idx < len(documents):
            results.append(documents[idx])

    return results