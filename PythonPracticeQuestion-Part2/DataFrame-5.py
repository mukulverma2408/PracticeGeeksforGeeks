#Reindexing in Pandas DataFrame
import pandas as pd
import numpy as np

column = ['a', 'b']
index = ['A', 'B']

# create a dataframe of random values of array
df = pd.DataFrame(np.random.rand(2, 2),
                   columns=column, index=index)
print("Original Dataframe is  - ")
print(df)

new_col = ['b', 'a']
new_index = ['B', 'A']

df1 = df.reindex(new_col, axis=1)
df2 = df.reindex(new_index)
print(df1)
print(df2)