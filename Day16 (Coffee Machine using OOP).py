from menu import MenuItem,Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
menu=Menu()

is_on=True

while is_on:
    choice=menu.get_items()
    user=input(f"What would you like to have? ({choice})")
    if user=="off":
        is_on=False
    elif user=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(user)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
