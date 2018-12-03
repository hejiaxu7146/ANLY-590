# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 01:38:33 2018

@author: hejia
"""
import pandas as pd

df = pd.read_csv("yelp2014usefultrain.csv")

df = df.drop('date', axis=1)
df = df.drop('stars', axis=1)
#df = df.drop('useful', axis=1)

df.to_csv("yelp2014usefultrain.csv", index = False)


###2014 useful train
