# keys must be immutabel and unique

#  create dict 
keys = ['name', 'age', 'major']
values = ['Iv', '33', 'Developer']

student = {}

for i in range(len(keys)):
    key = keys[i]
    value = values[i]
    student[key] = value

print(student)
print(student['name'])

# use dict func
student1 = dict(name = 'Ive', age = '34', major='Software Developer')
print(student1)

# use zip func
# It makes a dict form two lists
keys1 = ['name', 'age', 'major']
values1 = ['Iveto', '32', 'Dev']

new_student = dict(zip(keys1, values1))
print(new_student)

# few lines dict
student1 = {
    'name' : 'Ivi',
    'age' : 33,
    'major' : 'DevOps',
    'language' : 'Python'
}

# access keys
print(student1['name'])
print(student1['language'])

# access keys only
print(student1.keys())

# access values 
print(student1.values())

# access both
print(student1.items())

# we can take key and values and loop and print the together
for key, value in student1.items():
    print(key, value)

text = """check is it has simialr wrords word similar
 check if has chekc does it has has check similar
"""
word_count = {}
for word in text.lower().split():
    word = word.strip('.,')
    word_count[word] = word_count.get(word, 0) + 1

#  important lambda with dict
print(word_count)
sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[0], reverse=True))
sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
print(sorted_word_count)

# dict is faster because it uses the hash funcion
# look for hash tables

# get values with get() func
print(student1.get('name'))

# add new key value pair
student1['surname'] = 'Delcheva'
print(student1)

# if we call key with get() it will show none
#  if we call key directly it will give error
# print(student1['country']) error 
print(student.get('country')) # None

#  fi we have dublicated key it will always 
# retrieve the last value created

text = 'Hello'
counter = {}

for letter in text:
    counter[letter] = counter.get(letter, 0) + 1

print(counter)

# nested dicts
users = [
    {'name' : 'Iv', 'email' : 'apple' },
    {'name' : 'Iv'},
    {'name' : 'Ive', 'email' : 'google'}
]

# get() gives another value if there is no key
for user in users:
    # print(user)
    email = user.get('email', 'no email')
    print(f"{user['name']} - {email}")

# dict with list values
my_dict = {
    'names' : ['Ivi', 'Radi'],
    'age' : 33
}

# iterate over the list fo values for a key
for name in my_dict['names']:
    print(name)


#  change values
my_dict['age'] += 1
print(my_dict['age'])

# check if value exist in the hey or the values in dict
if 'name' in student1.keys():
    print(f"It exist {student1['name']}")

person = {
    'name' : 'Iveto',
    'age' : 33,
    'phone' : 23455677
}

phone = person.get('phone')

if phone:
    print(f"Phone {phone}")
else:
    print("No Phone")


# dict methods
# copy() makes a copy fo the dict
# clear() deltes from dict
person2 = person.copy()
person.clear()

print(person)
print(person2)

# assign values to keys 
keys = {'a', 'b', 'c'}
# fromkeys() Create a new dictionary with 
# keys from iterable and values set to value.
new_dict = dict.fromkeys(keys, 0)

# get() return value from key if exist f not return None
# items()
# values()
# keys()

# pop() returns the value from the key
# and removes it from the dict
element = new_dict.pop('a')
print(element)
print(new_dict)

# it doesn't work on its own. It should receive key
# but popitem() reoves the last element
new_element = new_dict.popitem()
print(new_element)

# setdefault() adds new key value pair
new_element_2 = new_dict.setdefault('8',2)
print(new_dict)
print(new_element_2)

# update() adds new key value pair to the dict
new_dict.update({'lqlq' : '57646467'})
print(new_dict)

# delete key value pair by key
del new_dict['lqlq']
print(new_dict)

#  delete the whole dict with del
# del new_dict
# print(new_dict) it will give error

student_records = {
    'Radi' : {'Math' : 5.50, 'English' : 5.00, 'Sport' : 6.00},
    'Ivi' : {'Math' : 4.50, 'English' : 4.00, 'Sport' : 6.00},
    'Mara' : {'Math' : 6.00, 'English' : 5.00, 'Sport' : 6.00}
}

# access the nested dict by key
print(student_records['Radi'])

# access specific value from the nested dict by nested key
print(student_records['Radi']['Math'])

# add new nested dict
student_records['Delch'] = {'Math' : 6.00, 'English' : 5.00, 'Sport' : 6.00}
print(student_records['Delch']['Sport'])

# iterate trought nested dict
for name, info in student_records.items():
    print(name)
    for key, value in info.items():
        print(key, value)
    
    print()


# dict comprehension
fruits = ['apple', 'kiwi', 'banana', 'apple']
fruit_lengths = {fruit: len(fruit) for fruit in fruits if len(fruit) % 2 == 0}
print(fruit_lengths)

numbers = [1, 2, 3, 4, 5]
squares = {num: num ** 2 for num in numbers if num % 2 == 0}
print(squares)