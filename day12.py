from art import logo
import random
print(logo)

print("sayı tahmini oyununa hoş geldiniz")
print("1 ile 100 arasında bir sayı tahmin edeceğiz. 1 ve 100 dahil")
gameContinue = True
gameDifficult = ""
gameNumber = 0
playerNumber = 0
leftHealt = 10
def controlEasytoHard(choseeGame):
    if choseeGame == "zor":
        return 5
    elif choseeGame == "kolay":
        return 10
    else:
        return 0
def controlYourNumber(number,kalanHak):
        if number > gameNumber:
            print("cevabınız çok yüksek")
            print("tekrar deneyiniz")
            return kalanHak - 1
        elif number < gameNumber:
            print("cevabınız çok düşük")
            print("tekrar deneyiniz")
            return kalanHak - 1
        else:
            print("Doğru bildiniz. Tebrikler")
            kalanHak = -1 
            return kalanHak
while gameContinue:
    gameNumber = random.randint(1, 100)
    gameDifficult = input("Lütfen zorluk seviyesini seçiniz. kolay yada zor ? : ").lower()
    leftHealt = controlEasytoHard(gameDifficult)
    if leftHealt == 0:
        print("yanlış seviye seçtiğiniz için oyun sona erdi")
        break
    while leftHealt > 0:
        print(f"kalan hakkınız : {leftHealt} -- lütfen bir sayı giriniz")
        playerNumber = int(input("Tahmininiz ? : "))
        leftHealt = controlYourNumber(playerNumber , leftHealt)
        if leftHealt == -1:
            gameContinue = False
            break
        elif leftHealt == 0:
            print("başka hakkınız kalmadı")
            gameContinue = False
            break
    