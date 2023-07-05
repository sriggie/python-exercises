# in python, we have the if, elif, and else statements for decision-making
# indented

# create a variable
x = 4

if x > 5:
    print("x is greater than 5")
    print(x * 2)

# handling multiple cases -> else
x = 4
if x > 5:
    print(f"{x} is greater than 5")
else:
    print(f"{x} is NOT greater than 5")

# handling multiple cases -> elif
x = 5
if x > 5:
    print(f"{x} is greater than 5")
elif x == 5:
    print(f"{x} is equal to 5")
else:
    print(f"{x} is NOT greater than 5")


# write a python program that checks if temperature is greater than or less than or equal to 23. if it is greater than 23 then tell the user to cover tomatoes, if it is less than 23 tell the user to uncover tomatoes and if it is equal to 23, tell the user to enjoy a fruit.

temp = 22

if temp > 23:
    print("Its Hot, Cover Your Tomatoes")
elif temp == 23:
    print("Please do enjoy a fruit!")
elif temp < 23:
    print("Uncover Your Tomatoes")

user_age = int(input("Please Enter Your Age: "))

if user_age > 18:
    print("You can enjoy the party!!!")
elif user_age == 18:
    print("You are Lucky this time, just enjoy the Party!!!")
elif user_age < 18:
    print("You are still an underage, you cannot go to party")

# write a python program to check if a number is equal to 5 and also if that number is indeed an integer. e.g if it is true, then print -> "x is equals to 5 and is an integer" otherwise, print -> "x is an integer, but is not equal to 5"

user_int = int(input("Please provide an integer: "))

if user_int == 5 and type(user_int) == int:
    print(f"{user_int} is equals to 5 and is an integer")
elif user_int != 5 and type(user_int) == int:
    print(f"{user_int} is not equals to 5 but is an integer")
else:
    print("Sorry, You must enter an integer")


# Next -> Python Loops -> For/while loops -> for-loop