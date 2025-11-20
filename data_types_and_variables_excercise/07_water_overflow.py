number_of_lines = int(input())

water_tank_capacity = 255
litters_in_tank = 0

for line in range(number_of_lines):
    liters_of_water = int(input())

    litters_in_tank += liters_of_water

    if litters_in_tank > water_tank_capacity:
        print(f'Insufficient capacity!')
        litters_in_tank -= liters_of_water
            

print(litters_in_tank)



