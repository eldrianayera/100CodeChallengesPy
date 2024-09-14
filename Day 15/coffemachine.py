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

coins = {
    'Penny' : 0.01 ,
    'Dime' : 0.10 ,
    'Nickel' : 0.05 ,
    'Quarter' : 0.25 ,
}

def order() :
    customer = input('What would you like ? (espresso/latte/cappuccino) :   ')\

    if customer == 'report' :
        for data in resources :
            print(data , ':' , resources[data], 'ml')
    if customer in MENU :
        water_stock = resources['water'] - MENU[customer]['ingredients']['water']
        milk_stock = resources['milk'] - MENU[customer]['ingredients']['milk']
        coffee_stock = resources['coffee'] - MENU[customer]['ingredients']['coffee']
        if water_stock > 0 and milk_stock > 0 and coffee_stock > 0 :
            resources['water'] = water_stock
            resources['milk'] = milk_stock
            resources['cofee'] = coffee_stock
            print('Please insert coins.')

order()