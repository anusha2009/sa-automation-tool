from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(text_chunk):
    return embedder.encode(text_chunk).tolist()
