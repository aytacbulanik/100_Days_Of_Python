# import smtplib

# myEmail = "itouchbulanik@gmail.com" #maili atacak adresimiz
# password = "zravhkinmoijelhi" #uygulama için mail e tanımladığım şifrem
# with smtplib.SMTP("smtp.gmail.com") as connection:#google stmp server e erişiyoruz.
#     connection.starttls() #bu kodla bir güvenlik katmanı oluşturuyoruz.
#     connection.login(user=myEmail, password=password)
#     connection.sendmail(from_addr=myEmail, 
#                         to_addrs="aytacbulanik@hotmail.com" , 
#                         msg="Subject:Hello\n\n My first email")# Subject parametresi maile konu ekliyor
#                         #Böylece spama düşmüyor.


# import datetime as dt

# now = dt.datetime.now() #şu anki saati almak için bunu giriyoruz. now değişkenini
# #kullanarak istediğimiz tarih kısmına ulaşabiliriz.
# print(now.year) #geçerli tarihten yılı alıyoruz.
# print(now.weekday()) #geçerli haftanın günün alıyoruz.

# #geçerli bir tarih ve zaman değerini nesne olarak oluşturup saklayabiliriz.
# myBirthDay = dt.datetime(year=1981,month=12,day=4,hour=16,minute=30)

# print(myBirthDay)


