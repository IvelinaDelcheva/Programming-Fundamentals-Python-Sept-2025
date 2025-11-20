def sum_numbers(first_num: int, second_num: int) -> int:
    return first_num + second_num

def subtract(some_result: int, third_num: int) -> int:
    return some_result - third_num

def add_and_subtract(first_num: int, second_num: int, third_num: int):
    result_sum = sum_numbers(first_num, second_num)
    result_subtract = subtract(result_sum, third_num)
    return print(result_subtract)

first_number = int(input())
second_number = int(input())
third_number = int(input())

add_and_subtract(first_number, second_number, third_number)