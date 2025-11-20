import sys
list_of_string_numbers = input().split(' ')
count_of_numbers_to_remove = int(input())

list_of_integers = []
list_of_string_integers = []


for number_string in list_of_string_numbers:
    list_of_integers.append(int(number_string))


for _count in range(count_of_numbers_to_remove):
    # min_value = min(list_of_integers)
    min_value = sys.maxsize
    for integer in list_of_integers:
        if integer < min_value:
            min_value = integer
    list_of_integers.remove(min_value)

for integer in list_of_integers:
    list_of_string_integers.append(str(integer))

print(', '.join(list_of_string_integers))

