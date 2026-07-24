import re


class ResumeCleaner:

    @staticmethod
    def clean_text(text: str):

        text = re.sub(r"\n", " ", text)

        text = re.sub(r"\s+", " ", text)

        text = re.sub(r"[^a-zA-Z0-9,. ]", "", text)

        return text.strip()