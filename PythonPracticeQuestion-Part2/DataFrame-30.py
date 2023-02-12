#Formatting float column of Dataframe in Pandas
#Code  # 1 : Round off the column values to two decimal places.
#use pd.option.display.float.format
import pandas as pd
# create the data dictionary
data = {'Month': ['January', 'February', 'March', 'April'],
        'Expense': [21525220.653, 31125840.875, 23135428.768, 56245263.942]}

# create the dataframe
df = pd.DataFrame(data, columns=['Month', 'Expense'])

print("Given Dataframe :\n", df)

df['Expense'] = df['Expense'].astype(float)

print(df)