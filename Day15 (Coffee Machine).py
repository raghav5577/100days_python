MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}
balance=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def res_check(ingredients):
    for i in ingredients:
        if ingredients[i]>=resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True

def process_money():
    print("Please insert money:")
    total=int(input("How many 10 rupee notes..."))*10
    total+=int(input("How many 20 rupee notes..."))*20
    total+=int(input("How many 50 rupee notes..."))*50
    total+=int(input("How many 100 rupee notes..."))*100
    total+=int(input("How many 200 rupee notes..."))*200
    total+=int(input("How many 500 rupee notes..."))*500
    return total

def payment_successful(money_received, drink_cost):
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is ₹{change} in change... ")
        global balance
        balance+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name,drink_ingredients):
    for i in drink_ingredients:
        global resources
        resources[i]-=drink_ingredients[i]
    print(f"Here is your {drink_name} ☕...Please come again 🙂...")

on=True
while on:
    user=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user=="off":
        on=False
    elif user=="report":
        print(f"Water:{resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ₹{balance}")
    else:
        drink=MENU[user]
        if res_check(drink["ingredients"]):
            payment=process_money()
            if payment_successful(payment,drink["cost"]):
                make_coffee(user,drink["ingredients"])


