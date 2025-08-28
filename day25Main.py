import csv

with open("weather_data.csv") as dataFile:
    data = csv.reader(dataFile) #csv dosyasının her satırını birer liste çevirir
    tempature = []
    for row in data:
        if row[1] == "temp":
            continue
        tempature.append(int(row[1])) #1 numaralı bir sütundaki elemanlar 
        #farklı bir listeye kaydediliyor.

print(tempature)