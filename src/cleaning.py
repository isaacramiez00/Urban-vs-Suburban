import pyspark as ps
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import lit
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import json
import datetime as dt
import os 
import pandas as pd
import numpy as np


# clean
def spark_df(filepath):
    '''
    loads filepath to spark
    '''
    df = spark.read.csv(filepath,\
                        header=True,\
                        quote='"',
                        sep=",",
                        inferSchema=True)
    return df


# clean
def address_sample_df(df, addressColumn, city, state='co', filterDict={}, replaceColumnName='address', sample=400, seed=463):
    '''  
    samples from SparkDataFrame and creates a pandas dataframe
    column is the address column: address STRtype
    expecting a dictionary for filter of: {columnName: columnsValue}
    city = str (allLowerCase)
    '''
    # filter
    if bool(filterDict):
        for k, v in filterDict.items():
            df = df.filter(col(k) == v)
    
    # rename columns
    df = df.withColumnRenamed(addressColumn, replaceColumnName)

    # create columns
    df = df.withColumn('city', lit(city))\
            .withColumn('state', lit(state))
    
    # select distinct value for columns
    df = df.select('address', 'city', 'state').distinct()
    
    # random sampling
    df = df.rdd.takeSample(False, sample, seed)
    
    #convert to pandas
    df = spark.createDataFrame(df)
    df = df.toPandas()
    df = df.apply(lambda x: x.astype(str).str.lower())
    # df['address'] = df['address'].apply(lambda row: row.split())
    df = clean_wrds(df)
    return df


# clean
def clean_wrds(df, col='address'):
    '''
    cleans up column (default=address)
    returns dataframe
    '''
    # breakpoint()
    bad_wrds = ['bldg', 'unit', 'apt', '#', 'irrp', 'ste', 'lot']
    clear_wrds = df.loc[:, col]
    for i, lst in enumerate(clear_wrds,0):
        # old_wrd = lst
        lst = lst.split()
        for wrd in lst:
            if wrd in bad_wrds:
                lst.remove(wrd)
                lst.pop(-1)
            else:
                continue

        lst = ' '.join(lst)
        df.loc[i, col] = lst

    return df


# clean
def single_query(link, payload):
    '''
    returns api xml file
    '''
    response = requests.get(link, params=payload)
    if response.status_code != 200:
        print('WARNING', response.status_code)
    else:
        return response.text

# clean
def deep_search_sample(df):
    '''
    storing zillowAPIdataset into a csv file
    '''
    api_url_base = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm'
    
    columns = ['address', 'amount', 'zipcode', 'city', 'state', 'latitude', 'longitude', 'usecode', 'bedrooms', 'last-updated']
    
    # lst that will be used to create dataframe
    for i in range(df.shape[0]):
    
        # grabs data from df
        address_param = df.loc[i,'address']
        citystatezip_param = df.loc[i, 'city'] + ' ' + df.loc[i, 'state']

        # upload data as param
        payload = {'zws-id':os.environ['ZWID_API_KEY'], 'address': address_param, 'citystatezip':citystatezip_param,\
                'rentzestimate': 'true'}

        # uploads api
        current_house_info = single_query(api_url_base, payload)
        
        # api to dataframe
        html_soup = BeautifulSoup(current_house_info, features='html.parser')
        
        dict = {}
        # creates dictionary
        for child in html_soup.recursiveChildGenerator():
            if child.name in columns:
                dict[child.name] = html_soup.find(child.name).text
        
        if len(html_soup.find_all('amount')) == 2:
            rental_val = html_soup.find_all('amount')[1].text
            dict['rent'] = rental_val
    
        if i == 0:
            deep_search_df = pd.DataFrame(dict, index=[0])
        else:
            deep_search_df = deep_search_df.append(dict, ignore_index=True)


    deep_search_df = clean_api_dataframe(deep_search_df)
    deep_search_df = deep_search_df[deep_search_df['bedrooms'] > 1]
    deep_search_df['rentPerUnit'] = deep_search_df['rent'] / (deep_search_df['bedrooms'] - 1)
    deep_search_df['totalMonthlyIncome'] = deep_search_df['rentPerUnit'] * deep_search_df['bedrooms']

    mortgage_details(deep_search_df)
    one_year_nwroi(deep_search_df)
    
    deep_search_df = deep_search_df.dropna()

    return deep_search_df

# clean
def clean_api_dataframe(df):

    # convert string columns to numeric floats
    to_numeric = ['amount', 'bedrooms', 'latitude', 'longitude', 'rent']

    for col in to_numeric:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df

