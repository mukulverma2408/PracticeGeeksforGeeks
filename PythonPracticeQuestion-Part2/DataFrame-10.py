#How to iterate over rows in Pandas Dataframe
import pandas as pd
input_df = [{'name':'Sujeet', 'age':10},
            {'name':'Sameer', 'age':11},
            {'name':'Sumit', 'age':12}]

df = pd.DataFrame(input_df)
#print(df)

for index, row in df.iterrows():
    print(index, row['name'], row['age'])
