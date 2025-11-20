quantity_of_decorations = int(input())
days_until_christmas = int(input())

ornament_sets = 2
tree_skirts = 5
tree_garlands = 3
tree_lights = 15

decoration_price_total = 0.0
christmas_spirit = 0

for day in range(1, days_until_christmas + 1):

    if day % 11 == 0:
        quantity_of_decorations += 2

    if day % 2 == 0:
        decoration_price_total += (quantity_of_decorations * ornament_sets)
        christmas_spirit += 5
    if day % 3 == 0:
        decoration_price_total += (quantity_of_decorations * tree_skirts) + (quantity_of_decorations * tree_garlands)
        christmas_spirit += 3 + 10
    if day % 5 == 0:
        decoration_price_total += (quantity_of_decorations * tree_lights)
        christmas_spirit += 17
    if day % 3 == 0 and day % 5 == 0:
        christmas_spirit += 30

    if day % 10 == 0:
        christmas_spirit -= 20
        decoration_price_total += tree_skirts + tree_garlands + tree_lights



if day % 10 == 0:
    christmas_spirit -= 30

print(f'Total cost: {decoration_price_total:.0f}')
print(f'Total spirit: {christmas_spirit:.0f}')

