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


coins = {
    'Penny' : 0.01 ,
    'Dime' : 0.10 ,
    'Nickel' : 0.05 ,
    'Quarter' : 0.25 ,
}

def order() :
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    ordering = True
    bank = 0
    while ordering :
        customer = input('What would you like ? (espresso/latte/cappuccino) :   ')
        if customer == 'report' :
            for data in resources :
                print(data , ':' , resources[data], 'ml')
            print(f'Money: ${bank}')
        if customer in MENU :
            water_stock = resources['water'] - MENU[customer]['ingredients']['water']
            coffee_stock = resources['coffee'] - MENU[customer]['ingredients']['coffee']
            if MENU[customer]['ingredients']['milk'] :
                milk_stock = resources['milk'] - MENU[customer]['ingredients']['milk']
            if water_stock < 0 :
                print('Not enough water')
            if milk_stock < 0 :
                print('Not enough milk')
            if coffee_stock < 0 :
                print('Not enough coffee')
            if water_stock > 0 and milk_stock > 0 and coffee_stock > 0 :
                resources['water'] = water_stock
                resources['milk'] = milk_stock
                resources['coffee'] = coffee_stock
                price = float(MENU[customer]['cost'])
                print(f'Price : {price} , Please insert coins.')
                money = 0
                for key in coins :
                    coinkey = int(input(f'How many {key} ? :  '))
                    money += ( coinkey * coins[key] )
                change = round(money - price,2)
                pay = False
                while not pay :
                    if change < 0 :
                        print('Your money is not enough. Try Again')

                    else :
                        print(f'Here is your change {change}')
                        print(f'Here is your {customer}')
                        pay = True
                        bank += price



order()
