## Calculator Implementation Rule

All calculator-related functionality must be implemented inside a single file: `calculator.py`.

- All operations (add, subtract, multiply, etc.) must be implemented **inside this single file**.
- All operations must be implemented **as methods of a single `Calculator` class**.
- No additional modules may be created for individual operations.
- Tests must always import the class using:
  `from calculator import Calculator`
- Tests must create an instance of the class:
  `calc = Calculator()`
- Tests must call methods on this instance, e.g.:
  `calc.add(...)`, `calc.subtract(...)`, `calc.multiply(...)`.

Standalone top-level functions for calculator operations are **not allowed**.