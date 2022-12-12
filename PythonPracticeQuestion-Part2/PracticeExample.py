import pandas as pd
"""
df = pd.read_csv('/home/mukul/PycharmProjects/ImportingData/Automobile_data.csv')
print(df.head())
#print(df.iloc[0,[1,2]])
#print(df.loc[0, ['company', 'body-style']])
print(df.iloc[[1,2,3],2])
"""

def fact(num):
    for i in range(num-1, 1, -1):
        num = num * (i)
    return num

def fact2(num):
    if num == 1:
        return num
    else:
        return (num * fact2(num-1))

print(fact(6))
print(fact2(6))
