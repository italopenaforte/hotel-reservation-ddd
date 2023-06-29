from src.shared.domain.exception import BaseMsgException


class RoomNotFoundException(BaseMsgException):
    message = "Room not found."


class RoomStatusException(BaseException):
    message = "Invalid request for current room status."
