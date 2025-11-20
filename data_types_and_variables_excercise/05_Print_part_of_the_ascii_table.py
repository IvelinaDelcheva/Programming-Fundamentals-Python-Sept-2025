char_index_start = int(input())
char_index_stop = int(input())

for char in range(char_index_start, char_index_stop + 1):
    print(chr(char), end=' ')