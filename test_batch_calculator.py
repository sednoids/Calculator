from batch_calculator import process_calculation


def test_process_add_calculation():
    assert process_calculation("add", "5", "5") == ("OK", 10.0, "")

def test_process_multiply_calculation():
    assert process_calculation("multiply", "6", "7") == ("OK", 42.0, "")

def test_process_subtract_calculation_as_floating_point():
    assert process_calculation("subtract", "42.0", "42.0") == ("OK", 0.0, "")

def test_process_divide_calculation():
    assert process_calculation("divide", "6", "2") == ("OK", 3.0, "")
    
def test_process_invalid_operation():
    assert process_calculation("something", "3", "9") == ("ERROR", "","UNKOWN_OPERATION")

def test_process_division_by_zero():
    assert process_calculation("divide", "0", "0") == ("ERROR", "", "DIVISION_BY_ZERO")

def test_process_invalid_number():
    assert process_calculation("subtract", "", "3") == ("ERROR", "", "INVALID_NUMBER")

def test_process_non_numberic_number():
    assert process_calculation("multiply", "two", "three") == ("ERROR", "", "INVALID_NUMBER")

def test_process_exponential_number():
    assert process_calculation("exponential", "3", "3") == ("OK", 27.0, "")
