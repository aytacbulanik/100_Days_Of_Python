import pandas

data = pandas.read_csv("weather_data.csv")
monday = data[data.day == "Monday"]
print(type(monday))