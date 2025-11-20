string_numbers = input().split(' ')

def rounding(numbers: list):
    roundet_numbers_list = []
    for number in numbers:
        roundet_numbers_list.append(round(float(number)))

    return roundet_numbers_list

roundet_numbers = rounding(string_numbers)
print(roundet_numbers)