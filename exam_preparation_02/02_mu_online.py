dungeons_rooms = input().split('|') 
initial_health = 100
bitcoins = 0
lost_the_game = False

for room in dungeons_rooms:
    command = room.split(' ')[0]
    number = int(room.split(' ')[1])

    if command == 'potion':
        initial_health += number
        if initial_health > 100:
            initial_health -= number
            diff = 100 - initial_health
            number = diff
            initial_health = 100
        print(f'You healed for {number} hp.')
        print(f'Current health: {initial_health} hp.')
    elif command == 'chest':
        bitcoins += number
        print(f'You found {number} bitcoins.')
    else:
        initial_health -= number
        if initial_health > 0:
            print(f'You slayed {command}.')
        elif initial_health <= 0:
            print(f'You died! Killed by {command}.')
            print(f'Best room: {dungeons_rooms.index(room) + 1}')
            lost_the_game = True
            break

if not lost_the_game:
    print(f'You\'ve made it!')
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {initial_health}')

