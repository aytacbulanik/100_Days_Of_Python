import smtplib

myEmail = "itouchbulanik@gmail.com" #maili atacak adresimiz
password = "zravhkinmoijelhi" #uygulama için mail e tanımladığım şifrem
with smtplib.SMTP("smtp.gmail.com") as connection:#google stmp server e erişiyoruz.
    connection.starttls() #bu kodla bir güvenlik katmanı oluşturuyoruz.
    connection.login(user=myEmail, password=password)
    connection.sendmail(from_addr=myEmail, 
                        to_addrs="aytacbulanik@hotmail.com" , 
                        msg="Subject:Hello\n\n My first email")# Subject parametresi maile konu ekliyor
                        #Böylece spama düşmüyor.
