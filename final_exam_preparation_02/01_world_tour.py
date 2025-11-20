stops = input()

while (command := input()) != 'Travel':
    parts = command.split(':')
    action = parts[0]

    match action:
        case 'Add Stop':
            index = int(parts[1])
            string = parts[2]
            if int(index) in range(len(stops)):
                stops = stops[:index] + string + stops[index:]
            print(stops)

        case 'Remove Stop':
            start_index = int(parts[1])
            end_index = int(parts[2])
            if start_index in range(len(stops)) and end_index in range(len(stops)):
                stops = stops[:start_index] + stops[end_index + 1:]
            print(stops)

        case 'Switch':
            old_string, new_string = parts[1:]
            if old_string in stops:
                stops = stops.replace(old_string, new_string)
            print(stops)

print(f'Ready for world tour! Planned stops: {stops}')