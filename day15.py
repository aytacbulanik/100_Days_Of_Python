from day15Main import resources
from day15Main import MENU
moneyArray = ["quarter","dime","nickel","penny"]
coin = 0.0
def getResources(resource):
    for resor in resource:
        print(f"{resor} : {resource[resor]} ml")
def calculateMoney(penny,dime,nickle,quarter):
    coin = (penny * 0.01) + (dime * 0.1) + (nickle * 0.05) + (quarter * 0.25)
    return coin 
whatDoYouWant = ""
whatDoYouWant = input("Ne içmek istersiniz ? (espresso , latte , cappucino)")
if whatDoYouWant == "report":
    getResources(resources)
elif whatDoYouWant == "espresso" or "latte" or "cappucino":
    quartersMoney = float(input("How many quarters ? :"))
    dimesMoney = float(input("How many dimes ? :"))
    nicklesMoney = float(input("How many nickles ? :"))
    penniesMoney = float(input("How many pennies ? :"))
    coin = calculateMoney(penniesMoney,dimesMoney,nicklesMoney,quartersMoney)
    coffeeCost = MENU[whatDoYouWant]["cost"]
    print(coin - coffeeCost)