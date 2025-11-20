command = input()
company = {}
while command != 'End':
    company_name, employee_id = command.split(' -> ')
    if company_name not in company.keys():
        company[company_name] = []
    if employee_id not in company[company_name]:
        company[company_name].append(employee_id)
    command = input()


for name, ids in company.items():
    print(name)
    for id in ids:
        print(f'-- {id}')

