import pandas
import csv



# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)


#data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# # print(temp_list)
#
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# print(data["temp"].mean())
#
# print(data["temp"].max())
# # Get data in columns
# print(data.temp)

# Get data in row
# print row where temp is max
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# #print(monday.condition)
#
# # celsius to fahrenheit: F = (C * 9/5) + 32.
# fahrenheit = (monday.temp * 9/5) + 32
# print(fahrenheit)

# Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# Code to count color of squirrels and export to squirrel_count.csv
data = pandas.read_csv("squirrel_census.csv")

# Turn column names to not have spaces and be lowercase
# data["Primary Fur Color"] == "Gray" --> could have worked too
data.columns = [c.replace(' ', '_').lower() for c in data.columns]

gray = data[data.primary_fur_color == "Gray"]
cinnamon = data[data.primary_fur_color == "Cinnamon"]
black = data[data.primary_fur_color == "Black"]

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [len(gray), len(cinnamon), len(black)]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")