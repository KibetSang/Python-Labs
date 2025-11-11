import pandas as pd
data = {
    "Name": ["John", "Kamau", "Samy"],
    "Age": [90, 80, 40],
    "Country": ["USA", "Kenya", "Uganda"]
}

df = pd.DataFrame(data)
# age = df [df["Country"] =="USA"]["Age"].item()
# print(age)
print(df.iloc[:,1])