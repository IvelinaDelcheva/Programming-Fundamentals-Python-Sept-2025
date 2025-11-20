command = input()
while command != 'Welcome!':
    student_name = command
    student_name_lenght = len(student_name)

    if student_name == 'Voldemort':
        print('You must not speak of that name!')
        break

    if student_name_lenght < 5:
        print(f'{student_name} goes to Gryffindor.')
    elif student_name_lenght == 5:
        print(f'{student_name} goes to Slytherin.')
    elif student_name_lenght == 6:
        print(f'{student_name} goes to Ravenclaw.')
    elif student_name_lenght > 6:
        print(f'{student_name} goes to Hufflepuff.')

    command = input()

else:
    print('Welcome to Hogwarts.')
