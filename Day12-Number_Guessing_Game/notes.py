# Name spaces - local vs global scope

################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
# exists within functions

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# this gives an error that potion strength is not defined
# the variable has local scope. Can only use it inside the function
# print(potion_strength)

# global scope
# to make it available outside the function
player_health = 10

def drink_potion():
    #defined, indented, inside the function
    potion_strength = 2
    print(player_health)

drink_potion()

# Namespace
# anything you give a name to has a namespace
# the concept of global or local scope

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)
    drink_potion()

# local scope to the drink_potion() function

# There is no block scope
# If you create an if statement

if 3 > 2:
    a_variable = 10
enemies = ["skeleton", "zombie", "alien"]

game_level = 3
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

# Global vs Local Variables

enemies = 1
def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies number is {enemies}")

# avoid modifying global scope. prone to errors and bugs
# do not modify within a function

def increase_enemies():
    return(enemies + 1)

enemies = increase_enemies()
print("enemies")
print(enemies)


# Global Constants
# something you will never change
# designate with all CAPS

PI = 3.14159
URL = "https://ww.google.com"
TWITTER_HANDLE = "@yu_angela"

