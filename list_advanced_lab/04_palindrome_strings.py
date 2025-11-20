words = input().split(' ')
palindrome = input()
palindromes = []

for word in words:
    if word == word[::-1]:
        palindromes.append(word)

found_palindrome = palindromes.count(palindrome)
print(palindromes)
print(f'Found palindrome {found_palindrome} times')