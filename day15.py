from day15Main import resources
from day15Main import MENU

coin = 0.0
cofeeMachine = True

def calculateMoney():
    print("lütfen bozuk para atınız.")
    quartersMoney = float(input("How many quarters ? : "))
    dimesMoney = float(input("How many dimes ? : "))
    nicklesMoney = float(input("How many nickles ? : "))
    penniesMoney = float(input("How many pennies ? : "))
    coin = (penniesMoney * float(0.01)) + (dimesMoney * float(0.1)) + (nicklesMoney * float(0.05)) + (quartersMoney * float(0.25))
    return coin

def getResource():
     print(f"Water : {resources["water"]} ml \nMilk : {resources["milk"]} ml\nCoffee : {resources["coffee"]} gr \nKasa : ${resources["caseCost"]}")

def controlResources(name):
    if resources["water"] < MENU[name]["ingredients"]["water"]:
        print(f"Yeterli su yok. Lütfen başka kahve seçiniz")
        return False
    elif resources["milk"] < MENU[name]["ingredients"]["milk"]:
        print(f"Yeterli süt yok. Lütfen başka kahve seçiniz")
        return False
    elif resources["coffee"] < MENU[name]["ingredients"]["coffee"]:
        print(f"Yeterli kahve yok. Lütfen başka kahve seçiniz")
        return False
    else:
         return True

def makeCoffee(name):
    coin = calculateMoney()
    coffeeCost = float(MENU[name]["cost"])
    if coin > coffeeCost:
        print(f"Paranızın üstü ${round(coin - coffeeCost , 2)} Bölmeden alabilirsiniz.")
        print(f"{name} hazır. Afiyet olsun.")
        resources["caseCost"] += coffeeCost
        for resource in ["water","milk","coffee"]:
            resources[resource] -= MENU[name]["ingredients"][resource]
    else:
        print("yeterli paranız yok. Paranızı bölmeden alabilirsiniz.")
                
whatDoYouWant = ""
while cofeeMachine:                    

    whatDoYouWant = input("Ne içmek istersiniz ? (espresso , latte , cappucino) : ")
    if whatDoYouWant == "report":
        getResource()
    elif whatDoYouWant == "latte" or whatDoYouWant == "cappuccino" or whatDoYouWant == "espresso":
        if controlResources(whatDoYouWant):
            makeCoffee(whatDoYouWant)
        else:
            continue
    else:
         print("Geçerli bir kahve ismi giriniz.")