import pandas as pd

data = pd.read_csv("E:/Training Materials/Pylabs\data.csv")
print(data.loc[data['ID'] == 1, 'Grade'].item())
# print(data.Grade[data.ID == 1].item())
# print(data.loc[data['ID'] == 1, ['Grade', 'Math']])

# # data_values = data["ID"] == 1
# # print(data.loc[data_values,'Grade'].item())

print(data.loc[data["Name"] == "Bob", ["Grade", "English", "Math"]])