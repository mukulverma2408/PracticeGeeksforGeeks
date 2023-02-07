#How to rename columns in Pandas DataFrame
#Rename a single column
import pandas as pd
# Define a dictionary containing ICC rankings
rankings = {'test': ['India', 'South Africa', 'England',
                     'New Zealand', 'Australia'],
            'odi': ['England', 'India', 'New Zealand',
                    'South Africa', 'Pakistan'],
            't20': ['Pakistan', 'India', 'Australia',
                    'England', 'New Zealand']}

# Convert the dictionary into DataFrame
rankings_pd = pd.DataFrame(rankings)

print(rankings_pd)

rankings_pd.rename({'test': 'Test_Ranking', 'odi': 'ODI_Ranking', 't20': 'T20_Ranking'}, axis=1, inplace=True)
print(rankings_pd)