def sorted_list(some_numbers: list) -> list:
    return sorted(some_numbers)


sequence_of_string_numbers = input().split()
sequence_of_numbers = []
for number in sequence_of_string_numbers:
    sequence_of_numbers.append(int(number))

print(sorted_list(sequence_of_numbers))