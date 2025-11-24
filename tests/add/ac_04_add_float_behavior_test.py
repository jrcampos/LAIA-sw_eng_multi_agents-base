import pytest
from calculator import Calculator

def test_add_float_behavior():
    calc = Calculator()
    # Both floats
    result = calc.add(3.5, 2.5)
    assert result == pytest.approx(6.0)
    
    # Float and int
    result = calc.add(5, 2.5)
    assert result == pytest.approx(7.5)
    
    # Very small floats
    result = calc.add(0.0001, 0.0002)
    assert result == pytest.approx(0.0003)