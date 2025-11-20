import re 

text = input()
word = input()

word_to_search = f'{word}'
pattern = fr'\b{word_to_search}\b'

matches = re.findall(pattern, text, re.IGNORECASE)
print(len(matches))