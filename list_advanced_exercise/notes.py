# we can use map() or list comprehension to read int from input
list_of_int = [int(digit) for digit in input().split(' ')]
print(list_of_int)

# assign 2 variables from split
chairs, visitors = input().split(' ')
print(chairs)
print(visitors)