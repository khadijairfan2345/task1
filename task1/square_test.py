import square

def test_square_positive_number():
    assert square.square(4) == 16

def test_square_negative_number():
    assert square.square(-3) == 9

def test_square_zero():
    assert square.square(0) == 0

def test_square_float_number():
    assert square.square(2.5) == 6.25

if __name__ == "__main__":
    import pytest
    pytest.main()
