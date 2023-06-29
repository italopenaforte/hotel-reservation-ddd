import random
import string

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import ClassVar


@dataclass(slots=True)
class ReservationNumber:
    _DATETIME_FORMAT: ClassVar[str] = "%y%m%d%H%M%S"
    _RANDOM_STR_LENGTH: ClassVar[int] = 7

    value: str

    @classmethod
    def generate(cls) -> ReservationNumber:
        time_part: str = datetime.now(timezone.utc).strftime(cls._DATETIME_FORMAT)
        random_strings: str = "".join(
            random.choice(string.ascii_uppercase + string.digits)
            for _ in range(cls._RANDOM_STR_LENGTH)
        )
        return cls(value=f"{time_part}:{random_strings}")
