number_of_electrons = int(input())

list_with_filled_shells = []
n = 1
while number_of_electrons > 0:
    maximum_number_of_electrons = 2 * n ** 2
    if number_of_electrons < maximum_number_of_electrons:
        list_with_filled_shells.append(number_of_electrons)
    else:
        list_with_filled_shells.append(maximum_number_of_electrons)
    number_of_electrons -= maximum_number_of_electrons
    n += 1

print(list_with_filled_shells)