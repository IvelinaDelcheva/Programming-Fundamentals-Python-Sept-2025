operator_ = input()
number1_ = int(input())
number2_ = int(input())

def calculate(operator: str, number1: int, number2: int):
    result = 0
    if operator == 'add':
        result = number1 + number2
    elif operator == 'subtract':
        result = number1 - number2
    elif operator == 'multiply':
        result = number1 * number2
    elif operator == 'divide':
        result = number1 // number2

    return result

result_from_calculation = calculate(operator_, number1_, number2_)
print(result_from_calculation)