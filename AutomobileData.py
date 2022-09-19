import pandas as pd
df = pd.read_csv("/home/mukul/PycharmProjects/ImportingData/Automobile_data.csv", index_col=0)
#print(df.head())
#print(df.info())
#print(df.tail())

max_price = df[df['price'] == df['price'].max()]
toyota_car = df[df['company'] == 'toyota']
car_group = df['company'].value_counts()
#print(car_group)

car_company = df.groupby('company')
pricedf = car_company['company', 'price'].max()
#print(pricedf)

AvgMileage = car_company['company', 'average-mileage'].mean()
#print(AvgMileage)

price_sort = df.sort_values(['price'], ascending = False)
#print(price_sort)

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
German = pd.DataFrame.from_dict(GermanCars)
#print(German)
Japan = pd.DataFrame.from_dict(japaneseCars)
#print(Japan)

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

df1 = pd.DataFrame.from_dict(Car_Price)
df2 = pd.DataFrame.from_dict(car_Horsepower)
df3 = pd.merge(df1, df2, on='Company')
print(df3)



