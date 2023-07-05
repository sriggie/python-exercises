# Ranges Methods
my_range = range(10)
print(type(my_range))
print(list(my_range))

# syntax for range with a step
# range(start, stop, step)
# create a range using start, stop and step
new_range = list(range(0, 10, 2))
print(new_range)

print(list(range(0, 10, 2)))

# -ve values for the start, stop and step arguments
print(list(range(-2, -10, -2)))

# you can also use indexes, as we did with strings or lists, to extract various elements from a range
print(new_range[0])
print(new_range[-1])

# you can also verify if a certain value is a member of the range by using 'in' and 'not in'
r = list(range(1, 11))
print(11 in r)
print(0 not in r)

# moreover, you can apply, for instance, the index() method to find out the index of a certain element of the range
print(r.index(4))

# you cannot slice a range, but you can convert it to a list then apply your slice
r2 = range(1, 101)
print(list(r2))
print(list(r2)[9:20])

# Next -> Dictionaries


