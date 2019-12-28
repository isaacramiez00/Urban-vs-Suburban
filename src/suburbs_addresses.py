# # #!/usr/bin/env python
# # # coding: utf-8


import pyspark as ps
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import lit




from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import json
# from pymongo import MongoClient
# from pymongo.errors import DuplicateKeyError, CollectionInvalid
import datetime as dt
import os 
import pandas as pd
import numpy as np

spark = ps.sql.SparkSession.builder.master("local[4]").appName("Colorado-Addresess").getOrCreate()
sc = spark.sparkContext
get_ipython().system('ls')


aurora_df = spark.read.csv('/home/jovyan/work/code/dsi/capstone-I/data/suburban/aurora_addresses.csv',
                         header=True,       # use headers or not
                         quote='"',         # char for quotes
                         sep=",",           # char for separation
                         inferSchema=True)

boulder_df = spark.read.csv('/home/jovyan/work/code/dsi/capstone-I/data/suburban/Boulder_addresses.csv',
                            header=True,
                            quote='"',
                            sep=",",
                            inferSchema=True)

broomfield_df = spark.read.csv('/home/jovyan/work/code/dsi/capstone-I/data/suburban/Broomfield-Addresses.csv',
                            header=True,
                            quote='"',
                            sep=",",
                            inferSchema=True)


centennial_df = spark.read.csv('/home/jovyan/work/code/dsi/capstone-I/data/suburban/centennial_addresses.csv',
                            header=True,
                            quote='"',
                            sep=",",
                            inferSchema=True)

thornton_df = spark.read.csv('/home/jovyan/work/code/dsi/capstone-I/data/suburban/thornton_Addresses.csv',
                            header=True,
                            quote='"',
                            sep=",",
                            inferSchema=True)


df = spark.read.csv('/home/jovyan/work/code/dsi/capstone-I/data/urban/urbanAddresses.csv',
header=True,       # use headers or not
quote='"',         # char for quotes
sep=",",           # char for separation
inferSchema=True)

df.select('FULL_ADDRESS').rdd.takeSample(False, 1000, seed=0)
type(df)
# broomfield_df.select('FULL_ADDRESS').filter(col('CITY') == 'BROOMFIELD').show()

# rename columns
df = df.withColumnRenamed("FULL_ADDRESS", "address")

df_sample = df.select('address').distinct().rdd.takeSample(False, 1000, seed=463)


# create new dataframe yoooo
new_df = spark.createDataFrame(df_sample)

new_df = new_df.withColumn("city", lit('Denver'))\
               .withColumn('state', lit('CO'))

test_df = new_df.toPandas()
# test_df.head()
test_df = test_df.apply(lambda x: x.astype(str).str.lower())
test_df['address'] = test_df['address'].apply(lambda row: row.split())

# print(test_df.head())
# print(new_df.show(50, truncate=False))


# '''
# CREATE A FUNCTION THAT RENAMES COLUMNS, TAKES A RANDOM SAMPLE, AND CREATES A NEW DATAFRAME OF SAMPLE
# '''


# aurora_df.printSchema()
# aurora_df.select('CITY').show()

# rename columns
aurora_df = aurora_df.withColumnRenamed("ADDRESS", "address")\
       .withColumnRenamed('CITY', 'city')

aurora_sample = aurora_df.select('address', 'city').filter(col('CITY') == 'Aurora')\
         .distinct().rdd.takeSample(False, 250, seed=463)


# create new dataframe yoooo
aurora_sample_df = spark.createDataFrame(aurora_sample)

aurora_sample_df = aurora_sample_df.withColumn('state', lit('CO'))


# print(aurora_sample_df.show(50, truncate=False))
aurora_test_df = aurora_sample_df.toPandas()
# test_df.head()
aurora_test_df = aurora_test_df.apply(lambda x: x.astype(str).str.lower())
aurora_test_df['address'] = aurora_test_df['address'].apply(lambda row: row.split())


# # aurora_df.select('ADDRESS').show()
# In[51]:

# boulder_df.printSchema()
# boulder_df.select('CITY').show()

boulder_df = boulder_df.withColumnRenamed("ADDRESS", "address")\
       .withColumnRenamed('CITY', 'city')

# boulder_df.select('ADDRESS').show()
boulder_sample = boulder_df.select('address', 'city').filter(col('CITY') == 'BOULDER')\
          .distinct().rdd.takeSample(False, 250, seed=463)


# create new dataframe yoooo
boulder_sample_df = spark.createDataFrame(boulder_sample)

boulder_sample_df = boulder_sample_df.withColumn('state', lit('CO'))

# print(boulder_sample_df.show(50, truncate=False))

boulder_test_df = boulder_sample_df.toPandas()
# test_df.head()
boulder_test_df = boulder_test_df.apply(lambda x: x.astype(str).str.lower())
boulder_test_df['address'] = boulder_test_df['address'].apply(lambda row: row.split())

# broomfield_df.printSchema()

# broomfield_df.select('FULL_ADDRESS').show()

# rename column
broomfield_df = broomfield_df.withColumnRenamed("FULL_ADDRESS", "address")\
       .withColumnRenamed('CITY', 'city')


broomfield_sample = broomfield_df.select('address', 'city').filter(col('CITY') == 'BROOMFIELD')\
             .distinct().rdd.takeSample(False, 250, seed=463)


# broomfield_df.select('CITY').show()


# create new dataframe yoooo
broomfield_sample_df = spark.createDataFrame(broomfield_sample)

broomfield_sample_df = broomfield_sample_df.withColumn('state', lit('CO'))
# print(broomfield_sample_df.show(50, truncate=False))


