from enum import StrEnum
from typing import Any, Self


class BaseStrEnum(StrEnum):
    _label: str

    def __new__(cls, *values: Any) -> Self:
        """
        Called only at class-definition time with:
         - (value,)        → no label
         - (value, label)  → with label

        Lookup at runtime (one-arg) never reaches here.
        """
        if len(values) not in (1, 2):
            raise TypeError(f"Invalid arguments for str enum: {values!r}")

        value: str = values[0]
        if not isinstance(value, str):
            raise TypeError(f"{value!r} is not an string")

        label: str = values[1] if len(values) == 2 else ""
        if not isinstance(label, str):
            raise TypeError(f"Enum label must be a string, not {label!r}")

        member = str.__new__(cls, value)
        member._value_, member._label = value, label
        return member

    def get_display(self) -> str:
        return self._label

    @property
    def display(self) -> str:
        return self._label


class Color(BaseStrEnum):
    RED = "red", "Red Like Blood"
    GREEN = "green"
    BLUE = "blue", "Love Is Blue"


print(Color.__members__)
print(Color._member_map_)
print(Color._value2member_map_)
print(Color._member_names_)
print()
print(Color.BLUE, Color.BLUE.name, Color.BLUE.value, Color.BLUE.display, Color.BLUE.get_display(), sep=", ")
print(Color("blue"), Color["BLUE"], sep=", ")
print()
print(Color.GREEN, Color.GREEN.name, Color.GREEN.value, Color.GREEN.display, Color.GREEN.get_display(), sep=", ")
print(Color("green"), Color["GREEN"], sep=", ")
