# numbers

num1 = 10
num2 = 2.5

# check the data types of the variables using type() function
print(type(num1))
print(type(num2))

# Operations you can perform using integers and floating-point numbers
# 1. Arithmetic Operations
# Addition -> '+' e.g 3 + 7
print("The sum is: " + str(3 + 7))

# Subtraction -> '-' e.g 3 - 7
print("The sub is: " + str(3 - 7))

# Division -> '/' e.g 3 / 7
print("The Quotient is: " + str(3 / 7))

# Multiplication -> '*' 3 * 7
print("The Product is: " + str(3 * 7))

# Raising to a power -> '**' e.g 3 ** 7
print("The power is: " + str(3 ** 7))

# Modulo -> '%' (this means finding out the remainder after the division of one number by another) e.g 20 % 6
print("The Modulo is: " + str(3 % 7))

# 2. Comparison Operators
# > - greater than
print(3 > 4)
# < - less than
print(3 < 4)
# >= - greater than or equal to
print(3 >= 4)
# <= - less than or equal to
print(3 <= 4)
# == - equal to
print(3 == 4)
# != - not equal to
print(3 != 4)

# Order of Evaluation
# 1. Raising to a power operation has the highest priority
# 2. Multiplication, Division and Modulo operations with equal priorities
# 3. Addition and Subtraction with equal priorities

100 - 5 ** 2 / 5 * 2

# conversions
# Python has two functions available for these operations
# 1. int() -> converts to an integer
print(int(1.99999999))

# 2. float() -> converts to a float
print(float(2))
print(float(1.99999999))

# abs() -> find the absolute value. This is the distance between the number we provide and 0
print(abs(5)) # returns 5
print(abs(-10))

# max() -> returns the largest number between two numbers
print(max(2, 4))

# min() -> returns the smallest number between two numbers
print(min(-2, -4))

# pow(a, b) -> power of a number : where 'a' is the base number and 'b' is the exponent/power
print(pow(10, 4))
print(10 ** 4)

# write a python program that captures user age and then returns the decades they've lived e.g 19 years = 1 decade
# user_name = input("Please enter your name: ")
# user_age = int(input("enter your age too: "))
# decades = user_age // 10  # integer division
# s = "s" if decades > 1 else ""
# print(f"Hello, {user_name}, You have lived for {decades} decade{s}")

# age in minutes
user_name = input("Please enter your name: ")
user_age = int(input("enter your age too: "))
age_in_minutes = 365.25 * 24 * 60 * user_age
print(f"Hello, {user_name}, You have lived for {age_in_minutes} minutes")

# create a python program that calculates the acceleration of an object whose initial velocity, final velocity, initial time and final time is 0, 20, 0 and 10 resp.
# solution
# create 5 variables
t1 = 0
t2 = 20
v1 = 0
v2 = 10
# compute the acceleration
acceleration = (v1 - v2) / (t1 - t2)
# display the computed acceleration
print(f"Acceleration is: {acceleration}")