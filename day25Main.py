#import csv

#with open("weather_data.csv") as dataFile:
#    data = csv.reader(dataFile) #csv dosyasının her satırını birer liste çevirir
#    tempature = []
#    for row in data:
#        if row[1] == "temp":
#            continue
#        tempature.append(int(row[1])) #1 numaralı bir sütundaki elemanlar 
#        #farklı bir listeye kaydediliyor.

#print(tempature)

import pandas

data = pandas.read_csv("weather_data.csv") #pandasta dataframe nesnesine dönüştürüyor.
dataDic = data.to_dict() #pandas dataFrame nesnesini dictionarye çeviriyor
tempList = data["temp"].to_list() #burada series nesnesi olan temp sütunu
#listeye çeviriyor.
newSeries = data["temp"] #dic mantığıyla bir dataframe objesini çağırırsak 
# bunu series nesnesine çeviriyor. her sütun bir series nesnesidir.
avg = newSeries.mean() #series nesnesindeki raklamların ortalamasını alıyor
data.temp #series nesnelerine .nesnegenel adı ile de ulaşılabilir
data[data.temp == 14] #bu şekilde her satırda arama yaparak sıcaklığı 14 olan
#satırları getiriyor.
data[data.day == "Monday"] #bu aramada günlerden monday olan satırı getiriyor.

maxTemp = data.temp.max()
print(data[data.temp == maxTemp]) #en yüksek sıcaklığa sahip satırı listeliyoruz

monday = data[data.day == "Monday"]
print(monday.temp * 9/5 + 32) #monday günüdeki sıcaklık değerini f e çevirdik

#pandas kütüphanesi kullanarak bir dict nesnesini dataFrame sonrada csv dosyasına çevirebiliriz.
dataDict = {
    "student" : ["ahmet","ayşe","Hülya"],
    "scores" : [75,45,60]
}
datamiz = pandas.DataFrame(dataDict) #pandas kullanarak dict dataFrame e dönüştürüldü
datamiz.to_csv("newData.csv") #pandas kullanarak dataFrame nesnesinden yeni bir csv dosyası oluşturuyoruz.
