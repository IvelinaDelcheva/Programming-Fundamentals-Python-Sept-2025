substrings = input().split(', ')
list_of_strings = input().split(', ')

contained_substrings = []

for substring in substrings:
    for string in list_of_strings:
        if substring in string:
            if substring not in contained_substrings:
                contained_substrings.append(substring)

print(contained_substrings)