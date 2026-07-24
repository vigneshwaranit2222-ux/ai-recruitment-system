from app.services.business_rules.rule_engine import (
    RuleEngine
)


class RecommendationEngine:

    @staticmethod
    def recommend(
        candidate,
        company,
        similarity_score,
        interview_score
    ):

        is_valid = (
            RuleEngine.validate_candidate(
                candidate,
                company
            )
        )

        if not is_valid:

            return {
                "status": "Rejected",
                "reason": "Business Rule Failed"
            }

        final_score = (
            similarity_score * 0.7
            +
            interview_score * 0.3
        )

        return {
            "status": "Recommended",
            "final_score": round(
                final_score,
                2
            )
        }