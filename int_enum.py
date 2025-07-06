from enum import IntEnum
from typing import Any, Self


class BaseIntEnum(IntEnum):
    _label: str

    def __new__(cls, *values: Any) -> Self:
        """
        Called only at class-definition time with:
         - (value,)        → no label
         - (value, label)  → with label

        Lookup at runtime (one-arg) never reaches here.
        """
        if len(values) not in (1, 2):
            raise TypeError(f"Invalid arguments for int enum: {values!r}")

        value: int = values[0]
        if not isinstance(value, int):
            raise TypeError(f"{value!r} is not an integer")

        label: str = values[1] if len(values) == 2 else ""
        if not isinstance(label, str):
            raise TypeError(f"Enum label must be a string, not {label!r}")

        member = int.__new__(cls, value)
        member._value_, member._label = value, label
        return member

    def get_display(self) -> str:
        return self._label

    @property
    def display(self) -> str:
        return self._label


class Switch(BaseIntEnum):
    ON = 1, "turn on"
    OFF = 0


print(Switch.__members__)
print(Switch._member_map_)
print(Switch._value2member_map_)
print(Switch._member_names_)
print()
print(Switch.ON, Switch.ON.name, Switch.ON.value, Switch.ON.display, Switch.ON.get_display())
print(Switch(1), Switch["ON"])
print()
print(Switch.OFF, Switch.OFF.name, Switch.OFF.value, Switch.OFF.display, Switch.OFF.get_display())
print(Switch(0), Switch["OFF"])
