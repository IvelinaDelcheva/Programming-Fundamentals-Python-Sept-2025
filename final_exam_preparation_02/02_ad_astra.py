import re 

text_string = input()
total_calories = 0
days = 0
results = []

pattern = r'(\||#)([A-Za-z ]+)\1([\d]{2}\/[\d]{2}\/[\d]{2})\1(\d+)\1'
matches = re.findall(pattern, text_string)

if matches:
    for match in matches:
        item_name, expiration_date, calories = match[1:]
        total_calories += int(calories)
        print_output = f'Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}'
        results.append(print_output)

if total_calories > 0:
    days = total_calories // 2000

print(f'You have food to last you for: {days} days!')
if results:
    print('\n'.join(results))