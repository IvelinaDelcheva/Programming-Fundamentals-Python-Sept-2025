def odd_and_even_sum(some_number: str): 
    odd_sum = 0
    even_sum = 0
    for current_number in some_number:
        if int(current_number) % 2 == 0:
            even_sum += int(current_number)
        else:
            odd_sum += int(current_number)
    return print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')


number = input()
odd_and_even_sum(number)