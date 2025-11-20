# list comprehension structure
# the result is on the left 
# x**2 for x in num if x > 0
# result  var input optional param
print('Comprehensions\n')
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

letters = ['a', 'b', 'c', 'd']
uppercase_letters = [letter.upper() for letter in letters]
print(uppercase_letters)

words = ['hello', 'world', 'python', 'programming', 'example']
filtered_words = [word.upper() for word in words if 'o' in word]
print(filtered_words)

# comprehension can't be debuged

# dict comprehesnion
numbers_1 = [1, 2, 3, 4, 5]
squared_dict = {num: num ** 2 for num in numbers}
print(squared_dict)

# set comprehension
even_set = {num for num in numbers if num % 2 == 0}
print(even_set)

# if else in comprehension
numbers_2 = [1, 2, 3, 4, 5]
result = [num ** 2 if num % 2 == 0 else num ** 3 for num in numbers]
print(result)


# methods
print()
print('List Methods\n')

# extend() adds another list to the list
#  can be done with +
my_list = [1, 2, 3]
# my_list += [7, 8]
my_list.extend([7, 8])
print(my_list)

# insert() object at index
my_list_1 = [1, 2, 3]
my_list_1.insert(0, 9)
print(my_list_1)

# clear() removes everything from the list

# pop() if empty removes by index or removes the last element
my_list_2 = [1, 2, 3]
my_list_2.pop(0)
print(my_list_2)

# remove() removes specific element from the list
my_list_3 = [1, 2, 85, 3]
my_list_3.remove(3)
print(my_list_3)

# count() how often elements appear
my_list_4 = [85, 1, 2, 85, 3, 85]
print(my_list_4.count(85))

# index() look element at which inderx is 
my_list_5 = [1, 2, 85, 3, 85]
print(my_list_5.index(85))

# reverse() reverses the list

# sorted() can sort by key 
todo_notes = []
sorted_notes = sorted(todo_notes, key=lambda x: int(x.split('-')[0]))
sorted_text = [note.split('-')[1] for note in sorted_notes]

print('Advanced Functions\n')
# sorted() by lenght
words_1 = ['banana', 'apple', 'pear', 'kiwi']
sorted_by_lenght = sorted(words_1, key=len)
print(sorted_by_lenght)

# sorted() by grade
students = [
    {'name' : 'Ivan', 'grade' : 5},
    {'name' : 'Gosho', 'grade' : 6},
    {'name' : 'Pesho', 'grade' : 3},
    {'name' : 'Maria', 'grade' : 6},
]

sorted_grade = sorted(students, key=lambda student: student['grade'])
print(sorted_grade)

# map() for each element apply something

# some_numbers = ['1', '2', '3']
# int_numbers = map(int, some_numbers)
# print(list(int_numbers))

# taking user input
# we have to specify is a list because it will give us map func
# it will not print
numbers_3 = list(map(int, input().split(', ')))
print(numbers_3)


numbers = [1, 2, 3, 4, 5]
# pply function to each element of the list
doubled = list(map(lambda x: x * 2, numbers))
doubled_2 = [number * 2 for number in numbers]
print(doubled)
print(doubled_2)


a = [1, 2, 3]
b = [4, 5, 6]
summed = list(map(lambda x, y: x + y, a, b))
print(summed)

# filter() will apply the func and return only what is true from the func
numbers_4 = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers_4))
print(evens)


numbers_5 = [-5, 0, 3, -1, 9]
positives = list(filter(lambda x: x > 0, numbers_5))
print(positives)

# filter by lenght
words_2 = ['cat', 'elephant', 'dog', 'hippo']
long_words = list(filter(lambda w: len(w) > 3, words_2))
print(long_words)

# we can use comprehension with sum()
# we save the number of time the condition was true
# works like counte rin a loop counter += 1
# counter = sum(num >= average_sum for num in numbers)

# another way of using if else
# message = 'happy' if counter >= total_count / 2 else 'not happy'

# swap use this to swap 2 or more elements in the list
x = 5
y = 10
x, y = y, x
print('x = ', x)
print('y = ', y)

# concatenating lists
# can be done with extend too
nums_1 = [1, 2, 3]
nums_2 = [3, 4, 5]
res = nums_1 + nums_2
print(res)


# set() func does not allow repetitive elements
nums_3 = [1, 2, 3, 3, 2, 4, 5, 5]
unique_numbers = set(nums_3)
print(unique_numbers)
# we can use it for one string, or for string list
print(set('banana'))

names = ['Iva', 'Iva', 'Radi', 'Iva']
print(set(names))


# reduce() func takes list and reduce to single value
from functools import reduce

result = reduce(lambda x, y: x + y, [1, 2, 3, 4])
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
print(result) # 10

letters_1 = ['a', 'b', 'c', 'd']
result_1 = reduce(lambda x, y: x + y, letters_1, 'Start: ') # Start is the initial argument
print(result_1)