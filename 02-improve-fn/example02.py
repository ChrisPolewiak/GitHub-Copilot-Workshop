"""Utility helpers for filtering collections of words."""

from __future__ import annotations

from typing import Iterable, List


def filter_long_words(words: Iterable[str], min_length: int = 6) -> List[str]:
    """Return words whose length is at least ``min_length``.

    Parameters
    ----------
    words:
        An iterable of strings to examine.
    min_length:
        The minimum number of characters a word must contain to be included in
        the result.  The default mirrors the previous behaviour of filtering
        words longer than five characters.
    """

    if min_length < 0:
        raise ValueError("min_length must be non-negative")

    return [word for word in words if len(word) >= min_length]


if __name__ == "__main__":
    print(filter_long_words(["apple", "code", "automation", "AI", "python"]))
