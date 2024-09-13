#
# with open("weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv('weather_data.csv')

# # print(type(data))  # = <class 'pandas.core.frame.DataFrame'> => LIKE EXCEL TABLE
# print(type(data["temp"]))  # = <class 'pandas.core.series.Series'> => LIKE JUST ONE COLUMN OF AN EXCEL TABLE

# data_dict = data.to_dict()
# print(data_dict)
# ---------------------------------------------------------------------------------------------------------------------

# temp_list = data["temp"].to_list()
# print(f"Length of the list 'Temperatures' : {len(temp_list)}")
#
# print(f"Mean of temperatures : {data["temp"].mean().round(2)}")
#
# print(f"Maximum value of temperatures : {data['temp'].max()}")

# ---------------------------------------------------------------------------------------------------------------------
# Getting data[condition] in columns
# print(data["condition"])
# Additionally, we can achieve this through that method.
# print(data.condition)
# Pandas does the jobs behind the scene, allowing us to manage our data by using the dot notation
# But you need to be aware of the column name you are using, as this process is case-sensitive.

# ---------------------------------------------------------------------------------------------------------------------

# Getting data in rows
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(f"The Temperature on Monday is {monday["temp"]*9/5 + 32} degrees Fahrenheit")

# --------------------------------------------------------------------------------------------------------------------

# # Creating a DataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "John"],
#     "scores": [76, 56, 65]
# }
# data_2 = pandas.DataFrame(data_dict)
# print(data_2)
# data_2.to_csv('new_data.csv')

# --------------------------------------------------------------------------------------------------------------------

bdata = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

black_fur = sum(bdata["Primary Fur Color"] == "Black")
cinnamon_fur = sum(bdata["Primary Fur Color"] == "Cinnamon")
gray_fur = sum(bdata["Primary Fur Color"] == "Gray")

print(black_fur)
print(cinnamon_fur)
print(gray_fur)

fur_colors = {
    "Fur Color": ["Black", "Cinnamon", "Gray",],
    "Count": [black_fur, cinnamon_fur, gray_fur],
}
fur_color_datas = pandas.DataFrame(fur_colors)
fur_color_datas.to_csv("fur_colors.csv")

squirrel_data = pandas.read_csv("fur_colors.csv")
print(squirrel_data)


