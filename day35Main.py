import requests
from twilio.rest import Client

apiKey = "3ab9c00817b1ff26d099dc919895bdf8"
account_sid = "AC936ac74c343ddc9f0b3eb7d9dcb25b9d"
auth_token = "2081cf3226af4f0ab0e17312de310e4c"

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

willRain = False
for dayly in listData:
    newId = dayly["weather"][0]["id"]
    if newId > 500:
        willRain = True    
if willRain:
    
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    content_sid='HX229f5a04fd0510ce1b071852155d3e75',
    content_variables='{"1":"409333"}',
    to='whatsapp:+905342447447'
    )

    print(message.sid)