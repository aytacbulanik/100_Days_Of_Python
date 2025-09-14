import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
name = "aytac".upper()
spellName = []
newDict = { row.letter : row.code for (index , row) in data.iterrows()}
spellName = [ newDict[letter] for letter in name]
print(spellName)