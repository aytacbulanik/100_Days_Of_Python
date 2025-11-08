# import random , pandas
# numbers = [1,2,3,4]
# newList = [str(n*2) for n in numbers] # liste deki her bir elemanı alıp ikiyle çarpıp stringe çeviriyor ve  yeni bir listeye atıyor

# newList2 = [name for name in numbers if name < 3] #koşula uygun elemanı listeye ekliyor. if bloğunu sağlarsa ekeleniyor

# #aşağıdaki örnekte stringler den oluşan bir listeyi çift olanları süzerek yeni bir sayı listesi oluşturuluyor.
# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(letter) for letter in list_of_strings]
# result = [number for number in numbers if number %2 == 0]

# #aşağıda iki dosyadan okunan harflerin boşluklarını alıp yeni bir dizye int olarak ekleniyor ve iki dizideki ortak elemanlar karşılaştırılıyor.
# newListA = []
# anotherArray = []
# # with open("file1.txt") as file1:
# #         newListA = [int(line.strip()) for line in file1] #herbir satırın boşluğunu sildi ve int çevirerek yeni dizi oluşturuyor
# # with open("file2.txt") as file2:
# #     anotherArray = [int(line.strip()) for line in file2]
# # result = [number for number in newListA if anotherArray.__contains__(number)] #iki dizideki ortak elemanı çekiyor. yeni diziye ekliyor.
# names = ["ali","hülya","ahmet","mehmet","nimet"]
# newDict = {student: random.randint(1,100) for student in names} #isim dizisini kullanarak yeni bir dict oluşturduk
# newPassDict = {student : score for (student,score) in newDict.items() if score > 60}# score 60 tan büyük öğrencilerle yeni bir dict oluşturuluyor 

# #aşağıda derece cinsinden değerleri olan bir dict fahrineth dict e çevriliyor
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {day : (degrees * 9/5) + 32 for (day , degrees) in weather_c.items()}

# travel_log = {
#   "France":  ["Paris", "Lille", "Dijon"],
#   "Germany":  ["Berlin", "Hamburg", "Stuttgart"]
#    }
# #Pandas kütüphanesindeki satırlara for döngüsü ile ulaşabiliriz
# data = pandas.DataFrame(travel_log)#dict kullanarak pandas dataframe elde ettik
# for (index,row) in data.iterrows(): #itterrows metodu her bir satıra ulaşmamızı sağlıyor
#     print(row.France)
#     print("-----------")
# #birden fazla değeri alan bir fonksiyon yarattık. burada * mutlaka olmalı sonrasında bir isim vermemiz gerekiyor.
# # bu isim tüm girilen değerleri tuple olarak alıyor  
# def add(*args):
#     toplam = 0
#     for n in args:
#         toplam += n
#     return toplam
# sonuc = add(3,17,41,5)
# print(sonuc)

# #birden fazla parametre alabilen bir fonksiyon yarattık. parametleri fonksiyonu çağırdığımızda ekleyebiliriz.bunlar 
# #önceden tanımlanmış özel degerlerdir. doc dosyasında detayı bulunur.
# def useArgs(**kwargs):
#     print(type(kwargs)) #bu tanımlanan parametrenin dict tipinde olduğunu gösteriyor
#     print(kwargs) #fonksiyon çağırıldığında kullanılan argümanların gict içerinde gösterimi
#     print(kwargs["number"])
#     kwargs.get("deneme")

# useArgs(number= 30 , name = "Ali")

from tkinter import *
import requests


def getNewWords():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()
    message = data["quote"]
    canvas.itemconfig(text,text=message)
window = Tk()
window.title("what did say Kayne west")
window.config(padx=40,pady=40)

imagePath = "./files/day33/background.png"
buttonImagePath = "./files/day33/kanye.png"

background = PhotoImage(file=imagePath)
kayne = PhotoImage(file=buttonImagePath)
canvas = Canvas(width=300,height=400,highlightthickness=0)
canvas.create_image(150,200,image=background)
canvas.grid(column=0,row=0)

changeButton = Button(image=kayne,command=getNewWords)
changeButton.grid(column=0,row=1)

text = canvas.create_text(150,200,
                          text="Buraya yazılar gelecek",
                          font=("Arial",18,"bold"),
                          width=200,
                          fill="white"
                          )

window.mainloop()