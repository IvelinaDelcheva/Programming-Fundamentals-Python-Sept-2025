list_of_characters = input().split(', ') 
ascii_dict = {char:ord(char) for char in list_of_characters}
print(ascii_dict)
