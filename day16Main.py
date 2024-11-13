from prettytable import PrettyTable 

table = PrettyTable()

table.add_column("Ad", ["ali","aytaç","mehmet","yeşim"])
table.add_column("Soyad", ["mehemt","kimya","öztürk","sönmez"], align="l")
print(table)
