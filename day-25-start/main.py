# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)
#
# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures: list = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(data["temp"].max())

print(data[data.temp == data.temp.max()])