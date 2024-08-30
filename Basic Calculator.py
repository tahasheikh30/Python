import math

print("Welcome to Calculator Prototype by NAT Softwares")

result = 0

while True:
    try:
        value = input("Enter value (Press Enter Key to end & C to clear): ")
        if value.lower() == "c":
            result = 0
            continue
        elif value == "":
            break
        elif value == "pi" or value == "π":
            value = math.pi
        else:
            value = float(value)
    except ValueError:
        print("Can't even enter values properly. GO BACK TO NURSERY!")
        continue

    operator = input("+, -, *, /, %, ^, sqrt, sin, cos, tan: ")

    def calculate(value1, value2, operator):
        if operator == "+":
            return value1 + value2
        elif operator == "-":
            return value1 - value2
        elif operator == "*":
            return value1 * value2
        elif operator == "/":
            if value2 != 0:
                return value1 / value2
            else:
                print("Division by zero!")
                return None
        elif operator == "%":
            return value1 % value2
        elif operator == "^":
            return value1**value2
        elif operator == "sqrt":
            return math.sqrt(value2)
        elif operator == "sin":
            return math.sin(value2)
        elif operator == "cos":
            return math.cos(value2)
        elif operator == "tan":
            return math.tan(value2)
        else:
            print(
                "Invalid operator. Please enter +, -, *, /, %, ^, sqrt, sin, cos, tan "
            )
            return None

    final_result = calculate(result, value, operator)

    if final_result is not None:
        result = final_result
        print("Your Total is:", result)

print("Calculation finished. Final result:", result)
