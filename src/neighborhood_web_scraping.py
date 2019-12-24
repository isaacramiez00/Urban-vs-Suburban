# neighborhood_web_scraping.py
# this script web scrapes the 


# import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import json
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, CollectionInvalid
import datetime as dt
import os 
import pandas as pd
import numpy as np

# webscrape the urban and suburban regions 
req = Request('https://www.liveurbandenver.com/areas/urban', headers={'User-Agent': 'Mozilla/5.0'})
suburban_req = Request('https://www.liveurbandenver.com/areas/suburban', headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, features="lxml")
urban_h6 = soup.find_all('h6')

webpage_suburbs = urlopen(suburban_req).read()
suburb_soup = BeautifulSoup(webpage_suburbs, features="lxml")
suburbs_h6 = suburb_soup.find_all('h6')

np.random.seed(64)

urban_lst =[]
for i in urban_h6:
    urban_lst.append(i.text)
# print(urban_lst)
# random sample from list
urban_neighborhood_sample = np.random.choice(urban_lst, size=5, replace=False)
print(urban_neighborhood_sample)
# ['Cherry Creek' 'Auraria/River Mile' 'RiNo' "Sloan's Lake" 'Congress Park']

suburban_lst =[]
for i in suburbs_h6:
    suburban_lst.append(i.text)
suburb_neighborhood_sample = np.random.choice(suburban_lst, size=5, replace=False)
print(suburb_neighborhood_sample) 
# ['Golden' 'Parker' 'Lone Tree' 'Cherry Hills Village' 'Wheat Ridge']



# zillow GetRegionChildren API
# Define the MongoDB database and table
db_client = MongoClient('localhost', 27017)
db = db_client['zillow-api']
table = db['deepSearchResults']


# api returns htm file (html)
# loop through to sample
def single_query(link, payload):
    response = requests.get(link, params=payload)
    if response.status_code != 200:
        print('WARNING', response.status_code)
    else:
        return response.text

def verify_cities(region_name):
    # region_name = dataframe['RegionName']
        if region_name in urban_lst:
            return 1
        elif region_name in suburban_lst:
            return 2
        else:
            return 0





if __name__ == '__main__':


    # print(os.environ)

    api_url_base = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm'
    payload = {'zws-id': os.environ['ZWID_API_KEY'], 'address': '4501 E 136th Pl', 'citystatezip':' Thornton CO'}
    html_str = single_query(api_url_base, payload)
    print(html_str)
    html_soup = BeautifulSoup(html_str, features="lxml")
    regionAllCity = html_soup.find_all('name')
    
    suburb_dict = {}
    for k in suburban_lst:
        suburb_dict[k] = 0


    all_city_lst = []    
    for i in regionAllCity:
        all_city_lst.append(i.text)


    for k in suburb_dict:
        if k in all_city_lst:
            # zillow-api contains data on that city
            suburb_dict[k] = 1
        else:
            # no data found for that specific data
            continue
    
    # dataset of homes in colorado
    df = pd.read_csv('/Users/isaacramirez/code/dsi/capstone-I/Addresses/zillow/City_Zhvi_TopTier.csv', encoding='latin-1')

    # cleaning df
    colorado_df = df[df['State']=='CO']
    by_region = colorado_df.groupby('RegionName').agg('mean')
    by_region.reset_index(inplace=True)

    by_region['urbanOrSuburb'] = by_region.apply(lambda row: verify_cities(row[0]), axis=1)

    print(urban_lst)
    print(suburban_lst)

