# sets
#   1. set () function
myList = [1, 2, 3, 4, 5, 2, 3]
print(myList)
print("  " * 1000)
#  apply the set() function to this list
myset = set(myList)
print(myset)
print("  " * 1000)

myList = list(myset)
print(myList)
print("  " * 1000)

#  you can create a set by passing a raw sequence to the set function
set1 = set([11, 12, 13, 14, 15, 15, 15, 15, 11])
print(set1)
print(type(set1))
print("  " * 1000)

# 2. second way to use calibraces '{}'
set2 = {11, 12, 13, 14, 15, 15, 15, 15, 11}
print(set2)
print(type(set2), "Reagan")
print("  " * 1000)

#  number of elements using the len() function
print(len(set2))
print("  " * 1000)

#  membership -> 'in' or 'not in' keywords

print(11 in set2)
print(10 in set2)
print(10 not in set2 )
print("  " * 1000)

#  we can add or remove elements/items
#  add() method -> adds an item into a set
set2.add(16)

#  remove () -> removes set items
set2.remove(11)

#  it doesnt allow duplicates
set2.add(16)


#  print the elements of set2
print(set2)


# SETS METHODS
#  to better understand set methods and operations lets create two sets first
set3 = {1,2, 3, 4}
set4 = {3, 5, 8}

#  we can identify the common elements of the two sets -> intersection() method

print(set3.intersection(set4))

print(set4.intersection(set3))

#  we can identify which elements does set3 have but set3 doesnt ->diffrence() method

print(set3.difference(set4))
print(set3.difference(set3))

#  we can unify the two sets with - > union()  function
print(set3.union(set4))
print(set4.union(set4))

#  remove a random element using the poop() element
set3.pop()
print(set3)

print(type({1}))
print(type({}))

