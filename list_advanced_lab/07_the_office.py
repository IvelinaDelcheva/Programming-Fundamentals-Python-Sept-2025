employees_happiness = list(map(int, input().split(' ')))
factor = int(input())

multiply_happiness = [employee * factor for employee in employees_happiness] 
average_happiness = sum(multiply_happiness) / len(multiply_happiness)
happy_employees = list(filter(lambda x: x >= average_happiness, multiply_happiness))
# multiply_1 = list(map(lambda x: x * factor, employees_happiness))

if len(happy_employees) >= len(multiply_happiness) / 2:
    print(f'Score: {len(happy_employees)}/{len(multiply_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(happy_employees)}/{len(multiply_happiness)}. Employees are not happy!')
