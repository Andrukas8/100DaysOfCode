from prettytable import PrettyTable
table1 = PrettyTable()

table1.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table1.add_row(["Adelaide", 1295, 1158259, 600.5])
table1.add_row(["Brisbane", 5905, 1857594, 1146.4])
table1.add_row(["Darwin", 112, 120900, 1714.7])
table1.add_row(["Hobart", 1357, 205556, 619.5])
table1.add_row(["Sydney", 2058, 4336374, 1214.8])
table1.add_row(["Melbourne", 1566, 3806092, 646.9])
table1.add_row(["Perth", 5386, 1554769, 869.4])
print(table1)


table2 = PrettyTable()
table2.field_names = ["Pokemon Name", "Type"]
table2.add_row(["Pikachu", "Electric"])
table2.add_row(["Squirtle", "Water"])
table2.add_row(["Charmander", "Fire"])

print(table2)


table3 = PrettyTable()
table3.add_column("Pkemon Name", ["Pikachu", "Squirtle", "Charmander"])
table3.add_column("Type", ["Electric", "Water", "Fire"])
table3.add_column("Cuteness Index", [10, 9, 8])
table3.align = "l"

print(table3)
