import requests
from datetime import datetime
import time

def isNearISS():
    myLati = 36.715912
    myLong = 37.125900
    #aşağıdaki satırla bir url e istek atıyoruz. bunu response değişkenine atıyoruz.
    response = requests.get(url="http://api.open-notify.org/iss-now.json") 
    response.raise_for_status() #hata kodunu yakalamak için bunu yazıyoruz.
    data = response.json() #json nesnesini değişkene atıyoruz.

    #json nesnesinin alt değerlerine ulaşıyoruz.
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    
    if myLong-5 <= longitude <= myLong+5 and myLati-5 <= latitude <= myLati+5:
        return True 
def isNight():
    myLati = 36.715912
    myLong = 37.125900
    #url sorgusundaki paramaetreleri python dict olarak gönderebiliriz.
    paramaters = {
        "lat" : myLati,
        "lng" : myLong,
        "formatted" : 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json",params=paramaters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    sunriseHour = int(sunrise.split("T")[1].split(":")[0])
    sunsetHour = int(sunset.split("T")[1].split(":")[0])
    now = datetime.now()
    if now.hour <= sunriseHour and now.hour >= sunsetHour:
        return True
while True:
    time.sleep(10) #while göngüsünü sürekli değilde belli aralıklarla çalışmasını sağlıyor
    if isNight() and isNearISS():
        print("Şu an IIS i görebilirsiniz")
    else:
        print("Şu an ISS i göremezsiniz")