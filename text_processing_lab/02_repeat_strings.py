sequence_of_strings = input().split()
concatenated_str = ''

for string in sequence_of_strings:
    concatenated_str += string * len(string)

print(concatenated_str)