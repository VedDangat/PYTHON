# Coffee Machine Program

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0.0
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources(drink):
    for item in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total


def check_transaction(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} dollars in change.")
        resources["money"] += drink_cost
        return True


def make_coffee(drink):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    print(f"Here is your {drink}. Enjoy!")


# Main Program Loop
machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        machine_on = False

    elif choice == "report":
        print_report()

    elif choice in MENU:
        if check_resources(choice):
            payment = process_coins()
            if check_transaction(payment, MENU[choice]["cost"]):
                make_coffee(choice)
    else:
        print("Invalid choice. Please try again.")
