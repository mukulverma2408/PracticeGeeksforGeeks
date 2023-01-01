#Creating Pandas dataframe using list of lists
import pandas as pd
data = [['Geeks', 10], ['for', 15], ['geeks', 20]]

df = pd.DataFrame(data, columns=['Tag', 'Value'])
print(df)