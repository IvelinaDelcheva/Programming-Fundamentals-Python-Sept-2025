import re

total_cost = 0
furnitures = []
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'

command = input()
while command != 'Purchase':

    match = re.search(pattern, command)
    if match:
        furniture_name, price, quantity =  match.groups()
        total_cost += float(price) * int(quantity)
        furnitures.append(furniture_name)
    command = input()

print(f'Bought furniture:')
for furniture in furnitures:
    print(furniture)
print(f'Total money spend: {total_cost:.2f}')