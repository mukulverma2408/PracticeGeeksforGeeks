#Python Progg to create a pandas column using for loop
import pandas as pd
lst = [['Ankur', 38], ['Mukul', 36], ['Vishu', 30], ['Nikita', 25]]
eligible = []
df = pd.DataFrame(lst, columns=['Name', 'Age'])
#print(df)
for i in df['Age']:
    if i > 35:
        eligible.append('Old')
    elif i < 35:
        eligible.append('New')
df['eligiblity'] = eligible

print(df)
