# create an empty list to store our books
books = []


# TO DO
# create a path to our file to save our books in it


# function to add books
def add_books(title, author):
    books.append({
        'title': title,
        'author': author,
        'read_status': False
    })


# function to list all books
def list_all_books():
    for book in books:
        read = "Yes" if book['read_status'] is True else "No"
        print(f"{book['title']} written by {book['author']}, Read: {read}")


# function to mark a book as read
def mark_book_as_read(title, author):
    for book in books:
        if book['title'].lower() == title.lower() and book['author'] == author.lower():
            book['read_status'] = True


# function to save all the book (helper function)
def _save_books():
    pass


# function to delete a book
def delete_a_book(title):
    for book in books:
        if book['title'].lower() == title.lower():
            books.remove(book)
