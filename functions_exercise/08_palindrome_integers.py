def palindrome(some_number: str) -> bool:
    return some_number == some_number[::-1]

list_of_positive_integers = input().split(', ')

for number in list_of_positive_integers:
    print(palindrome(number))