book_name = input()

books_counter = 0
name_of_book = input()
isFound = False
while name_of_book != 'No More Books':
    if name_of_book == book_name:
        isFound = True
        break

    books_counter += 1
    name_of_book = input()
if isFound:
    print(f'You checked {books_counter} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {books_counter} books.')
