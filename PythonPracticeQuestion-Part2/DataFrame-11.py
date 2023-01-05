#Selecting rows in pandas DataFrame based on conditions
import pandas as pd
record = {

    'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya'],
    'Age': [21, 19, 20, 18, 17, 21],
    'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'],
    'Percentage': [88, 92, 95, 70, 65, 78]}

df = pd.DataFrame(record)
print(df[df['Percentage'] > 80])
print(df.query('Percentage > 80'))