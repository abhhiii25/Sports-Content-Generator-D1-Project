import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from pathlib import Path

# Load embedding model once
#model = SentenceTransformer("all-MiniLM-L6-v2")

dimension = 384
index = faiss.IndexFlatL2(dimension)

documents = []
metadata = []

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_PATH = BASE_DIR / "data" / "sample_match_reports.txt"


def get_embedding(text: str):
    return model.encode([text])[0]


def load_documents():
    if not DATA_PATH.exists():
        print("No sample data found.")
        return

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split("|")
        if len(parts) == 3:
            sport, teams, recap = parts
            add_document(recap.strip(), sport.strip(), teams.strip())

    print("Vector DB Loaded with", len(documents), "documents")


def add_document(text, sport, teams):
    embedding = get_embedding(text)
    index.add(np.array([embedding]).astype("float32"))
    documents.append(text)
    metadata.append({"sport": sport, "teams": teams})


def search(query, sport_filter=None, k=3):
  #  embedding = get_embedding(query)
   # D, I = index.search(np.array([embedding]).astype("float32"), k)

#    results = []

 #   for idx in I[0]:
  #      if idx == -1:
   #         continue

    #    if idx < len(documents):
     #       if sport_filter:
      #          if metadata[idx]["sport"].lower() == sport_filter.lower():
       #             results.append(documents[idx])
        #    else:
         #       results.append(documents[idx])

    return []# results
