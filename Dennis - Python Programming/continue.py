list1 = [4, 5, 6]
list2 = [10, 20, 30]

for x in list1:
    for y in list2:
        if y == 20:
            continue
        print(x * y)
    print("Outside the nested loop.")

4 * 10
"Outside the nested loop."
4 * 30

5 * 10
"Outside the nested loop."
5 * 30

6 * 10
"Outside the nested loop."
6 * 30

4 * 10
4 * 30
"Outside the nested loop."

5 * 10
5 * 30
"Outside the nested loop."

6 * 10
6 * 30
"Outside the nested loop."

# pass statement
for i in range(10):
    pass

print(10)

