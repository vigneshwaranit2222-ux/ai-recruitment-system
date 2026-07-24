from app.vector_db.chroma_client import (
    ChromaClient
)


class Collections:

    candidate_collection = (
        ChromaClient.client.get_or_create_collection(
            name="candidates"
        )
    )

    company_collection = (
        ChromaClient.client.get_or_create_collection(
            name="companies"
        )
    )