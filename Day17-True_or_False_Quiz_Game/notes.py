# class User:
#     None
#
# # create a new class. Create new attributes for the class.
# user_1 = User()
# user_1.id = "001"
# user_1.username = "angela"
#
# print(user_1.username)
#
# user_2 = User()
# user_2.id = "002"
# user_2.username = "jack"


# Constructor (initializing an object)

# Creating attributes (the thing the object has)
class User:
    def __init__(self, user_id, username, followers):
        print("new user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.following += 1
        self.following += 1



# create a new class. Create new attributes for the class.
user_1 = User("001", "Angela")


print(user_1.username)

user_2 = User("002", "Jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)

# Constructor (initializing an object)

class Car:
    def __init__(self, seats):
        self.seats = seats

my_car = Car(5)
print(my_car.seats)


# Creating Methods (the things that object does)

class Car:
    def enter_race_mode(self):
        self.seats = 2

my_car.enter_race_mode()