# clean
def mortgage_details(df, downPayment=0.035, interestRate=0.0366,\
                     pmiRate=0.01, loanTerms_years=30, paymentsPerYear=12,\
                     taxRate=0.008, insuranceRate=0.005, vacancy=100,\
                     capitalExpenditures=100, maintenance=100):
    '''
    creates mortgage detail columns
    '''
    df['downPayment'] = df['amount'] * downPayment
    df['loanAmount'] = df['amount'] * (1 - downPayment)   
    df['interestRate'] = interestRate
    df['pmiRate'] = pmiRate
    df['loanTerm_years'] = loanTerms_years
    df['paymentsPerYear'] = paymentsPerYear
    df['taxRate'] = taxRate
    df['insuranceRate'] = insuranceRate

    
    df['monthlyInterest'] = (df['loanAmount'] * interestRate) / 12
    df['monthlyPrincipal'] = df['monthlyInterest'] * 0.45
    df['monthlyP&I'] = df['monthlyInterest'] + df['monthlyPrincipal']
    df['monthlyTaxes'] = (df['amount'] * taxRate) / 12
    df['monthlyInsurance'] = (df['amount'] * insuranceRate) / 12
    df['monthlyPMI'] = (df['loanAmount'] * pmiRate) / 12
    df['subTotalMonthlyPayment'] = df['monthlyP&I'] + df['monthlyTaxes'] +\
                                df['monthlyInsurance'] + df['monthlyPMI']
    df['vacancy'] = vacancy
    df['capitalExpenditures'] = capitalExpenditures
    df['maintenance'] = maintenance
    df['subtotalMonthlyReserves'] = df['vacancy'] + df['capitalExpenditures'] +\
                                    df['maintenance']
    df['totalMonthlyExpenses'] = df['subTotalMonthlyPayment'] +\
                                 df['subtotalMonthlyReserves']

    return df

# clean
def one_year_nwroi(df, rehabCost=20000, closingCosts=0.02, appreciation=0.06):

    df['rehabCost'] = rehabCost
    df['closingCosts'] = df['amount'] * closingCosts
    df['initialInvestment'] = df['downPayment'] +\
                              df['rehabCost'] +\
                              df['closingCosts']

    df['monthlyCashFlow'] = df['totalMonthlyIncome'] -\
                            df['totalMonthlyExpenses']
    df['yearlyLoanPaydown'] = df['monthlyPrincipal'] * 12
    df['appreciationAmount'] = df['amount'] * appreciation

    df['oneYearNWROI'] = (((df['monthlyCashFlow'] + df['rentPerUnit']) * 12) +\
                          df['yearlyLoanPaydown'] +\
                          df['appreciationAmount']) /\
                          df['initialInvestment']

    return df

def get_zillow_data():

    # clean
    # aurora
    aurora_df = spark_df('/home/jovyan/work/code/dsi/capstone-I/data/suburban/aurora_addresses.csv')
    aurora_df = address_sample_df(aurora_df, 'ADDRESS', 'aurora', filterDict={'CITY':'Aurora'})

    # clean
    #boulder
    boulder_df = spark_df('/home/jovyan/work/code/dsi/capstone-I/data/suburban/Boulder_addresses.csv')
    boulder_df = address_sample_df(boulder_df, '_c2', 'boulder', filterDict={'CITY': 'BOULDER'})

    # clean
    # broomfield
    broomfield_df = spark_df('/home/jovyan/work/code/dsi/capstone-I/data/suburban/Broomfield-Addresses.csv')
    broomfield_df = address_sample_df(broomfield_df, 'STREET_NAME', 'broomfield', filterDict={'CITY':'BROOMFIELD'})

    # clean
    # thornton
    thornton_df = spark_df('/home/jovyan/work/code/dsi/capstone-I/data/suburban/thornton_Addresses.csv')
    thornton_df = address_sample_df(thornton_df, 'ADDRESS', 'thornton', filterDict={'CITY':'THORNTON'})

    # clean
    # centennial
    centennial_df = spark_df('/home/jovyan/work/code/dsi/capstone-I/data/suburban/centennial_addresses.csv')
    centennial_df = address_sample_df(centennial_df, 'FULLADDR', 'centennial', filterDict={'IS_RESIDENTIAL':'RES', 'City':'CENTENNIAL'})       

    # clean
    # denver - urban
    urban_denver_df = spark_df('/home/jovyan/work/code/dsi/capstone-I/data/urban/urbanAddresses.csv')
    urban_denver_df = address_sample_df(urban_denver_df, 'FULL_ADDRESS', 'denver', sample=2000)

    # clean
    # concat suburban dfs
    suburbs = [centennial_df, thornton_df, broomfield_df, boulder_df, aurora_df]
    suburbs_df = pd.concat(suburbs, ignore_index=True)

    urb_df, sub_df = shape_zillow_size(urban_denver_df, suburbs_df)
    urb_df.to_csv('/home/jovyan/work/code/dsi/capstone-I/data/zillowQueryUrban.csv')
    sub_df.to_csv('/home/jovyan/work/code/dsi/capstone-I/data/zillowQuerySuburb.csv')

    return None
    
def shape_zillow_size(urb_df, sub_df):
    '''
    zillows api may return null values
    samples through each dataset to get equal sample size
    '''
    suburbs_df = deep_search_sample(urb_df)
    urban_denver_df = deep_search_sample(sub_df)

    if urban_denver_df.shape[0] < suburbs_df.shape[0]:
        suburbs_df = suburbs_df.sample(urban_denver_df.shape[0])
    else:
        urban_denver_df = urban_denver_df.sample(suburbs_df.shape[0])

    return urban_denver_df, suburbs_df
    

if __name__ == '__main__':
    # clean
    # initialize apache spark
    spark = ps.sql.SparkSession.builder.master("local[4]").appName("Colorado-Addresess").getOrCreate()
    sc = spark.sparkContext
    get_ipython().system('ls')

    get_zillow_data()

    suburb_df = pd.read_csv('/home/jovyan/work/code/dsi/capstone-I/data/zillowQuerySuburb.csv')
    urban_denver_df = pd.read_csv('/home/jovyan/work/code/dsi/capstone-I/data/zillowQueryUrban.csv')
