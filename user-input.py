studentName = input("entre your full names : ")
maths = int(input("Enter score in maths"))
eng = int(input("Enter score in English"))
sci = int(input("Enter score in Science"))
kisw = int(input("Enter score in Kiswahili"))
sst = int(input("Enter score in Social Studies "))

# store the student data inside a list
studentList = [studentName, maths, eng, sci, kisw, sst]

#  total score method1
studentMarks = studentList[1] + studentList[2] + studentList[3] + studentList[4] + studentList[5]
#  total score method 2

#  calculate the total score
print(studentMarks)



#  calculate the average score
averagescore = studentMarks/ 5


print(averagescore)

# write a python program that captures users age and the returns the decades theyeve lived e.g 19 years = 1 decade
#
# username = input("What is your full name : ")
# userAge = int(input("How old are you : "))
# decades = userAge // 10
# s = "s" if decades > 1 else ""
#
# print(f"Hello ,  {username} , you have lived for {decades} deacades {s}")

#  write a python program that prompts a user for their age and then retruns the minutes theyve lives
user_name = input("please enter your name : ")
user_age = int(input("Please enter your age : "))
years = user_age
days = user_age * 365
hours = user_age * 8760.25
space = "->"
print(f" hello {user_name} {space} you have lived for {hours} hours " )