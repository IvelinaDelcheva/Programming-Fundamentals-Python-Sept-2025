# we can change the values in the list

my_list = [[1, 2, 3, 4, 5], 
           [1, 2, 3, 4, 6], 
           [1, 2, 3, 4, 7]]

print(my_list) # [[1, 2, 3, 4, 5], [1, 2, 3, 4, 6], [1, 2, 3, 4, 7]]

my_list[0][0] = 15
print(my_list) # [[15, 2, 3, 4, 5], [1, 2, 3, 4, 6], [1, 2, 3, 4, 7]]

# if we remove an element 
# the indexes are also changing

# sort() does not work with mixed data types
my_list = [1, 2, 3, 4, 5]
# my_list.sort(reverse=True)
print(my_list) # [1, 2, 3, 4, 5]

# if we wrok with strngs it sorts first the capital adn the samell letters
letters = ['a', 'b', 'A', 'B']
letters.sort()
print(letters)

# using pop() we cal also save the value in a variable
digit = my_list.pop(4)
print(digit) # 5

# when we use insert() the indexes are changing, 
# the value it is not rmeoved if we want to insert 
# value at the same index

# del func deletes element at specific index
index = 3 # is number 4
del my_list[index]
print(my_list) # [1, 2, 3]

new_list = [1, 2, 3, 1, 2, 3]
# delete all occurences of specfic element
some_element = 3
while some_element in new_list:
    new_list.remove(some_element) 
print(new_list) # [1, 2, 1, 2]

# differnece between pop() and del is that pop() returns the value

# removing elemtns from list in a loop
# we have to start from the last eleemnt to the first
# because if we start from the first the indexes will change everyime we delete the fist item
# and it will give us an error
for index in range(len(my_list) - 1, -1, -1):
    print(f' Removing {new_list.pop(index)}')

# use this method whenn you want to remove elements
# and want to loop trough it

# remove() deletes by value del by index   

# deletes the whole list with 
# del my_list 

# if we want to empty the list
# just say it is empty
# my_list = []

# clear()
# removes all the elements from the list
# my_list.clear()


# enumerate gives us the index and the value
new_list_2 = [1, 2, 3, 1, 2, 3]
for index, value in enumerate(new_list_2):
    print(index, value)

# range returns only the index