#!/usr/bin/env python
# coding: utf-8

# In[37]:


# importing libraries need
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


# In[93]:


# loading file 1 - work on data one at a time - leave all outputs to check what I've done
# !ls
affordability = pd.read_csv('Affordability_Wide_2019Q3_Public.csv')
affordability.info()
affordability.describe()
affordability.head()
affordability.shape
affordability.tail()

def check_for_CO(region_name):
    split_str = region_name.split()
    if split_str[-1] == 'CO':
        return 1
    else:
        return 0

affordability.head()   
affordability['InColorado'] = affordability.apply(lambda row: check_for_CO(row[1]), axis=1)
colorado_affordability = affordability[affordability['InColorado'] == 1].copy()

colorado_affordability.drop(columns='InColorado', inplace=True)
colorado_affordability.sort_values(by='RegionName', inplace=True)
colorado_affordability.reset_index(drop=True, inplace=True)
colorado_affordability.head()


# In[104]:


# plt some shiittt - Boulder

# fig, ax = plt.subplots(3, 2, figsize=(12,8))

num_of_axes = len(colorado_affordability['RegionName'].unique())

# get data
time_indices = colorado_affordability.loc[:, '1999-12':].copy()
periods = len(time_indices.columns)
x = pd.period_range(start=time_indices.columns[0], periods=periods, freq='Q').to_timestamp().to_pydatetime()
y = time_indices.iloc[0, :]
y_rent = time_indices.iloc[1,:]
# plot
plt.plot(x, y, label='Mortgage')
plt.plot(x, y_rent, label='rent')
plt.legend()


# In[102]:


# colorado_affordability[colorado_affordability['Index'] == 'Price To Income']
colorado_affordability.head()


# In[90]:


time_indices


# In[134]:


# new data
# !ls
city_single_family = pd.read_csv('City_Zhvi_SingleFamilyResidence.csv', delimiter=',', encoding='latin-1')
city_single_family.head()

colorado_single_family = city_single_family[city_single_family['State']=='CO'].copy()
colorado_single_family.sort_values('RegionName', inplace=True)
colorado_single_family.reset_index(drop=True, inplace=True)

colorado_single_family['Metro'].value_counts()
mean_co_sf_by_metro = colorado_single_family.groupby('Metro').agg('mean')
mean_co_sf_by_metro.reset_index(inplace=True)
mean_co_sf_by_metro


# In[148]:


city_sf_time_indices = mean_co_sf_by_metro.iloc[:, 3:].copy()
city_sf_periods = len(city_sf_time_indices.columns)
x = pd.period_range(start=city_sf_time_indices.columns[0], periods=city_sf_periods, freq='M').to_timestamp().to_pydatetime()
y = city_sf_time_indices.iloc[0,:]

plt.plot(x, y)

def num_of_axes(dataframe):
    '''
    creates a certain amount of axes based on
    number of rows (for the unique locations)
    '''
    rows = int(np.ceil(np.sqrt(dataframe.shape[0])))
    columns = rows
    return rows, columns


def plot_by_metro_single_family(dataframe, metro_arr):
    '''
    plots all possible locations for metro single families
    dataframe is clean and first column are the unique locations
    '''

    # setting up data
    locations_labels = dataframe.iloc[:,0].to_numpy()
    time_series_df = dataframe.iloc[:, 1:].copy()
    periods = len(time_series_df.columns)
    x = pd.period_range(start=dataframe.columns[0], periods=periods, freq=freq).to_timestamp().to_pydatetime()

    # setting up plot
    axes_rows, axes_columns = num_of_axes(dataframe)
    fig, ax = plt.subplots(axes_rows, axes_columns, figsize(12,12))

    rows = dataframe.shape[0]
    for i in range(rows):
        pass







