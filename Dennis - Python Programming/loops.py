# Python Loops
# 1. For Loop

# create a list of vendors
vendors = ["Cisco", "Hp", "Nortel", "Avaya", "Juniper"]

# display the elements of our list
for each_vendor in vendors:
    print(each_vendor)
    # other statements.....

# Explanation ->

# Iterating over strings
my_string = "Cisco"

for letter in my_string:
    print(letter)
    print(letter * 2)
    print(letter * 3)

# how to use a for loop to iterate over range
for number in list(range(10)):
    print(number * 2)

# what if we want to iterate over a list using list indexes?
# consider vendors list
# lets apply the len() function to our list
print(len(vendors))

# we know that range(5) returns the integers starting with 0 up to, but not including 5, right? Moreover, we can convert this range to a list, using the list() function.
print(list(range(5))) # [0, 1, 2, 3, 4]

# we can look at the elements of this list as being the indexes of each element of our list, vendors. So, the element 'cisco' will be positioned at index 0, 'HP' at index 1 and so on
# This means that if we want to get a list of indexes to iterate over, using a for loop, we can use range(len(vendors)) to obtain that list
# lets create a for-loop that prints out each element of the vendors list by its index

for element_index in list(range(len(vendors))):
    print(vendors[element_index])

# both the index and the element value -> enumerate() function

for index, element in enumerate(vendors, start=1):
    # print(index + 1, element)
    print(index, element)

# 2. while loop
x = 1

while x <= 10:
    print(x)
    x = x + 1
# while loop syntax
# while True:
#     do something

# nested for loop
list1 = [4, 5, 6]
list2 = [10, 20, 30]

for x in list1:
    for y in list2:
        print(x * y)

# Create a mathematics Times Table using a for-loop
for a in list(range(1, 13)):
    print(f"Times Tables For {a}")
    print("=" * 50)
    for b in list(range(1, 13)):
        print(f"{a} X {b} = {a * b}")
        print("-" * 50)
    print("=" * 50)


# break, continue and pass


