from OOP.CoffeMachineWithOOP.menu import Menu
from OOP.CoffeMachineWithOOP.coffee_maker import CoffeeMaker
from OOP.CoffeMachineWithOOP.money_machine import MoneyMachine

this_menu = Menu()
this_coffee_maker = CoffeeMaker()
this_money_machine = MoneyMachine()
is_on = True

this_coffee_maker.report()
this_money_machine.report()


while is_on:
    menu = this_menu.get_items()
    order_name = input(f"What would you like? ({menu}): ").lower()

    if order_name == "off":
        is_on = False
    elif order_name == "report":
        this_coffee_maker.report()
        this_money_machine.report()
    else:
        drink = this_menu.find_drink(order_name)
        if this_coffee_maker.is_resource_sufficient(drink) and this_money_machine.make_payment(drink.cost):
            this_coffee_maker.make_coffee(drink)
        else:
            pass
















