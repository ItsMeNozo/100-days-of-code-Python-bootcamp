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

import pandas

data = pandas.read_csv("weather_data.csv") # pandas read file for you, no need to open file
temp_series = data["temp"]
# temp_list = data["temp"].to_list()
# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)
# print(data[data.temp == data.temp.max()]) # print row with max temp
# print(data[data.day == "Monday"].condition)
monday_temp = int(data[data.day == "Monday"].temp)
monday_temp_f = monday_temp * 1.8 + 32
# print(monday_temp_f)

# Create DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
# export csv file as "new_data.csv"
data.to_csv("new_data.csv")