#!/usr/bin/env python
# coding: utf-8


import pyspark as ps
from pyspark.sql.functions import col

spark = ps.sql.SparkSession.builder.master("local[4]").appName("Colorado-Addresess").getOrCreate()
sc = spark.sparkContext
get_ipython().system('ls')


aurora_df = spark.read.csv('aurora_addresses.csv',
                         header=True,       # use headers or not
                         quote='"',         # char for quotes
                         sep=",",           # char for separation
                         inferSchema=True)

boulder_df = spark.read.csv('Boulder_addresses.csv',
                            header=True,
                            quote='"',
                            sep=",",
                            inferSchema=True)

broomfield_df = spark.read.csv('Broomfield-Addresses.csv',
                            header=True,
                            quote='"',
                            sep=",",
                            inferSchema=True)


centennial_df = spark.read.csv('centennial_addresses.csv',
                            header=True,
                            quote='"',
                            sep=",",
                            inferSchema=True)

thornton_df = spark.read.csv('thornton_Addresses.csv',
                            header=True,
                            quote='"',
                            sep=",",
                            inferSchema=True)


'''
CREATE A FUNCTION THAT RENAMES COLUMNS, TAKES A RANDOM SAMPLE, AND CREATES A NEW DATAFRAME OF SAMPLE
'''


# aurora_df.printSchema()
# aurora_df.select('CITY').show()

# rename columns
aurora_df = aurora_df.withColumnRenamed("ADDRESS", "address")\
       .withColumnRenamed('CITY', 'city')

aurora_sample = aurora_df.select('address', 'city').filter(col('CITY') == 'Aurora')\
         .distinct().rdd.takeSample(False, 250, seed=463)


# create new dataframe yoooo
aurora_sample_df = spark.createDataFrame(aurora_sample).show()


# aurora_df.select('ADDRESS').show()
# In[51]:

# boulder_df.printSchema()
# boulder_df.select('CITY').show()

boulder_df = boulder_df.withColumnRenamed("ADDRESS", "address")\
       .withColumnRenamed('CITY', 'city')

# boulder_df.select('ADDRESS').show()
boulder_sample = boulder_df.select('address', 'city').filter(col('CITY') == 'BOULDER')\
          .distinct().rdd.takeSample(False, 250, seed=463)


# create new dataframe yoooo
boulder_sample_df = spark.createDataFrame(boulder_sample).show()




# broomfield_df.printSchema()

# broomfield_df.select('FULL_ADDRESS').show()

# rename column
broomfield_df = broomfield_df.withColumnRenamed("FULL_ADDRESS", "address")\
       .withColumnRenamed('CITY', 'city')


broomfield_sample = broomfield_df.select('address', 'city').filter(col('CITY') == 'BROOMFIELD')\
             .distinct().rdd.takeSample(False, 250, seed=463)

# broomfield_df.select('CITY').show()


# create new dataframe yoooo
broomfield_sample_df = spark.createDataFrame(broomfield_sample).show()



# centennial_df.printSchema()
centennial_df.select('city').show()


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
centennial_sample_df = spark.createDataFrame(centennial_sample).show()

# In[42]:



# thornton_df.printSchema()


#rename column
thornton_df = thornton_df.withColumnRenamed("address", "address")\
       .withColumnRenamed('city', 'city')

thornton_sample = thornton_df.select('address', 'city').filter(col('CITY') == 'THORNTON').distinct()\
.rdd.takeSample(False, 250, seed=463)


# create new dataframe yoooo
thornton_sample_df = spark.createDataFrame(thornton_sample).show()
# In[ ]:




