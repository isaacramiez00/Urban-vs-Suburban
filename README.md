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

These are the areas I sampled from to the API:
* Red - Suburban
* Blue - Urban

![denverMap](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/denver_map.png)

One of the following questions I wanted to explore was what property types are
the most common among the to different communities.

Based on our findings, we see Single Family Homes excess the greatest amount of
property type followed by Townhouse with an average count difference of 758 for 
both communities.

![property_type](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/usecode_urban_suburban.png)

#### What are the most common number Of bedrooms?
From our findings, 3 bedroom and 2 bedroom homes are the most common. One of my Search
results for Urban homes had a unit that filled 78 bedrooms. I don't know if that is 
an error but I left it.

![bedrooms](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/bedrooms_urban_suburban.png)

#### What are the average purchase price for homes in each community?
For a Suburban Home:

* Avg purchase price: $556,602

Urban Homes:

* Avg purchase price: $556,657

Comparing the two, their is no significant difference between the two communities.

![amount](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/amount_hist_urban_suburb.png)

#### what are the average rent listings for homes in each community?

For a Suburban Home:

* Avg rent price: $2,257

Urban Homes:

* Avg rent price: $2,284

Comparing the two, their is no significant difference between the two communities.

![rent](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/rent_hist_urban_suburb.png)

#### How Much would each bedroom/unit be charged for rent based on the rent listing?

How did I go about calculating this?

What I did was take the rent of each home and divided by the number of bedrooms minus
one (since you will be living in the one of the units).

For a Suburban Home:

* Avg rent price per unit: $1,424

Urban Homes:

* Avg rent price per unit: $1,189

Comparing the two, suburban homes can charge $300 dollars more per room. This was
an intersting find and surprise. I suspected that Urban home rent prices would be
more expensive


![rentPerUnit](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/rentPerUnit_hist_urban_suburb.png)

#### How much would my initial investment be to do a house hack?

Crunching the numbers...

Your initial investment is by far the most expensive part when purchasing a property.
The calculations performed to estimate the initial investment:

* 3.5% for Down Payment. I am assuming you are using an FHA Loan (3.5%).
* 5% for closing cost. This is seperate from the down payment. Typically the closing
cost estimate around 5% of the purchase price.
* $20,000 for repairs and maintance. Personally, it's better to overestimate for any possible rehabs
expenses the property may need.

Based on the histograms for both communities, we are averaging arond $50,000 for the
initial investment. 


![initialInvestment](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/initialInvestment_hist_urban_suburb.png)

#### What is my One Year Net Worth Return On Investment (NWROI)

Craig Curelop, author of the House Hacking Strategy came up with Net Worth Return
On Investment.

Your net worth return on investment (NWROI), similar to a cash-on-cash return,
summarizes exactly how good an investment will be (or has been) through a percentage. The higher the percentage, the better the deal.
Unlike cash-on-cash return, NWROI takes into account all wealth generators of real estate:
cash flow, appreciation, and loan paydown; and it shows the overall impact it has on your net worth. 

NWROI = (cashflow and rent savings + loan paydown + appreciation) / Initial Investment

* Cashflow is how much you are making per month 
* rent savings is how much you are saving per month 
* loan paydown how much principal you have payed off on the loan
* appreciation - On average, appreciation 6% per year thus, simply take what your purchase price is and multiply it by .06 (6%).



![NWROI](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/oneYearNWROI_hist_urban_suburb.png)

#### How much passive income  (cash flow) am I making per month?

Monthly Cash Flow = Profit - Expenses

* Profit - All the rent roomates pay combined
* Expenses - Monthly Mortgage payment + Monthly Reserves

Reserves - Reserves are how much we are storing per month for vacancy, maintenance, and capital expenditures.

![monthlyCashFlow](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/monthlyCashFlow_hist_urban_suburb.png)

# Hypothesis Test

#### Are suburban homes a better investment than urban homes?

variables:
* Null Hypothesis - Urban Homes outperform Suburban homes for a house hacking investment
* Alternative Hypothesis - Suburban homes are a better house hacking investment than urban homes
* alpha level: 0.05
* z-statistic: 0.21
* p-value: .42


According to our findings below, we can see that our the Z statistic for suburban homes is 0.21.
The probaility of having this z-statistic results, or more extreme, given the null hypothesis is true is 0.42.
Therefore, we cannot reject the null, the monthly cash flow for suburban homes are not significantly greater than urban homes.


![hypoTest](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/ztest_urban_suburban_cdf.png)

# conclusion

In conclusion, there is no significant difference between urban homes and suburban homes for a house hack. We also found that
the most common types of property for both communities are 3 bedroom single family homes. The average purchase price for each
home are above $500,000.

The average initial investment for both communities are on average $50,000.

The average cashflow for a suburban home are $250/month
The average cashlow for an urban home are $0 (Still a great things, you are not paying your mortgage. Essentially living for free!).

The average Net Worth Return On Investment for both communties is at least 100% (impact the deal has on your networth

#### In the Future
For future research, I'd like to explore which property types each house cash flows

For the future I plan to work with a real estate agent and use this house hacking deal analysis to run calculations on whether this house
is a good investment for a house hack.

# Reference
Curelop, Craig. The House Hacking Strategy: How to Use Your Home to Achieve Financial Freedom. BiggerPockets Publishing, 2019.

