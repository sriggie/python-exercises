for number in range(10):
    if number == 7:
        break
    print(number)


list1 = [4, 5, 6]
list2 = [10, 20, 30]

for x in list1:
    for y in list2:
        if y == 20:
            break
        print(x * y)
    print("Outside the nested loop.")


