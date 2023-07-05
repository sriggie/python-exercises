# Type conversions
# convert from an integer or floating-point number  to a string -> str() function
num = 2
f = 2.5

# check the type
print(type(num))
print(type(f))

# convert a number to a string
num2 = str(num)
print(num2)
print(type(num2))

# convert a float to a string
f2 = str(f)
print(f2)
print(type(f2))

# backwards -> convert a string to an integer -> using int() method
str1 = "5"
print(type(str1))

int1 = int(str1)
print(type(int1))
print(int1)

# integers to floating-point numbers, using float() function and vice-versa, using the int() function
num3 = 5
f3 = float(num3)
print(f3)
print(type(f3))

# convert a float to integer -> int
f4 = 3.5
num4 = int(f4)
print(num4)

# NB: notice that the int() function on a float will return the integer part of that number

# Now, moving to sequences, lets convert a tuple into a list, using the list() function
tuple1 = (1, 2, 3)
print(type(tuple1))
print(tuple1)
list1 = list(tuple1)
print(type(list1))
print(list1)

# we can also convert a list into a tuple
list2 = [1, 2, 3]
tuple2 = tuple(list2)
print(type(tuple2))
print(tuple2)

# we can also convert a list or tuple into a set
set1 = set(list2)
print(type(set1))
print(set1)

# we can also convert between different numerical representations of numbers, and I am referring to decimal, binary, and hex notations, so base-10, base-2, and base-16 numbers. For this we will need the bin(), hex() and int() functions
num = 200
# convert decimal into binary
num_bin = bin(num)
print(num_bin)

# convert decimal to hex
num_hex = hex(num)
print(num_hex)

# convert binary to hex
bin_to_num = int(num_bin, 2)
print(bin_to_num)

# convert hex to num
hex_to_num = int(num_hex, 16)
print(hex_to_num)

# Next - Conditionals -> if / elif / else