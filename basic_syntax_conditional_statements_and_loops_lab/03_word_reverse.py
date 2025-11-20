word = input()

for letter in range(len(word) - 1, -1, -1):
    print(word[letter], end='')

# Use String Slicing to reverse word.
# This means start form the end of the word and move 1 step backwards with
# negtive one 
# print(word[::-1])