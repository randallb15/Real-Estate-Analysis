{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Cleaning the Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "%run src/loadindata.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "REcleaned = REdf[['region_id','region_type_id','region_name','region_type','median_sale_price','median_sale_ppsf','median_pending_sqft']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "REcleaned = REcleaned.dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "REcleaned.to_csv('data/REcleaned.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "listingsdfcleaned = listingsdf[['id','name','host_id','neighbourhood','latitude','longitude','room_type','price','availability_365']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "listings2dfcleaned = listingsdf2[['id','listing_url','name','neighbourhood_cleansed','latitude','longitude','property_type','room_type','accommodates','availability_30','bathrooms_text','bedrooms','beds']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "listings_comb = pd.merge(listingsdfcleaned,listings2dfcleaned,on=['id','name','latitude','longitude','room_type'],how='outer')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "listings_comb = listings_comb.dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "listings_comb = listings_comb.drop(['neighbourhood_cleansed'],axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "listings_comb['neighbourhood'] = listings_comb['neighbourhood'].astype('category')\n",
    "listings_comb['room_type'] = listings_comb['room_type'].astype('category')\n",
    "listings_comb['property_type'] = listings_comb['property_type'].astype('category')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "listings_comb['bedrooms'] = listings_comb['bedrooms'].astype('int')\n",
    "listings_comb['beds'] = listings_comb['beds'].astype('int')\n",
    "listings_comb['accommodates'] = listings_comb['accommodates'].astype('int')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_bath(str):\n",
    "    x = re.search('^\\d\\S*\\S*\\S*',str)\n",
    "    if x:\n",
    "        return x.group()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "listings_comb['bathrooms_text'] = listings_comb['bathrooms_text'].apply(get_bath)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "listings_comb['bathrooms_text'] = listings_comb['bathrooms_text'].astype('float')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "listings_comb.to_csv('data/AUSlistingscomb.csv')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
