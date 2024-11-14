from day16Menu import Menu, MenuItem
from day16coffee_maker import CoffeeMaker
from day16Money_machine import MoneyMachine

myMoneyMachine = MoneyMachine()
myCoffeeMaker = CoffeeMaker()
menu = Menu()
isOn = True
myCoffeeMaker.report()

while isOn:
    option = menu.get_items()
    choseDrink = input(f"wahat do you drink ? {option}: ")
    if choseDrink == "off":
        isOn = False
        break
    elif choseDrink == "report":
        myCoffeeMaker.report()
        myMoneyMachine.report()