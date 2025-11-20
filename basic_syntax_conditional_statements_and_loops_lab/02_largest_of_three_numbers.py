first_num, secon_num, third_num = int(input()), int(input()), int(input())

if first_num > secon_num and first_num > third_num:
    print(first_num)
elif secon_num > first_num and secon_num > third_num:
    print(secon_num)
elif third_num > first_num and third_num > secon_num:
    print(third_num)

# or
# print(max(first_num, secon_num, third_num))

