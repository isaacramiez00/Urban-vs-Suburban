# House Hacking In The Mile High


# Table Of Contents
1. Overview/ Background
2. Questions
3. Data
4. EDA
5. Conclusion
6. References



# Overview/ Background
What is House Hacking? In short, House hacking is the idea of when you buy a home and
rent out the other bedrooms. Essentially, Roomates that help pay off your mortgage.
House hacking has been around for quite some time and continues to be a trend for
building passive income and great for long term real estate investing.

What's great about doing a house hacking investment is that because you are living
your home, you can put down an owner-occupied loan for as low as 3.5%! (FHA Loan).
On top of that, with an FHA Loan, you are only required to live in you home for 1 year
so what do you do? You Buy another house and do the same thing.

House Hacking is a great way to generate wealth.

Why am I interested in House Hacking?

As stated previously, I am looking to generate wealth and gain financial freedom.
I want the opportunity to not have to work for the next 40 years just to scrape 
by and save up for retirement. By analyzing the right deals and finding the
right roomates, My goal is to build $10,000/month just on passive income in
the next 10 years.

And so, the purpose for my research is to see the house hacking strategy be applied in
Colorado.

# Questions
In site of this research, a couple questions came in mind:


* Most common property yypes
* Most common number Of bedrooms
* Average amount
* Rent 
* Rent per Unit
* Initial Investment
* One Year Net Worth Return on Investment
* Monthly Cash Flow

I was curious in particular whether Suburban are a better Investment than Urban Homes.
Before performing a hypothesis test, my guess (Alternative Hypothesis) is that Suburban
homes are a better investment than urban homes for a house hacking strategy.

Here's Why:

* Suburban homes contain more single family homes which means more rooms to rent out
* Becuase of Urban Homes popularity due to location, I assumed that urban home prices
are more expensive than suburban homes

# Data
The way I broke out the distinguishment between Urban Homes and Suburban Homes was I checkout 
https://www.liveurbandenver.com/ Where the website breaks up what's consider
Urban and Suburban. In conclusion, Urban Homes are considered the city of Denver and
Suburban are listed here https://www.liveurbandenver.com/ (Suburban neighbothood).

## Preparing and getting the data
Now that I know the distinguishment, I need a select which cities I wanted to sample from
to answer my questions. 

For my research, I was using Zillow's Get Deep Search results API. The parameters I
needed to pass in to get the query was the address of the houses I was exploring. And
so, I stared off by grabbing the addresses dataset of each city so I can then use it
for the Zillow API. At first, I tried running a random selection from the list of
Suburban homes to avoid any bias in my experiment but, as it find out, it was a
challenge to find the address dataset from each city, as some did not have any so I
then chose the following:

* Thornton
* Boulder
* Broomfield
* Centennial
* Aurora



## Cleaning
This was the part during my research I spend the most time on.
The address datasets for each city contained around 70 to 80,000 rows so I started off
using Spark. I had to clean up the addresses in the address dataset because plenty
contained words the API could not read.

Afterwards, I grabbed a random sample of 1000 for each population.
(Urban and Suburban datasets) from here I then passed the each address to the API.
The API returned to me an unstructed dataset so I had to shape and clean up the
the features I wanted to use for my dataset to a structured dataset. Lastly,
I saved the API dataset to a csv file in my local machine.

# Data Vizualization

![denverMap](/Users/isaacramirez/code/dsi/capstone-I/img/denver_map.png)


![property_type](/Users/isaacramirez/code/dsi/capstone-I/img/usecode_urban_suburban.png)

![bedrooms](/Users/isaacramirez/code/dsi/capstone-I/img/bedrooms_urban_suburban.png)

![amount](/Users/isaacramirez/code/dsi/capstone-I/img/amount_hist_urban_suburb.png)

![rent](/Users/isaacramirez/code/dsi/capstone-I/img/rent_hist_urban_suburb.png)

![rentPerUnit](/Users/isaacramirez/code/dsi/capstone-I/img/rentPerUnit_hist_urban_suburb.png)

![initialInvestment](/Users/isaacramirez/code/dsi/capstone-I/img/initialInvestment_hist_urban_suburb.png)

![NWROI](/Users/isaacramirez/code/dsi/capstone-I/img/monthlyCashFlow_hist_urban_suburb.png)

# Hypothesis Test

![hypoTest](/Users/isaacramirez/code/dsi/capstone-I/img/ztest_urban_suburban_cdf.png)

