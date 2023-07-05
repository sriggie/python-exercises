import random

# Functions
# syntax
# def function_name(<optional params>):
#     do something

# invoking/calling a function -> write the name of the function followed by parenthesis

def greetUser():
    print("Hello Everyone!!!")

# greetUser()

def greetUserName():
    name = "Dennis"
    print(f"Hello {name}.")

# greetUserName()

# parameters -> a value you pass into a function
# a param is a variable you pass into a function definition

# param -> user_name

def my_function(user_name):
    greetings = f"Greetings {user_name}"
    print(greetings)


# argument
# my_function("Dennis")


def addTwoNumbers(num1, num2, num3):
    result = num1 + num2 + num3
    print(f"The result is: {result}")


# addTwoNumbers(6, 7, 8)

# return -> returns a value and terminates the function


def favoriteColor(color):
    return color


# print(favoriteColor("Blue"))
# favColor = favoriteColor("Red")
# print(favColor)


def square_of_a_number(base, exp):
    sq = base ** exp
    return sq


# print(square_of_a_number(2, 10))
# print(square_of_a_number(3, 10))
# print(square_of_a_number(4, 10))
# print(square_of_a_number(5, 10))

def area_of_a_circle(radius):
    area = 22 / 7 * (radius ** 2)
    return area

# print(area_of_a_circle(7))
# print(area_of_a_circle(15))


# challenge Solution
def get_user_name():
    user_name = input("Please Enter Your Name: ")
    return user_name


def get_user_age():
    user_age = int(input("Enter Your Age Too: "))
    return user_age


def get_user_age_in_seconds(age):
    age_in_seconds = age * 365.25 * 24 * 60 * 60
    return age_in_seconds


def get_user_decades(age):
    user_decades = age // 10
    return user_decades


def print_user_info():
    user_name = get_user_name()
    user_age = get_user_age()
    age_in_seconds = get_user_age_in_seconds(user_age)
    user_decades = get_user_decades(user_age)
    print(f"Hello {user_name}, You have lived for {user_decades} decades and {age_in_seconds} seconds")


# print_user_info()

# solution to challenge 1
def difference(alist):
    return max(alist) - min(alist)

print(difference([45, 67, 90, 2, 5, -34]))

# solution to challenge 2
def largerst_odd_number(numbers):
    odds_list = []
    for number in numbers:
        if number % 2 == 1:
            odds_list.append(number)
    return max(odds_list)


numbers = [23, 34, 67, 89, -34, 3, 9]
print(largerst_odd_number(numbers))

# while (len(numbers) <= 100):
#     numbers.append(random.randint(1, 100))
# print(numbers)
# print(largerst_odd_number(numbers))

print(random.randint(1, 5))

