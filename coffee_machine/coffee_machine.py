

import emoji


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# check if resources are sufficient and which resource is insufficient
def is_sufficient(beverage):
    if beverage == "espresso":
        if MENU["espresso"]["ingredients"]["water"] > resources["water"]:
            print("Sorry, there is not enough water.")
            return False
        elif MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, there is not enough coffee.")
            return False
        else:
            return True
    else:
        if MENU[beverage]["ingredients"]["water"] > resources["water"]:
            print("Sorry, there is not enough water.")
            return False
        elif MENU[beverage]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry, there is not enough milk.")
            return False
        elif MENU[beverage]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, there is not enough coffee.")
            return False
        else:
            return True


#make drink and deduct resources and add money
def is_enough(beverage, payment):
    # Check that it's enough
    if payment >= MENU[beverage]["cost"]:
        return True
    else:
        print("Not enough money. Refunded")
        return False







money = 0.00
coffee = True
while coffee == True:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    # If report is typed
    if choice == "report":
        for each in resources:
            if each == "water" or each == "milk":
                print(f"{each.capitalize()}: {resources[each]}ml")
            elif each == "coffee":
                print(f"{each.capitalize()}: {resources[each]}g")
        print(f"Money: ${money:,.2f}")
    elif choice == "off":
        coffee = False
    elif choice in ["espresso", "latte", "cappuccino"]:
        # will exit program if not sufficient resources
        if not is_sufficient(choice):
            continue
        else:
            # insert and calculate money
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))

            # Add money inserted in cents
            paid = (((25 * quarters) + (10 * dimes) + (5 * nickels) + (1 * pennies)) * 0.01)

            # check to make sure enough was inserted
            if is_enough(choice, paid):
                change = paid - MENU[choice]["cost"]
                # print(f'${change:,.2f}')
                print(f"Here is ${change:,.2f} in change.")
                print(f"Here is your {choice} \u2615 Enjoy!")

                # Add money to total
                money += MENU[choice]["cost"]

                # Deduct resources
                if choice == "espresso":
                    resources["water"] -= 50
                    resources["coffee"] -= 18
                elif choice == "latte":
                    resources["water"] -= 200
                    resources["milk"] -= 150
                    resources["coffee"] -= 24
                elif choice == "cappuccino":
                    resources["water"] -= 250
                    resources["milk"] -= 10
                    resources["coffee"] -= 24
            else:
                continue
    else:
        exit("Sorry, you have entered an invalid choice.")


