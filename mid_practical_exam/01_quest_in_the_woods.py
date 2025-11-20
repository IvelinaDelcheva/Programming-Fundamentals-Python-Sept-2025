days_of_adventure = int(input())
number_of_participants = int(input())
groups_energy = float(input())
water_per_day_for_person = float(input())
food_per_day_for_person = float(input())
no_energy = False

total_water = days_of_adventure * number_of_participants * water_per_day_for_person
total_food = days_of_adventure * number_of_participants * food_per_day_for_person

for day in range(1, days_of_adventure + 1):
    amount_of_energy_loss = float(input())

    groups_energy -= amount_of_energy_loss
    if groups_energy <= 0:
        no_energy = True
        break

    if day % 2 == 0:
        total_water *= 0.7
        groups_energy += groups_energy * 0.05

    if day % 3 == 0:
        total_food -= total_food/number_of_participants
        groups_energy += groups_energy * 0.1


if no_energy:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
else:
    print(f'You are ready for the quest. You will be left with {groups_energy:.2f} energy!')
