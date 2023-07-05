import random


# Lottery Game App

# create a function to generate lottery numbers
def create_lottery_numbers():
    # values = []
    # for x in range(6):
    #     values.append(random.randint(1, 20))
    # return values
    values = set()
    while len(values) < 6:
        values.add(random.randint(1, 50))
    return values


# print(create_lottery_numbers())


# create a function to get player numbers
def get_player_numbers():
    numbers_csv = input("Enter your six numbers, separated by commas: ")
    numbers_list = numbers_csv.split(",")
    # I want to create a set of integers from numbers_list
    numbers_set = {int(number) for number in numbers_list}
    return numbers_set


# print(get_player_numbers())


# create a function to display the menu
def menu():
    # ask players for numbers
    player_numbers = get_player_numbers()
    # calculate the lottery numbers
    lottery_numbers = create_lottery_numbers()
    # print out the winnings
    winning_numbers = player_numbers.intersection(lottery_numbers)
    matched_numbers = 0 if winning_numbers == set() else winning_numbers
    print(f"The Winning Numbers Were: {lottery_numbers}")
    print(f"You matched {matched_numbers} numbers and you won Kes{100 ** len(matched_numbers)}")


menu()