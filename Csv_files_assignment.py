#writing a csv file
import csv
import pandas as pd

data = {"Name": ["Patience", "Okafor", "James","David","Teejah","Onwumi"],
        "Age":[23,21,25,23,22,20]
        }

data = pd.DataFrame(data)
data.to_csv("age_data.csv",index=False)
print(data.head())

data = pd.read_csv("age_data.csv")
print(data.head())