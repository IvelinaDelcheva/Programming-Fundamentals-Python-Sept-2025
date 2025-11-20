# def even_numbers(some_number) -> int:
#     if int(some_number) % 2 == 0:
#         return some_number


sequence_of_string_numbers = input().split(' ')
sequence_of_numbers = []
for number in sequence_of_string_numbers:
    sequence_of_numbers.append(int(number))

even_numbers = lambda x: x % 2 == 0
result_even_numbers = list(filter(even_numbers, sequence_of_numbers))
print(result_even_numbers)