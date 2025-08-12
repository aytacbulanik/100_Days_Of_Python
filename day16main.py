from prettytable import PrettyTable
table = PrettyTable()
table.add_column("İsimler",["Ali","Ayşe","Mehmet"])
table.add_column("Yaşlar", [25, 30, 22])
print(table)