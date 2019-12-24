#!/usr/bin/env python
# coding: utf-8

import pyspark as ps
from pyspark.sql.types import IntegerType
spark = ps.sql.SparkSession.builder.master("local[4]").appName("Colorado-Addresess").getOrCreate()
sc = spark.sparkContext


df = spark.read.csv('urbanAddresses.csv',
                         header=True,       # use headers or not
                         quote='"',         # char for quotes
                         sep=",",           # char for separation
                         inferSchema=True)



# df.select('FULL_ADDRESS').rdd.takeSample(False, 1000, seed=0)
type(df)
# broomfield_df.select('FULL_ADDRESS').filter(col('CITY') == 'BROOMFIELD').show()

# rename columns
df = df.withColumnRenamed("FULL_ADDRESS", "address")

df_sample = df.select('address').distinct().rdd.takeSample(False, 1000, seed=463)


# create new dataframe yoooo
new_df = spark.createDataFrame(df_sample).show()


# df.select('STREET_NAME').rdd.takeSample(False, 250, seed=0)


