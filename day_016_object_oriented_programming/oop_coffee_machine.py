from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True

while machine_on:
    drink_options = menu.get_items()
    choice = input(f"What would you like? ({drink_options}): ")
    if choice == "off":
        print("Powering down now. Goodbye.")
        machine_on = False
    elif choice == "report":
        coffee_maker.report() 
        money_machine.report() 
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    # The ELSE below doesn't seem to work because the menu.find_drink(choice) will return "Sorry that item is not available." and errors
    # else:
    #     print("Sorry, you've entered an unknown request. Please try again.")
