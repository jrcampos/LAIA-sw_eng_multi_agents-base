import pytest
from calculator import Calculator

def test_add_negative_numbers():
    calc = Calculator()
    # Both negative numbers
    result = calc.add(-3, -5)
    assert result == -8
    
    # Mix of positive and negative
    result = calc.add(10, -20)
    assert result == -10
    
    # Zero with negative
    result = calc.add(0, -5)
    assert result == -5