#How to randomly select rows from Pandas DataFrame
import pandas as pd
import random
# Define a dictionary containing employee data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj', 'Geeku'],
        'Age': [27, 24, 22, 32, 15],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj', 'Noida'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd', '10th']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
#print(df)
counter = random.randint(0,4)
print('===================================')
print(counter)
print(df.iloc[counter, 0:3])