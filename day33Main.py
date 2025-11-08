import requests

#aşağıdaki satırla bir url e istek atıyoruz. bunu response değişkenine atıyoruz.
response = requests.get(url="http://api.open-notify.org/iss-now.json") 
response.raise_for_status() #hata kodunu yakalamak için bunu yazıyoruz.
data = response.json() #json nesnesini değişkene atıyoruz.

#json nesnesinin alt değerlerine ulaşıyoruz.
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

issPosition = (longitude,latitude)

print(issPosition)