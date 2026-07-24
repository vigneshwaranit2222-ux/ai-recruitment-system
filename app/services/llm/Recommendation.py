import google.generativeai as genai


class RecommendationExplainer:

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    @classmethod
    def explain(
        cls,
        candidate_name,
        score,
        skills
    ):

        prompt = f"""
Explain why candidate should be hired.

Candidate:
{candidate_name}

Score:
{score}

Skills:
{skills}
"""

        response = cls.model.generate_content(
            prompt
        )

        return response.text