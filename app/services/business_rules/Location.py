class LocationFilter:

    @staticmethod
    def validate(
        candidate_location,
        company_location
    ):

        return (
            candidate_location
            .lower()
            ==
            company_location.lower()
        )