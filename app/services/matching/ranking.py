class RankingEngine:

    @staticmethod
    def calculate_final_score(
        similarity_score,
        interview_score
    ):

        final_score = (
            similarity_score * 0.7
        ) + (
            interview_score * 0.3
        )

        return round(final_score, 2) 