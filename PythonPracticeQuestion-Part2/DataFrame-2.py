#Python | Creating DataFrame from dict of narray/lists
import pandas as pd

data = {'Category':['Array', 'Stack', 'Queue'],
        'Marks':[20, 21, 19]}

df = pd.DataFrame(data)
print(df)
