text = input()

encrypted_text = ''
for character in text:
    char_enc = ord(character) + 3
    encrypted_text += chr(char_enc)

print(encrypted_text)