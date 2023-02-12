#Using dictionary to remap values in Pandas DataFrame columns

import pandas as pd

# Creating the DataFrame
df = pd.DataFrame({'Date': ['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                   'Event': ['Music', 'Poetry', 'Theatre', 'Comedy'],
                   'Cost': [10000, 5000, 15000, 2000]})

# Print the dataframe
print(df)

dict = {'Music': 'M', 'Poetry' : 'P', 'Theatre' : 'T', 'Comedy' : 'C'}
df.replace({"Event": dict}, inplace=True)

print(df)
