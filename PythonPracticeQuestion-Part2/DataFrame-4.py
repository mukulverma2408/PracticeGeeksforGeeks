#Clean the string data in the given Pandas Dataframe
import pandas as pd
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                   'Product':[' UMbreLla', '  maTtress', 'BaDmintoN ', 'Shuttle'],
                   'Updated_Price':[1250, 1450, 1550, 400],
                   'Discount':[10, 8, 15, 10]})
print(df)
word = print(df.iloc[0][1])

#df.iloc[0][1] = df.iloc[0][1].strip().capitalize()
df.iat[0,1] = df.iat[0,1].strip().capitalize()
print(df.iloc[0][1])

"""
def Format_Dataframe(dataframe):
    for i in range(dataframe.shape[0]):
        print(dataframe[i][1])

Format_Dataframe(df)
"""