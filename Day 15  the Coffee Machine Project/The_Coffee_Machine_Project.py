MENU = {
    """Contains all kinds of beverages in the machine
    """
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
PROFIT = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredient):
    """return true if the resource is sufficient ,False if ingredients are insufficient"""

    for items in order_ingredient:
        if order_ingredient[items] >= resources[items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True


def process_coins():
    """return the total calculated from coins inserted

    Returns: total
        integer: total coins inserted
    """
    print('please insert some coins')
    total = float(input('how many quarters : ')) * 0.25
    total += float(input('how many dimes : ')) * 0.1
    total += float(input('how many nickel : '))*0.05
    total += float(input('how many pennies : '))*0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """return True when the payment is accepted,or False is mony is insufficient

    Args:
        money_received (float): The money that the user puts in the coffee machine 
        drink_cost (float): Cost of the drink

    Returns:
        bool: return True when the payment is accepted,or False is mony is insufficient
    """
    global PROFIT
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is {change} coins in change")
        PROFIT += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredient):
    """deduct the required ingredients from the resources

    Args:
        drink_name (str): the name of coffee drink
        order_ingredient (dict): coffee order ingredients 
    """
    for items in order_ingredient:
        resources[items] -= order_ingredient[items]
    print(f"here is your {drink_name}☕😋😊")


is_on = True
while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino) : ')
    if choice == "off":
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${PROFIT}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if (is_transaction_successful(payment, drink['cost'])):
                make_coffee(choice, drink["ingredients"])
