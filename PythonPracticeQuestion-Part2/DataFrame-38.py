#Get the index of maximum value in DataFrame column

import pandas as pd

# making data frame
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

print(df.head(10))
print(df['Salary'].idxmax())
print(df.iloc[109, :])
print(df['Salary'].max())