import json
file = open('friends_json.txt', 'r')

file_contents = json.load(file) # reads file and turns it into a python object(dictionary)

file.close()

print(file_contents['friends'][0]['name'])

# sample dictionary
cars = [
    {'make': 'Ford', 'Model': 'Fiesta'},
    {'make': 'Ford', 'Model': 'Focus'}
]

file = open('cars_json.txt', 'w')
json.dump(cars, file)
file.close()