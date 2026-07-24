from app.vector_db.collections import (
    Collections
)


class VectorStore:

    @staticmethod
    def store_candidate(
        candidate_id: str,
        text: str,
        embedding
    ):

        Collections.candidate_collection.add(
            ids=[candidate_id],
            documents=[text],
            embeddings=[embedding]
        )

    @staticmethod
    def store_company(
        company_id: str,
        text: str,
        embedding
    ):

        Collections.company_collection.add(
            ids=[company_id],
            documents=[text],
            embeddings=[embedding]
        )