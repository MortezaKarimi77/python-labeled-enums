# Python Labeled Enums

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A flexible Python library that extends the standard `enum.Enum`, `enum.IntEnum`, and `enum.StrEnum` classes to support optional human-readable display labels for each enum member. This functionality is inspired by Django's `choices` pattern, making it easier to represent values that have both an internal identifier and a user-friendly description.

---

## ✨ Why This Library? ✨

We built `python-labeled-enums` to solve a common developer headache: managing data values that need both a machine-readable identifier and a human-readable label. Here's why it's a game-changer for your Python projects:

-   **Intuitive & Pythonic**: Extend standard `Enum` classes with a familiar API for display values.
-   **Enhanced Readability**: Transform cryptic internal values into clear, understandable labels for users.
-   **Reduced Boilerplate**: Say goodbye to manual mapping dictionaries or redundant code for display logic.
-   **Seamless Integration**: Works effortlessly with existing `Enum`, `IntEnum`, and `StrEnum` patterns.
-   **Future-Proof**: Centralize your display logic, making internationalization (i18n) and UI updates a breeze.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [LabeledEnumMixin](#labeledenummixin)
  - [BaseEnum (Generic Enums)](#baseenum-generic-enums)
  - [BaseIntEnum (Integer Enums)](#baseintenum-integer-enums)
  - [BaseStrEnum (String Enums)](#basestrenum-string-enums)
- [Contributing](#contributing)
- [License](#license)

## Features

-   **Optional Labels**: Define enum members with just a value or with both a value and a custom display label.
-   **Django `choices`-like Behavior**: Mimics the familiar pattern of associating a value with a human-readable text.
-   **Unified API**: Access the display label via a convenient `display` property or a `get_display()` method.
-   **Type-Specific Support**: Dedicated base classes for generic (`Enum`), integer (`IntEnum`), and string (`StrEnum`) enums, ensuring proper type handling during initialization.
-   **Reduced Redundancy**: Uses a `LabeledEnumMixin` to consolidate common display logic.

## Project Structure

The core logic of this library is consolidated into a single file:

-   `enum_mixin.py`: Contains the `LabeledEnumMixin` and the three specialized base enum classes (`BaseEnum`, `BaseIntEnum`, `BaseStrEnum`), along with example usage for each. This file is designed to be easily integrated into your project.

## Installation

Currently, this library is provided as a single Python file. You can use it by simply copying `enum_mixin.py` into your project and importing the desired base enum classes from it.

```bash
# Example: Copy the file to your project's `utils` directory
cp path/to/downloaded/enum_mixin.py your_project/utils/