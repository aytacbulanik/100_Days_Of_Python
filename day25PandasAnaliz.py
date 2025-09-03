import pandas

data = pandas.read_csv("2018Data.csv")
graySeries = pandas.Series(data.PrimaryFurColor[data.PrimaryFurColor == "Gray"])
grayCount = graySeries.count()
redSeries = pandas.Series(data.PrimaryFurColor[data.PrimaryFurColor == "Cinnamon"])
redCount = redSeries.count()
blackSeries = pandas.Series(data.PrimaryFurColor[data.PrimaryFurColor == "Black"])
blackCount = blackSeries.count()

newTable = pandas.DataFrame({"Fur color" : ["gray","red","black"] , "count" : [grayCount,redCount,blackCount]})
#newTable.to_csv("cincapCount.csv")