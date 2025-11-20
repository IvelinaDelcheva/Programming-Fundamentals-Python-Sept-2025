input_line = input()
students = []
while ':' in input_line:
    students.append(input_line)
    input_line = input()

course = input_line
for student in students:
    if course[1:5] in student:
        name = student.split(':')[0]
        ID = student.split(':')[1]
        print(f'{name} - {ID}')