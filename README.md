# House Hacking Data Analysis


# Table Of Contents
1. Overview/Background
2. Project Questions/Goal
3. Data
4. Exporatory Data Analysis (EDA)
5. Analysis
6. Conclusion
7. References



# Overview/ Background
House Hacking. What is that?

In short, House hacking is when you buy a house, live in it, and rent out the other bedrooms (roomates that help pay your mortgage). 

Why House Hack?

House hacking is a great real estate investment strategy to build passive income and generate wealth. The goal of house hacking is to
cash flow(reference link) positively and live for free!

Another pro to house hacking is since you are living in the property, can qualify for an owner-occupied loan (down payment as low as 3.5%
- FHA Loan). With an FHA Loan, you are only required to live in the property for a year so after the first year,
you buy another house hack and do the same thing.

You can learn more about how to house hack here (link)

# Project Questions/Goals

My main goal for this project was to answer the following question:

Are suburban homes a better house hacking investment than urban area homes?

Other curiousities I had among suburban areas and urban areas were:

* What are the most common property types in each? (Property type and Number of Units/bedrooms)
* What are the average purchase prices for each living area?
* Average rent?
* Average rent per unit/bedroom?
* Average initial investment?
* Average One Year Net Worth Return on Investment and Monthly Cash Flow?

# The Data
The data for this project consist a variety of datasets.

I used Zillow's Get Deep Search Results API for my final dataset and the parameters consist of the address of the home. Therefore,
I needed to gather and collect the addresses from each city I was observing.

