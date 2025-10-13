try:
    file = open("./files/myFile.txt")
    aDict = {"key" : "Value"}
    print(aDict["key"])
    #her hata için ayrı bir except yapısı tanımlayabiliriz.
except KeyError as message:
    print(f"The key {message} does not exist")#hata mesajına değişken tanımlayıp kullanıyoruz
except FileNotFoundError:
    file = open("data.txt","w")
    file.write("something")
else:
    print("there was not an error") #hata olmayınca bu blog çalışır.
finally:
    file.close()
    print("her koşulda bu blog çalışacak.")