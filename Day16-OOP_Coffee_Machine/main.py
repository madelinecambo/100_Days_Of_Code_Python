from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()


coffee_machine_on = True

while coffee_machine_on:
    user_choice = input(f"What would you like? ({menu.get_items()[:-1]})? ")

    if user_choice == "off":
        print("Powering coffee machine off....")
        coffee_machine_on = False
    elif user_choice == "report":
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffeemaker.is_resource_sufficient(drink):

            if not moneymachine.make_payment(drink.cost):
                print("Sorry that's not enough money. Money refunded")
            else:
                coffeemaker.make_coffee(drink)





