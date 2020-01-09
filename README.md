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

“Urban Area Info.” Live Urban Real Estate, www.liveurbandenver.com/areas/urban.

“Suburban Area Info.” Live Urban Real Estate, www.liveurbandenver.com/areas/suburban.

