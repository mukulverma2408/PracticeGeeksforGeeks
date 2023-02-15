#Split a text column into two columns in Pandas DataFrame

import pandas as pd

# create a new data frame
df = pd.DataFrame({'Name': ['John Larter', 'Robert Junior', 'Jonny Depp'],
                   'Age': [32, 34, 36]})

print("Given Dataframe is :\n", df)
lname = []
for nm in df['Name']:
    tmp = nm.split(' ')[1]
    lname.append(tmp)

df['Last Name'] = lname
print(df)


