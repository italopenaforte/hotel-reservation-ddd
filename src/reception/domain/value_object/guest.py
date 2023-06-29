from dataclasses import dataclass


@dataclass(slots=True)
class Guest:
    mobile: str
    name: str | None = None
