#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:52:28 2021

@author: simon
"""

import vaex as vx
import numpy as np
path= 'test_vaex.hdf5'
data= vx.open(path)

#%% Method 1
# Can add new data data just like pandas
data['new_column']= np.random.uniform(size=len(data))

#%% Method 2
# Can also add new rows by using concat
times= [np.datetime64('2001-01-01')+ np.timedelta64(i, 'm') for i in range(0, 1000, 1)]
values= np.random.uniform(0, 1, size=len(times))
test= vx.from_arrays(time= times, x= values)
times= [np.datetime64('2002-01-01')+ np.timedelta64(i, 'm') for i in range(0, 1000, 1)]
values= np.random.uniform(10, 1000, size=len(times))
test2= vx.from_arrays(time= times, x= values)
merged= vx.concat((test, test2))
#%% Method 3
# You don't have to combine where a column matches, but the lengths of the dataframe must be the same
times= [np.datetime64('2001-01-01')+ np.timedelta64(i, 'm') for i in range(0, 1000, 1)]
values= np.random.uniform(0, 1, size=len(times))
test= vx.from_arrays(time= times, x= values)
times= [np.datetime64('2001-01-01')+ np.timedelta64(i, 'm') for i in range(0, 1000, 1)]
values= np.random.uniform(10, 1000, size=len(times))
test2= vx.from_arrays(other_time= times, y= values)
merged= test.join(test2)
#%% Method 4
# Can also add new data by using where a specified column matches, this case time
times= [np.datetime64('2001-01-01')+ np.timedelta64(i, 'm') for i in range(0, 1000, 5)]
values= np.random.uniform(0, 1, size=len(times))
test= vx.from_arrays(time= times, x= values)
times= [np.datetime64('2001-01-01')+ np.timedelta64(i, 'm') for i in range(0, 1000, 1)]
values= np.random.uniform(10, 1000, size=len(times))
test2= vx.from_arrays(time= times, y= values)
merged= test.join(test2, on='time')

#%% Method 5
# If you have columns in the data frames with the same name you can add a string
# on the end so you know which dataframe they came from
times= [np.datetime64('2001-01-01')+ np.timedelta64(i, 'm') for i in range(0, 1000, 1)]
values= np.random.uniform(0, 1, size=len(times))
test= vx.from_arrays(time= times, x= values)
times= [np.datetime64('2001-01-01')+ np.timedelta64(i, 'm') for i in range(0, 1000, 2)]
values= np.random.uniform(10, 1000, size=len(times))
test2= vx.from_arrays(time= times, x= values)
merged= test.join(test2, on='time', lsuffix='_1', rsuffix='_2')