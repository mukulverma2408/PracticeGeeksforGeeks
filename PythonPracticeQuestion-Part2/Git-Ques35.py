#https://github.com/guipsamora/pandas_exercises/blob/master/01_Getting_%26_Knowing_Your_Data/Chipotle

import pandas as pd
chipo = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv", sep='\t')
pd.set_option('display.max_columns', None)
#print(chipo.head(5))
#print(chipo.shape[0])
#print(chipo.info())
#print(chipo.shape[1])
#print(chipo.columns)
#print(chipo.index)
#print(chipo.head(5))
#df1 = chipo.groupby('item_name')['item_name'].count()
#df1 = df1.sort_values(ascending = False)
#print(df1)

#df2 = chipo.groupby('choice_description')['choice_description'].count()
#df2 = df2.sort_values(ascending=False)
#print(df2.head(1))
#print(chipo['item_name'].count())

new_price = []
for i in chipo['item_price']:
    temp = float((i.split('$')[1]).split(' ')[0])
    new_price.append(temp)
#print((new_price))
chipo['flot_price'] = new_price

#print(chipo.head(5))
#print(chipo.info())
#print(chipo['flot_price'].dtype)

#print(chipo.head(5))
#print(chipo['order_id'].value_counts().count())

#print(chipo.info())
#print(chipo.head(3))
print(sum(chipo['quantity']* chipo['flot_price'])/chipo['order_id'].count())
#print(chipo['order_id'].count())