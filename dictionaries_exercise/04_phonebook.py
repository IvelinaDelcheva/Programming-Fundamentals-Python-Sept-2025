notebook = {}
input_line = input()
while input_line.isnumeric() == False:
    name, number = input_line.split('-')
    notebook[name] = number

    input_line = input()

for person_ in range(int(input_line)):
    name = input()
    if name in notebook.keys():
        print(f'{name} -> {notebook[name]}')
    else:
        print(f'Contact {name} does not exist.')