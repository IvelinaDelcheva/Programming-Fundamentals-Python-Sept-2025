sequence_of_elements = input().split()
moves = 0
command = input()
while command != 'end':

    index_1 = int(command.split(' ')[0])
    index_2 = int(command.split(' ')[1])
    moves += 1

    if index_1 == index_2 or index_1 not in range(len(sequence_of_elements)) or index_2 not in range(len(sequence_of_elements)):
        middle_index = len(sequence_of_elements) // 2
        sequence_of_elements.insert(middle_index, f"-{moves}a")
        sequence_of_elements.insert(middle_index, f"-{moves}a")
        print(f'Invalid input! Adding additional elements to the board')
    
    elif sequence_of_elements[index_1] == sequence_of_elements[index_2]:
        print(f'Congrats! You have found matching elements - {sequence_of_elements[index_1]}!')
        sequence_of_elements.pop(max(index_1, index_2))
        sequence_of_elements.pop(min(index_1, index_2))

    elif sequence_of_elements[index_1] != sequence_of_elements[index_2]:
        print('Try again!')

    if not sequence_of_elements:
        print(f'You have won in {moves} turns!')
        break

    command = input()

if sequence_of_elements:
    print(f'Sorry you lose :(')
    print(' '.join(sequence_of_elements))
    