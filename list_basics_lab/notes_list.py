# Lists are muyable.Thie smeans we can change them
# List also have indexes and repeatble values
# Lists can expand and shrink and to store differenct data types
# We can also have nested lists
list_example = ['apple', 'banana', 'cherry', 'banana', 3.14, {'name' : 'Iva'}, True, False, [1, 2, 3, 4, 5]]
print(list_example[1])  # banana
# we can also check the type
print(type(list_example))

# this will save only the unique values
set_example = {'apple', 'banana', 'cherry', 'banana'}
print(set_example)

# matrix is used for pixels
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
print(list_example)
# access elemnent from the list by index
print(list_example[8])

# recursive lists
my_list = [1, 2, 3]

# ad element to the list
my_list.append(4)

# add the list to the list
my_list.append(my_list)
# the result will be endless loop
# keeps addind itself endlesly
print(my_list) # [1, 2, 3, 4, [...]]

# lists in pytho are like arrays
# when e want array in python 
import numpy as np

# use array func from numpy library
# data types should be the same
# they are used for mathematical calculations
arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)

# changed to float it will still work
arr = np.array([1, 2, 3.14, 4, 5]) #[ 2.    4.    6.28  8.   10.  ]
print(arr * 2)

arr_int = np.array([1, 2, 3, 4, 5], dtype=np.int32)
print(arr_int) #[1 2 3 4 5]
print(arr_int.dtype) 

# if we try to add float to it it will ignore it and leave it as int
arr_int = np.array([1, 2, 3.14, 4, 5], dtype=np.int32)
print(arr_int) #[1 2 3 4 5]

# Initialize list
list_1 = []
list_2 = list()

print(type(list_1)) # <class 'list'>
print(type(list_2)) # <class 'list'>

list_2 = list(range(1, 11))
print(list_2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_3 = list(['apple', 'banana', 'cherry'])
print(list_3) # ['apple', 'banana', 'cherry']


# split() func
some_text = 'a b c d'
# above example there are spaces between the letters
# it splits them by what is between the letters
list_4 = some_text.split(' ')
print(list_4) # ['a', 'b', 'c', 'd']

some_text = 'a-b-c-d'
# should be '-' because letters are splitted by '-'
list_4 = some_text.split('-') 
print(list_4) # ['a', 'b', 'c', 'd']

# user_data = input().split(', ')
# print(user_data) # ['1', '2', '3'] returns stirngs


# use map func to parse it to int
user_data = list(map(int, input().split(', ')))
print(user_data) # [1, 2, 3]

user_data_1 = input().split(' ') # Ivelina Delcheva
# This is called unpacking of a list
first_name, last_name = user_data_1
print(f'First name: {first_name}') # First name: Ivelina
print(f'Last name: {last_name}') # Last name: Delcheva

# string.join() func
# this joins list with the delimeter we want
list_5 = ['a', 'b' , 'c']
join_list = ''.join(list_5)
# the final result is string
# we cannot join int or float
print(join_list) #abc

# we have a list but we don't know which one is the last one
# the first one is at index 0
# the last one is alway -1
# no matter how long is the list
fruits = ['kiwi', 'apple', 'banana']
# this works like the string slicing
#return them from right to left
print(fruits[::-1])
print(fruits[0]) # kiwi
# elements backwards 
print(fruits[-1]) # banana
print(fruits[-2]) # apple
print(fruits[-3]) # kiwi

# take part of the list
part_list = fruits[0:2]
print(f'Part list: {part_list}')

# Eelemnt swap
x = 6
y = 3

x, y = y, x
print(x)
print(y)

#Unpacking of a list if we don't know how many elements
new_data = input().split(' ') # iv del 33 pld bul
first_name_1, last_name_2, *additiona_data = new_data

print(first_name_1) # iv
print(last_name_2) # del
print(additiona_data) # ['33', 'pld', 'bul']