broomfield_test_df = broomfield_sample_df.toPandas()
# test_df.head()
broomfield_test_df = broomfield_test_df.apply(lambda x: x.astype(str).str.lower())
broomfield_test_df['address'] = broomfield_test_df['address'].apply(lambda row: row.split())

# centennial_df.printSchema()
centennial_df.select('city')


# filter((!col("Name2").rlike("[0-9]")) | (col("Name2").isNotNull))
# print(centennial_df.select('IS_RESIDENTIAL').count()) 

#rename column
centennial_df = centennial_df.withColumnRenamed("FULLADDR", "address")\
       .withColumnRenamed('city', 'city')

centennial_sample = centennial_df.select('address', 'city').filter((col('IS_RESIDENTIAL') == 'RES') &\
                                                (col('city') == 'CENTENNIAL')).distinct()\
                                                .rdd.takeSample(False, 250, seed=463)
# centennial_df.select('FULLADDR', 'IS_RESIDENTIAL').filter(col('IS_RESIDENTIAL') == 'RES').show()

# create new dataframe yoooo
centennial_sample_df = spark.createDataFrame(centennial_sample)

centennial_sample_df = centennial_sample_df.withColumn('state', lit('CO'))
# print(centennial_sample_df.show(50, truncate=False))

centennial_test_df = centennial_sample_df.toPandas()
# test_df.head()
centennial_test_df = centennial_test_df.apply(lambda x: x.astype(str).str.lower())
centennial_test_df['address'] = centennial_test_df['address'].apply(lambda row: row.split())




# thornton_df.printSchema()


#rename column
thornton_df = thornton_df.withColumnRenamed("address", "address")\
       .withColumnRenamed('city', 'city')

thornton_sample = thornton_df.select('address', 'city').filter(col('CITY') == 'THORNTON').distinct()\
.rdd.takeSample(False, 250, seed=463)


# create new dataframe yoooo
thornton_sample_df = spark.createDataFrame(thornton_sample)
# In[ ]:

thornton_sample_df = thornton_sample_df.withColumn('state', lit('CO'))

# print(thornton_sample_df.show(50, truncate=False))

thornton_test_df = thornton_sample_df.toPandas()
# test_df.head()
thornton_test_df = thornton_test_df.apply(lambda x: x.astype(str).str.lower())
thornton_test_df['address'] = thornton_test_df['address'].apply(lambda row: row.split())


def clean_wrds(df, col='address'):
    
    bad_wrds = ['bldg', 'unit', 'apt', '#', 'irrp']
    clear_wrds = df.loc[:, col]
    for i, lst in enumerate(clear_wrds,0):
        for wrd in lst:
            if wrd in bad_wrds:
                lst.remove(wrd)
                lst.pop(-1)
        lst = ' '.join(lst)
        clear_wrds[i] = lst

    return clear_wrds

testing = [test_df, thornton_test_df, boulder_test_df, broomfield_test_df, aurora_test_df, centennial_test_df]

for test in testing:
       clean_wrds(test)
#        print(test.head())


def single_query(link, payload):
    response = requests.get(link, params=payload)
    if response.status_code != 200:
        print('WARNING', response.status_code)
    else:
        return response.text

def deep_search_sample(df):
       '''
       sample through each df and store values into api df
       reads a pandas dataframe
       '''
       api_url_base = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm'
       
    
       # lst that will be used to create dataframe
       lst = []
       for i in range(df.shape[0]):
       
              # grabs data from df
              address_param = df.loc[i,'address']
              citystatezip_param = df.loc[i, 'city'] + ' ' + df.loc[i, 'state']

              # upload data as param
              payload = {'zws-id':os.environ['ZWID_API_KEY'], 'address': address_param, 'citystatezip':citystatezip_param}

              # uploads api
              current_house_info = single_query(api_url_base, payload)
              
              # api to dataframe
              html_soup = BeautifulSoup(current_house_info, features='html.parser')
              
              dict = {}
              # creates dictionary
              for child in html_soup.recursiveChildGenerator():
                     if child.name in dict:
                            continue
                     else:
                            dict[child.name] = html_soup.find(child.name).text

       # puts in lst
              lst.append(dict)
       deep_search_df = pd.DataFrame(lst, index=[0])
       return deep_search_df

test = deep_search_sample(thornton_test_df)
# print(test)
html_soup = BeautifulSoup(test, features="html.parser")
# print(html_soup.find('amount').text)
# html_soup = html_soup.prettify()
# print(html_soup)

def api_to_dataframe(df):
       test = deep_search_sample(df)
       html_soup = BeautifulSoup(test, features='html.parser')
       lst = []
       dict = {}
       for child in html_soup.recursiveChildGenerator():
              if child.name in dict:
                     continue
              else:
                     dict[child.name] = html_soup.find(child.name).text
       

       deep_search_df = pd.DataFrame(dict, index=[0])
       return deep_search_df

taska_black = api_to_dataframe(thornton_test_df)
print(taska_black.columns)

# print(dict)

# for tag in html_soup.find_all():
#        print(f'{tag.clear} : {tag.text}\n')


# print(deep_search_df)



# os.environ['ZWID_API_KEY']
# api_url_base = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm'
# payload = {'zws-id':'X1-ZWz1hj43m8rojv_1ekgn', 'address': '4501 E 136th Pl', 'citystatezip':'Thornton CO'}
# html_str = single_query(api_url_base, payload)
# print(html_str)

# tags = [str(tag) for tag in html_soup.find_all()]
# print(tags)


# print(os.environ)


