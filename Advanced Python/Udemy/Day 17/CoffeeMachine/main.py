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
    "water": 10,
    "milk": 2000,
    "coffee": 10,
}
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
machine_coins = 0
machine_off = False
def get_value(item, recipe):
        return MENU[item]["ingredients"][recipe]
# print(MENU["espresso"]["ingredients"]["water"])
def check_resource(user_want):
    if get_value(user_input, "water") > resources["water"]:
        print("Sorry, you don't have enough water!")
    if get_value(user_input, "milk") > resources["milk"]:
        print("Sorry, you don't have enough milk!")
    if get_value(user_input, "coffee") > resources["coffee"]:
        print("Sorry, you don't have enough coffee!")

while not machine_off:
    user_input = input("What would you like? \n Espresso \n Latte \n Cappuccino)\n Enter your choice:  ").lower()
    if user_input == "print":
        print(f"Water: {water} \n Milk: {milk} \n Coffee: {coffee} \n {machine_coins}")
    elif user_input == "off":
        machine_off = True
    elif check_resource(user_input):
        machine_off = False
    else:
        total_cost = int(MENU[user_input]["cost"])
        print(f"Total cost is ${total_cost}: Enter your coins: Accepted coins are "
              f"quarters = $0.25, \n dimes = $0.10,\n nickles = $0.05, \n pennies = $0.01 ")
        # coins = input(f"Total cost is {MENU[user_input]["cost"]}. Enter your coins?: ")
        quarters = int(input("Enter Quarters Coins: if none enter 0: "))
        nickles = int(input("Enter Nickles Coins: if none enter 0: "))
        dimes = int(input("Enter Dimes Coins: if none enter 0: "))
        pennies = int(input("Enter Pennies. if none enter 0: "))
        total_coins = (quarters * 0.25) +  (dimes * 0.10) + (nickles * 0.05) +(pennies *0.01)
        if total_coins < total_cost:
            print("Sorry, you don't have enough money: Collect the refund")
        elif total_coins > total_cost:
            print(f"You have some change {total_coins - total_cost}:")
        machine_coins += total_cost
        water -= get_value(user_input, "water")
        milk -= get_value(user_input, "milk")
        coffee -= get_value(user_input, "coffee")



