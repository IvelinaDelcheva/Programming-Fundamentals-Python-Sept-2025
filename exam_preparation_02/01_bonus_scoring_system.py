import sys
from math import ceil
number_of_the_students = int(input())
number_of_the_lectures  = int(input())
additional_bonus  = int(input())
max_number = 0
attended_lectures = 0

if number_of_the_lectures:
    for student in range(number_of_the_students):
        attendance_of_each_student = int(input())

        total_bonus = (attendance_of_each_student / number_of_the_lectures) * (5 + additional_bonus)
        if total_bonus > max_number:
            max_number = total_bonus
            attended_lectures = attendance_of_each_student

print(f'Max Bonus: {ceil(max_number)}.')
print(f'The student has attended {attended_lectures} lectures.')