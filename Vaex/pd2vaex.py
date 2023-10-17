#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 28 12:57:37 2021

@author: simon
"""
""" Imports """
import pandas as pd
import numpy as np
import vaex as vx

# path to pandas file
pandas_path= 'test.h5'
# path to where the vaex file want to be put
vaex_path= 'test_vaex.hdf5'
# load the pandas store
store=pd.HDFStore(pandas_path, mode='r')
# create an empty list to put the dataframes in
dfs=[]
for key in store.keys(): #Loop through the keys in the HDF store
    # Load the data frame for the chosen key and change to vaex format
    data= vx.from_pandas(store.select(key),copy_index=True) # copy index is important to preserve the index from the pandas data frame
    # Create a new column and populate it with strings based on the key
    data['sat_id']= np.array([key[1:]]*len(data))
    # rename the index column (that would've orginally been the actual index in the pandas file) to something sensible
    data.rename('index', 'Date_UTC')
    # add the vaex data frame to the list
    dfs.append(data)
# combine the vaex data frame together
data= vx.concat(dfs)
# export the new vaex data frame as a hdf5 file
data.export_hdf5(vaex_path)

