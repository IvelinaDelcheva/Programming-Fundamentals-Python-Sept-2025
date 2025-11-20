def positive(some_numbers: list) -> list:
    return ', '.join([str(number) for number in some_numbers if number >= 0])

def negative(some_numbers: list) -> list:
    return ', '.join([str(number)  for number in some_numbers if number < 0])

def even(some_numbers: list) -> list:
    return ', '.join([str(number)  for number in some_numbers if number % 2 == 0])

def odd(some_numbers: list) -> list:
    return ', '.join([str(number)  for number in some_numbers if number % 2 != 0])

numbers = [int(number) for number in input().split(', ')]

print(f'Positive: {positive(numbers)}')
print(f'Negative: {negative(numbers)}')
print(f'Even: {even(numbers)}')
print(f'Odd: {odd(numbers)}')