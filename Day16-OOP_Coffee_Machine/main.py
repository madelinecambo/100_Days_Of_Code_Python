from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects from classes
menu = Menu()
coffeemaker = CoffeeMaker()
money_machine = MoneyMachine()

# By default coffee machine is on
coffee_machine_on = True


while coffee_machine_on:
    user_choice = input(f"What would you like? ({menu.get_items()[:-1]})? ")
    if user_choice == "off":
        print("Powering coffee machine off....")
        coffee_machine_on = False
    elif user_choice == "report":
        coffeemaker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffeemaker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)





