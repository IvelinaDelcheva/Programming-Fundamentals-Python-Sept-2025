product_ = input()
quantity_ = int(input())

def calculate_order(product: str, quantity: int):
    total = 0

    if product == 'coffee':
        total = quantity * 1.50
    elif product == 'water':
        total = quantity * 1.00
    elif product == 'coke':
        total = quantity * 1.40
    elif product == 'snacks':
        total = quantity * 2.00
    
    return f'{total:.2f}'

order_total = calculate_order(product_, quantity_)
print(order_total)


