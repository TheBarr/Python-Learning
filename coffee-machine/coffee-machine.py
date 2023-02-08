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

def resource_value(name, resource):
    return MENU[name]['ingredients'][resource]

def overall_resource(name):
    if name == 'espresso':
        resources['water'] -= resource_value(name, 'water')
        resources['coffee'] -= resource_value(name, 'coffee')
    else:
        resources['water'] -= resource_value(name, 'water')
        resources['coffee'] -= resource_value(name, 'coffee')
        resources['milk'] -= resource_value(name, 'milk')

def resource_check(name):
    if name == "espresso":
        if resource_value(name, 'water') > resources["water"]:
            print("Sorry there is not enough water.")
            return False
        elif resource_value(name, 'coffee') > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            overall_resource(name)
            return True
    else:
        if resource_value(name, 'water') > resources["water"]:
            print("Sorry there is not enough water.")
            return False
        elif resource_value(name, 'milk') > resources["milk"]:
            print("Sorry there is not enough milk.")
            return False
        elif resource_value(name, 'coffee') > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            overall_resource(name)
            return True
def money():
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("how many dimes? ")) * 0.10
    nickles = int(input("how many nickles? ")) * 0.05
    pennies = int(input("how many pennies? ")) * 0.01
    suma = quarters + dimes + nickles + pennies
    return suma

def money_check(coffee_name):
    if m >= coffee_cost(coffee_name):
        change = round((m - coffee_cost(coffee_name)), 2)
        print(f'Here is ${change} in change.')
        print(f'Here is your {coffee_name} enjoy!')
        return coffee_cost(coffee_name)
    else:
        print("Sorry that's not enough money. Money refunded.")

def coffee_cost(name):
    return MENU[name]["cost"]

profit = 0
switch = True
while switch:
    decision = input("What would you like? (espresso/latte/cappuccino): ")
    if decision == 'espresso':
        if resource_check('espresso'):
            m = money()
            profit += money_check('espresso')

    elif decision == 'latte':
        if resource_check('latte'):
            m = money()
            profit += money_check('latte')
    elif decision == 'cappuccino':
        if resource_check('cappuccino'):
            m = money()
            profit += money_check('cappuccino')
    elif decision == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money= ${profit}")
    elif decision == 'off':
        switch = False

