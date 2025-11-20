string_of_integer = input().split(', ')
count_of_beggars = int(input())
list_with_money = []

for number in string_of_integer:
    money = int(number)
    list_with_money.append(money)

list_with_total_sum_for_beggar = []
start_index = 0

for beggar in range(count_of_beggars):
    sum = 0
    for index in range(beggar, len(list_with_money), count_of_beggars):
        sum += list_with_money[index]
    
    list_with_total_sum_for_beggar.append(sum)

print(list_with_total_sum_for_beggar)