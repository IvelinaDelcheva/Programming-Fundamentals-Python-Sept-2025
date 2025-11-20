input_line = input().split(' ')
products_to_search = input().split()
stock = {}

for line in range(0, len(input_line), 2):
    product = input_line[line]
    quantity = input_line[line + 1]
    stock[product] = quantity

for product in products_to_search:
    if product in stock.keys():
        print(f'We have {stock[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")