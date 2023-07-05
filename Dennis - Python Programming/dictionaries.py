from pprint import pprint

# create an empty dictionary
dict1 = {}

# check the type
print(type(dict1))

# populate our dictionary
dict1 = {"vendor": "Cisco", "model": "2600", "IOS": "12.4", "ports": "4"}

print(dict1)

# DICTIONARIES - METHODS
# extract "12.4" from dict1
print(dict1["IOS"])

# output -> cisco
print(dict1['vendor'].upper())

# add a new key-value pair to our dictionary
dict1["RAM"] = "128"

# modify a key-value pair -> IOS to 15.6
dict1["IOS"] = "15.6"

# we can also delete a pair from the dict1 dictionary -> using the del command
del dict1['ports']

# we can use the len() function to find out the number of key-value pairs inside a dictionary
print(len(dict1))

# we can verify if a certain string is a key in a dictionary or not
print("IOS" in dict1)
print("IOS" not in dict1)

# Three important python methods to deal with keys and values
# 1. keys() -> is used to obtain a list having the keys in a dictionary as elements.
print(list(dict1.keys()))

# 2. values() -> is used to get a list having the values in the dictionary as list elements
print(list(dict1.values()))

# 3. items() -> returns a list of tuples, each tuple containing the key and value of each dictionary pair.
print(list(dict1.items()))

print(dict1)

# Next -> Conversions Between Data Types

# Challenges
# 1. create a dictionary of keys a, b, and c where each key has as value a list from 1-10, 11-20 and 21-30 respectively. Then print out the dictionary in a nice format.

my_dict = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
# print(my_dict)

dict2 = {}
dict2['a'] = list(range(1, 11))
dict2['b'] = list(range(11, 21))
dict2['c'] = list(range(21, 31))
# print(dict2)

dict3 = {'a': list(range(1, 11)), 'b': list(range(11, 21)), 'c': list(range(21, 31))}
# print(dict3)

# 2. Access the third value of key b from the dictionary. Expected output: 13
print(dict3['b'][2])
output = dict3['b']
print(output[2])

# 3. Create a list of "person" dictionaries with a name, age, and a list of hobbies for each person.Fill in any data you want.
people = [
    {
        'name': 'Sheema',
        'age': 18,
        'hobbies': ['dancing', 'singing', 'coding']
    },
    {
        'name': 'Alex',
        'age': 20,
        'hobbies': ['cooking', 'basketball']
    },
    {
        'name': 'Reagan',
        'age': 19,
        'hobbies': ['swimming', 'eating', 'sleeping', 'coding']
    }
]

print(people)