sequence_of_numbers = list(map(int, input().split(', ')))
group = 10

while sequence_of_numbers:

    list_of_numbers = [number for number in sequence_of_numbers if number <= group]
    print(f'Group of {group}\'s: {list_of_numbers}')
    group += 10
    sequence_of_numbers = [number for number in sequence_of_numbers if number not in list_of_numbers]