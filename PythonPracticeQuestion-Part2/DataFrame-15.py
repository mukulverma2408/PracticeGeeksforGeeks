#Insert row at given position in Pandas Dataframe
import pandas as pd
# Let's create the dataframe
df1 = pd.DataFrame({'Date': ['10/2/2011', '12/2/2011', '13/2/2011', '14/2/2011'],
                   'Event': ['Music', 'Poetry', 'Theatre', 'Comedy'],
                   'Cost': [10000, 5000, 15000, 2000]})

# Let's visualize the dataframe
#counter = df.shape[0]
print(df1)
dict = {'Date':['11/2/2011'], 'Event':['Artist'], 'Cost':[2000]}
df2 = pd.DataFrame(dict)
print(df2)

#df3 = df1.append(df2)
#print(df3)

first_half = df1.iloc[:1, :]
second_half= df1.iloc[1:, :]
print(first_half)
print(second_half)

df = first_half.append([df2, second_half], ignore_index=True)
print(df)