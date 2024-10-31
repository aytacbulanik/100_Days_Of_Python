from art import logo
import random
print(logo)

print("sayı tahmini oyununa hoş geldiniz")
print("1 ile 100 arasında bir sayı tahmin edeceğiz. 1 ve 100 dahil")
gameContinue = True
gameDifficult = ""
gameNumber = 0

playerNumber = 0
while gameContinue:
    gameNumber = random.randint(1, 100)
    def controlYourNumber(number):
        if number > gameNumber:
            print("cevabınız çok yüksek")
            print("tekrar deneyiniz")
        elif number < gameNumber:
            print("cevabınız çok düşük")
            print("tekrar deneyiniz")
        else:
            print("Doğru bildiniz. Tebrikler")
            gameContinue = False
    gameDifficult = input("oyun zor mu kolay mı olsun : ").lower()
    leftHealt = 10
    while leftHealt > 0 :
        if gameDifficult == "zor":
            leftHealt = 5
        elif gameDifficult == "kolay":
            leftHealt = 10
        else:
            print("yanlış bir ifade girdiniz")
            break
        print(f"oyunu bitirmek için {leftHealt} hakkınız var. o zaman başlayalım")
        playerNumber = int(input("Tahmin giriniz : "))
        controlYourNumber(playerNumber)
        leftHealt -= 1
        print(leftHealt)