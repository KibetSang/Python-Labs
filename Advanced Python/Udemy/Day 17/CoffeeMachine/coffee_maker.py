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
profit =0
resources = {
    "water": 10,
    "milk": 2000,
    "coffee": 10,
}
def check_resources(ingredients):
    """
    This fucntion check if the ingredients are enough to make drink
    """
    for item in ingredients:
        if ingredients[item] < resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
def process_coins():
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    total_coins = int(input("How many  quarter coins?: ")) * 0.25
    total_coins += int(input("How many  dimes coins?: ")) * 0.1
    total_coins += int(input("How many  nickles coins?: ")) * 0.05
    total_coins += int(input("How many  pennies coins?: ")) * 0.01
    return total_coins
def  transaction_successful(payment, total_coins):
    if drink["cost"] <= total_coins:
        print(f"Sorry there is not enough {payment}")
        return False
    else:
        return True
def make_coffee(drink):
    for item in drink["ingredients"]:
        drink["igredients"] -= drink["ingredients"][item]


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        is_on = False
    if choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
    if check_resources(drink["ingredients"]):
        process_coins()
        if transaction_successful(total_coins, drink["cost"]):
            make_coffee(choice)


