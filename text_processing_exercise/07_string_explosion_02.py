string_explosion = input()
strength = 0

list_explosion = [ch for ch in string_explosion]

for index in range(len(list_explosion)):
    if list_explosion[index] == '>':
        strength += int(list_explosion[index + 1])

        start_index = index + 1
        stop_index = index + 1 + strength

        for inner_index in range(start_index, stop_index):
            if list_explosion[inner_index] == '>':
                break
            list_explosion[inner_index] = 'remove'
            strength -= 1

cleaned = [ch for ch in list_explosion if ch != 'remove']
print(''.join(cleaned))
