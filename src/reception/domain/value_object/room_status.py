from enum import Enum


class RoomStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    RESERVED = "RESERVED"
    OCCUPIED = "OCCUPIED"

    @property
    def is_available(self) -> bool:
        return self == RoomStatus.AVAILABLE

    @property
    def is_reserved(self) -> bool:
        return self == RoomStatus.RESERVED

    @property
    def is_occupied(self) -> bool:
        return self == RoomStatus.OCCUPIED
