string_values = input().split()
inverted_values = []

for value in string_values:
    inverted_value = -int(value)
    inverted_values.append(inverted_value)

print(inverted_values)