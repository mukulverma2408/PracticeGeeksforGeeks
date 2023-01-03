#Reshape a pandas DataFrame using stack, unstack and melt method
import pandas as pd
# making dataframe
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
# it was print the first 5-rows
print(df.head())

#df_stacked = df.stack()
#print(df_stacked.head(26))

df_melt = df.melt(id_vars=['Name', 'Salary'])
print(df_melt)