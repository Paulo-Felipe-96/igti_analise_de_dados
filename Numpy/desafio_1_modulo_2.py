import pandas as pd
import numpy as np

df = pd.read_csv("/home/paulo.martins/Downloads/bike-sharing.csv")
# print(df.head())

length_dataframe = df.shape
media_temp = df['temp'].mean()
media_windspeed = df['windspeed'].mean()
registers_2011 = df[(df['datetime'] >= '2011') & (df['datetime'] < '2012')].shape
registers_2012 = df[(df['datetime'] >= '2012') & (df['datetime'] < '2013')].shape
b = df[(df['datetime'] >= '2012') & (df['datetime'] < '2013')].sum()

for i in range(0, 24):
    wd_hr_md = df[(df['weekday'] == 6) & (df['hour'] == i)].mean()
    print(f'Hora do dia {i}h: {wd_hr_md["total_count"]}')

# for i in range(1, 5):
#     season = df[(df['season'] == i)].mean()
#     print(f'Estação do ano {i}: {season["total_count"]}')

# for i in range(0, 7):
#     wday = df[(df['weekday'] == i)].mean()
#     print(f'Weekday {i}: {wday["total_count"]}')

# if __name__ == '__main__':
# print(df.head())
# print(length_dataframe)
# print(media_temp)
# print(media_windspeed)
# print(registers_2011)
# print(registers_2012)
# print(b)
