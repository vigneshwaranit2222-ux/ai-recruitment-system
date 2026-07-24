class CandidateRanker:

    @staticmethod
    def rank_candidates(
        candidates
    ):

        ranked = sorted(
            candidates,
            key=lambda x: x["final_score"],
            reverse=True
        )

        for index, candidate in enumerate(
            ranked,
            start=1
        ):
            candidate["rank"] = index

        return ranked