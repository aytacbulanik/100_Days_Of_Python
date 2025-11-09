#haftanın gününü kontrol ederek pazartesi ise motivasyon maili atan bir uygulama yazdık
import datetime as dt
import pandas
import smtplib
from random import choice

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