import pandas as pd
data = pd.read_csv('weather.csv')
# print(type(data["temp"]))
# print(type(data))
# print(data["temp"].head(4))
# print(data.head(4))
# data_dict = data.info()
# print(data_dict)
# sum_of_temp = 0
list_of_numbers = data["temp"].to_list()
# for number in range(len(list_of_numbers)):
#     list_of_numbers[number] = int(list_of_numbers[number])
#     sum_of_temp += list_of_numbers[number]
# average_of_temp = sum_of_temp / len(list_of_numbers)
# print(average_of_temp)
max_temp = data["temp"].max()
mean_of_temp = data["temp"].mean()
# print(data["condition"])
# print(list_of_numbers)
# print(max_temp)
# print(mean_of_temp)
# print(mean_of_temp)
# print(max_temp)

# data_max = data.temp.max()
# print(data_max)

# data_monday = data[data.day== "Monday"]
# print(data_monday)
#
# print(data.day[data.temp == data.temp.max()])
# monday_temp = data.temp[data.day == "Monday"] * 9/5 + 32
# print(monday_temp)
# monday = data[data.day == "Monday"]
# temp_mon = monday.temp
# tmep_f_mon = temp_mon * 9/5 + 32
# print(tmep_f_mon)


# Create DataFrame from scratch
data_dict = {"student": ["angela", 'kibet'],
             "marks": [23,87]
                }
data_frame = pd.DataFrame(data_dict)
print(data_frame)
data_frame.to_csv('weather2.csv', index=False)