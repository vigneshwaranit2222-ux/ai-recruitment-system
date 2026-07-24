class ScoreCalculator:

    @staticmethod
    def calculate_overall_score(
        communication,
        problem_solving,
        coding,
        leadership
    ):

        overall = (
            communication +
            problem_solving +
            coding +
            leadership
        ) / 4

        return round(overall, 2)