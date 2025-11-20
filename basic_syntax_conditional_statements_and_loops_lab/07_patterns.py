number = int(input())

# for star in range(1, number + 1):
#     for star1 in range(0, star):
#         print('*', end='')
#     print()

# for star in range(number - 1, 0, -1):
#     for star1 in range(0, star):
#         print('*', end='')
#     print()

for star in range(0, number + 1):
    print(star * '*')

for star in range(number - 1, 0, -1):
    print(star * '*')