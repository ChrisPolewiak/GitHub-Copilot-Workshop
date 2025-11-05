"""Example module showcasing a simple ``average`` helper."""

from __future__ import annotations

from typing import Iterable


def average(numbers: Iterable[float]) -> float:
    """Return the arithmetic mean of ``numbers``.

    The implementation purposefully uses :func:`sum` and :func:`len` to show how
    built-in helpers simplify iteration logic.  An informative :class:`ValueError`
    is raised when no values are provided so that callers can handle the edge
    case explicitly instead of receiving a ``ZeroDivisionError``.
    """

    values = list(numbers)
    if not values:
        raise ValueError("average() requires at least one number")

    return sum(values) / len(values)


if __name__ == "__main__":
    result = average([10, 20, 30, 40])
    print(result)
