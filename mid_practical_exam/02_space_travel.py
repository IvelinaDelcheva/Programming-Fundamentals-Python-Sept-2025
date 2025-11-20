travel_route_to_titan = input().split("||")
fuel = int(input()) 
ammunition = int(input()) 

for line in travel_route_to_titan:
    command = line.split(' ')[0]

    if command == 'Titan':
        print(f'You have reached Titan, all passengers are safe.')
        break

    command_power = int(line.split(' ')[1])

    if command == 'Travel':
        if command_power <= fuel:
            fuel -= command_power
            print(f'The spaceship travelled {command_power} light-years.')
        else:
            print(f'Mission failed.')
            break

    elif command == 'Enemy':

        if ammunition >= command_power:
            ammunition -= command_power
            print(f'An enemy with {command_power} armour is defeated.')
        elif ammunition < command_power:
            if fuel >= (command_power * 2):
                fuel -= command_power * 2
                print(f'An enemy with {command_power} armour is outmaneuvered.')
            else:
                print('Mission failed.')
                break
        
    elif command == 'Repair':
        fuel += command_power
        ammunition += command_power * 2
        print(f'Ammunitions added: {command_power * 2}.')
        print(f'Fuel added: {command_power}.')