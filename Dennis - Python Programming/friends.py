# ask the user for a list of three friends
# For each friend, we'll tell the user whether they are nearby or not
# for each nearby friend, we'll save them to nearby_friends.txt file

# friend_one = input("Enter your First Friend: ")
# friend_two = input("Enter your Second Friend: ")
# friend_three = input("Enter your Third Friend: ")
#
# friends = [friend_two, friend_two, friend_three]

friends = input("Enter Three Friend Names separated by commas (no spaces please): ").split(',')

people = open('people.txt', 'r')
# people_nearby = people.readlines() #return a list of lines(people)
people_nearby = [line.strip() for line in people.readlines()]
people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

friends_nearby = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with Them.')
    friends_nearby.write(f'{friend}\n')
