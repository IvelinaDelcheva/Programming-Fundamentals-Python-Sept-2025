def perfect_number(some_number: int):
    aliquot_sum = 0
    for number in range(1, some_number):
        if some_number % number == 0:
            aliquot_sum += number
    
    if aliquot_sum == some_number:
        return 'We have a perfect number!'
    else:
        return 'It\'s not so perfect.'
    

number = int(input())
print(perfect_number(number))





