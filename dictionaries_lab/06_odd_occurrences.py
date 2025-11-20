words = input().split(' ')
word_dict = {}

for word in words:
    if word.lower() in word_dict.keys():
        word_dict[word.lower()] += 1
    else:
        word_dict[word.lower()] = 1

odd_occurences = [ word for word, occurence in word_dict.items() if occurence % 2 != 0]

print(' '.join(odd_occurences))
