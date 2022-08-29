import pandas as pd
# Create the dataframe
df = pd.DataFrame({'Date': ['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                   'Product': [' UMbreLla', '  maTress', 'BaDmintoN ', 'Shuttle'],
                   'Updated_Price': [1250, 1450, 1550, 400],
                   'Discount': [10, 8, 15, 10]})
# Print the dataframe
for i in range (df.shape[0]):
    #print(i)
    #print(df.iloc[i, 1])
    df.iloc[i,1] = df.iloc[i,1].strip().capitalize()
print(df)
