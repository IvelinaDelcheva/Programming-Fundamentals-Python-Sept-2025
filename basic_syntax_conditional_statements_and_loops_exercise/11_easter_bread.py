budget = float(input())
flour_price_per_kg = float(input())
loaves_made = 0
coloured_eggs = 0

eggs_price = flour_price_per_kg * 0.75
milk_price_per_litre = flour_price_per_kg * 1.25
milk_for_recipe = milk_price_per_litre * 0.25

loave_price = flour_price_per_kg + eggs_price + milk_for_recipe

while budget >= loave_price:
    budget -= loave_price
    loaves_made += 1
    coloured_eggs += 3

    if loaves_made % 3 == 0:
        coloured_eggs -= loaves_made - 2

print(f'You made {loaves_made} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.')








