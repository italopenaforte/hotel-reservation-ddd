class BaseMsgException(Exception):
    message: str

    def __str__(self) -> str:
        return self.message


class ValueObjectEnumError(Exception):
    def __str__(self) -> str:
        return "Value Object got invalid value."
