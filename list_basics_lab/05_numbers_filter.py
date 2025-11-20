number_range = int(input())
list_of_numbers = []
filtered_list = []

for _ in range(number_range):
    current_number = int(input())
    list_of_numbers.append(current_number)

command = input()

for number in list_of_numbers:

    if command == 'even' and number % 2 == 0:
        filtered_list.append(number)
    elif command == 'odd' and number % 2 != 0:
        filtered_list.append(number)
    elif command == 'negative' and number < 0: 
        filtered_list.append(number)
    elif command == 'positive' and number >= 0:
        filtered_list.append(number)

print(filtered_list)