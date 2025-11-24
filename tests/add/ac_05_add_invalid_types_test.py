import pytest
from calculator import Calculator

def test_add_invalid_types():
    calc = Calculator()
    # Test with string
    with pytest.raises(TypeError):
        calc.add('a', 5)
    
    # Test with None
    with pytest.raises(TypeError):
        calc.add(None, 5)
    
    # Test with list
    with pytest.raises(TypeError):
        calc.add([1, 2], 5)
    
    # Test with both invalid
    with pytest.raises(TypeError):
        calc.add('a', 'b')