string_explosion = input()
strength = 0
index = 0
working_str = string_explosion
if len(working_str) > 0:
    while index < len(working_str):

        if working_str[index] == '>':
            strength += int(working_str[index + 1])

            while strength > 0 and strength in range(len(working_str)):
                if working_str[index + 1] == '>':
                    break
                working_str = working_str[:index + 1] + working_str.replace(working_str[:index + 1 + 1], '', 1)
                strength -= 1

        index += 1

print(working_str)
