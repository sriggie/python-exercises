# Tuples -> ordered collection of non-unique elements, meaning indexes and duplicates are allowed
my_tuple = ()
print(type(my_tuple))

# NB -> if you have a tuple with one element, put a comma after the element
my_tuple = (9)
my_tuple2 = (9,)
print(type(my_tuple))
print(type(my_tuple2))

# lets populate my_tuple
my_tuple = (1, 2, 3, 4, 5)

# access the first element of our tuple
print(my_tuple[0])
# access the second element of our tuple
print(my_tuple[1])
# access the third element of our tuple
print(my_tuple[2])
# access the fourth element of our tuple
print(my_tuple[3])
# access the fifth element of our tuple
print(my_tuple[4])

# check whether tuples ar immutable
# my_tuple[1] = 10

# removing elements is not permitted when working with tuples
# del my_tuple[0]

# tuple assignment -> assigning a tuple of variables to a tuple of values
tuple1 = ("Cisco", "2600", "12.4")
(vendor, model, ios) = tuple1
print(vendor)
print(model)
print(ios)

tuple2 = (1, 2, 3, 4)
(p, x, y, z) = tuple2
print(x)
print(y)
print(z)

# assigning values in a tuple to variables in another tuple
(a, b, c) = (10, 20, 30)
print(a)
print(b)
print(c)

########## TUPLES METHODS ############

# len() function
print(len(tuple2))

# min() and max() functions available fpr finding the lowest and greatest values inside a tuple
print(min(tuple2))
print(max(tuple2))

# we can also concatenate and .....
print(tuple2 + (5, 6, 7))

# ..... multiply a tuple
print(tuple2 * 3)

# slicing
tuple2 = (1, 2, 3, 4)

print(tuple2[0:2])

tuple2[:2]

tuple2[:]

tuple2[1:]

tuple2[:-2]

tuple2 = (1, 2, 3, 4)

tuple2[::2]

tuple2[::-1]

# membership -> 'in' and 'not in'
tuple2 = (1, 2, 3, 4)

print(3 in tuple2)
print(3 not in tuple2)
print(5 not in tuple2)
print(2 in tuple2)

# complete the script so that it prints the second item of the list
# Expected output: b
letters = ['a', 'b', 'c', 'd', 'e', 'e', 'f', 'g', 'h', 'i']

letters.clear()
letters = "a,b,c,d,e,f,g,h,i"
letters2 = letters.split(",")
letters3 = tuple(letters2)
# letters4 = list(letters3)
print(letters3[:7:2])
print(letters3[1:2])
print(letters3[1])
# Write a python program that asks the user for any string as input and then returns the number of words of that string
# Hello Everyone -> 2
any_string = input("Enter Any String: ")
new_string = any_string.split(" ")
print(len(new_string))