string_explosion = input()
strength = 0
final_str = ''
sub_str = ''
for index in range(len(string_explosion)):

    if string_explosion[index] == '>':
        strength += int(string_explosion[index +  1])
        start_index = index + 1
        stop_index = index + 1 + strength
        for sub_index in range(start_index, stop_index):
            if string_explosion[sub_index] == '>':
                break
            # string_explosion = string_explosion.replace(string_explosion[:sub_index], ' ', 1)
            string_explosion = string_explosion[:sub_index] + string_explosion.replace(string_explosion[:sub_index + 1], ' ', 1)
            strength -= 1


print(string_explosion.replace(' ', ''))

