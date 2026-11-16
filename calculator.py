# SCCM4910 DevOps - a calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def exp(a, b):
    return a ** b

def main():
    while True:
        a = float(input("Enter the first number: "))
        operator = input("Enter the operator: ")
        b = float(input("Enter the second number: "))

        match operator:
            case "+":
                print(f"Result: {add(a, b)}")
            case "-":
                print(f"Result: {subtract(a, b)}")
            case "*":
                print(f"Result: {multiply(a, b)}")
            case "/":
                print(f"Result: {divide(a, b)}")
            case "^":
                print(f"Result: {exp(a, b)}")
            case _:
                print("Enter a valid operator.")
            

if __name__ == "__main__":
    main()
