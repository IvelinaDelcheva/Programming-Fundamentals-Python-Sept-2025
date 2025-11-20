stock = {}
sold_goods = 0

while (command := input()) != 'Complete':
    parts = command.split(' ')
    action = parts[0]
    food = parts[2]
    quantity = int(parts[1])

    match action:
        case 'Receive':
            if quantity <= 0:
                continue

            if food not in stock.keys():
                stock[food] = 0
            stock[food] += quantity
        
        case 'Sell':
            if food not in stock.keys():
                print(f'You do not have any {food}.')
            elif stock[food] < quantity:
                sold_goods += stock[food]
                print(f"There aren't enough {food}. You sold the last {stock[food]} of them.")
                stock.pop(food)
            else:
                stock[food] -= quantity
                sold_goods += quantity
                print(f'You sold {quantity} {food}.')
                if stock[food] == 0:
                    stock.pop(food)

for stock_food, stock_quantity in stock.items():
    print(f'{stock_food}: {stock_quantity}')
print(f'All sold: {sold_goods} goods')

