text = input()
vowels = ['a', 'o', 'u', 'e', 'i']

no_vowels = [ch for ch in text if ch.lower() not in vowels]
print(''.join(no_vowels))