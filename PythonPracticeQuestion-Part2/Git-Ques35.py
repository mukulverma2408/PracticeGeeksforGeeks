#https://github.com/guipsamora/pandas_exercises/blob/master/01_Getting_%26_Knowing_Your_Data/Chipotle

import pandas as pd
chipo = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv", sep='\t')
pd.set_option('display.max_columns', None)
#print(chipo.head(10))
#print(chipo.shape[0])
#print(chipo.info())
#print(chipo.shape[1])
#print(chipo.columns)
#print(chipo.index)
#print(chipo.head(5))
