import pandas as pd

data = pd.read_csv("../../../Desktop/100 Days of Code The Complete Python Pro Bootcamp for 2023/25 - Day 25 - Intermediate - Working with CSV Data and the Pandas Library/004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

df = pd.DataFrame(data)

#print(df.head())
#colors_df = df["Primary Fur Color"].value_counts()
#print(colors_df)

#colors_df.to_csv('colors_data.csv')

df["Primary Fur Color"].value_counts().to_csv('colors_data.csv')