from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on= True
order =  (menu.find_drink(input('What do you want to order ?') ))


print(money_machine.report())
print(coffee_maker.report())
print(order)
print(coffee_maker.is_resource_sufficient(order))