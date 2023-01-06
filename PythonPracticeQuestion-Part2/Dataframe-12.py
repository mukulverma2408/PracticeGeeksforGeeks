#Select any row from a Dataframe using iloc[] and iat[] in Pandas
import pandas as pd
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11'],
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
                    'Cost':[10000, 5000, 15000, 2000]})

print(df)
print(df.iloc[[1,2], [2]])
