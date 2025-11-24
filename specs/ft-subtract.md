# Feature: Subtraction

## Functional Requirement

### FR-01
The system shall return the result of subtracting one numeric value from another.

## Acceptance Criteria

### AC-01 (Subtract – Positive Numbers)
Given two positive numbers, the system returns the correct difference.

### AC-02 (Subtract – Negative Numbers)
The system correctly handles subtraction involving negative values.

### AC-03 (Subtract – Zero)
Subtracting zero returns the original number.  
Subtracting a number from zero returns the negative of that number.

### AC-04 (Subtract – Float Behavior)
Given floats, the system returns the difference within normal floating-point precision.

### AC-05 (Subtract – Invalid Types)
If either operand is not a numeric type, the system raises a TypeError.

## Inputs & Outputs
- Inputs: integers or floats.
- Output: numeric result.
- Invalid inputs must raise TypeError.

## Edge Cases
- Very large values.
- Mixed ints/floats.
- Negative minus positive.
- Positive minus negative (double negative scenario).