import pytest

@pytest.mark.parametrize(
    "a,b,expected",
    [(0,5,0),(1,5,5),])
def test_multiplication(a,b,expected):
    assert a* b == expected


def test_addition():
    assert 1+1 == 2

def test_subtraction():
    diff = 1 - 1
    assert diff == 0
    
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1/0


