from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True
while is_on:
    """The while test when machibe is off"""
    options = menu.get_items()
    choice = input(f"What would you like to have? {options}:  ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        my_drink = menu.find_drink(choice)
        if (coffee_maker.is_resource_sufficient(my_drink) and
                money_machine.make_payment(my_drink.cost)):
                coffee_maker.make_coffee(my_drink)


