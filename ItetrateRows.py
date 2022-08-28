#Python Progg to itetrate over rows -
import pandas as pd
input_df = [{'name':'Sujeet', 'age':10},
            {'name':'Sameer', 'age':11},
            {'name':'Sumit', 'age':12}]
df = pd.DataFrame(input_df)
#print(df)
for index, row in df.iterrows():
    #print(row['name'], row['age'])
    pass
for row in df.itertuples():
    print(row[1], row[2])
