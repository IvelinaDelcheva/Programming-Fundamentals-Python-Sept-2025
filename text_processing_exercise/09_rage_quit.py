string_number_sequences = input()

unique_symbols = []
rage_message = ''
str_build = ''
number = 0
for i in range(len(string_number_sequences)):

    if not string_number_sequences[i].isnumeric():
        if string_number_sequences[i].lower() not in unique_symbols:
            unique_symbols.append(string_number_sequences[i].lower())
        str_build += string_number_sequences[i]

    elif string_number_sequences[i].isnumeric():
        if i + 1 in range(len(string_number_sequences)):
            if string_number_sequences[i + 1].isnumeric():
                rage_message += str_build.upper() * int(string_number_sequences[i] + string_number_sequences[i + 1])
            else:
                rage_message += str_build.upper() * int(string_number_sequences[i])
        else:
                rage_message += str_build.upper() * int(string_number_sequences[i])
        str_build = ''

print(f'Unique symbols used: {len(unique_symbols)}')
print(rage_message)