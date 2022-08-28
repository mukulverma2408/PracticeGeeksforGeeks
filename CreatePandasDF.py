#Create Pandas Datframe from List
import pandas as pd
lst = [['Geek', 25], ['is', 30],
       ['for', 26], ['Geeksforgeeks', 22]]
#print(lst)
df = pd.DataFrame(lst, columns=['Tag', 'Numbers'])
print(df)

