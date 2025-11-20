def min_max_and_sum(some_numbers: list) -> list:
    min_max_and_sum_list = []
    min_max_and_sum_list.append(f'The minimum number is {min(some_numbers)}')
    min_max_and_sum_list.append(f'The maximum number is {max(some_numbers)}')
    min_max_and_sum_list.append(f'The sum number is: {sum(some_numbers)}')

    return min_max_and_sum_list

sequence_of_string_numbers = input().split(' ')
sequence_of_numbers = []
for number in sequence_of_string_numbers:
    sequence_of_numbers.append(int(number))

print('\n'.join(min_max_and_sum(sequence_of_numbers)))