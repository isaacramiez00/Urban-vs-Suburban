#!/usr/bin/env python
# coding: utf-8
import pyspark as ps
from pyspark.sql.types import IntegerType
spark = ps.sql.SparkSession.builder.master("local[4]").appName("Colorado-Addresess").getOrCreate()
sc = spark.sparkContext


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


df = spark.read.csv('/home/jovyan/work/code/dsi/capstone-I/data/urban/urbanAddresses.csv',
                         header=True,       # use headers or not
                         quote='"',         # char for quotes
                         sep=",",           # char for separation
                         inferSchema=True)



# df.select('FULL_ADDRESS').rdd.takeSample(False, 1000, seed=0)
# type(df)
# broomfield_df.select('FULL_ADDRESS').filter(col('CITY') == 'BROOMFIELD').show()

# rename columns
df = df.withColumnRenamed("FULL_ADDRESS", "address")

df_sample = df.select('address').distinct().rdd.takeSample(False, 1000, seed=463)


# create new dataframe yoooo
new_df = spark.createDataFrame(df_sample)

# print(new_df.show())


def single_query(link, payload):
    response = requests.get(link, params=payload)
    if response.status_code != 200:
        print('WARNING', response.status_code)
    else:
        return response.text






api_url_base = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm'
payload = {'zws-id': os.environ['ZWID_API_KEY'], 'address': pull_test, 'citystatezip':' Denver CO'}
html_str = single_query(api_url_base, payload)
print(html_str)

# df.select('STREET_NAME').rdd.takeSample(False, 250, seed=0)


