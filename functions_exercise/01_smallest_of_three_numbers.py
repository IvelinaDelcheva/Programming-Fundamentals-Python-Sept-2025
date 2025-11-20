def smallest_number(some_numbers: list) -> int:
    return min(some_numbers)

first_number = int(input())
second_number = int(input())
third_number = int(input())

numbers = []
numbers.append(first_number)
numbers.append(second_number)
numbers.append(third_number)

smalles_number_of_the_list = smallest_number(numbers)
print(smalles_number_of_the_list)