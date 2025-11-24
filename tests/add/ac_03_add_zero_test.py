import pytest
from calculator import Calculator

def test_add_zero():
    calc = Calculator()
    # Adding zero to positive number
    result = calc.add(5, 0)
    assert result == 5
    
    # Adding zero to negative number
    result = calc.add(-10, 0)
    assert result == -10
    
    # Adding zero to zero
    result = calc.add(0, 0)
    assert result == 0