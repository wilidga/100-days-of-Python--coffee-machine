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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
coffee_machine = True


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_resources_sufficient(coffee_ingredients):
    for item in coffee_ingredients:
        if coffee_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def check_transaction_successful(pay, cost):
    if pay < cost:
        print("Sorry that's not enough money. Money refunded.")
        return  False
    else:
        change = round(pay - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


while coffee_machine:
    option_menu = input("What would you like? (espresso/latte/cappuccino) ☕ ")

    if option_menu == "report":
        print_report()
    elif option_menu == "off":
        coffee_machine = False
        print("Good Bye!!")
    else:
        coffee = MENU[option_menu]
        check_resources_sufficient(coffee["ingredients"])
        pay_amount = process_coins()
        if check_transaction_successful(pay_amount, coffee["cost"]):
            make_coffee(option_menu, coffee["ingredients"])
