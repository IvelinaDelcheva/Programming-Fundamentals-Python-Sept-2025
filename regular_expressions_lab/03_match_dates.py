import re

dates = input()

pattern = r'(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})'

matches = re.finditer(pattern, dates)

for match in matches:
    day = match[1]
    month = match[3]
    year = match[4]
    print(f'Day: {day}, Month: {month}, Year: {year}')