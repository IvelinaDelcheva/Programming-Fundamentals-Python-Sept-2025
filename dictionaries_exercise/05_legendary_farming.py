key_materials = ['shards', 'fragments', 'motes']
materials = dict.fromkeys(key_materials, 0)
legendary_obtained = False


while not legendary_obtained:
    line_list = input().split(' ')
    for index in range(0, len(line_list), 2):
        quantity = int(line_list[index])
        material = line_list[index + 1].lower()

        if material not in materials.keys():
            materials[material] = 0
        materials[material] += quantity
        if materials['shards'] >= 250:
            materials['shards'] -= 250
            print(f'Shadowmourne obtained!')
            legendary_obtained = True
            break
        elif materials['fragments'] >= 250:
            materials['fragments'] -= 250
            print(f'Valanyr obtained!')
            legendary_obtained = True
            break
        elif materials['motes'] >= 250:
            materials['motes'] -= 250
            print(f'Dragonwrath obtained!')
            legendary_obtained = True
            break


for key, value in materials.items():
    print(f'{key}: {value}')


