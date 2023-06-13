# # Create an empty list
# list1 = [2, 9, "python"]
#
# # Check the length of the list
# print(len(list1))
#
# if len(list1) == 0:
#     print("Your List is empty")
# else:
#     print(f"you have {len(list1)} elements.")
#
# # Check the type of the list
# print(type(list1))
#
# # Lets populate our list
# list1 = ["cisco", "python", "Avaya", 10, 10.5, -11]
# print(len(list1))
# print(list1[1:2])
# print(list1[1])
# # Both line 18 an 19 returns python
# # Print the contents of our list
#
# print(list1[-1])
# # indexError
# # print(list1[100])
#
# list1 = ["cisco", "python", "Avaya", 10, 10.5, -11]
# list1[2] = "hp"
#
# # LIST METHODS
# # min() -> returns the smallest number within a list
# list2 = [-11, 2, 12]
# print(min(list2))
#
# # max() -> returns the largest number within a list
# print(max(list2))
#
# # create a list of strings
# list3 = ["a", "b", "c"]
# print(min(list3))
# print(max(list3))
# list4 = ["a", "A"]
# print(max(list4))
#
# list1 = ["John", "Junet", "Julius", "Justus"]
# print(max(list1))
#
# # Appending an element into a list
# list1.append(100)
#
# # deleting Elements from a list
# # 1.del command
# del list1[4]
#
# # 2.pop()
# list1.pop(0)
#
# # 3.Remove()
# list1.remove("HP")
#
# # Inserting an element into a list
# list1.insert(2, "")
# rint(list1)
#
#
# list4 = [9, 99, 999]
#
# list4.append(list4)
# print(list4)
#
# print(list1.index(-11))
#
# #  find out the occurences of an element in a list -> count() method
# list1.append(10)
# list1.append(10)
# list1.append(10)
#
# print(list1.count)
#
# list2.append(1)
# list2.append(25)
# list2.append(500)
#
# list2.sort()
# print(list2)
#
# # 2. revverse
# list2.reverse()
# print(list2)
#
#
# #  print the content of our list
#
# # 3 sorted() -> sorts a new list and creates a new list in place
# my_new_list = sorted(list2)
# print(my_new_list)
# new_list = sorted(my_new_list ,reverse=true)
#
# #  concatinating list -> plus operator -> '+' ' - '
#

#  list slices
#  create a new list
list5 = [1, 2, 3, 'a', 'b', 'c']
# 1 . extract the first 3 elements
print(list5[0:3],"method 1")
print(" __ " * 60)
print("1","2" ,"3","method 2")
print(" __ " * 60)

# 2 Extract [3,a ,b]
print(list5[2:4], "method 1" )
print("method 2 - >", "3,", "a," , "b,")
print(" __ " * 60)

# 3. extract [1 ,2,3,'a', 'b', 'c'] -> use two ways fpr that
print(list5[0:5], "method 1")
print("1", "2" , "3" , "4" , "a", "b", "c" , "method 2")
print(" __ " * 60)

# 4. uisng negative indexes,  extract [3,'a','b']
print(list5[-1:-4] ,"method 1")
print("3," "a," "b,")
print(" __ " * 60)

# 5. using -ve indexes , extract['a','b','c']
print(list5[-1:-2])
print("1" ,"b" , "c")
print(" __ " * 60)


# 6. using -ve indexes, extract[1,2,3]
print(list5[-1:-6])
print("-1" , "-2" , "-3")
print(" __ " * 60)


# 7. use a step to extract [1,2,3]
print(list5[::-1])
print("1" , "2" , "3")
print(" __ " * 60)

# 8. use a step to reverse the list ['c','b','a',3,2,1]
print(list5[1:2:3])
print("1", "a", "b")