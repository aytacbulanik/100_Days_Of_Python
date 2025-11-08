import requests
from datetime import datetime

# #aşağıdaki satırla bir url e istek atıyoruz. bunu response değişkenine atıyoruz.
# response = requests.get(url="http://api.open-notify.org/iss-now.json") 
# response.raise_for_status() #hata kodunu yakalamak için bunu yazıyoruz.
# data = response.json() #json nesnesini değişkene atıyoruz.

# #json nesnesinin alt değerlerine ulaşıyoruz.
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]

# issPosition = (longitude,latitude)
#url sorgusundaki paramaetreleri python dict olarak gönderebiliriz.
paramaters = {
    "lat" : 46.34512,
    "lng" : -37.23107,
    "formatted" : 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=paramaters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
sunriseHour = sunrise.split("T")[1].split(":")[0]
sunsetHour = sunset.split("T")[1].split(":")[0]
print(sunriseHour)
print(sunsetHour)
now = datetime.now()
print(now.hour)