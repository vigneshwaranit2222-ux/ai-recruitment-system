class ExplanationPrompt:

    TEMPLATE = """
You are an AI Recruitment Assistant.

Explain why this candidate is suitable.

Candidate Name:
{name}

Candidate Skills:
{skills}

Experience:
{experience}

Interview Score:
{interview_score}

Similarity Score:
{similarity_score}

Final Score:
{final_score}

Provide:
1. Skill Match
2. Experience Match
3. Interview Performance
4. Hiring Recommendation

Keep response professional.
"""