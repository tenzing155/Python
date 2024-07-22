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

def is_resource_sufficient(ingredients):
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f" “Sorry there is not enough {item}.​")
            return False
    return True

def process_coins():
    print("Insert coins: ")
    quarters = int(input("Enter coins: quarters: ")) * 0.25
    dimes = int(input("Enter coins: dimes: ")) * 0.10
    nickels = int(input("Enter coins: nickels: ")) * 0.05
    pennies = int(input("Enter coins: pennies: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total

def process_transaction(total,drink_cost):
    if total >= drink_cost:
        change = round(total - drink_cost,2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.​")
        return False

def make_coffee(drink_name,ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your drink {drink_name}")



is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):​ ")
    if choice == "off":
        is_on = False
        break
    elif choice == "report":
        print(f"Water: {resources}ml") 
        print(f"Milk: {resources}ml ")
        print(f"Coffee: {resources}g") 
        print(f"Money: ${profit}") 
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            total = process_coins()
            if process_transaction(total,drink['cost']):
                make_coffee(choice,drink['ingredients'])