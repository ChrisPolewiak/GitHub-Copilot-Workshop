"""Refactored version of the intentionally messy ``calcThings`` helper."""

from __future__ import annotations

import operator
from typing import Any, Callable, Dict, Union

Number = Union[int, float]


def _coerce_operand(value: Any) -> Number:
    """Return ``value`` as a numeric type.

    Strings are accepted to keep parity with the workshop's original example.  A
    :class:`ValueError` is raised when conversion is impossible so that calling
    code can decide how to handle the invalid input instead of silently
    continuing with a bogus default.
    """

    if isinstance(value, (int, float)):
        return value

    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            raise ValueError("Empty string cannot be coerced to a number")
        try:
            # Preserve integers when possible so subtraction and modulus behave
            # naturally, while still allowing decimal input.
            return int(stripped) if stripped.isdigit() else float(stripped)
        except ValueError as exc:  # pragma: no cover - tutorial simplicity
            raise ValueError(f"Unable to convert '{value}' to a number") from exc

    raise TypeError(f"Unsupported operand type: {type(value)!r}")


def _apply_bonus(result: Number, mode: str, enabled: bool) -> Number:
    """Apply optional adjustments mirroring the legacy behaviour."""

    if not enabled:
        return result

    adjustments: Dict[str, Callable[[Number], Number]] = {
        "add": lambda value: value + 10,
        "sub": lambda value: value - 5,
    }
    adjust = adjustments.get(mode, lambda value: value)
    return adjust(result)


def calcThings(x: Any, y: Any, mode: str | None = None, extra: bool | None = None) -> Number:
    """Perform an arithmetic operation between ``x`` and ``y``.

    Parameters
    ----------
    x, y:
        Operands which may already be numeric or strings that represent
        numbers.
    mode:
        Arithmetic mode to use.  Supported values: ``"add"``, ``"sub"``,
        ``"multi"``, and ``"div"``.  Defaults to addition to maintain backwards
        compatibility with the lab exercise.
    extra:
        When truthy, apply the same adjustments that the legacy version tacked
        on at the end of the computation.
    """

    normalized_mode = (mode or "add").lower()
    operations: Dict[str, Callable[[Number, Number], Number]] = {
        "add": operator.add,
        "sub": operator.sub,
        "multi": operator.mul,
        "div": lambda left, right: left / right,
    }

    if normalized_mode not in operations:
        raise ValueError(f"Unsupported mode: {mode}")

    left = _coerce_operand(x)
    right = _coerce_operand(y)

    if normalized_mode == "div" and right == 0:
        raise ZeroDivisionError("Division by zero is undefined")

    result = operations[normalized_mode](left, right)
    result = _apply_bonus(result, normalized_mode, bool(extra))

    print(f"Result is: {result}")
    return result


if __name__ == "__main__":
    calcThings("8", "4", mode="div")
