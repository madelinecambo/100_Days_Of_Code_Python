#Deterministic
#they will perform repeated actions in a fully predictable way
# pseudo random number generators
# Python uses the Mersenne Twister


# will use the random module
# random integers, random floating point numbers

#import random module
# each module is responsible for a different bit of functionality
# import random
# import my_module
#
# random_integer = random.randint(1, 10)
# print(random_integer)
#
# print(my_module.my_number)
#
# random_float = random.random()
# print(random_float)
#
# random_0to5 = random.randint(0, 4) + random.random()
# print(random_0to5)
#
# random_0to5 =  random.random() * 5
# print(random_0to5)
#
# love_score = random.randint(0,100)
# print(f"Your Love Score is: {love_score}")

# could be used to create a dice, flip a coin. Create a game etc.

# Lists
# preserves order

states_of_america = ["Delaware", "Pennsylvania", "New Hampshire", "New York"]
# get first item in the list
print(states_of_america[0])

# get last item in the list
print(states_of_america[-1])

#Can change elements in the list
states_of_america[1] = 'Pencilvania'

print(states_of_america)

# to add an item at the end of the list
states_of_america.append("Angelaland")

print(states_of_america)

# adding multiple items to a list
states_of_america.extend(["Angeland2", "AnotherItem"])

print(states_of_america)

# Most Common Error - Index Out of Range

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery"]

#nested list
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)




