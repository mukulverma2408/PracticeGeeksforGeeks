#How to get column names in Pandas dataframe
# Import pandas package
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

#print(data.head())
for col_name in data.columns:
    print(col_name)