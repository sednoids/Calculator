#!/bin/python
from calculator import add, subtract, multiply, divide, exp
import sys

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

def test_multiplication_by_zero():
    # Arrange
    a, b = 0, 0
    # Act
    result = multiply(a, b)
    # Assert
    assert result == 0

def main():
    try:
        test_add()
        test_subtract()
        test_multiply()
        test_divide()
        test_exp()
        test_multiplication_by_zero()
        sys.exit(0)
    except AssertionError as error:
        print(f"QUALITY GATE FAILED: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()
