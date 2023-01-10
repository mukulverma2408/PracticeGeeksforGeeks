#Drop rows from the dataframe based on certain condition applied on a column

import pandas as pd
df = pd.read_csv('/home/mukul/PycharmProjects/ImportingData/nba.csv')
print(df.head())
print(df.shape)
print(df.info())
#Filter row where player age is > 25

index = df[df['Age'] > 25]
df.drop(index, inplace=True)