import pandas as pd
df = pd.read_csv("/home/mukul/PycharmProjects/ImportingData/Automobile_data.csv", index_col=0)
#print(df.head())
#print(df.tail())

print(df[df['price'] == df['price'].max()])
