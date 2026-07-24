class SalaryFilter:

    @staticmethod
    def validate(
        candidate_salary,
        company_budget
    ):

        return (
            candidate_salary
            <=
            company_budget
        )