from app.services.matching.candidate_ranker import (
    CandidateRanker
)

from app.services.matching.top_candidates import (
    TopCandidates
)


class RecommendationEngine:

    @staticmethod
    def generate_company_recommendations(
        candidate_results
    ):

        ranked = (
            CandidateRanker.rank_candidates(
                candidate_results
            )
        )

        return (
            TopCandidates.get_top_candidates(
                ranked
            )
        )