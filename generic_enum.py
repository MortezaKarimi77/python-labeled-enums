from enum import Enum
from typing import Any, Self


class BaseEnum(Enum):
    _label: str

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

    def get_display(self) -> str:
        return self._label

    @property
    def display(self) -> str:
        return self._label


class Status(BaseEnum):
    DRAFT = "draft", "Draft"
    PUBLISHED = "published"
    ARCHIVED = "archived", "Archived"


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
