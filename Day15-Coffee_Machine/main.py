from setup import MENU, resources, current_money, logo


def return_ingredients(beverage_choice):
    """Takes the user's beverage choice as input and
    returns the list of ingredients to make the beverage"""
    ingredients = MENU[beverage_choice]['ingredients'].keys()
    return list(ingredients)


# Check resources are sufficient? If no, return message " “Sorry there is not enough xxx."
def check_coffee_machine_resources(beverage_choice):
    """ Based on the current resources dictionary
    will check if there is enough of each resource to make the user's beverage choice.
    Will return if there is enough ingredients to proceed (true or false)"""
    ingredients = return_ingredients(beverage_choice)
    for item in ingredients:
        if resources[item] < MENU[beverage_choice]['ingredients'][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    else:
        return True


# Print report Function. Print Water, Milk, Coffee, Money
def coffee_machine_report(current_resources, current_money):
    """If user inputs report, the current amounts of each resource and the current cash
    in the machine will be printed"""
    print(f"Water: {current_resources['water']}ml")
    print(f"Milk: {current_resources['milk']}ml")
    print(f"Coffee: {current_resources['coffee']}g")
    print(f"Money: ${current_money}")


# Prompt User with : What would you like? (espresso/latte/cappuccino). Repeat every time drink served

def user_prompt():
    """A function to allow the user to make a selection, request a report or power the machine off.
    Will return the user's choice"""
    user_choice = input("What would you like? (espresso/latte/cappuccino)?")
    if user_choice in ("espresso", "latte", "cappuccino", "report", "off"):
        return user_choice
    else:
        print("That is not a valid choice. Try again.")


# Take User Money and calculate total
def total_user_money():
    """Function that will add up the money that the user input into the machine.
    Will return the total cash the user has deposited"""
    print("Please insert coins.")
    total_money = int(input("How many quarters?: ")) * .25
    total_money += int(input("How many dimes?: ")) * .1
    total_money += int(input("How many nickels?: ")) * .05
    total_money += int(input("How many pennies?: ")) * .01

    return total_money


def check_sufficient_money(user_choice, user_money):
    """A function to check if the user input enough money to purchase their beverage of choice.
    Will return True or False if enough money as been deposited."""

    if MENU[user_choice]['cost'] > user_money:
        print("Sorry that's not enough money. Money refunded")
        return False
    else:

        return True


def make_coffee(user_choice):
    """Makes the coffee for the user.
    For each ingredient the function will reduce the amount needed to make the coffee from the resources"""
    ingredients = return_ingredients(user_choice)
    for item in ingredients:
        resources[item] -= MENU[user_choice]['ingredients'][item]


print(logo)
# By default, the coffee machine is powered on and running
coffee_machine_on = True

# Continue asking the user which beverage they would like until they power the machine down
while coffee_machine_on:
    user_response = user_prompt()
    if user_response == 'off':
        coffee_machine_on = False
    elif user_response == 'report':
        coffee_machine_report(resources, current_money)
    elif user_response in ("espresso", "latte", "cappuccino"):
        enough_ingredients = check_coffee_machine_resources(user_response)
        if enough_ingredients:
            user_paid_total = total_user_money()
            enough_money = check_sufficient_money(user_response, user_paid_total)
            if enough_money:
                make_coffee(user_response)
                beverage_cost = MENU[user_response]['cost']
                current_money += beverage_cost
                refund = round(user_paid_total - beverage_cost, 2)
                print(f"Here is ${refund} in change.")
                print(f"Here is your {user_response} ☕ Enjoy")
                coffee_machine_on = True
    else:
        print("That is not a valid response. Try again!")
else:
    print("Coffee Machine Powering Down")
