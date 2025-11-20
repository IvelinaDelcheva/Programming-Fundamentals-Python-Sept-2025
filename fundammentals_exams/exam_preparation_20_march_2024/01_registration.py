username = input()

while (command := input()) != 'Registration':
    parts = command.split(' ')
    action = parts[0]

    match action:
        case 'Letters':
            lower_upper = parts[1]
            match lower_upper:
                case 'Lower':
                    username = username.lower()
                case 'Upper':
                    username = username.upper()
            print(username)

        case 'Reverse':
            start_index = int(parts[1])
            end_index = int(parts[2])
            if start_index in range(len(username)) and end_index in range(len(username)):
                sub = username[start_index:end_index + 1]
                print(sub[::-1])

        case 'Substring':
            sub_str = parts[1]
            if sub_str in username:
                username = username.replace(sub_str, '')
                print(username)
            else:
                print(f"The username {username} doesn't contain {sub_str}.")
            
        case 'Replace':
            char = parts[1]
            username = username.replace(char, '-')
            print(username)

        case 'IsValid':
            valid_char = parts[1]
            if valid_char in username:
                print(f'Valid username.')
            else:
                print(f'{valid_char} must be contained in your username.')
    


