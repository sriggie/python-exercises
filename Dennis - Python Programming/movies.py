# create an empty list to store the movies
movies = []


# create a function to add the movies into our list
def add_movies():
    title = input("Enter The Movie Title: ")
    director = input("Enter The Movie Director: ")
    release_year = input("Enter The Movie release Year: ")

    # add the movie info to a dictionary and append it to the movies list
    movies.append({
        'title': title,
        'director': director,
        'year': release_year
    })


# create a function to show all movies
def list_movies():
    if len(movies) is 0:
        print("You Don't have any Movies at the moment")
    else:
        for movie in movies:
            print_movie(movie)


# create a function to find a movie
def find_movie():
    title = input("Enter the title of the movie you wish to search: ").lower()
    for movie in movies:
        if movie['title'].lower() == title:
            print_movie(movie)


# TO DO
# create a helper function to output a movie in a nice format
def print_movie(movie):
    print(f"{movie['title']} directed by {movie['director']}, released: {movie['year']}")

# prompt the user to choose from the menu options
MENU_PROMPT = "\nEnter \n'a' to add a movie, \n'l' to see your movies, \n'f' to find a movie by title or \n'q' to quit\nYour Choice: "


# create the menu function
def menu():
    # create a var to store the user choice
    selection = input(MENU_PROMPT)

    # loop as long as selection is not equal to 'q'
    while selection != 'q':
        if selection == 'a':
            add_movies()
        elif selection == 'l':
            list_movies()
        elif selection == 'f':
            find_movie()
        else:
            print("Invalid Command, Please Try Again!!!")
        selection = input(MENU_PROMPT)

# call the menu function
menu()
