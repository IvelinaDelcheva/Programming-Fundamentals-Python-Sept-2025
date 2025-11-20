sequence_of_numbers = input().split(' ')

abs_values_list = []

for number in sequence_of_numbers:
    abs_values_list.append(abs(float(number)))

print(abs_values_list)