number_range = int(input())
magic_word = input()

list_of_strings = []
list_with_magic_word = []

for _ in range(number_range):
    current_string = input()
    list_of_strings.append(current_string)

    # if magic_word in current_string:
    #     list_with_magic_word.append(current_string)

for element in list_of_strings:
    if magic_word in element:
        list_with_magic_word.append(element)

print(list_of_strings)
print(list_with_magic_word)