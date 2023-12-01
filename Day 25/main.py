# בס״ד

import pandas as pd

raw_data = pd.read_csv("../../../Desktop/100 Days of Code The Complete Python Pro Bootcamp for 2023/25 - Day 25 - "
                       "Intermediate - Working with CSV Data and the Pandas Library/002 weather-data.csv")

df = pd.DataFrame(raw_data)
avg_temp = round(df.temp.mean())

print(df[df.temp == df.temp.max()]['temp'])
print(avg_temp)
