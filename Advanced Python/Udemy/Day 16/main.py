from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Poke Mon", ["Pikuchu", "Lemon", "Quoar"])
table.add_column("Type", ["Main", "Siri", "Water"])
table.add_column("State", ["Mulima","Siri", "Water"])
table.align = "l"
print(table)