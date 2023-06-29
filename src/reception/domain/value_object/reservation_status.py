from enum import Enum


class ReservationStatus(str, Enum):
    IN_PROGRESS = "IN-PROGRESS"
    CANCELLED = "CANCELLED"
    COMPLETE = "COMPLETE"

    @property
    def in_progress(self) -> bool:
        return self == ReservationStatus.IN_PROGRESS

    @property
    def is_cancelled(self) -> bool:
        return self == ReservationStatus.CANCELLED

    @property
    def is_complete(self) -> bool:
        return self == ReservationStatus.COMPLETE
