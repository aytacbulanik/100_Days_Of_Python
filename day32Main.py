# import datetime as dt

# now = dt.datetime.now() #şu anki saati almak için bunu giriyoruz. now değişkenini
# #kullanarak istediğimiz tarih kısmına ulaşabiliriz.
# print(now.year) #geçerli tarihten yılı alıyoruz.
# print(now.weekday()) #geçerli haftanın günün alıyoruz.

# #geçerli bir tarih ve zaman değerini nesne olarak oluşturup saklayabiliriz.
# myBirthDay = dt.datetime(year=1981,month=12,day=4,hour=16,minute=30)

# print(myBirthDay)

#hantanın gününü kontrol ederek pazartesi ise motivasyon maili atan bir uygulama yazdık
import datetime as dt
import pandas
import smtplib
from random import choice

# data = pandas.read_csv("./files/day32/quotes.txt")
# dataList = data.to_dict(orient="records")

# def getNewWords():
#     return choice(dataList)
# isDayMonday = dt.datetime.now().weekday()

def sendEmail(message):
    myEmail = "itouchbulanik@gmail.com" #maili atacak adresimiz
    password = "zravhkinmoijelhi" #uygulama için mail e tanımladığım şifrem
    with smtplib.SMTP("smtp.gmail.com") as connection:#google stmp server e erişiyoruz.
        connection.starttls() #bu kodla bir güvenlik katmanı oluşturuyoruz.
        connection.login(user=myEmail, password=password)
        connection.sendmail(from_addr=myEmail, 
                            to_addrs="aytacbulanik@hotmail.com", 
                            msg=f"Subject:Happy Birthday\n\n{message}")
                            # Subject parametresi maile konu ekliyor
                            #Böylece spama düşmüyor.

# if isDayMonday == 1:
#     newWord = getNewWords()["words"]
#     sendEmail(newWord)
# else:
#     print("Bugün değil")

with open("./files/day32/birthdays.txt") as data:
    newData = pandas.read_csv(data)
    dataList = newData.to_dict(orient="records")
def nowTime():
    now = dt.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    return dt.datetime(year=year,month=month,day=day)

def checkWho(now):
    for object in dataList:
        if now.day == object["day"] and now.month == object["month"]:
            with open("./files/day32/letter.txt",encoding="utf-8") as file:
                contents = file.read()
                contents = contents.replace("[NAME]", object["name"])
            sendEmail(contents)

checkWho(nowTime())