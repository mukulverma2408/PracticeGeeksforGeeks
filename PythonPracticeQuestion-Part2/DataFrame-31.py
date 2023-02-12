#Create a new column in Pandas DataFrame based on the existing columns

import pandas as pd

# Creating the DataFrame
df = pd.DataFrame({'Date': ['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                   'Event': ['Music', 'Poetry', 'Theatre', 'Comedy'],
                   'Cost': [10000, 5000, 15000, 2000]})

# Print the dataframe
print(df)
#Now we will create a new column called ‘Discounted_Price’ after applying a 10% discount on the existing ‘Cost’ column.
df['DiscountedPrice'] = df['Cost']*90/100
print(df)
