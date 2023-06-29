from dataclasses import dataclass

from src.reception.domain.exception.room import RoomStatusException
from src.reception.domain.value_object.room_status import RoomStatus


@dataclass(eq=False, slots=True)
class Room:
    number: str
    room_status: RoomStatus

    def reserve(self):
        if not self.room_status.is_available:
            raise RoomStatusException

        self.room_status = RoomStatus.RESERVED
