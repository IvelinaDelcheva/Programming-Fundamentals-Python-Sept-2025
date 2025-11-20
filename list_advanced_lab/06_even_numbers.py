numbers = list(map(int, input().split(', ')))
even_numbers = []
for number in enumerate(numbers):
    if number[1] % 2 == 0:
        even_numbers.append(number[0])
print(even_numbers)