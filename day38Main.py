import requests

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 174
AGE = 44
xappid = "app_500abcfe0b8d45fa84852786"
xappkey = "nix_live_1oW8hv05jKPP9EeESMZaY2XX8yUhzRHG" #"x-app-key"

baseEndpoint = "https://app.100daysofpython.dev"
excersizeEndpoint = f"{baseEndpoint}/v1/nutrition/natural/exercise"

headers = {
    "x-app-id" : xappid,
    "x-app-key" : xappkey
}

dataJson = {
    "query" : "some practise",
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age" : AGE,
    "gender" : GENDER
}
response = requests.post(url=excersizeEndpoint,headers=headers,json=dataJson)
print(response.json())


