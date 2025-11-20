import re

phone = '07674234567'

pattern_hpne = r'^07[1-9]\d{7}'

if re.match(pattern_hpne, phone):
    print(f'{phone} is valid number!')
else:
    print(f'{phone} is not valid number!')

# there are multiple sources with ready regex patterns
# for emails, numbers etc.

email = 'webbersof@gmail.com'

pattern_emal = r'^[a-zA-Z0-9_.+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

if re.match(pattern_emal, email):
    print(f'{email} is valid!')
else:
    print(f'{email} is not valid!')

text = 'My number is 12345'

# \d finds all of the numbers in text
result = re.findall(r'\d', text)
print(result)

# \D matches all thet is not digit
result2 = re.findall(r'\D+', text)
print(result2)

# \b boundary for beggining or end fo word
# we can choose which word to find from start to end
text1 = 'The cat scattered the concatenation of cats'
result3 = re.findall(r'\bcat\b', text1)
print(result3)

# \s macthes spaces only
result4 = re.findall(r'\s', text1)
print(result4)

# \S macthes everything that is not space
result5 = re.findall(r'\S', text1)
print(result5)

# \w matches letter and numbers and underscore
# + means one or more occurences
result6 = re.findall(r'\w+', text)
print(result6)

# \W finds everything different form letters, numbers and underscore
result7 = re.findall(r'\W+', text)
print(result7)

# \ this means it will be speacial order like \w

# . matches everythng .+ match the whole sentance

#  to match . we use \.

text2 = 'The year is 2025'
result8 = re.findall(r'\d+', text2)
print(result8)

# * means 0 or more occurences
text3 = 'looooo loo lo k'
result9 = re.findall(r'lo*', text3)
print(result9)

# | or operator
text4 = 'cat'
result10 = re.findall(r'cat|dog', text4)
print(result10)

text5 = 'The ball is red and big'
pattern = '(red|blue) and (big|small)'
result11 = re.findall(pattern, text5)
print(result11)

# capture group (red|blue)

# {} exactly speciafied number of occurences
# it will find only groups with 3 digits or the 3 digit of the group
text6 = '1234 123 4 12 5 12345'
result12 = re.findall(r'\d{3}', text6)
print(result12) # ['123', '123', '123']

# add , it will catch 3 or more r'\d{3,}' - ['1234', '123', '12345']

# ^ starts with
text7 = 'Hello SoftuUni!'
result13 = re.findall(r'^Hello', text7)
print(result13)

# $ ends with
text8 = 'Hello SoftuUni!'
result14 = re.findall(r'SoftuUni!$', text8)
print(result14)

# sets []
text9 = 'Python is interpreted language345 16:45'
pattern = '[arn]'
pattern = '[a-n]'
# returnd everything that does not have those letters
pattern = '[^arn]'
#  works with numbers too
pattern = '[345]'
pattern = '[0-6][0-9]'
result15 = re.findall(pattern, text9)
# return all of thee occurences of those letters
print(result15) #['n', 'n', 'r', 'r', 'a', 'n', 'a']

# \b\d{1,2} has from 1 to 2 digits

# methods in regex

# findall() returns list with all ocurrences

# finditer() return iterable object

example_text = "cat mat bat"
x = re.finditer("\\b\w{3}\\b", example_text)

# retunrs object
# with group we print the word
# with start() and end() we can see at which indexes were found
for match in x:
    print(match.group())
    print(match.group(), 'found at', match.start(), '-', match.end())

# search returns object we have to print with group
example_text1 = "Hello 123 world 456"
match = re.search(r'\d+', example_text1)
print(match.group())

# split()
parts = re.split(' ', example_text1)
print(parts)

# sub() we can replace pattern with whatever we want
parts1 = re.sub('\d+', 'NUM', example_text1)
print(parts1)

# () use this for groups
# second group is the delimiter and with \2
#  we say take the same delimiter as group 2
reg = r'(\d{2})([-./])([A-Z][A-Z]{2})\2(\d{4})'

# we can take lements from match[0] object from finditer()
#  and findall 
# 12.Dec.2025
# we can take the dates with group(0) gives the whole result
# group(1) will give the date frist

# search() will search for a match but return only the first occurence
# and None if there is no match

# flags 
# it will not find it because Hello and hello is not capital
# but adding flag e.IGNORECASE will ignore that
txt = 'Hello World'
res = re.findall('hello', text, re.IGNORECASE)
print(res)

