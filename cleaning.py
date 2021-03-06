def cleaning_city(cwd,city):
    import pandas as pd
    import gzip
    import shutil
    import re


    with gzip.open('{}/listings.csv.gz'.format(cwd), 'rb') as f_in:
        with open('{}/listings2.csv'.format(cwd), 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    citylistingsdf = pd.read_csv('{}/listings.csv'.format(cwd))
    citylistingsdf2 = pd.read_csv('{}/listings2.csv'.format(cwd))
    listingsdfcleaned = citylistingsdf[['id','name','host_id','neighbourhood','latitude','longitude','number_of_reviews','room_type','price','availability_365']]
    listings2dfcleaned = citylistingsdf2[['id','listing_url','name','neighbourhood_cleansed','latitude','longitude','property_type','room_type','accommodates','availability_30','bathrooms_text','bedrooms','beds']]

    listings_comb = pd.merge(listingsdfcleaned,listings2dfcleaned,on=['id','name','latitude','longitude','room_type'],how='outer')
    listings_comb = listings_comb.dropna()
    listings_comb = listings_comb.drop(['neighbourhood_cleansed'],axis=1)
    listings_comb['neighbourhood'] = listings_comb['neighbourhood'].astype('category')
    listings_comb['room_type'] = listings_comb['room_type'].astype('category')
    listings_comb['property_type'] = listings_comb['property_type'].astype('category')
    listings_comb['bedrooms'] = listings_comb['bedrooms'].astype('int')
    listings_comb['beds'] = listings_comb['beds'].astype('int')
    listings_comb['accommodates'] = listings_comb['accommodates'].astype('int')

    def get_bath(str):
        x = re.search('^\d\S*\S*\S*',str)
        if x:
            return x.group()

    listings_comb['bathrooms_text'] = listings_comb['bathrooms_text'].apply(get_bath)
    listings_comb['bathrooms_text'] = listings_comb['bathrooms_text'].astype('float')
    listings_comb = listings_comb[listings_comb['number_of_reviews'] >= 5]
    listings_comb['PricePerAccommodates'] = listings_comb['price']/listings_comb['accommodates']
    listings_comb['PricePerBedrooms'] = listings_comb['price']/listings_comb['bedrooms']
    listings_comb = listings_comb[listings_comb['PricePerAccommodates'] <= 500]
    listings_comb = listings_comb[listings_comb['room_type'] == 'Entire home/apt']
    listings_comb.to_csv('{}/city_listings_comb{}.csv'.format(cwd,city))
    listings_comb.to_pickle('{}/city_listings_comb{}.pkl'.format(cwd,city))