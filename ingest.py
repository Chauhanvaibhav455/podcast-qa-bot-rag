from sentence_transformers import SentenceTransformer
import faiss
import pickle

with open("transcript.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

chunks = []

chunk_size = 150

for i in range(0, len(lines), chunk_size):
    chunk = "\n".join(lines[i:i + chunk_size])
    chunks.append(chunk)

print("Chunks:", len(chunks))

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(
    chunks,
    show_progress_bar=True
)

index = faiss.IndexFlatL2(
    embeddings.shape[1]
)

index.add(embeddings)

faiss.write_index(
    index,
    "podcast.index"
)

with open(
    "chunks.pkl",
    "wb"
) as f:
    pickle.dump(chunks, f)

print("Done")