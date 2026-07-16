import pytest
from src.calculator import add, divide, sub

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(6, 2) == 3
    
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Деление на ноль невозможно"):
        divide(10, 0)

def test_sub():
    assert sub(19,3) == 16
    assert sub(-3, -5) == 2