from string import ascii_lowercase

sequence_of_strings = [string for string in input().split()]

total_sum = 0

for string in sequence_of_strings:
    first_letter = string[0]
    last_letter = string[-1]
    number = int(string[1:-1])
    sum = 0
    if first_letter.isupper():
        position = ascii_lowercase.index(first_letter.lower()) + 1
        sum += number / position
    elif first_letter.islower():
        position = ascii_lowercase.index(first_letter) + 1
        sum += number * position

    if last_letter.isupper():
        position = ascii_lowercase.index(last_letter.lower()) + 1
        sum -= position
    elif last_letter.islower():
        position = ascii_lowercase.index(last_letter) + 1
        sum += position
    
    total_sum += sum

print(f'{total_sum:.2f}')

