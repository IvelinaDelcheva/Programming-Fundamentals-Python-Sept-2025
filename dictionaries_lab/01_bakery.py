input_line = input().split(' ')
stock = {}

for line in range(0, len(input_line), 2):
    food = input_line[line]
    quantity = int(input_line[line + 1])
    stock[food] = quantity

print(stock)