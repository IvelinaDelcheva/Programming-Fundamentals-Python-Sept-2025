string_input = input()
chars_in_string = {}

for char in string_input:
    if char != ' ':
        if char not in chars_in_string.keys():
            chars_in_string[char] = 0
        chars_in_string[char] += 1


for char, occurrences in chars_in_string.items():
    print(f'{char} -> {occurrences}')