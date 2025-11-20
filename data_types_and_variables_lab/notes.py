# Immutable means that can’t be changed.
# If it is a string you can’t remove letters from it or move the characters and hange their places. Stirng is immutable.
# List is mutable becaseu we can replace the places and remove items from it. 
# The difference between set and list is that list will always have the same order 
# for the items and the set will not. It will always return the items in different indexes. 
# In the set are stored only unique values. If we have in the list [1, 1, 2, 3]  
# if we convert it to a set it will store only the unique values and 
# it will look like this {3, 2, 1}
# The tuple is like the list but is immutable. It can’t be changed. 
# Elements only can be accessed by index. Is like the string. 
# We can see what is there, but we can’t change it. 
# Dictionary is key value pairs data structure. 
# We can have lists in the list and this is called 2 dimensional matrix
# And It looks like this 
# My_list = [[1,2,3], [4,5,6]] lists in the list
# 	        0 index      1index
# Matrix  
# 1,2,3
# 4,5,6

# The list inside also have index and can be accessed like this
# Print(my_list[0][1]) and this will return 2 

# Dict is with {} brackets and the keys inside can only be unique 
# If we say the same key name and different value, it will overwrite the first value 
# My_dict = {name : ‘Amy’, age : 30}
# My_dict = {name : ‘Iva’} the name will become with the value Iva
# We use tuple when we don’t ever want to change this data structure
# And list when we know the data structure will be changed 
# Tuple is used for the final grades for the year. They will not be changed. 
# Dict information for each student.
# List for all student names. 

# List with dictionaries 
class_10_b = [{'name' : 'Iva', 'grade' : 5.50}, 
              {'name' : 'Rado'}
              ]

# All data structures can have different data types 

my_list = [] # [] brackets
my_set = {} # () brackets
my_tuple = () # () brackets
my_dict = {} # {} brackets 

# Functiona that returns the data type 
# type() 
name = 'Iva'
print(type(name))

# Function isinstance() check if data type is specific type
# takes two arguments, the variable adn the data type
# Returns true or false
print(isinstance(name, str))

# This is very usefull when we change the type of the variable
# with this function we can verify if is still the data type that 
# want it to be

# Access the string chars
print(name[0])
# Check the lenghts of the str
print(len(name))

# indexes of Iva are 0, 1, 2
# chars of Iva are 3

#  if we try to acces index 3 it will give error
# because indexes start from 0 and the last one is 2

# In python we can count form left to right
#  and fro right to left but then indexes will be negative
# Iva - -3, -2, -1 indexes
# This is used when we want the last index intead to count them 
# we don't know how many they are we can just say give me -1 index
# This will always be the last one
# Strings are immutable cannot be changed by index
# String can be changed with replace()

name = name.replace('I', 'i')
print(name)

# Immutable means that we cannot changed it by index
#  not that we can't change it at all

# String interpolation is aving placeholders in the string
print(f'{name}')

# in operator
#  item is in sequence

# None is something that is missing 
#  but is also not false


# no output here
number = None
if number:
    print(number)

# output here
number = 1
if number:
    print(number)

# bool() is func that checks if something is true


# None value can be checked with is keyword
null_variable = None
if null_variable is None:
    print(null_variable)


# Access chars from ASCII table

# With chr() and the Decimal number of the ysmbol in ASCII is giving us the symbol
print(chr(97))

# With ord() and the symbol that is under Chars in ASCII Table is giving us the decimal 
print(ord('a'))

# There is also library 
from string import ascii_letters

# Logger function in python
import logging


