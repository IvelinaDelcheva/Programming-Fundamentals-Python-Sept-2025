n = int(input())
students = {}
for _ in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in students.keys():
        students[student_name] = []
    students[student_name].append(grade)

for student, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 4.50:
        print(f'{student} -> {avg_grade:.2f}')