# declaring and invoking functions
#  takes parameters and type and returns result
# the type is for information only to know what the function is taking
def sum_numbers(a: int, b: int):
    result = a + b
    return result
    # return a + b


# for i in range(1):
#     a = int(input('Insert values for a: '))
#     b = int(input('Insert values for b: '))
#     result = sum_numbers(a, b)  # what we give when we call the func
    # is arguments not parameters
    # print(result)

# built in functions
print(abs(-50))

numbers = [5, 7, 8, 4, 1]
print(min(numbers))
print(max(numbers))

pi = 3.14158
print(round(pi, 2)) # round of pi with two decimal lplaces

fruits = ['banana', 'apple', 'orange', 'kiwi']
print(sorted(fruits))

def is_even(n):
    return n % 2 == 0

# filter fi;ters the numbers
# we use the func to check even numbers
# we always have to give func as first argument
numbers = [5, 7, 8, 4, 1]
even_numbers = list(filter(is_even, numbers))
print('filter', even_numbers) # [8, 4]

def square(n):
    return n ** 2
# map exceutes the function with each of the elemnts from the list
numbers = [5, 7, 8, 4, 1]
squared_numbers = list(map(square, numbers))
print(squared_numbers) # [25, 49, 64, 16, 1]


# diff between map() and filter()
# use the same func to see diff
# Filter will only return the numbers that are tru for the func
# Map will go trough all of the numbers
# and it will give us boolean result
# True if the func applies and False if it does not
# Map is applied on each digit
# Filter only for the valid for the func
squared_numbers = list(map(is_even, numbers))
print('map', squared_numbers) # [False, False, True, True, False]


# This will give list of all builtin func in python
# import builtins
# print(dir(builtins))

# it is possible that func does not return anything
# just prints

def print_text(user: str):
    print(f'Welcome {user}!')

username = 'Ivelina'
print_text(username)




def sum_numbers(a, b, c):
    return a + b + c

first_num = 3
second_num = 5
third_num = 4

# We can specify the order which variable we give as argument
result = sum_numbers(a=third_num, b=first_num, c=second_num)
print(result)


# how o vie the docstring of a func
# print(map.__doc__)
# print(filter.__doc__)
# print(help(min))

# Docstring example

def calculate_square(num):
    """

    This calculate the square of a given number.

    :return
    float: The square of the input number.
    """
    square = num ** 2
    return square

# print(calculate_square.__doc__)

# Functions can be invoked from the body of other funcs

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator():
    operation = input('Enter the operation (+, -, *, /): ')
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    result = 0

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)

    print(result)

# calculator()

# recursion
# ckeck python func recursion
def count_number(n):
    if n <= 10:
        print(n, end=' ')
        count_number(n + 1)

# we give as an args the start number
# it is like loop
count_number(1)
print()
# we can have funct without params
def say_hello():
    print('Hello!')

say_hello()

# return gives the result from the func
def give_me_five():
    return 5

print(give_me_five())

# or we can save it in variable
five = give_me_five()
print(five)

# return in if statement
def divide_numbers(a, b):
    if b == 0:
        return 'Error: Division by zero!'
    else:
        return a / b
    
print(divide_numbers(6, 2))

# we can return multiple values separated by comma
def calculate_rectangle_properties(lenght, width):
    area = lenght * width
    perimeter = 2 * (lenght + width)
    diagonal = (lenght ** 2 + width ** 2) ** 0.5

    return area, perimeter, diagonal

print(calculate_rectangle_properties(10, 5))

# we can also unpack them
area_, perimeter_, diagonal_ = calculate_rectangle_properties(10, 5)
print(area_)
print(perimeter_)
print(diagonal_)

# Anything we do after "return" it will not be executed


# Func args can have default values
# if the func is called without the arg
# the args get te default value

def greet(name, greeting='Hello'):
    print(f'{greeting}, {name}')

greet('Ivelina')
# Hello, Ivelina

# lambda func
# it is like anonymous func for one-time operation
# like a func it can take param and return result
# a, b, c: are the params that is taking
sum_numbers = lambda a, b, c: a + b + c
print(f'Lambda func {sum_numbers(10, 20, 30)}')

# receives a number and check if it is even
is_even = lambda num: num % 2 == 0
print(f'Lambda result: {is_even(3)}')

# where we use lambda
# they are used very often in sorting