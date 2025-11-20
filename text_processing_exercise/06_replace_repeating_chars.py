string = input()
replaced_str = ''

for index in range(len(string)):
    
    if replaced_str:
        if string[index] != replaced_str[-1]:
            replaced_str += string[index]
    else:
        replaced_str += string[index]
        

print(replaced_str)