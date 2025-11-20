secret_message = input().split(' ')
decipher_list = []
for word in secret_message:
    digits = []
    letters = []
    for char in word:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
    letters[0], letters[-1] = letters[-1], letters[0]
    decipher_word = chr(int(''.join(digits))) + ''.join(letters)
    decipher_list.append(decipher_word)

print(' '.join(decipher_list))