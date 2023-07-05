import sqlite3


# create a function to create books table
def create_table():
    connection = sqlite3.connect('bookstore.db')
    cursor = connection.cursor()
    query = "CREATE TABLE IF NOT EXISTS books (name TEXT PRIMARY KEY NOT NULL UNIQUE, author TEXT, read INTEGER)"
    cursor.execute(query)
    connection.commit()
    connection.close()


# create a function that adds a book to our file
def add_book(name, author):
    connection = sqlite3.connect('bookstore.db')
    cursor = connection.cursor()
    insert_query = "INSERT INTO books VALUES(?, ?, ?)"
    cursor.execute(insert_query, (name, author, 0))
    connection.commit()
    connection.close()


# create a function that displays/shows all the books to the user
def get_all_books():
    connection = sqlite3.connect('bookstore.db')
    cursor = connection.cursor()
    select_query = "SELECT * FROM books"
    cursor.execute(select_query)

    books = [
        {'name': book[0], 'author': book[1], 'read': book[2]}
        for book in cursor.fetchall()
    ]

    connection.close()
    return books


# create a function that marks a book as read -> change 0 to 1
def mark_book_as_read(name):
    connection = sqlite3.connect('bookstore.db')
    cursor = connection.cursor()
    # check for the book in the db
    book = cursor.execute("SELECT * FROM books WHERE name = ?", (name, ))
    # if book is in db ->
    if book.fetchone():
        # update it
        update_query = "UPDATE books SET read = ? WHERE name = ?"
        cursor.execute(update_query, (1, name))
    else:
        # otherwise -> raise an error
        print("No Such Book In Your Collection!")
    connection.commit()
    connection.close()


# create a function to delete a book
def delete_book(name):
    connection = sqlite3.connect('bookstore.db')
    cursor = connection.cursor()
    delete_query = "DELETE FROM books WHERE name = ?"
    cursor.execute(delete_query, (name,))
    connection.commit()
    connection.close()


def count_books():
    connection = sqlite3.connect('bookstore.db')
    cursor = connection.cursor()
    cursor.execute("SELECT count(*) FROM books")
    count = cursor.fetchall()
    connection.close()
    return count[0][0]
