"""Complete this function for the SCCM4910 coursework.

Place this file beside your existing lab calculator.py. The runner and
file handling are supplied; write your own processing logic and tests.
"""

from calculator import add, subtract, multiply, divide, exp


def process_calculation(operation, a_text, b_text):

    try:
        a = float(a_text)
        b = float(b_text)

        match operation:
            case "add":
                return ("OK", add(a, b), "")
            case "subtract":
                return ("OK", subtract(a, b), "")
            case "multiply":
                return ("OK", multiply(a, b), "")
            case "divide":
                return ("OK", divide(a, b), "")
            case "exponential":
                return ("OK", exp(a, b), "")
            case _:
                return ("ERROR", "", "UNKOWN_OPERATION")
            
    except ValueError:
        return ("ERROR", "", "INVALID_NUMBER")
    except ZeroDivisionError:
        return ("ERROR", "", "DIVISION_BY_ZERO")

"""
    Return (status, result, error_code) for one calculation.

    Inputs are strings. Trim whitespace and use the four imported lab functions.
    Success: ("OK", numeric_result, "").
    The error_code is empty on success because there is no error to report.
    Error: ("ERROR", "", error_code).

    Check errors in order: UNKNOWN_OPERATION, INVALID_NUMBER, DIVISION_BY_ZERO.
    See the brief for the full contract. You may add small helper functions.
"""
