from math import ceil

number_of_the_students = int(input())
number_of_the_lectures  = int(input())
additional_bonus  = int(input())

max_bonus = 0
max_bonus_student_attendances = 0

if number_of_the_lectures:

    for student_ in range(number_of_the_students):
        attendance_of_each_student = int(input())
        total_bonus = (attendance_of_each_student / number_of_the_lectures) * (5 + additional_bonus)

        if total_bonus > max_bonus:
            max_bonus = total_bonus
            max_bonus_student_attendances = attendance_of_each_student



print(f'Max Bonus: {ceil(max_bonus)}.')
print(f'The student has attended {max_bonus_student_attendances} lectures.')

