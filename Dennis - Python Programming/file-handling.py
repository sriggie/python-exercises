import json

# open() -> used for openning files in python
# takes two parameters -> file_name and mode
# open(books.txt, 'w')

# we have several modes for opening files with
# 1. read -> 'r' - reading a file -> returns an error if the file you are opening to read doesn't exist
# 2. write -> 'w' - writing to a file -> creates the file if it doesn't exist -> it overwrites the existing data
# 3. append -> 'a' - appending to a file -> creates the file if it doesn't exist
# 4. delete -> 'x' - delete a file

# write to file -> 'a' append mode
# my_file = open('my_file.txt', 'a')
# user_name = "dennisCreatives"
# password = "p@$$w0rd"
# my_file.write(user_name + "\n")
# my_file.write(password + "\n")
# my_file.close()

# write to file -> 'w' write mode
# my_file = open('my_file.txt', 'w')
# user_age = 20
# my_file.write(f"{user_age}\n")
# my_file.close()

# read a file -> 'r' read mode
# file = open('my_file.txt', 'r')
# contents = file.read()
# file.close()
# print(contents)

# opening files using context managers
# with open('file_name', 'mode') as f:
#     do something

# with open('my_file.txt', 'a') as f:
#     username = input("Enter your user name: ")
#     password = input("Enter Your Password Too: ")
#     f.write(username + '\n')
#     f.write(password + '\n')

# with open('my_file.txt', 'r') as f:
#     file_contents = f.read()
#     print(file_contents)

    # 1. Write a python script which queries the user for input (infinite loop with exit possibility) and then writes to a file.
# running = True
#
# while running:
#     print("Choose From The Menu")
#     print("1. Add Input")
#     print("Q. Quit")
#     user_choice = input("Enter Your Choice: ")
#     if user_choice == '1':
#         data_to_store = input("Please Provide Your Input: ")
#         with open('sample.txt', 'a') as f:
#             f.write(data_to_store)
#             f.write("\n")
#     elif user_choice == 'Q':
#         running = False


# 2. Add another option to your UI (user interface): The user should be able to output data stored in the file in the terminal readLines()
# running = True
#
# while running:
#     print("Choose From The Menu")
#     print("1. Add Input")
#     print("2. Output File Data")
#     print("Q. Quit")
#     user_choice = input("Enter Your Choice: ")
#     if user_choice == '1':
#         data_to_store = input("Please Provide Your Input: ")
#         with open('sample.txt', 'a') as f:
#             f.write(data_to_store)
#             f.write("\n")
#     elif user_choice == '2':
#         with open('sample.txt', 'r') as f:
#             file_contents = f.read()
#             print(file_contents)
#     elif user_choice == 'Q':
#         running = False

    # 3. Store the user input in a list (instead of directly adding it to a file) and write that list to the file - using pickle and json

running = True
user_input_list = []

while running:
    print("Choose From The Menu")
    print("1. Add Input")
    print("2. Output File Data")
    print("Q. Quit")
    user_choice = input("Enter Your Choice: ")
    if user_choice == '1':
        data_to_store = input("Please Provide Your Input: ")
        user_input_list.append(data_to_store)
        with open('sample.txt', 'w') as f:
            f.write(json.dumps(user_input_list))
    elif user_choice == '2':
        with open('sample.txt', 'r') as f:
            file_contents = json.loads(f.read())
            for line in file_contents:
                print(line)
    elif user_choice == 'Q':
        running = False