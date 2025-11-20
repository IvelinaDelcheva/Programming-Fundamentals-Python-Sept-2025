#  we can have func as a value in a dict
def surname():
    return 'Delcheva'

student = {
    'name': 'Ivi',
    'surname': surname()
}

print(student) # {'name': 'Ivi', 'surname': 'Delcheva'}
print(student['surname']) # Delcheva