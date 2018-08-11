book1 = input()
book1 = book1.lower()

book_list = []

while True:
    line = input()
    if line == 'q':
        break
    book_list.append(line)

if book1 in book_list:
    print('Yes', end=' ')
    print(book_list.index(book1)+1)
else:
    print('No', len(book_list))
