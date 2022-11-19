import pandas as pd

df = pd.read_csv('~/Downloads/uk-500.csv')
#print(df.head())

#print lasst columns
#print(df.iloc[:, -1])

#print first row and first column
#print(df.iloc[[0,1], [0,3]])

print(df.iloc[[1,7], 0:3])