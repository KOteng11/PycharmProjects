# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data["temp"]))
# print(type(data))

data_dict = data.to_dict()
# print(data_dict)

# print(data['temp'].max())
#
# print(data.temp.max())
#
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# monday_temp = monday.temp[0]
# print((monday_temp * 9 / 5) + 32)

# Create a dataframe from scratch
data_dict = {
    'student': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("new_data.csv")