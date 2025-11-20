some_sting = input()
final_string = ''
strenght = 0

for index in range(len(some_sting)):
    if strenght > 0 and some_sting[index] != '>':
        strenght -= 1

    elif some_sting[index] == '>':
        final_string += '>'
        strenght += int(some_sting[index + 1])
    else:
        final_string += some_sting[index]

print(final_string)