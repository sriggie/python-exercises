# sets
# 1. set() function.
myList = [1, 2, 3, 4, 5, 2, 3]
print(set(myList))

# apply the set() function to this list
# mySet = set(myList)
# print(mySet)
#
# myList = list(mySet)
# print(myList)

# you can create a set by passing a raw sequence to the set() function
set1 = set([11, 12, 13, 14, 15, 15, 15, 11])
print(set1)
print(type(set1))

# 2. second way is to use curly braces -> '{}'
set2 = {11, 12, 13, 14, 15, 15, 15, 11}
print(set2, type(set2))

# we can find the number of elements in a set using the len() function
print(len(set2))

# membership - 'in' and 'not in' keywords
print(11 in set2)
print(10 in set2)
print(10 not in set2)

# we can add or remove set elements/items
# add() method -> adds an item into a set
set2.add(16)

# remove() -> removes set items
set2.remove(11)

# print the elements of set2
print(set2)

# SETS METHODS
# To better understand set methods and operations, lets create two sets first
set3 = {1, 2, 3, 4}
set4 = {3, 5, 8}

# we can identify the common elements of the two sets -> intersection() method
print(set3.intersection(set4))
print(set4.intersection(set3))

# we can identify which elements does set3 have but set4 doesn't -> difference() method
print(set3.difference(set4))
print(set4.difference(set3))

# we can unify the two sets using -> union() function
print(set3.union(set4))

# remove a random element in a set using the pop() method
set3.pop()
print(set3)
print(set3.pop())
print(set3)

# we can also clear a set by using the clear() method
set3.clear()
print(set3)

print(type({1}))

