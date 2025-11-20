wagons = int(input())
train = [0 for wagon_ in range(wagons)]
# train = [0] * wagons

while True:
    command = input()
    if command == 'End':
        break

    if 'add' in command:
        people = command.split(' ')[1]
        train[-1] += int(people)
    elif 'insert' in command:
        index = command.split(' ')[1]
        people = command.split(' ')[2]
        train[int(index)] += int(people)
    elif 'leave' in command:
        index = command.split(' ')[1]
        people = command.split(' ')[2]
        train[int(index)] -= int(people)

print(train)