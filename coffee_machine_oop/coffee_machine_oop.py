from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = True
cm = CoffeeMaker()
mm = MoneyMachine()
menu1 = Menu()

while coffee == True:
    choice = input(f"What would you like? {menu1.get_items()}: ").lower()

    # Get MenuItem object of valid drink choice
    menu_item = menu1.find_drink(choice)

    # If report is typed
    if choice == "report":
        cm.report()
        mm.report()

    # Turn off coffeemaker
    elif choice == "off":
        coffee = False

    elif menu_item.name in ["espresso", "latte", "cappuccino"]:
        # will exit program if not sufficient resources
        if not cm.is_resource_sufficient(menu_item):
            continue
        else:
            # insert and calculate money
            if mm.make_payment(menu_item.cost):
                cm.make_coffee(menu_item)
