command = input()
stock = {}
while (command != 'statistics'):
    product, quantity = command.split(': ')
    if product in stock.keys():
        stock[product] += int(quantity)
    else:
        stock[product] = int(quantity)

    command = input()

print('Products in stock:')
for product, quantity1 in stock.items():
    print(f'- {product}: {quantity1}')

print(f'Total Products: {len(stock.keys())}')
print(f'Total Quantity: {sum(stock.values())}')
