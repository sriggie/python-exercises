file = open('csv_data.txt', 'r')
lines = file.readlines()
file.close()

# lines = lines[1:]
lines = [line.strip() for line in lines[1:]]

# iterate over the line
for line in lines:
    person_data = line.split(',')
    name = person_data[0]
    age = person_data[1]
    university = person_data[2]
    degree = person_data[3]

    print(f'{name} is {age}, studying {degree} at {university}.')