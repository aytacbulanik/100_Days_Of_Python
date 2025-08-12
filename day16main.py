from day16Menu import Menu, MenuItem
from day16coffee_maker import CoffeeMaker
from day16Money_machine import MoneyMachine

myMoneyMachine = MoneyMachine()
myCoffeeMaker = CoffeeMaker()
menu = Menu()
isOn = True

while isOn:
    option = menu.get_items()
    choseDrink = input(f"wahat do you drink ? {option}: ")
    if choseDrink == "off":
        isOn = False
        break
    elif choseDrink == "report":
        myCoffeeMaker.report()
        myMoneyMachine.report()
    else:
        drink = menu.find_drink(choseDrink)
        result = myCoffeeMaker.is_resource_sufficient(drink)
        if result:
            if myMoneyMachine.make_payment(drink.cost):
                myCoffeeMaker.make_coffee(drink)