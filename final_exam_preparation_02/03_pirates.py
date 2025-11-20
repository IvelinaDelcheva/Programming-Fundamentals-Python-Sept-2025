cities = {}


while (command := input()) != 'Sail':
    parts = command.split("||")

    city = parts[0]
    population = int(parts[1])
    gold = int(parts[2])
    if city in cities.keys():
        cities[city]['population'] += population
        cities[city]['gold'] += gold
    else:
        cities[city] = {'population' : population, 'gold' : gold}


while (second_command := input()) != 'End':
    second_parts = second_command.split('=>')
    action, town = second_parts[:2]

    match action:
        case 'Plunder':
            people, stolen_gold = list(map(int, second_parts[2:]))
            cities[town]['gold'] -= stolen_gold
            cities[town]['population'] -= people
            print(f'{town} plundered! {stolen_gold} gold stolen, {people} citizens killed.')
            if cities[town]['gold'] <= 0 or cities[town]['population'] <= 0:
                print(f'{town} has been wiped off the map!')
                cities.pop(town)

        case 'Prosper':
            gold_new = int(second_parts[2])
            if gold_new < 0:
                print('Gold added cannot be a negative number!')
            else:
                cities[town]['gold'] += gold_new
                print(f"{gold_new} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")


if cities:
    print(f"Ahoy, Captain! There are {len(cities.keys())} wealthy settlements to go to:")

    for city in cities.items():
        # print(f"{city} -> Population: {info['population']} citizens, Gold: {info['gold']} kg")
        print(f"{city[0]} -> Population: {city[1]['population']} citizens, Gold: {city[1]['gold']} kg")
else:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')