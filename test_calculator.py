from calculator import add, subtract, multiply, divide, exp, modulo,circleArea

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 4) == 1

def test_multiply():
    assert multiply(6, 6) == 36

def test_divide():
    assert divide(6, 2) == 3

def test_exp():
    assert exp(3, 3) == 27

def test_modulo():
    assert modulo(4, 2) == 0

def test_circleArea():
    assert circleArea(-4) == "Error"

def test_multiplication_by_zero():
    # Arrange
    a, b = 0, 0
    # Act
    result = multiply(a, b)
    # Assert
    assert result == 0

