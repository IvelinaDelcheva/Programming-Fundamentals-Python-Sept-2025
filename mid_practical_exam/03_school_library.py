shelf_with_books = input().split('&') 

while True:
    input_line = input()

    if input_line == 'Done':
        break

    command = input_line.split(' | ')[0]
    if command == 'Add Book':
        book_name = input_line.split(' | ')[1]
        if book_name not in shelf_with_books:
            shelf_with_books.insert(0, book_name)
    elif command == 'Take Book':
        book_name = input_line.split(' | ')[1]
        if book_name in shelf_with_books:
            shelf_with_books.remove(book_name)
    elif command == 'Swap Books':
        book_1 = input_line.split(' | ')[1]
        book_2 = input_line.split(' | ')[2]

        if book_1 in shelf_with_books and book_2 in shelf_with_books:
            book_1_index = shelf_with_books.index(book_1)
            book_2_index = shelf_with_books.index(book_2)

            shelf_with_books[book_1_index], shelf_with_books[book_2_index] = shelf_with_books[book_2_index], shelf_with_books[book_1_index]

    elif command == 'Insert Book':
        book_name = input_line.split(' | ')[1]
        if book_name not in shelf_with_books:
            shelf_with_books.append(book_name)

    elif command == 'Check Book':
        index = int(input_line.split(' | ')[1])
        if index in range(len(shelf_with_books)):
            print(shelf_with_books[index])

print(', '.join(shelf_with_books))