number_of_rooms = int(input())
total_free_chairs = 0
messages = []

for room in range(1, number_of_rooms + 1):
    chairs_and_visitors = input().split(' ')
    chairs = chairs_and_visitors[0]
    visitors = int(chairs_and_visitors[1])
    total_free_chairs += len(chairs) - visitors
    if len(chairs) < visitors:
        free_chairs = False
        messages.append(f'{visitors - len(chairs)} more chairs needed in room {room}')


if messages:
    print('\n'.join(messages))
else:
    print(f'Game On, {total_free_chairs} free chairs left')


