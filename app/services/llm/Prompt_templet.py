class PromptTemplates:

    REQUIREMENT_EXTRACTION_PROMPT = """
You are an expert HR AI Assistant.

Extract hiring requirements from the user prompt.

Return ONLY JSON.

Format:

{
 "role":"",
 "skills":[],
 "experience":0,
 "communication":""
}

User Prompt:
{prompt}
"""