import pandas as pd

REdf = pd.read_csv('data/weekly_housing_market_data_most_recent.tsv',delimiter='\t')
listingsdf = pd.read_csv('data/listings.csv')

import gzip
import shutil
with gzip.open('data/calendar.csv.gz', 'rb') as f_in:
    with open('data/calendar.csv', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
        
with gzip.open('data/listings.csv.gz', 'rb') as f_in:
    with open('data/listings2.csv', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
        
cal_df = pd.read_csv('data/calendar.csv')

listingsdf2 = pd.read_csv('data/listings2.csv')