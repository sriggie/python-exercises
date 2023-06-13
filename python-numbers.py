 # numbers
num1 = 10
num2 = 2.5

# check the data types of the variables using type() function
print(type(num1))
print((type(num2)))

 # operations you can perfom using integers and floating-point numbers
 # 1. Arithmetic operations
 #  Addition -> '+' e.g 3 + 7
print("The sum is: " + str( 3 + 7 ))
# subtraction -> '-' e,g 3-7
print("The sub is:" + str(3 -7 ))
#  Division -> '/' e.g 3/7
print ("The quotient is: " + str(3 / 7))
#  Multiplication '*' e.g 3 * 7
print ("The product is :" + str( 3* 7))
#  Raising to a power -> '**' e.g 3 ** 7
print("The product is : " + str(3**7))
#  Modulo -> '%' (this means finding out the remainder after the division of one number by another) e.g 20%6
print("The modulo is : " + str(3 % 7))

#  conversions
# 1. int() -> converts to an integer
print(int(1.7))

# 2. float() -> converts to a float
print(float(1.55555))

# 3. abs() -> find the absolute value. This is the distance between the number we provide and 0
print(abs(-10))

# 4. max() -> returns the largest number between two numbers
print(max(2 , 4))
#  . min () -> returns the smallest number
print(min(-2 , -4))

# 5. pow(a , b) -> power of a number : where 'a' is the base number and 'b'
print(pow(5 , 10))



# 2. Comparison Operators
#  > greater than
print(3>4)
# < less than
print((3>4))
# >= greater than or equal to
print(3>=4)
#  == equal to
print(3 == 4)
#  != not equal to
print(3 != 4)


#  create a python program that calculates the salary of an employee. (staffID ,  name , workingHoursData, HourlyRtae, WorkingdDays, totalLeaveToken)

#  create all the variable for our program

empNumber = input("Enter Your Employee Number: ")
print("=" * 60)

emName = input("Enter your full names: ")
print("=" * 60)

workingHoursPerDay = float(input("Entre Your Working hours in a day: "))
print("=" * 60)

HourlyRate = float(input("Entre your hourly rate: "))
print("=" * 60)

workingDays = int(input("Enter your working days: "))
print("=" * 60)

#  workingDays = int(input("Enter your working Days"))
totalDays = int(input("Entre Your total working Days: "))
print("=" * 60)

totalLeaveTaken = int(input("Enter your total number of leave Days: "))
print("=" * 60)

#  program to calculate the employees salary
workingDays = totalDays - totalLeaveTaken
salary = workingDays * workingHoursPerDay * HourlyRate

#  Display the employees total paysli[p
print(f" {empNumber} {emName} has worked for {workingDays} days")
print("=" * 60)
print(f"Basic Salary: {salary}")
print("=" * 60)

