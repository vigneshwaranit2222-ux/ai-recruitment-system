from sklearn.metrics.pairwise import cosine_similarity


class SimilarityEngine:

    @staticmethod
    def calculate_similarity(
        candidate_embedding,
        company_embedding
    ):

        score = cosine_similarity(
            [candidate_embedding],
            [company_embedding]
        )[0][0]

        return round(score * 100, 2)