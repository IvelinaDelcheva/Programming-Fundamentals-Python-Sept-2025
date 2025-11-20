number_of_cars = int(input())
cars = {}

for _ in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    cars[car] = {'mileage' : int(mileage), 'fuel' : int(fuel)}

while (command := input()) != 'Stop':
    action, car_type = command.split(' : ')[:2]
    
    match action:
        case 'Drive':
            distance, fuel_to_drive = map(int, command.split(' : ')[2:])
            if cars[car_type]['fuel'] < fuel_to_drive:
                print(f'Not enough fuel to make that ride')
            else:
                cars[car_type]['fuel'] -= fuel_to_drive
                cars[car_type]['mileage'] += distance
                print(f'{car_type} driven for {distance} kilometers. {fuel_to_drive} liters of fuel consumed.')
            if cars[car_type]['mileage'] >= 100000:
                cars.pop(car_type)
                print(f'Time to sell the {car_type}!')

        case 'Refuel':
            fuel_refill = int(command.split(' : ')[2])
            liters_fuel = min(75 - cars[car_type]['fuel'], fuel_refill)
            cars[car_type]['fuel'] += liters_fuel
            print(f'{car_type} refueled with {liters_fuel} liters')

        case 'Revert':
            kilometers = int(command.split(' : ')[2])
            if cars[car_type]['mileage'] - kilometers < 10000:
                cars[car_type]['mileage'] = 10000
            else:
                print(f'{car_type} mileage decreased by {kilometers} kilometers')
                cars[car_type]['mileage'] -= kilometers

        

for car, data in cars.items():
    print(f"{car} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")