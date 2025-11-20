def all_characters_in_between(first_char: str, second_char: str):
    chars_in_between = []

    for char in range(ord(first_char) + 1, ord(second_char)):
        chars_in_between.append(chr(char))
    return print(' '.join(chars_in_between))

first_character = input()
second_character = input()

all_characters_in_between(first_character, second_character)

