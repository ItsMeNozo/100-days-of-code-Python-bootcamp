from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker_obj = CoffeeMaker()

while True:
    items = menu.get_items()
    order = input(f"What would you like? {items}")
    if order == "report":
        coffee_maker_obj.report()
        money_machine.report()
    elif order == "off":
        break
    else:
        drink = menu.find_drink(order)
        if drink == "":  # same as drink == ""
            print("That item is not on the menu.")
        else:
            if coffee_maker_obj.is_resource_sufficient(drink):
                is_transaction_successful = money_machine.make_payment(drink.cost)
                if is_transaction_successful:
                    coffee_maker_obj.make_coffee(drink)
