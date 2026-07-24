class AvailabilityFilter:

    @staticmethod
    def validate(
        status
    ):

        return (
            status.lower()
            ==
            "available"
        )