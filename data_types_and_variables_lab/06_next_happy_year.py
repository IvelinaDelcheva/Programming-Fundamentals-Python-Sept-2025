year = int(input())

while True:
    
    year += 1

    current_year_as_str = str(year)

    if len(set(current_year_as_str)) == len(current_year_as_str):
        print(current_year_as_str)
        break

    # happy_year = ''

    # for digit in current_year_as_str:
    #     if digit not in happy_year:
    #         happy_year += digit
    
    # if len(happy_year) == len(current_year_as_str):
    #     print(happy_year)
    #     break










