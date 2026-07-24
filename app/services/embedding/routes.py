from fastapi import APIRouter

from app.services.embedding.embedding_service import (
    EmbeddingService
)

router = APIRouter(
    prefix="/embedding",
    tags=["Embedding"]
)


@router.post("/generate")
def generate_embedding(
    text: str
):

    vector = (
        EmbeddingService.generate_embedding(
            text
        )
    )

    return {
        "dimension": len(vector),
        "embedding": vector[:10]
    } 