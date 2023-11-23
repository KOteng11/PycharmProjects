from prettytable import PrettyTable
table_1 = PrettyTable()
table_1.align = "l"
table_1.field_names = ["Welcome to Python Pizza Deliveries"]
table_1.add_rows([
    ["Small Pizza: $15"],
    ["Medium Pizza: $20"],
    ["Large Pizza: $25"],
    ["Pepperoni for Small Pizza: +$2"],
    ["pepperoni for Medium or Large Pizza: +$3"],
    ["Extra cheese for any size Pizza: +$1"]
])
