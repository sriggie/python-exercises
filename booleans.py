# booleans data types -> true or false values
print(1 == 1) # retruns True
print(1 == 2) # returns False
print(3 <= 3) # returns True

# 1 . and
print(1 == 1) and (2 == 2) #  retrurns true

# 2 or
print((1 ==1) or (3 == 2)) # retruns true
print((11 == 12) or (3 >= 2)) #  returns
print((("java" != "Java" and (23.99 == 24) )))
#3 . Not
print(not(1 >= 1))

# Log in process

# users credentials in our DB
userNameDB = "REAGAN"
password = "password"

# users credentials to log in
userName = "REAGAN"
password = "password"

#  check if the user credentials match with the ones in th DB
if (
    userName == userNameDB
)and (
    password == passwordDB
):
    # log in the user if they match
print("logged in successfully....")
else:
    # print an error if they do not match
    print("Wrong credentials please try again.")