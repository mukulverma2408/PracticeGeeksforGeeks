#Python | Change column names and row indexes in Pandas DataFrame

import pandas as pd
df = pd.DataFrame({"Name": ['Tom', 'Nick', 'John', 'Peter'],
                   "Age": [15, 26, 17, 28]})

print(df)

df1 = df.rename(columns={'Name':'New_Name'})
df2 =  df.rename(columns=lambda x : x+'x')

print(df2)
