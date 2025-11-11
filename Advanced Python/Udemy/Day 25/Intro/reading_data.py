# with open("weather_data.csv") as csvfile:
#      data = csvfile.readlines()
#      print(data)
import csv
with open("weather_data.csv") as file:
     data = csv.reader(file)
     temperatures = []
     for row in data:
         if row[1] != "temp":
             temperatures.append(int(row[1]))
     print(temperatures)