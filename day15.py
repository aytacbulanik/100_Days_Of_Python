from day15Main import resources
from day15Main import MENU

moneyArray = ["quarter","dime","nickel","penny"]
coin = 0.0

def calculateMoney(penny,dime,nickle,quarter):
    coin = (penny * 0.01) + (dime * 0.1) + (nickle * 0.05) + (quarter * 0.25)
    return coin 

def calculateResources(name):
    if name == "report":
        for resor in resources:
            print(f"{resor} : {resources[resor]} ml")
    elif name == "espresso" or "latte" or "cappucino":
        for resource in ["water","milk","coffee"]:
            if resources[resource] < MENU[name]["ingredients"][resource]:
                print(f"Yeterli {resource} yok")
            else:
                quartersMoney = float(input("How many quarters ? :"))
                dimesMoney = float(input("How many dimes ? :"))
                nicklesMoney = float(input("How many nickles ? :"))
                penniesMoney = float(input("How many pennies ? :"))
                coin = calculateMoney(penniesMoney,dimesMoney,nicklesMoney,quartersMoney)
                coffeeCost = MENU[whatDoYouWant]["cost"]
                print(coin - coffeeCost)
                for resource in ["water","milk","coffee"]:
                    resources[resource] -= MENU[name]["ingredients"][resource]
whatDoYouWant = ""
whatDoYouWant = input("Ne içmek istersiniz ? (espresso , latte , cappucino) : ")
calculateResources(whatDoYouWant)