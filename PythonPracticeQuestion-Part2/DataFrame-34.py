#Getting Unique values from a column in Pandas dataframe
#Get unique continent
import pandas as pd

gapminder_csv_url = 'http://bit.ly/2cLzoxH'
# load the data with pd.read_csv
record = pd.read_csv(gapminder_csv_url)

print(record.head())
print(record['continent'].unique())