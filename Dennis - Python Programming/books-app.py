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
            prompt_add_book()
        elif user_choice == 'l':
            show_books()
        elif user_choice == 'r':
            prompt_mark_book()
        elif user_choice == 'd':
            prompt_delete_book()
        else:
            print("Invalid Choice, Please try again!!!")
        user_choice = input(USER_CHOICE)


# create a function to prompt the user to create a book
def prompt_add_book():
    title = input("Enter The Title of The New Book: ")
    author = input("Enter The Author of The New Book: ")
    database.add_books(title, author)


def show_books():
    database.list_all_books()


def prompt_mark_book():
    title = input("Enter The Title of the book You've finished Reading: ")
    author = input("Enter The Author of the book You've finished Reading: ")
    database.mark_book_as_read(title, author)


def prompt_delete_book():
    title = input("Enter the title of the book you wish to delete: ")
    database.delete_a_book(title)


menu()
