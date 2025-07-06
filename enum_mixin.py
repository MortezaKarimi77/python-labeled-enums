from enum import Enum, IntEnum, StrEnum
from typing import Any, Self


class LabeledEnumMixin:
    _label: str

    def get_display(self) -> str:
        return self._label

    @property
    def display(self) -> str:
        return self._label


class BaseStrEnum(LabeledEnumMixin, StrEnum):
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


class BaseIntEnum(LabeledEnumMixin, IntEnum):
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


class BaseEnum(LabeledEnumMixin, Enum):
    def __new__(cls, *values: Any) -> Self:
        """
        Called only at class-definition time with:
         - (value,)        → no label
         - (value, label)  → with label

        Lookup at runtime (one-arg) never reaches here.
        """
        if len(values) not in (1, 2):
            raise TypeError(f"Invalid arguments for enum: {values!r}")

        value: Any = values[0]
        label: str = values[1] if len(values) == 2 else ""
        if not isinstance(label, str):
            raise TypeError(f"Enum label must be a string, not {label!r}")

        member = object.__new__(cls)
        member._value_, member._label = value, label
        return member


class Color(BaseStrEnum):
    RED = "red", "Red Like Blood"
    GREEN = "green"
    BLUE = "blue", "Love Is Blue"


class Switch(BaseIntEnum):
    ON = 1, "turn on"
    OFF = 0


class Status(BaseEnum):
    DRAFT = "draft", "Draft"
    PUBLISHED = "published"
    ARCHIVED = "archived", "Archived"


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
print(33 * "*", "\n")

print(Switch.__members__)
print(Switch._member_map_)
print(Switch._value2member_map_)
print(Switch._member_names_)
print()
print(Switch.ON, Switch.ON.name, Switch.ON.value, Switch.ON.display, Switch.ON.get_display(), sep=", ")
print(Switch(1), Switch["ON"], sep=", ")
print()
print(Switch.OFF, Switch.OFF.name, Switch.OFF.value, Switch.OFF.display, Switch.OFF.get_display(), sep=", ")
print(Switch(0), Switch["OFF"], sep=", ")
print(33 * "*", "\n")

print(Status.__members__)
print(Status._member_map_)
print(Status._value2member_map_)
print(Status._member_names_)
print()
print(Status.DRAFT, Status.DRAFT.name, Status.DRAFT.value, Status.DRAFT.display, Status.DRAFT.get_display(), sep=", ")
print(Status("draft"), Status["DRAFT"], sep=", ")
print()
print(
    Status.PUBLISHED,
    Status.PUBLISHED.name,
    Status.PUBLISHED.value,
    Status.PUBLISHED.display,
    Status.PUBLISHED.get_display(),
    sep=", ",
)
print(Status("published"), Status["PUBLISHED"], sep=", ")
