first_string, second_string = input().split()
total_sum = 0

max_index = max(len(first_string), len(second_string))

for index in range(max_index):
    if index in range(len(first_string)) and index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    else:
        if len(first_string) == max_index:
            total_sum += ord(first_string[index])
        else:
            total_sum += ord(second_string[index])

print(total_sum)