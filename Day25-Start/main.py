# message = "hello"
# for i, x in enumerate(message):
#     print(i+1, x, sep="-")

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     next(data)
#     for row in data:
#         temperatures.append(int(row[1]))
#
# print(temperatures)
# print(data)

import pandas

data = pandas.read_csv("weather_data.csv")

# print(data)
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
# data_list = data["temp"].tolist()
# print(data_list)
# print(data["temp"].mean())
# print(data["temp"].max())
print(data[data["temp"] == data["temp"].min()])
tuesday = data[data.day == "Tuesday"]
print(tuesday.temp)
print(tuesday.temp[1])
# new_dict = {'day': ['Monday', 'Tuesday'],
#             'temp': [12, 14],
#             'condition': ['Sunny', 'Rain']}
# test_data = pandas.DataFrame(new_dict)
# test_data.to_csv("new_text.csv")

# new_data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 58, 64]
# }
# new_data = pandas.DataFrame(new_data_dict)
# new_data.to_csv("new_data.csv")

# # Primary Fur Color, Count
# squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# squirrel_color = squirrel_data["Primary Fur Color"]
# gray_count = len(squirrel_data[(squirrel_data["Primary Fur Color"] == "Gray")])
# black_count = len(squirrel_data[(squirrel_data["Primary Fur Color"] == "Black")])
# cinnamon_count = len(squirrel_data[(squirrel_data["Primary Fur Color"] == "Cinnamon")])
# print(squirrel_data["Primary Fur Color"])
# squirrel_dict = {
#     "Fur Color": ["Gray", "Black", "Cinnamon"],
#     "Count": [gray_count, black_count, cinnamon_count]
# }
# squirrel_count_data = pandas.DataFrame(squirrel_dict)
# squirrel_count_data.to_csv("squirrel_count.csv")
