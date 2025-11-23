import requests
from datetime import datetime as dt

#antreman verisini girecek kişinin genele bilgileri değişken olarak alınıyor.
GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 174
AGE = 44
#api keyler
xappid = "app_500abcfe0b8d45fa84852786"
xappkey = "nix_live_1oW8hv05jKPP9EeESMZaY2XX8yUhzRHG" #"x-app-key"
#zamanı tarih ve saat olarak ayırıyoruz.
now = dt.now()
nowDate = now.strftime("%d/%m/%Y")
nowTime = now.strftime("%H:%M:%S")
#end pointler
baseEndpoint = "https://app.100daysofpython.dev"
excersizeEndpoint = f"{baseEndpoint}/v1/nutrition/natural/exercise"
sheetEndpoint = "https://api.sheety.co/426a997d2a4c936fab96ea547b7071dd/myProject/works"
#endpointlere istek atarken kullanılan headerslar
headers = {
    "x-app-id" : xappid,
    "x-app-key" : xappkey
}

bearer_headers = {
    "Authorization": "Basic YXl0YWNidWxhbmlrOkE5ODQ2OTg0NmE/"
}
#antreman api için json ile post isteği atıyoruz.
dataJson = {
    "query" : "swam for 1 hour",
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age" : AGE,
    "gender" : GENDER
    }

response = requests.post(url=excersizeEndpoint,json=dataJson,headers=headers)
result = response.json()
#cevap olarak dönen veri de işimize yarayan verileri alıp google sheet e yazacağız.
for exercise in result["exercises"]:
    sheet_inputs = {
        "work": {
            "date": nowDate,
            "time": nowTime,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheetEndpoint, json=sheet_inputs,headers=bearer_headers)

    print(sheet_response.text)


