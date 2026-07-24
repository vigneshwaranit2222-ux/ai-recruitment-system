class TopCandidates:

    @staticmethod
    def get_top_candidates(
        ranked_candidates,
        limit=3
    ):

        return ranked_candidates[:limit]