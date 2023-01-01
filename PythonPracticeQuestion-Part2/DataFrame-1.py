#Make a Pandas DataFrame with two-dimensional list
import pandas as pd
lst = [['Geek', 25], ['is', 30],
       ['for', 26], ['Geeksforgeeks', 22]]

df = pd.DataFrame(lst, columns=['Tag', 'Number'])
print(df, type(df))