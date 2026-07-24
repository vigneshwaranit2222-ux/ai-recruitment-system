from app.services.embedding.sentence_transformer import (
    EmbeddingModel
)


class EmbeddingService:

    @staticmethod
    def generate_embedding(
        text: str
    ):

        embedding = (
            EmbeddingModel.model.encode(
                text
            )
        )

        return embedding.tolist()