# unicode table
# ascii table

# unicode - uses utf-8

# String Literals are surrounded by quotes
# single or double 
#  if we have nested quotes use \ or double outer quotes
message = "He said, 'Hello'"
print(message)

#  if we have \ in path we should escape it with double \\

# multiline string

message_1 = """"Hello,
Iv.
How
are
you?
"""
print(message_1)

# call func docstri
# funk_name.__doc__

#  str method return string
x = 3.5
print(str(x))

# split() splits str intro list
#  default split is by empty space

# + used for concatenation
mes = 'Hello'
mes2 = 'Iv'
res = mes + mes2
print(res)

# we can multiple text
res2 = mes * 3
print(res2)

# formatting with % operator
name = 'Iv'
age = 33

text = 'My name is %s and I am %d years old' % (name, age)
print(text)

price = 15.50
quantity = 100
total_cost = 'The total cost is ${:.2f} for {} items'.format(price * quantity, quantity)
# or
total_cost = f'The total cost is ${price * quantity:.2f} for {quantity} items'

print(total_cost)

# substrings

# slicing can be used for iterable object
text1 = 'This is SoftUni Fundamentals'
course = text1[16:]
print(course)
last_letter = text1[-1]
print(last_letter)
course_from_back = text1[-12:]
print(course_from_back)

numbers = [1, 2, 3, 4, 5]
subset = numbers[1:4]
print(subset)

text2 = 'Python Programming'
slice = text2[0:-1:2]
print(slice)

# reverse
reverse = text2[::-1]
print(reverse)

# String methods

# isdigit() check if it is digit
string1 = '12345'
print(string1.isdigit())

# upper() cast to capital letters
s = 'hello world'
print(s.upper())

# lower() cast ro lower letters
s2 = 'HELLO WORLD'
print(s2.lower())

# capitalize() cast the first letter to capital
s3 = 'hello world'
print(s3.capitalize())

#  title() makes all words with first letter capital
s4 = 'hello world'
print(s4.title())

# add symbol between the word with center()
s5 = 'hi'
print(s5.center(10, '-'))

# ljust() symbols after the word
s6 = 'hi'
print(s5.ljust(5, '*'))

# rjust() symbols before the word
s7 = 'hi'
print(s5.rjust(5, '*'))

# zfill() add zeros before the str including the str symbols
print('42'.zfill(5))

# count() it counts symbols
s8 = 'banana'
print(s8.count('a'))


# find() the times symbols appear
s9 = 'banana'
print(s8.find('na'))

# index() finds the index of the first symbol
s10 = 'banana'
print(s8.index('na'))

# rindex() finds the index of the right side of the string 
s11 = 'banana'
print(s8.rindex('na'))
# it will give error if the symbol does not exist

# isallnum() check if it is alphanumeric
# gives false if the is space 'abc 123'
s12 = 'abc123'
print(s12.isalnum())

# isdigit() check if it is number
s13 = '123'
print(s13.isdigit())

# isspace() check if it is space
space = ''
print(space.isspace())

# istitle() check if it starting with capital
s14 = 'Softuni'
print(s14.istitle())


# startswith() check if it is starting with specific symbols
s14 = 'Hello, SoftUni!'
print(s14.startswith('He'))

# endswith() check if it is ending with specific symbols
s15 = 'Hello, SoftUni!'
print(s15.endswith('i'))

s16 = 'one, two, three'
print(s16.split())

# split by numbers of symbols
s17 = 'one, two, three'
print(s16.split(', ', 1))


print('    hi     '.split())

# splitlines() makes multiline in a list
s18 = 'line1\nline2\nline3'
print(s18.splitlines())

# strip() removes empty space from str
s19 = '   hello   '
print(s19.strip())

# strip() removes empty space from str on the left
s20 = '   hello   '
print(s20.lstrip())

# strip() removes empty space from str on the right
s21 = '   hello   '
print(s21.rstrip())


# replace() replaces symbols
s22 = 'I like cats'
print(s22.replace('cats', 'dogs'))

# we can specify which number of symbol to replace
print(s22.replace(' ', '_', 1))


# replace but save in a variable
txt = 'I like bananas'