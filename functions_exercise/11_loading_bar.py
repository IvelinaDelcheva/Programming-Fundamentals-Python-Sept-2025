def loading_bar(num: int):
    if num == 100:
      return '100% Complete!\n[%%%%%%%%%%]'

    loaded = (num // 10) 
    return f"{num}% [{'%' * loaded}{'.' * (10 - loaded)}]\nStill loading..."

number = int(input())
result = loading_bar(number)
print(result)

