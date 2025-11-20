factor = int(input())
count = int(input())

factorial_list = [index * factor for index in range(1, count + 1)]

# for index in range(1, count + 1):
#     result = factor * index
#     factorial_list.append(result)

print(factorial_list)

