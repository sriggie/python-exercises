# create an empty list
list1 = [2, 9, "python"]

# check the length of the list
print(len(list1))

# check the type of the list
print(type(list1))

# lets populate our list
list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]

# you can also access elements of a list as you did with string, using indexes
# access the second element -> Juniper
print(list1[1]) # returns juniper


# access the last element using -ve index


print(list1[-1])

# indexError
# print(list1[100])

# change avaya to HP
list1[5] = "HP"

# LISTS METHODS
list2 = [-11, 2, 12]

# min() -> returns the smallest number within list elements
print(min(list2))

# max() -> returns the largest number within a list
print(max(list2))

# create a list of strings
list3 = ["a", "b", "c"]
print(min(list3))

print(max(list3))
list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]
# print(max(list1))

print(max(["John", "Junet", "Julius", "Justus"]))

# appending an element into a list -> append()
list1.append(100)

# deleting elements from a list
# 1. del command/keyword -> removes an element using its index
del list1[2]

# 2. pop() -> another way to remove an element by its index
list1.pop(0)

# 3. remove() -> removes an element by specifying the element itself
list1.remove(10.5)

# insert an element at a particular index -> insert()
list1.insert(2, "Nortel")

# appending a list to another list -> extend() method
list4 = [9, 99, 999]

list1.extend(list4)

# find the index of an element in a list -> index() method
print(list1.index(-11))

# find the occurrences of an element in a list -> count() method
list1.append(10)
list1.append(10)
list1.append(10)

print(list1.count(10))

# sorting list elements
# 1. sort() method
list2.append(1)
list2.append(25)
list2.append(500)

# sort in asc
list2.sort()
print(list2)

# 2. reverse() - reverses the order
list2.reverse()
print(list2)

# 3. sorted() -> sorts a list and creates a new list in place
my_new_list = sorted(list2)
print(my_new_list)

new_list = sorted(my_new_list, reverse=True)
print(new_list)

# concatenating lists -> plus operator -> '+'
print(list1 + list2)

# repeat a list -> multiplication operator -> '*'
print(list2 * 5)

# print the contents of our list
print(list1)

# LIST SLICES
# create a new list
list5 = [1, 2, 3, 'a', 'b', 'c']

# 1. extract the first three elements(use 2 ways
# 2. extract [3, 'a', 'b']
# 3. extract [1, 2, 3, 'a', 'b', 'c']
# 4. using -ve indexes, extract [3, 'a', 'b']
# 5. using -ve indexes, extract ['a', 'b', 'c']
# 6. using -ve indexes, extract [1, 2, 3]
# 7. use a step to extract [1, 3, 'b']
# 8. use a step to reverse the list ['c', 'b', 'a', 3, 2, 1]

# Exercise 1
# Write a python program that asks a student for their name and marks for 5 units/subjects. Store the name and marks in a user-defined list. Then output the average mark of the student in a nice format.

# solution
# prompt the user for the student name
studentName = input("Please enter the student names: ")

# prompt the user for the student marks for each subject
maths = int(input("Enter marks for Maths: "))
english = int(input("Enter marks for English: "))
kiswahili = int(input("Enter marks for Kiswahili: "))
science = int(input("Enter marks for Science: "))
SST = int(input("Enter marks for Social Studies: "))

# store the student name and marks in a list
# create an empty list
studentList = []

# method 1: saving the list elements
# studentList = [studentName, maths, english, kiswahili, science, SST]

# method 2:
studentList.append(studentName)
studentList.append(maths)
studentList.append(english)
studentList.append(kiswahili)
studentList.append(science)
studentList.append(SST)

# total score
# method 1:
# totalScore = studentList[1] + studentList[2] + studentList[3] + studentList[4] + studentList[5]
# method 2:
studentMarks = studentList[1:]

# calculate the average score
# averageScore = totalScore / 5
# averageScore = (studentMarks[0] + studentMarks[1] + studentMarks[2] + studentMarks[3] + studentMarks[4]) / 5

averageScore = sum(studentMarks) / len(studentMarks)

# display the student name and average score
print(f"Hello {studentList[0]}, You did {len(studentMarks)} subjects, and scored {averageScore}%")

