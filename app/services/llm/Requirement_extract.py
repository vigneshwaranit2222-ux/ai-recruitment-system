import json

import google.generativeai as genai

from app.config import settings

from app.services.llm.prompt_templates import (
    PromptTemplates
)

genai.configure(
    api_key=settings.GEMINI_API_KEY
)


class RequirementExtractor:

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    @classmethod
    def extract_requirements(
        cls,
        user_prompt: str
    ):

        prompt = (
            PromptTemplates
            .REQUIREMENT_EXTRACTION_PROMPT
            .format(prompt=user_prompt)
        )

        response = cls.model.generate_content(
            prompt
        )

        cleaned = (
            response.text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(cleaned)