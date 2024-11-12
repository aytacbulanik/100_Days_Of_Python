from day15Main import resources
from day15Main import MENU

moneyCost = 0.0
coin = 0.0
cofeeMachine = True

def calculateMoney():
    print("lütfen bozuk para atınız.")
    quartersMoney = float(input("How many quarters ? : "))
    dimesMoney = float(input("How many dimes ? : "))
    nicklesMoney = float(input("How many nickles ? : "))
    penniesMoney = float(input("How many pennies ? : "))
    coin = (penniesMoney * 0.01) + (dimesMoney * 0.1) + (nicklesMoney * 0.05) + (quartersMoney * 0.25)
    return coin

def getResource():
     print(f"Water : {resources["water"]} ml \nMilk : {resources["milk"]} ml\nCoffee : {resources["coffee"]} gr \nKasa : ${moneyCost}")
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
    coffeeCost = MENU[name]["cost"]
    if coin > coffeeCost:
        print(f"Paranızın üstü ${coin - coffeeCost}. Bölmeden alabilirsiniz.")
        print(f"{name} hazır. Afiyet olsun.")
    else:
        print("yeterli paranız yok. Paranızı bölmeden alabilirsiniz.")
    #print(coin - coffeeCost)
    #for resource in ["water","milk","coffee"]:
    #   resources[resource] -= MENU[name]["ingredients"][resource]
                
whatDoYouWant = ""
while cofeeMachine:                    

    whatDoYouWant = input("Ne içmek istersiniz ? (espresso , latte , cappucino) : ")
    if whatDoYouWant == "report":
        getResource()
    elif whatDoYouWant == "latte" or "cappuccino" or "espresso":
        if controlResources(whatDoYouWant):
            makeCoffee(whatDoYouWant)
        else:
            continue
    else:
         print("Geçerli bir kahve ismi giriniz.")