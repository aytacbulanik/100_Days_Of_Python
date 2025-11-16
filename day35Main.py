import requests
apiKey = "3ab9c00817b1ff26d099dc919895bdf8"

parameters = {
    "lat" : 45.93,
    "lon" : 5.8,
    "appid" : apiKey,
    "cnt" : 4, #sadece 4 veriyi eçkiyor sınır koymuş oluyoruz
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",
                        params=parameters)
response.raise_for_status()
listData = response.json()["list"]

for dayly in listData:
    newId = dayly["weather"][0]["id"]
    if newId > 500:
        print("You must take a shamp")
        break