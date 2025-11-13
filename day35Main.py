import requests
apiKey = "3ab9c00817b1ff26d099dc919895bdf8"

parameters = {
    "lat" : 36.71,
    "lon" : 37.10,
    "appid" : apiKey
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",
                        params=parameters)

print(response.json()["list"][0]["weather"][0]["description"])