# src/calculator.py

from typing import Union

Number = Union[int, float]


class Calculator:
    """
    Baseline Calculator for the multi-agent course project.
    Implements basic arithmetic operations:
      - addition

    Future functionalities (multiply, divide, exponentiation, etc.)
    will be added by the Coder agent based on specifications + tests.
    """

    def _validate(self, *values: Number) -> None:
        """Ensure all provided values are ints or floats."""
        for v in values:
            if not isinstance(v, (int, float)):
                raise TypeError(f"Invalid input {v!r}: expected int or float.")

    def add(self, a: Number, b: Number) -> Number:
        self._validate(a, b)
        return a + b
    