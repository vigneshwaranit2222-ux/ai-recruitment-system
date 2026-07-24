import spacy

nlp = spacy.load("en_core_web_sm")


class ResumeParser:

    SKILLS = [
        "python",
        "fastapi",
        "java",
        "spring boot",
        "react",
        "nodejs",
        "docker",
        "kubernetes",
        "langchain",
        "rag",
        "llm",
        "postgresql",
        "mongodb",
        "sql",
        "power bi"
    ]

    @staticmethod
    def extract_name(text):

        doc = nlp(text)

        for ent in doc.ents:
            if ent.label_ == "PERSON":
                return ent.text

        return "Unknown"

    @staticmethod
    def extract_skills(text):

        found_skills = []

        text_lower = text.lower()

        for skill in ResumeParser.SKILLS:

            if skill in text_lower:
                found_skills.append(skill)

        return list(set(found_skills))