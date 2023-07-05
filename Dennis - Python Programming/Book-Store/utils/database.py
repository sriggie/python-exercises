# create a file
file_path = "books.txt"


# create a function that adds a book to our file
def add_book(name, author):
    with open(file_path, 'a') as file:
        file.write(f"{name},{author},0\n")
        print(f"Book with the name {name}, created successfully!")


# create a function that displays/shows all the books to the user
def get_all_books():
    with open(file_path, 'r') as file:
        all_books = [book.strip('\n').split(',') for book in file.readlines()]

        return [
            {'name': book[0], 'author': book[1], 'read': book[2]}
            for book in all_books
        ]


# create a function that marks a book as read -> change 0 to 1
def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = "1"
    _save_all_books(books)


# create a helper function to save all the books
def _save_all_books(books):
    with open(file_path, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


# create a function to delete a book
def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)
