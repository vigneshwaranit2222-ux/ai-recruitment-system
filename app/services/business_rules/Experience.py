class ExperienceFilter:

    @staticmethod
    def validate(
        candidate_experience,
        required_experience
    ):

        return (
            candidate_experience
            >=
            required_experience
        )