import pandas

data = pandas.read_csv("./files/nato_phonetic_alphabet.csv")

newDict = { row.letter : row.code for (index , row) in data.iterrows()}
def writeAlphabetic():
    name = input("Enter a word : ").upper()
    try:
        spellName = [ newDict[letter] for letter in name]
    except:
        print("Sorry, only letters in the alphabet")
        writeAlphabetic() #fonksiyon içerisine aynı fonksiyonu koyarsak recursive fonk kullanmış oluruz. otomatik döngü oluşur.
    else:
        print(spellName)

writeAlphabetic()