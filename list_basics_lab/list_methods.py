# append adds element to the list at the end
empty_list = []
empty_list.append(1)
empty_list.append(2)
empty_list.append(3)
empty_list.append(4)
empty_list.append(5)
empty_list.append(5)

print(empty_list)


# remove it removes elements from the list
# removes by value not by index
empty_list.remove(3)
print(empty_list)

# typing help(list) in the console will give us the documentation

# copy() copies the list
copy_empty_list = empty_list.copy()
print(copy_empty_list)

# count() counts specific element
print(empty_list.count(5))

# extend() adds another list
empty_list.extend([1, 2, 3])
print(empty_list)

# index returns the index of an item in the list
index = empty_list.index(5)
# it will return the first occurence
print(index) # 3

# we can return then the other 5 by startitng from index 4
# we have to give the index after the first occurence
# meaning if 5 is at index 3 we give index 4 as a start
index_2 = empty_list.index(5, 4)
print(index_2)

# insert() inserts element in the list at a index
# first we give the index
# we can also work with strings
empty_list.insert(0, 10)
print(empty_list)

# pop() removes the last element
empty_list.pop() # [10, 1, 2, 4, 5, 5, 1, 2, 3]
print(empty_list) # [10, 1, 2, 4, 5, 5, 1, 2]

# pop() rwe can aslo specify at which index to remove it
empty_list.pop(0) # [10, 1, 2, 4, 5, 5, 1, 2, 3]
print(f'After pop 0 element{empty_list}') # [10, 1, 2, 4, 5, 5, 1, 2]

# reverse() reverses the list from backwards to forwards
empty_list.reverse() # [10, 1, 2, 4, 5, 5, 1, 2, 3]
print(empty_list) # [2, 1, 5, 5, 4, 2, 1, 10]

# sort() it sorts the list
empty_list.sort()
print(empty_list)

# loop trough list over the elements
for number in empty_list:
    print(number, end= ' ')

print()


# loop trough list with range
for index in range(len(empty_list)):
    print(empty_list[index], end=' ')

print()

# loop trough list with while
index = 0
while index < len(empty_list):
    print(empty_list[index], end=' ')
    index += 1

print()

# list comprehension
even_numbers = [number for number in [1, 2, 3, 4, 5, 6] if number % 2 == 0]
print(even_numbers)

# search for elements in the list
# in
if 7 in even_numbers:
    print(even_numbers)
else:
    print('Not exist!')


# search for elements in the list
# not in
if 7 not in even_numbers:
    print('Element is not in the list!')
else:
    print(even_numbers)