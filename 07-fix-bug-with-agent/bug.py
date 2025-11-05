"""Small module used in Lab 07 to demonstrate bug fixing with an agent."""

from __future__ import annotations

from typing import Iterable


def calculate_average(numbers: Iterable[float]) -> float:
    """Return the arithmetic mean of ``numbers``.

    A :class:`ValueError` is raised when the iterable is empty so that the
    caller can decide how to handle the edge case.
    """

    values = list(numbers)
    if not values:
        raise ValueError("calculate_average() requires at least one value")

    return sum(values) / len(values)


if __name__ == "__main__":
    values = [10, 20, 30, 40]
    result = calculate_average(values)
    print("Average is:", result)