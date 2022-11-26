# with open("weather_data.csv") as csv_file:
#     contents = csv_file.readlines()
#
# data = []
# for line in contents:
#     data.append(line)
# print(data)

# import csv
#
# with open("weather_data.csv") as csv_file:
#     data = csv.reader(csv_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

# import pandas

# data = pandas.read_csv("weather_data.csv") # pandas read file for you, no need to open file
# temp_series = data["temp"]
# temp_list = data["temp"].to_list()
# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)
# print(data[data.temp == data.temp.max()]) # print row with max temp
# print(data[data.day == "Monday"].condition)
# monday_temp = int(data[data.day == "Monday"].temp)
# monday_temp_f = monday_temp * 1.8 + 32
# print(monday_temp_f)

# Create DataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# export csv file as "new_data.csv"
# data.to_csv("new_data.csv")
import pandas

# Task: extract a cvs file of fur color count in Primary fur color column
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# fur_color_list = data[data["Primary Fur Color"].isnull() == False]["Primary Fur Color"].to_list()
# fur_count_dict = {}
#
# for color in fur_color_list:
#     # if color.isnull():
#     #     continue
#     fur_count_dict[color] = fur_color_list.count(color)
# unique_fur_color_list = []
# count_list = []
# for color in fur_count_dict:
#     unique_fur_color_list.append(color)
#     count_list.append(fur_count_dict[color])
# csv_dict = {
#     "Fur Color": unique_fur_color_list,
#     "Count": count_list
# }
#
# fur_count_data = pandas.DataFrame(csv_dict)
# fur_count_data.to_csv("squirrel_count.csv")

# shorter code
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_count = data["Primary Fur Color"].value_counts()
color_count.to_csv("squirrel_count_fast.csv")