Orignally I was going to randomly select from a list of suburban cities(https://www.liveurbandenver.com/) but found not many datasets
of city address are public thus, used the follow available suburban city address datasets:

* Thornton
* Boulder
* Broomfield
* Aurora
* Centennial

For my urban city dataset, I found that all of Denver(https://www.liveurbandenver.com/ ) is consider Urban. Therefore, only one Denver's
addresses dataset was required for my urban population.

### Data Wrangling
The city address datasets and converting Zillow's API to a structured dataset was the most time comsuming. The columns for each address
dataset were unique in their own way and there were filter words in the Addresses that the Zillow API could not comprehend, leading to
lot's of null values. Thus, I had to go back and clean the string text to minimize the missing values for the API dataset. Lastly,
I had to create columns to analyze if the house was a good house hacking investment.

The final dataset consist of 894 rows and 41 columns for both urban and suburban populations. (Two seperate final datasets)

### Feature Columns
To achieve my project goals I went deeper into these feature columns:

e.g Suburbs dataset

![feature_columns](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/feature_columns.png)

# Exploratory Data Analysis (EDA)

Visible areas I sampled from the API:
* Red - Suburban
* Blue - Urban

![denverMap](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/denver_map.png)

#### What are the most common property types in each living area?

Based on our findings, we see Single Family Homes excess the greatest amount of
property type for both living areas, followed by Condominums. The least popular for both living areas are triplex properties. 

![property_type](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/usecode_urban_suburban.png)

#### What are the most common units of living?
From our findings, 3 bedroom and 4 bedroom homes are the most common. Another interesting finding was that 2 bedroom homes are more
common in Urban areas than suburban areas. The one 78 unit home was from the Denver dataset, I assume that it was a apartment complex
listing all the units.

![bedrooms](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/bedrooms_urban_suburban.png)

#### What are the average purchase price for homes in each living area?
For suburban homes:

* Avg purchase price: $556,657

Urban Homes:

* Avg purchase price: $556,602

Comparing the two, their is no significant difference between the two communities.

![amount](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/amount_hist_urban_suburb.png)

#### what are the average rent listings for homes in each community?

For suburban homes:

* Avg rent price: $2,284

Urban Homes:

* Avg rent price: $2,257

Comparing the two, their is no significant difference between the two communities.

![rent](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/rent_hist_urban_suburb.png)

#### How much rent would each bedroom/unit be?

How did I go about calculating this?

What I did was I took the rent of each home and divided by the number of bedrooms minus
one (since you will be living in the one of the units).

For suburban homes:

* Avg rent price per unit: $1,189

Urban homes:

* Avg rent price per unit: $1,424

Comparing the two living areas, urban homes can charge $300 dollars more per room. This was
makes sense due to the high demand for location in urban areas.


![rentPerUnit](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/rentPerUnit_hist_urban_suburb.png)

#### How much would my initial investment be to do a house hack?

Your initial investment is by far the most expensive part when purchasing a property.
The calculations performed to estimate the initial investment:

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

#### What is my One Year Net Worth Return On Investment (NWROI)

Craig Curelop, author of the House Hacking Strategy(link) came up with Net Worth Return
On Investment.

Your net worth return on investment (NWROI), similar to a cash-on-cash return,
summarizes exactly how good an investment will be (or has been) through a percentage. The higher the percentage, the better the deal.
Unlike cash-on-cash return, NWROI takes into account all wealth generators of real estate:
cash flow, appreciation, and loan paydown; and it shows the overall impact it has on your net worth. 

NWROI = (cashflow and rent savings + loan paydown + appreciation) / Initial Investment

* Cashflow is how much you are making per month 
* rent savings is how much you are saving per month 
* loan paydown how much principal you have payed off on the loan (.45 of P&I expense)
* appreciation - On average, appreciation 6% per year thus, Appreciation amount = purchase price * 0.06

For suburban homes:

* Avg one year NWROI: 115%

Urban homes:

* Avg one year NWROI: 125%


![NWROI](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/oneYearNWROI_hist_urban_suburb.png)

#### How much passive income (cash flow) am I making per month?

Monthly Cash Flow = Profit - Expenses

* Profit - All the rent roomates pay combined
* Expenses - Monthly Mortgage payment + Monthly Reserves

Reserves - Reserves are how much we are storing per month for vacancy, maintenance, and capital expenditures. (fixed $300/month)

For suburban homes:

* Avg monthly cash flow: $-14.03 (This means you would still pay $14 to live where you do...Still a great deal!)

Urban homes:

* Avg monthly cash flow: $256.09

![monthlyCashFlow](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/monthlyCashFlow_hist_urban_suburb.png)

# Analysis

#### Are suburban homes a better investment than urban homes?

Pre-Assumptions:
Going into this project I had already had this hypothesis test in mind. Before going through EDA and performing my test, I initally
thought suburban homes are a better investment than urban homes because I thought single family homes were more common in suburban homes
than urban homes thus, more rooms to rent out. And, because urban areas are more populated possibly because of location and convenience,
I thought Urban homes were going to be more expensive and thus higher monthly expense cost. 


variables:
* Null Hypothesis - Urban Homes outperform Suburban homes for a house hacking investment
* Alternative Hypothesis - Suburban homes are a better house hacking investment than urban homes
* alpha level: 0.05
* z-statistic: -0.24
* p-value: .60


According to our findings below, we can see that our the Z statistic for suburban homes is -0.24.
The probaility of having this z-statistic results, or more extreme, given the null hypothesis is true is 0.60.
Therefore, we cannot reject the null, the monthly cash flow for suburban homes are not significantly greater than urban homes.


![hypoTest](https://github.com/isaacramiez00/Urban-vs-Suburban/blob/develop/img/ztest_urban_suburban.png)

# conclusion

In conclusion, there is no significant difference between urban homes and suburban homes for a house hack. We also found that
the most common types of property for both living areas are 3 bedroom single family homes. The average purchase price for each
home are above $550,000.

The average initial investment for both communities are on average above $50,000.

The average cashflow for a suburban home is $-14/month, Which means you would still pay $14 to for your living situation.
The average cashlow for an urban home is $250/month.

The average Net Worth Return On Investment for both communties is at slightly above 100% (impact the deal has on your networth).

#### In the Future
In the future, I would like to answer if single family homes cash flow the most compare to the rest of property types.

I would also like to explore more in depth what the minumum purchase,rent, and initial investment would be to break even on house hack.

Lastly, explore which relationship has the stongest correlation of monthly cash flow.

# Reference
Curelop, Craig. The House Hacking Strategy: How to Use Your Home to Achieve Financial Freedom. BiggerPockets Publishing, 2019.

“Urban Area Info.” Live Urban Real Estate, www.liveurbandenver.com/areas/urban.

“Suburban Area Info.” Live Urban Real Estate, www.liveurbandenver.com/areas/suburban.

