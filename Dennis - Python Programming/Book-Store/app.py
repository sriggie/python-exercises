from utils import database

# user choices
USER_CHOICE = """
Enter:
-> 'a' to add a new book
-> 'l' to list all the books
-> 'r' to mark a book as read
-> 'd' to delete a book
-> 'q' to quit

Enter Your Choice: """


# create the menu function
def menu():
    user_choice = input(USER_CHOICE)
    # deal with the user's choice
    while user_choice != 'q':
        if user_choice == 'a':
            prompt_add_new_book()
        elif user_choice == 'l':
            list_books()
        elif user_choice == 'r':
            prompt_mark_book()
        elif user_choice == 'd':
            prompt_delete_book()
        else:
            print("Invalid Choice, Please try again!!!")
        user_choice = input(USER_CHOICE)


# create a function to prompt the user to add a new book (name, author)
def prompt_add_new_book():
    name = input("Enter The Name Of The New Book: ")
    author = input("Enter The Author Of The New Book: ")
    database.add_book(name, author)


# create a function to show all the books
def list_books():
    books = database.get_all_books()
    for book in books:
        read = "Yes" if book['read'] == "1" else "No"
        print(f"{book['name']} written by {book['author']}, Read Status: {read}")


# create a function to mark a book as read
def prompt_mark_book():
    name = input("Enter the name of the book you've finished reading: ")
    database.mark_book_as_read(name)


# create a function to delete a book
def prompt_delete_book():
    name = input("Enter the name of the book you'd like to delete: ")
    database.delete_book(name)


menu()
