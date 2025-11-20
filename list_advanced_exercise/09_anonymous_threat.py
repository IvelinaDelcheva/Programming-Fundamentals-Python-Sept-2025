array_of_data = input().split(' ')
tokens = input().split(' ')


while tokens[0] != '3:1':
    command = tokens[0]

    if command == 'merge':
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        if start_index in range(len(array_of_data)) and end_index in range(len(array_of_data)):
            array_of_data[start_index : end_index + 1] = [''.join(array_of_data[start_index : end_index + 1])]
        elif end_index not in range(len(array_of_data)):
            array_of_data[start_index : end_index + 1] = [''.join(array_of_data[start_index : len(array_of_data)])]

    elif command == 'divide':
        index = int(tokens[1])
        partitions = int(tokens[2])
        
        divide_element = array_of_data[index]
        array_of_data.pop(index)
        if len(divide_element) % partitions == 0:
            n = len(divide_element) // partitions
            splitted = ([(divide_element[i:i+n]) for i in range(0, len(divide_element), n)])
            for item in splitted:
                array_of_data.insert(index, item)
                index += 1
        # splitted = []
        # for index in range(partitions):
        #     splitted.append(divide_element[:number_of_elements])
        #     divide_element = divide_element[number_of_elements:]
        # print(splitted)



    tokens = input().split(' ')

print(' '.join(array_of_data))





