import numpy as np
import pandas as pd

df = pd.read_csv("/home/paulo.martins/Downloads/bike-sharing.csv")
# cs = df['casual'] > 3
temp = df['temp'].mean()
# casual_registered = df[df['casual'].isin([-1, 32])]
# casual_registered = df[(df['casual'] == 1) | (df['registered'] == 0) | (df['total_count'].notna())]
# season = df.loc[df['year'] != 0, 'season']
season = df.iloc[:, :]
if __name__ == '__main__':
    # print(df.head())
    # print(cs)
    # print(df.head())
    # print(df.head())
    # print(df.loc[df['temp'].median()])
    print(temp)
