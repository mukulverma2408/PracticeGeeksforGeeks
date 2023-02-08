#Return the Index label if some condition is satisfied over a column in Pandas Dataframe
import pandas as pd
# Create the dataframe
df = pd.DataFrame({'Date': ['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                   'Product': ['Umbrella', 'Mattress', 'Badminton', 'Shuttle'],
                   'Last_Price': [1200, 1500, 1600, 352],
                   'Updated_Price': [1250, 1450, 1550, 400],
                   'Discount': [10, 10, 10, 10]})

# Create the indexes
df.index = ['Item 1', 'Item 2', 'Item 3', 'Item 4']

# Print the dataframe
print(df)

#Now, we want to find out the index labels of all items whose ‘Updated_Price’ is greater than 1000.
counter = df.shape[0]
item = df[df['Updated_Price'] > 1000].index
print(item)

