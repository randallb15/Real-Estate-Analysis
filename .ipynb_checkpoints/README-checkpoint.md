# Real Estate Investing Analysis - Buying an Airbnb in Austin

## Motivation:
I bought my first house in 2018.  What made buying the house doable, and profitable, was that there was a "casita" or back house in the backyard.  After buying the house in late October, I paid a friend to design it and buy furniture for it and I was able to put it on Airbnb by the end of December.  I didn't know it at the time, but this would lead me much further into real estate and Airbnb.  I have now owned or managed 5 listings on Airbnb in the San Antonio and Austin, TX area.  This has been a fun side gig but has also taught me a lot about real estate and made me some money as well.

Through this process, I have wondered how I would go about buying a rental property to put on Airbnb, and what would have the best Return on Investment.  There's a lot of considerations when thinking about real estate investing, especially when putting a property in the short-term rental space.  I wanted to explore three specific things that I would look at when buying an investment property to put onto Airbnb:

**1. City Location:**

It is no surprise that some cities do better on Airbnb than others.  While most cities now have properties listed on Airbnb now, some are huge tourist destinations and can command more money per night on a short-term rental, since the demand is so high.  Other cities are also new to the market and have very low supply, so they can also charge high rates.  Some markets, like San Antonio, are budget markets since people are coming to San Antonio to visit family or to get away for the weekend and don't look for really high-quality listings (however, San Antonio actually has a fairly high tourism rate and has a pretty consistent customer base for short term rentals).  I am seeking to compare the Austin market to several other cities to see how it compares.  I also want to normalize for the median price per square foot of sale prices in the cities so that I can have a better idea of real return on investment.

**2. House Size:**

House size can make a big difference in terms of return on investment.  One of the primary advantages of Airbnbs over hotel rooms is that they can house large numbers of people in the same location for a relatively low price per person.  So, obviously, you can charge more per night with a larger house with more bedrooms.  However, can you charge more per night per bedroom?  In other words, is the amount that you can charge per night a linear relationship with the amount of bedrooms in the house?  For example, if you can charge 100 USD per night for a 1 bedroom house, can you charge 300 USD per night for a 3 bedroom house or 500 USD per night for a 5 bedroom house, etc.?

**3. Area within the City:**

It also should come as no surprise that there are areas in the city that fair better for a short term rental than others.  The conventional wisdom is that a downtown Airbnb will always do better than an Airbnb that is not downtown, but is this the case?  Even if a downtown Airbnb makes more money than one that isn't downtown, can it offset the higher real estate cost?

## City Location
Austin is an incredibly fast growing city.  According to USA Today, it was the fourth fastest growing city in the United States between 2010 and 2018 (https://www.usatoday.com/story/money/2019/05/09/americas-fastest-growing-cities/39442201/).  Tourism is high and real estate prices have risen faster than a lot of places around the country.  So how does it compare to other cities?

To satisfy my curiosity, I wanted to compare with 3 other cities.  I chose a city on the East coast, the West coast and one that is more centrally located.  The three cities I chose were Boston, San Francisco and Nashville.  I did not have data on tourism rates but I was able to find the number of Airbnbs, average nightly price, and average sale price per square foot as of October 2020.  

Here's some baseline information about each city that sets the stage for the analysis:
![Comparing Cities](img/cities.png)



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

