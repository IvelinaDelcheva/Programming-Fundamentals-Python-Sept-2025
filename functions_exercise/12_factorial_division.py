def factorial(some_number: int) -> int:
    factorial_number = 1
    for number in range(1, some_number + 1):
        factorial_number *= number
    
    return factorial_number

def divide_factorials(number1: int, number2: int) -> float:
    res_num_1 = factorial(number1)
    res_num_2 = factorial(number2)
    return f'{(res_num_1 / res_num_2):.2f}'

num1 = int(input())
num2 = int(input())

result = divide_factorials(num1, num2)
print(result)