number_of_coffees = 0

while True:
    current_command = input()

    if current_command == 'END':
        break

    if current_command.isupper():
        if current_command == 'CODING' \
        or current_command == 'DOG' \
        or current_command == 'CAT' \
        or current_command == 'MOVIE':
            number_of_coffees += 2
        else:
            continue
    elif current_command.islower():
        if current_command == 'coding' \
        or current_command == 'dog' \
        or current_command == 'cat' \
        or current_command == 'movie':
            number_of_coffees += 1
        else:
            continue

if number_of_coffees > 5:
    print('You need extra sleep')
else:
    print(number_of_coffees)