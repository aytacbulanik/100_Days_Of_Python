import requests
#post metodunu gönderirken bu sefer değer yazmak için gerekli parametreleri
#giriyoruz.
pixelaEndpoint = "https://pixe.la/v1/users"
userName = "aytacbulanik"
userToken = "hbs6s906svdvaovmau3ja5"
userParams = {
    "token" : userToken,
    "username" : userName,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}
#post metodunda json parametresi kullanarak veriyi gönderiyoruz.
# response = requests.post(url=pixelaEndpoint,json=userParams)
# print(response.text) #response kısmındaki cevabı almak için yazıyoruz.


graphsEndpoint = f"{pixelaEndpoint}/{userName}/graphs"

graphConfig = {
    "id" : "graph1",
    "name" : "My Hoobit",
    "unit" : "Km",
    "type" : "float",
    "color" : "shibafu"
}
#burası api dökümanında header alanı girilmesi zorunlu ve token istiyor.
headers = {
    "X-USER-TOKEN" : userToken
}

# response = requests.post(url=graphsEndpoint,json=graphConfig,headers=headers)
# print(response.text)

setPixelEndpoint = f"https://pixe.la/v1/users/{userName}/graphs/graph1"

pixelConfig = {
    "date" : "20251120",
    "quantity" : "3.2"
}

response = requests.post(url=setPixelEndpoint,json=pixelConfig,headers=headers)
print(response.text)