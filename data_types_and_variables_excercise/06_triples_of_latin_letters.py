number_of_letters = int(input())

for first_char in range(97, 97 + number_of_letters):
    for second_char in range(97, 97 + number_of_letters):
        for third_char in range(97, 97 + number_of_letters):
            print(f'{chr(first_char)}{chr(second_char)}{chr(third_char)}')