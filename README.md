# House Hacking Data Analysis


# Table Of Contents
1. [Overview/Background](#overview/-background)
2. [Project Questions/Goal](#project-questions/goals)
3. [Data](#the-data)
4. [Exporatory Data Analysis (EDA)](#exploratory-data-analysis-(eda))
5. [Analysis](#analysis)
6. [Conclusion](#conclusion)
7. [References](#references)



# Overview/ Background

What does the term "House Hacking" mean?

In short, house hacking is when you buy a house, live in it, and rent out the other bedrooms (roomates that help pay your mortgage). 

Why House Hack?

House hacking is a great real estate investment strategy to build passive income and generate wealth. The goal of
[house hacking](https://www.biggerpockets.com/blog/2013-11-02-hack-housing-get-paid-live-free) is to
cash flow positively and live for free!

Another pro to house hacking is since you are living in the property, you can qualify for an owner-occupied loan with a down payment
as low as 3.5% (FHA Loan). With an FHA Loan, you are only required to live in the property for a year so after the first year,
you buy another house hack, and do the same thing.


# Project Questions/Goals

My main goal for this project was to answer the following question:

Are suburban homes a better house hacking investment than urban homes?

Other curiousities I had among suburban areas and urban areas were:

* What are the most common property types in each living area? (Property type and number of units/bedrooms).
* What are the average purchase prices for each living area?
* Average rent?
* Average rent per unit/bedroom?
* Average initial investment?
* Average One Year [Net Worth Return on Investment](https://www.biggerpockets.com/blog/metric-tracking-success-real-estate-deals)
and Monthly Cash Flow?

# The Data

The data for this project consist a variety of datasets.

I used [Zillow's Get Deep Search Results API](https://www.zillow.com/howto/api/GetDeepSearchResults.htm) for my final dataset and the parameters consist of the address of the property. Therefore,
I needed to gather and collect the addresses from each city I was observing.

Orignally I was going to randomly select from a [list of suburban cities](https://www.liveurbandenver.com/areas/suburban) but found not many datasets
of city address are public thus, used the follow available suburban city address datasets I could find:

* Thornton
* Boulder
* Broomfield
* Aurora
* Centennial

For my urban city dataset, I found that all of [Denver is consider urban](https://www.liveurbandenver.com/areas/urban). Therefore, I only
needed Denver addresses dataset for my urban population.

### Data Wrangling
The city address datasets and converting Zillow's API to a structured dataset was the most time comsuming. The columns for each address
dataset were unique in their own way and there were filter words in the address columns that the Zillow API could not comprehend, leading to
lot's of null values. I had to go back and clean the string text to minimize the missing values for the API dataset. Lastly,
I had to create new columns to analyze if the house was a good house hacking investment.

![all_feature_columns](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/master/img/all_feature_columns.png)

The final dataset consist of 894 rows and 41 columns for both urban and suburban populations. (Two seperate datasets)

### Feature Columns

To achieve my project goals I went and dove deeper into these feature columns:

e.g Suburbs dataset

![feature_columns](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/feature_columns.png)

# Exploratory Data Analysis (EDA)

#### Visible areas I sampled from Zillows Get Deep Search Results API:

* Green - Suburban
* Blue - Urban

![denverMap](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/denver_map.png)

#### What are the most common property types in each living area?

Based on our findings, we see single family homes excess the greatest amount of
property type for both living areas, followed by condominums. The least popular for both living areas are triplex properties. 

![property_type](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/usecode_urban_suburban.png)

#### What are the most common units of living?

From our findings, 3 bedroom and 4 bedroom homes are the most common. Another interesting finding was that 2 bedroom homes are more
common in urban areas than suburban areas. The one 78 unit home was from the Denver dataset, I assume that it was a apartment complex
listing all the units.

![bedrooms](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/bedrooms_urban_suburban.png)

#### What are the average purchase price for homes in each living area?

For suburban homes:

* Avg purchase price: $556,657

Urban homes:

* Avg purchase price: $556,602

Comparing the two, their is no significant difference between the two communities.

![amount](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/amount_hist_urban_suburb.png)

#### what are the average rent/month listings for homes in each community?

For suburban homes:

* Avg rent price: $2,284/month

Urban Homes:

* Avg rent price: $2,257/month

Comparing the two, their is no significant difference between the two communities.

![rent](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/rent_hist_urban_suburb.png)

#### How much rent would each bedroom/unit be per month?

How did I go about calculating this?

What I did was I took the rent of each home and divided by the number of bedrooms minus
one (since you will be living in the one of the units).

Rent per unit = Total rent profit - (Number of bedrooms - 1)

For suburban homes:

* Avg rent price per unit: $1,189/month

Urban homes:

* Avg rent price per unit: $1,424/month

Comparing the two living areas, urban homes can charge $300 dollars more per room. This makes sense possibly due to the high demand
for location in urban areas.


![rentPerUnit](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/rentPerUnit_hist_urban_suburb.png)

#### How much would the initial investment be to do a house hack?

Your initial investment is by far the most expensive part when purchasing a property.
The calculations I performed to estimate the initial investment are:

* 3.5% for Down Payment. (I am assuming you are using an FHA Loan)
* 5% for the closing cost. Typically the closing cost estimates around 5% of the purchase price.
* $20,000 for repairs and maintance. Personally, it's better to overestimate for any possible rehabs
expenses the property may need.

For suburban homes:

* Avg initial investment: $51,116

Urban homes:

* Avg initial investment: $50,613


Based on the histograms for both communities, we are averaging a little over $50,000 for the
initial investment. 


![initialInvestment](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/initialInvestment_hist_urban_suburb.png)

#### What is the one year net worth return on investment (NWROI)?

Craig Curelop, author of the [House Hacking Strategy](https://www.amazon.com/House-Hacking-Strategy-Achieve-Financial/dp/1947200151) came up with
the term net worth return on investment.

Your NWROI, similar to a cash-on-cash return, summarizes exactly how good an investment will be (or has been) through a percentage.
The higher the percentage, the better the deal. Unlike cash-on-cash return, NWROI takes into account all wealth generators of real estate:
cash flow, appreciation, and loan paydown; and it shows the overall impact it has on your net worth. 

NWROI = (cashflow and rent savings + loan paydown + appreciation) / Initial Investment

* **Cashflow** is how much you are making per month (after expenses have been payed)
* **rent savings** is how much you are saving per month 
* **loan paydown** how much principal you have payed off on the loan (.45 of PITI expense)
* **appreciation** on average, appreciates 6% per year thus, appreciation amount = purchase price * 0.06

For suburban homes:

* Avg one year NWROI: 115%

Urban homes:

* Avg one year NWROI: 125%


![NWROI](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/oneYearNWROI_hist_urban_suburb.png)

#### How much passive income (cash flow) is made on average per month?

Monthly Cash Flow = Profit - Expenses

* Profit - All the rent roomates pay combined
* Expenses - Monthly Mortgage payment + Monthly Reserves

Reserves - Reserves are how much we are storing per month for vacancy, maintenance, and capital expenditures. (fixed $300/month)

For suburban homes:

* Avg monthly cash flow: $-14.03/month (This means you would still pay $14 to live where you do...Still a great deal!)

Urban homes:

* Avg monthly cash flow: $256.09/month

![monthlyCashFlow](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/monthlyCashFlow_hist_urban_suburb.png)

# Analysis

#### Are suburban homes a better investment than urban homes?

Pre-Assumptions:
Going into this project I had already had this hypothesis test in mind. Before going through EDA and performing my test, I initally
thought suburban homes are a better investment than urban homes because I believed single family homes were more common in suburban homes
than urban homes thus, more rooms to rent out. And, because urban areas are more populated possibly because of location and convenience,
I thought urban homes were going to be more expensive and thus higher monthly expense cost. 


One tail hypothesis test variables:
* Null Hypothesis - Urban Homes outperform Suburban homes for a house hacking investment
* Alternative Hypothesis - Suburban homes are a better house hacking investment than urban homes
* alpha level: 0.05
* z-statistic: -0.24
* p-value: .60


According to our findings below, we can see that our the Z statistic for suburban homes is -0.24.
The probaility of having this z-statistic results, or more extreme, given the null hypothesis is true is 0.60.
Therefore, we cannot reject the null, the monthly cash flow for suburban homes are not significantly greater than urban homes.

I was somewhat off ...


![hypoTest](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/ztest_urban_suburban.png)

# Conclusion

In conclusion, there is no significant difference between urban homes and suburban homes for a house hack. We also found that
the most common types of property for both living areas are 3 bedroom single family homes. The average purchase price for each
home are above $550,000.

The average initial investment for both communities are on average above $50,000.

The average cashflow for a suburban home is $-14/month, Which means you would still pay $14 to for your living situation.
The average cashlow for an urban home is $250/month.

The average NWROI for both communties is at slightly above 100% (impact the deal has on your networth).

#### In the Future
In the future, I would like to answer if single family homes cash flow the most compare to the rest of property types.

I would also like to explore more in depth what the minumum purchase,rent, and initial investment would be to break even on house hack.

Lastly, explore which relationship has the stongest correlation with monthly cash flow.

# References
Curelop, Craig. The House Hacking Strategy: How to Use Your Home to Achieve Financial Freedom. BiggerPockets Publishing, 2019.

“Urban Area Info.” Live Urban Real Estate, www.liveurbandenver.com/areas/urban.

“Suburban Area Info.” Live Urban Real Estate, www.liveurbandenver.com/areas/suburban.

