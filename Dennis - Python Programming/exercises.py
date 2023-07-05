# 1. Create a list of names of your classmates and use a for loop to output the length of each name
names = ['Fridah', 'Simon', 'Ian', 'Joe', 'Divin', 'Milton', 'Michael', 'Sheema', 'Desta', 'francis', 'Alex', 'Anne', 'Risper', 'Elvis', 'Lloyd', 'Joy', 'Alfred', 'Dennis']

# for name in names:
#     print(name)
#     print(len(name))

for name in names:
    print(f"The length of {name} is: {len(name)}")
print("=" * 50)
# 2. Add an if-statement inside the loop to only output names longer than 5 characters long
for name in names:
    if len(name) > 5:
        # print(name)
        print(f"{name}'s length is greater than 5 chars and it has: {len(name)} characters.")


print("=" * 50)

# 3. Add another if check to see whether a name includes a 'n' or 'N' character
for name in names:
    if len(name) > 5 and ('N' in name or 'n' in name):
        print(name)

print("=" * 50)
# 4. use a while loop to empty the list of names
while len(names) >= 1:
    print(names.pop())

# print(names)

print("=" * 50)

# create a python program that iterates over a string using a for loop and adds the letters to a list
# my_list = []
# my_name = "dennis"
#
# for letter in my_name:
#     my_list.append(letter)
#
# print(my_list)

# list Comprehension
my_name = "dennis"
my_list = [letter for letter in my_name]
print(my_list)

print("=" * 50)

# 1. Create a list of "person" dictionaries with a name, age, and a list of hobbies for each person. Fill in any data you want.
people = [
    {
        'name': 'Sheema',
        'age': 21,
        'hobbies': ['dancing', 'singing', 'coding']
    },
    {
        'name': 'Alex',
        'age': 22,
        'hobbies': ['cooking', 'basketball']
    },
    {
        'name': 'Reagan',
        'age': 21,
        'hobbies': ['swimming', 'eating', 'sleeping', 'coding']
    },
    {
        'name': 'Francis',
        'age': 23,
        'hobbies': ['swimming', 'eating','coding']
    }
]

print(people)

print("=" * 50)
# 2. use list comprehension to convert this list of persons into a list of names(of the person)
people_names = [person['name'] for person in people]
print(people_names)

print("=" * 50)
# 3. Use list comprehension to check whether all persons are older than 20 years old

# are_older = [person['name'] for person in people if person['age'] > 20]
# print(are_older)

are_older = [person['age'] > 20 for person in people]
print(are_older)


print("=" * 50)
# 4. Copy the person list such that you can safely edit the name of the first person (without changing the original list)

# copied_people = people[:]
# copied_people["name"] = "Sheemah"
# copied_people[0] = "name": "Sheemah"
# copied_people[0]['name'] = "Shamil"
# print(copied_people)

copied_people = [person.copy() for person in people]
copied_people[0]['name'] = 'Sheema Shamil'

print(copied_people)
print(people)


print("=" * 50)

# 5. Unpack the persons of the original list into different variables and output these variables

# This is indexing NOT unpacking
# p1 = people[0]
# p2 = people[1]
# p3 = people[2]
# p4 = people[3]
#
# print(p1)
# print(p2)
# print(p3)
# print(p4)

# This is unpacking
p1, p2, p3, p4 = people

print(p1)
print(p2)
print(p3)
print(p4)

print("=" * 50)


# Challenge Solution
# create 2 variables -> user_password and correct_password
# use a loop
is_correct = True

correct_password = "secret"
user_password = input("Enter Password: ")

while is_correct:
    if user_password == correct_password:
        print("Logged In Successfully!")
        is_correct = False
    else:
        print("Invalid Password, Please Try Again!!!")

        user_password = input("Enter Password: ")




