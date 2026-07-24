from sentence_transformers import (
    SentenceTransformer
)


class EmbeddingModel:

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )