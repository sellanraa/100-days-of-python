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

income = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# print report of resources
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${income}") 
    
# check if resources are sufficient
def resource_check(order_ingredients):
    """returns true if there are enough ingredients, false if there aren't enough ingredients to make the drink"""
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient} to make your drink.")
            return False
    return True

# process payment
def process_payment():
    """takes payment and returns the total payment calculated from coins inserted"""
    print("Please insert coins.")
    total_payment = int(input("How many quarters? ")) * 0.25
    total_payment += int(input("How many dimes? ")) * 0.1
    total_payment += int(input("How many nickels? ")) * 0.05
    total_payment += int(input("How many pennies? ")) * 0.01
    return total_payment

# check if transaction successful - if not, refund, if so...
def transaction(money_received, drink_cost):
    """Return true if the payment is adequate and make a drink, else return false and offer a refund"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here's your change: ${change}")
        global income
        income += drink_cost
        return True
    else:
        print("Sorry, that's not enough for your drink. Here's your money back.")
        return False

# make drink and deduct resources
def make_drink(drink_choice, order_ingredients):
    """deduct ingredients from resources"""
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here's your {drink_choice}.")


# initial interface:

machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        print("Powering down now. Goodbye.")
        machine_on = False
    elif choice == "report":
        report()
    elif choice == "latte" or "espresso" or "cappuccino":
        drink = MENU[choice]
        if resource_check(drink["ingredients"]):
            payment = process_payment()
            if transaction(payment, drink["cost"]):
                make_drink(choice, drink["ingredients"])
    else:
        print("Sorry, you've entered an unknown request. Please try again.")
