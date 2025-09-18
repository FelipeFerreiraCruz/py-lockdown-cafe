import datetime


class VaccineError(Exception):
    """Base class for vaccine-related errors."""


class NotVaccinatedError(VaccineError):
    def __init__(self, name: str) -> None:
        super().__init__(f"{name} is not vaccinated.")


class OutdatedVaccineError(VaccineError):
    def __init__(self, name: str) -> None:
        super().__init__(f"{name} has an expired vaccine.")


class NotWearingMaskError(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"{name} is not wearing a mask.")


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor.get("name", "Unknown")

        if "vaccine" not in visitor:
            raise NotVaccinatedError(name)

        expiration = visitor["vaccine"].get("expiration_date")
        if expiration is None or expiration < datetime.date.today():
            raise OutdatedVaccineError(name)

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(name)

        return f"Welcome to {self.name}"


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
