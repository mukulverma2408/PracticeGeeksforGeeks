#Get all rows in a Pandas DataFrame containing given substring
#1: Filter all rows where either Team contains ‘Boston’ or College contains ‘MIT’.
# importing pandas
import pandas as pd

# Creating the dataframe with dict of lists
df = pd.DataFrame({'Name': ['Geeks', 'Peter', 'James', 'Jack', 'Lisa'],
                   'Team': ['Boston', 'Boston', 'Boston', 'Chele', 'Barse'],
                   'Position': ['PG', 'PG', 'UG', 'PG', 'UG'],
                   'Number': [3, 4, 7, 11, 5],
                   'Age': [33, 25, 34, 35, 28],
                   'Height': ['6-2', '6-4', '5-9', '6-1', '5-8'],
                   'Weight': [89, 79, 113, 78, 84],
                   'College': ['MIT', 'MIT', 'MIT', 'Stanford', 'MIT'],
                   'Salary': [99999, 99994, 89999, 78889, 87779]},
                  index=['ind1', 'ind2', 'ind3', 'ind4', 'ind5'])
df = df.query('Team == "Boston" | College == "MIT"')
print(df)