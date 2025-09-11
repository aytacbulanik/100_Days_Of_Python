numbers = [1,2,3,4]
newList = [str(n*2) for n in numbers] # liste deki her bir elemanı alıp ikiyle çarpıp stringe çeviriyor ve  yeni bir listeye atıyor

newList2 = [name for name in numbers if name < 3] #koşula uygun elemanı listeye ekliyor. if bloğunu sağlarsa ekeleniyor

#aşağıdaki örnekte stringler den oluşan bir listeyi çift olanları süzerek yeni bir sayı listesi oluşturuluyor.
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(letter) for letter in list_of_strings]
result = [number for number in numbers if number %2 == 0]

#aşağıda iki dosyadan okunan harflerin boşluklarını alıp yeni bir dizye int olarak ekleniyor ve iki dizideki ortak elemanlar karşılaştırılıyor.
newListA = []
anotherArray = []
with open("file1.txt") as file1:
        newListA = [int(line.strip()) for line in file1] #herbir satırın boşluğunu sildi ve int çevirerek yeni dizi oluşturuyor
with open("file2.txt") as file2:
    anotherArray = [int(line.strip()) for line in file2]
result = [number for number in newListA if anotherArray.__contains__(number)] #iki dizideki ortak elemanı çekiyor. yeni diziye ekliyor.
