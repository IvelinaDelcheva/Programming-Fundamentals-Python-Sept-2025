n = int(input()) 
parking_lot = {}
for _ in range(n):
    input_line = input().split(' ')
    command = input_line[0]
    username = input_line[1]

    if command == 'register':
        license_plate_number = input_line[2]
        if username not in parking_lot.keys():
            parking_lot[username] = license_plate_number
            print(f'{username} registered {license_plate_number} successfully')
        else:
            print(f'ERROR: already registered with plate number {license_plate_number}')
        
    elif command == 'unregister':
        if username not in parking_lot.keys():
            print(f'ERROR: user {username} not found')
        else:
            parking_lot.pop(username)
            print(f'{username} unregistered successfully')

for user, licence_plate in parking_lot.items():
    print(f'{user} => {licence_plate}')