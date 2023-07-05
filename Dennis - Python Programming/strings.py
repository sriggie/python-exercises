# Naming Conventions
# 1. Camel-case
# 2. snake-case
# 3. pascal-case

# Strings
my_string = "This is my first string"
# print(my_string)
# print("Python Programming is Cool")
# print(5 + 5)

my_string = """This
is
my
first
string.
"""
# print(my_string)

string1 = "Cisco Router"

# Find the length of string1
print(len(string1))
# print(string1[20])

# Finding the index of a character in a string -> index() function
print(string1.index("c"))
print(string1.index("t"))

# finding how many times a character appears in sequence -> count() method
print(string1.count("T"))

# Search for a sequence of characters in a string/sequence -> find() method
print(string1.find("sco"))

# python returns value -1 if it doesn't find a match using the find() function
print(string1.find("xyz"))

# Transform a string into Uppercase -> upper() method
a = "Cisco Switch"
print(a.upper())

# Transform a string into lowercase -> lower() method
print(a.lower())

print(a)

# startswith() methods verifies whether a string starts with a particular character
print(a.startswith("c"))

# endswith() methods verifies whether a string ends with a particular character
print(a.endswith("H"))

# strip() method - eliminates white spaces at the start and end of a string
b = "    Cisco Switch        "
print(b.strip())
print(b)

c = "$$$$$Cisco Switch$$$$$$$$"
print(c.strip("$"))

# replace() method -> removes white spaces at the beginning, the end and also inside a string
b = "    Cisco Switch        "
print(b.replace(" ", ""))

# split() ->
d = "Cisco,Juniper,Hp,Nortel,Avaya,Huawei"

print(d.split(","))

# join() ->
# c_i_s_c_o__s_w_i_t_c_h
a = "Cisco Switch"
print("_".join(a))

x = "*".join(a)
print(x)

# String Formatting (Concatenation)

# 1. + operator
firstName = "Dennis"
secondName = "Muthui"
age = 18
fullName = firstName + " " + secondName + " - " + str(age) + " years old."
print(fullName)

# 2. format()
print("{} {} - {} years old.".format(age, secondName, firstName))
print("{first_name} {last_name} - {u_age} years old."
      .format(u_age=age, first_name=firstName, last_name=secondName))

# 3. f"" or f'' - f-string formatter
print(f"{firstName} {secondName} - {age} years old.")

# String Slices (Slicing) -> Extracting various parts of a sequence
string2 = "0 E2 10.110.8.9 [160/5] via 10.119.254.6, 10.119.254.6, 0:01:00, Ethernet2"

# extract/slice 10.110.8.9 -> Challenge
# print("10.110.8.9")
# variable_name[ start_index : stop_index ]
print(string2[5:15])

# What if we don't specify the second index?
print(string2[5:])

# What if we don't specify the first index?
print(string2[:10])

# What if we don't enter any index at all?
print(string2[:])

# challenge -> Ethernet -> negative indexes
print(string2[-9:-1])

# challenge -> using -ve indexes -> extract "rnet2"
print(string2[-5:])

# challenge -> extract the first 5 elements
print(len(string2))
print(string2[:5])

# step
# syntax -> variable_name[start:stop:step]
print(string2[::2])

# Reverse a string using a step
print(string2[::-1])


