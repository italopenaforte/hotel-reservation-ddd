from datetime import datetime
from dataclasses import dataclass


from src.reception.domain.entity.room import Room
from src.reception.domain.value_object.guest import Guest
from src.reception.domain.value_object.room_status import RoomStatus
from src.reception.domain.value_object.reservation_status import ReservationStatus
from src.reception.domain.value_object.reservation_number import ReservationNumber

from src.reception.domain.exception.room import RoomStatusException
from src.reception.domain.exception.reservation import ReservationStatusException


@dataclass(eq=False, slots=True)
class Reservation:
    room: Room
    reservation_status: ReservationStatus
    reservation_number: ReservationNumber
    date_in: datetime
    date_out: datetime
    guest: Guest

    @classmethod
    def make(cls, room: Room, date_in: datetime, date_out: datetime, guest: Guest):
        room.reserve()
        return cls(
            room=room,
            date_in=date_in,
            date_out=date_out,
            guest=guest,
            reservation_number=ReservationNumber.generate(),
            reservation_status=ReservationStatus.IN_PROGRESS,
        )

    def cancel(self):
        if not self.reservation_status.in_progress:
            raise ReservationStatusException

        self.reservation_status = ReservationStatus.CANCELLED
        self.room.room_status = RoomStatus.AVAILABLE

    def check_in(self):
        if not self.room.room_status.is_reserved:
            raise RoomStatusException

        if not self.reservation_status.in_progress:
            raise ReservationStatusException

    def check_out(self):
        if not self.room.room_status.is_occupied:
            raise RoomStatusException

        if not self.reservation_status.in_progress:
            raise ReservationStatusException

        self.reservation_status = ReservationStatus.COMPLETE
        self.room.room_status = RoomStatus.AVAILABLE

    def change_guest(self, guest: Guest) -> None:
        self.guest = guest
