force_book = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break
    no_force_user = True
    if '|' in command:
        force_side, force_user = command.split(' | ')
        if force_side not in force_book.keys():
            force_book[force_side] = []
        
        for users in force_book.values():
            if force_user in users:
                no_force_user = False
        if not no_force_user:
            continue

        force_book[force_side].append(force_user)
    elif '->' in command:
        force_user, force_side = command.split(' -> ')
        if force_side not in force_book.keys():
            force_book[force_side] = []
        
        for users in force_book.values():
            if force_user in users:
                no_force_user = False

        if force_user:
            for users in force_book.values():
                for user in users:
                    if user == force_user:
                        users.remove(user)
            force_book[force_side].append(force_user)
        print(f'{force_user} joins the {force_side} side!')


for key, values in force_book.items():
    if values:
        print(f'Side: {key}, Members: {len(values)}')
        for value in values:
            print(f'! {value}')