import pandas as pd
data = pd.read_csv('Squirrel_Data.csv')
# Lets count the number of instances
gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])
# We use len() for count because we are dealing with tuples
# Lets create a data dictionary
data_dict = {
    "Primary Fur Color": ["Gray","Cinnamon","Black" ],
    "Count": [gray,red,black]
}
data_file = pd.DataFrame(data_dict)
data_file.to_csv('Squirrel_Data_Color.csv')





