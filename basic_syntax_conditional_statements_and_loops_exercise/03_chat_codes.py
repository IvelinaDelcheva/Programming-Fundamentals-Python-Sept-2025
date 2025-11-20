n = int(input())

for _ in range(n):
    number_message = int(input())

    if number_message == 88:
        print('Hello')
    elif number_message == 86:
        print('How are you?')
    elif number_message < 88:
        print('GREAT!')
    elif number_message > 88:
        print('Bye.')