#Python | Creating a Pandas dataframe column based on a given condition
import pandas as pd

# Creating the dataframe
df = pd.DataFrame({'Date': ['11/8/2011', '11/9/2011', '11/10/2011',
                            '11/11/2011', '11/12/2011'],
                   'Event': ['Music', 'Poetry', 'Music', 'Comedy', 'Poetry']})

# Print the dataframe
print(df)
# add a column called ‘Price’ which contains the ticket price for a particular day based on the type of event that will be conducted on that particular day.

dict = {'Music': 100, 'Poetry': 200, 'Comedy': 300}

df['Price'] = [1500 if x == 'Music' else 800 for x in df['Event']]
print(df)

df['UpdPrice'] = df['Event'].map(dict)
print(df)
