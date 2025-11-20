from math import prod
products = {}
command = input()
while command != 'buy':
    name, price, quantity = command.split(' ')
    
    if name in products.keys():
        products[name][0] = float(price)
        products[name][1] += int(quantity)

    if name not in products.keys():
        products[name] = []
        products[name].append(float(price))
        products[name].append(int(quantity))

    command = input()

for product, total_price in products.items():
    print(f'{product} -> {prod(total_price):.2f}')
