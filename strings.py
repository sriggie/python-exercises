# Naming cconvections
# 1. Camel-case 
# 2. Snake-case
# 3. Pascal-Case
 
# strings
my_string = "This is my first string"
print(my_string)
print ("python is cool")
print ("5 + 5")

my_string = """this
is 
my
first
string
"""

my_paragraph = """ry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown 
printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, 
but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with 
the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software 
like Aldus PageMaker including versions of Lorem Ipsury. Lorem Ipsum has been the industry's standard dummy text ever 
since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has 
survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It 
was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently 
with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsu"""

print(my_string)

string1  = "Cisco Router"
# EXtract the first character of string1
print(string1[0])
# extract the third character S
print(string1[2])
# extract the r
print(string1[11])
# use negative indexing
print(string1[-2])

# finding how many times acharacter appears in a sequence -> count() method
print(string1.count("T"))

#  Search for a sequence of a character ina astring using the find method
print(string1.find("SCO"))

#  Python returns value -1 when it doeasnt find a match using the find() function
print(string1.find("xyz"))

# Transform a string into uppercase -> upper () method
a = "cisco switch"
print(a.upper())

# Transfer into lower case -> lower () method
a = "CISCO SWITCH"
print(a.lower())
print(a)


# Verify startswith() methods whether a string starts with a particular chaarcter
print(a.startswith("c"))
# Verify endsswith() methods whether a string starts with a particular chaarcter
print(a.endswith("H"))

# strip method - eliminates whiete spaces at the start and ata the end of a string
b = "   Cisco Switch"
print(b.strip())

c = "$$$$$$$$Cisco$$$$$$$$$$$$"
print(b.strip("$"))

# using the replace method that removes  wide spaces ata the beginning at a the end and also at the middle of the string
b = "              Cisco           Switch                        "
print(b.replace("", ""))

# replace letter i with e
i = "Cisco Switch"
print(i.replace("i","e"))

# split() ->
d = "Cisco,Juniper,HP,Nortel,Ayaya,Huawei"
print(d.split(","))

# join() ->
# C$IS$C$O$
a = "Cisco Switch"
x = "_".join(a)
print(x)

x = "x".join(a)
print(x)

# string formatting
First_Name = "Simon"
Second_Name = "Reagan"
age = 21
Full_Name = First_Name + " " + Second_Name
print("my name is " + Full_Name + "-> " + " " + str(age) + " " + " years old")

# 2 format method
print("{} {} {} years old.".format(age,Second_Name, First_Name))

print("{first_Name} {Second_Name} - {u_age} years old."
       .format(u_age=age, first_Name=First_Name, Second_Name=Second_Name))

# 3 f"" or f'' - f-string formatter
print(f"{First_Name} {Second_Name} - {age} years old.")

# string slices (slicing ) -> extracting various parts of a sequence
string2 = " 0 E2 10.110.8.9 [160/5] VIA 10.119.254.6, 10.119.254.6 0:01:00, Ethernet2"

# extract slice 10.110.8.9 -> challange
#  variable_name [start_index : stop_index ]
print(string2[5:14])

#  What if we dont specify the second index
print(string2[5:])

#  what if we dont specify the first index
print(string2[:10])

#  What if we dont enter any index at all ?
print(string2[:])

#  challange -> ethenet -> negative indexes

print(string2[-9:-1])

print(string2[-5:])

print(len(string2)
print(string2[-74:-69])

# step
#  syntax -> variable_name[start:stop:step]

print(string2[::2])

#  Reversing indexing using step
print(string2[::-1])

#  slicing 254
print(string2[50:53])


# write a python programm that asks the user for the names of three people and thn print them out in capital Lettters

full_names = input("Please enter the names of your friends , (no spaces) ,  sepperated by commas").upper()
print(full_names)

full_names.split()