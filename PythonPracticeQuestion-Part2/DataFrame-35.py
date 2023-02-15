#Getting frequency counts of a columns in Pandas DataFrame
# importing pandas as pd
import pandas as pd

# sample dataframe
df = pd.DataFrame({'A': ['foo', 'bar', 'g2g', 'g2g', 'g2g',
                         'bar', 'bar', 'foo', 'bar'],
                   'B': ['a', 'b', 'a', 'b', 'b', 'b', 'a', 'a', 'b']})
print(df)

print(df['B'].value_counts())