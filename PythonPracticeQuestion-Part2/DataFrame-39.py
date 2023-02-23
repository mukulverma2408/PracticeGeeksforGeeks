#Get n-largest values from a particular column in Pandas DataFrame
import pandas as pd

# making data frame
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

print(df.head(5))
#Get top 5 salary
df_sal = df.query("select Salary from df")
print(df_sal.head())