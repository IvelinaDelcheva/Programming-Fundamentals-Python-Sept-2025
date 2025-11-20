import re

pattern = r'\d+'
numbers = []
line = input()
while line:

    matches = re.findall(pattern, line)
    numbers += matches

    line = input()

print(' '.join(numbers))