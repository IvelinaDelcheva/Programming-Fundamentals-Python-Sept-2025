input_list = input().split(' ')
shuffle_count = int(input())

half_deck = len(input_list) // 2
top_deck = (input_list[:half_deck])
bottom_deck = input_list[half_deck:]

for _count in range(shuffle_count):
    shuffle_list = []
    for index in range(half_deck):
        shuffle_list.append(top_deck[index])
        shuffle_list.append(bottom_deck[index])
    
    top_deck = (shuffle_list[:half_deck])
    bottom_deck = shuffle_list[half_deck:]

print(shuffle_list)


