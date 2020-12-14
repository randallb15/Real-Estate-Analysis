# Real Estate Investing Analysis - Buying an Airbnb

### Hypotheses:

Null Hypothesis: A 3 Bed, 2 Bath house earns more revenue % house price than a 1 Bed, 1 Bath
Alternative Hypothesis: There is no difference in revenue % house price for a 3/2 than a 1/1

- For this, need to specify area, price range, etc.
---

Null Hypothesis: A 1/1 within 5 miles from downtown earns more revenue than a 1/1 further than 5 miles from downtown
Alternative Hypothesis: There is no difference in revenue between 1/1 5 miles from downtown or further

#### High level description of project:
Where is the best place to buy an Airbnb for a real estate investor in Austin?  How do we go about solving this problem?

First, we want to compare the real estate market for Austin to different places around the world.  This will give us an idea of how good the Austin market looks in terms of Airbnb investment as compared to other cities.
- Possible Hypothesis - Austin is no better than Portland, Seattle, DC, Boston, San Francisco, Nashville, New Orleans, Denver, Asheville for Airbnb Rental Prices vs. Price per sqft for sold houses vs. Alternate Hypothesis that it is.
- Will cherry-pick 3 cities other than Austin to compare based on EDA

### Comparing a 3 bedroom house to a 1 bedroom house in terms of median nightly price per bedroom
Null Hypothesis: A 3 bedroom house has the same or lower median nightly price per bed than a 1 bedroom house
Alternative Hypothesis: A 3 bedroom house has a higher median nightly price per bed than a 1 bedroom house

#### Also compared a 3 bedroom house to a 5 bedroom house and a 5 bedroom house to a house with 6 or more bedrooms




### Next, we will want to compare zip codes in Austin and determine which are the best zip codes
Downtown zip codes: 78701, 78702, 78703, 78705
(All other zip codes considered outside of downtown)

- We will need to estimate revenue based on price and availability
- We can also just look at price per bed or per bed/bath to determine where the prices are the highest
- We can look at the relationship between price per bed and availability for different zip codes
- NOTE: average zip code ppsqft does not take into consideration the variation in ppsqft for different houses.  There would need to be more data and analysis to find out what would be the best ROI per ppsqft.




#### Data Source(s): 
Websites and/or databases:
https://www.redfin.com/news/data-center/
http://insideairbnb.com/get-the-data.html
https://www.propstream.com/

#### Data Quality:
- In order to remove listings that are outliers - don't get booked or priced too highly to be competitive - **require at least 5 reviews**
    - _This cut down almost half of the listings in Austin!!_
    - There were still remaining outliers - most or all of them seemed to be by a company named WanderJaunt who has 433 listings around the country.  They had a number of listings that looked like they were moved up to 9,999 USD per night.  I am guessing that this is the maximum price per night allowed on the platform.  I am not sure why they are moved up so much - whether they are booked on a different platform or they do not want bookings, but they have days blocked off and they have reviews which is misleading.  **I also took these out of the data.**
- Also, this only includes listings that are entire home/apt... Listings that are a private room, shared room, or hotel room are not considered.
    
REdf:
Has a region ID for different counties: 
- 2866 for Travis County - the main county in Austin TX
- ? Nashville?
- ? SF?
- ? NYC?

listings2 df:
- Had to use unzip to get data
- used regular expressions to extract bathrooms from text

Cleaning.py:
- This is used to clean the incoming Airbnb data for each city.  Since I had already done it for Austin, this was easy to reproduce for the other 13 cities.

**NOTE: AUSppsf obtained manually and not all information is completely up to date.  Some zip codes have the most recent info from March.**
- data obtained from propstream.com

### Further Study
I would like to look at correlations between house Airbnb prices and availability.  I think you could find a sweet spot in terms of house size, house price, location, Airbnb price, and availability to maximize revenue.

