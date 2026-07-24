from app.services.business_rules.experience_filter import (
    ExperienceFilter
)

from app.services.business_rules.salary_filter import (
    SalaryFilter
)

from app.services.business_rules.location_filter import (
    LocationFilter
)

from app.services.business_rules.availability_filter import (
    AvailabilityFilter
)


class RuleEngine:

    @staticmethod
    def validate_candidate(
        candidate,
        company
    ):

        if not ExperienceFilter.validate(
            candidate["experience"],
            company["required_experience"]
        ):
            return False

        if not SalaryFilter.validate(
            candidate["salary_expectation"],
            company["budget"]
        ):
            return False

        if not LocationFilter.validate(
            candidate["location"],
            company["location"]
        ):
            return False

        if not AvailabilityFilter.validate(
            candidate["available"]
        ):
            return False

        return True