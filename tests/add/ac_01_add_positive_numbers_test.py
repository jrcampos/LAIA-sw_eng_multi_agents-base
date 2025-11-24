import pytest
from calculator import Calculator

def test_add_positive_numbers():
    calc = Calculator()
    result = calc.add(3, 5)
    assert result == 8
    
    # Additional test case
    result = calc.add(10, 20)
    assert result == 30