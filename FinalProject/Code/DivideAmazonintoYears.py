# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 00:31:12 2018

@author: hejia
"""

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("amazon.csv")
df['reviews.date'] = pd.to_datetime(df['reviews.date'], errors='coerce')
df['reviews.date'] = df['reviews.date'].dt.year

df1 = pd.DataFrame()
df1["text"] = df["reviews.text"]
df1["useful"] = df["reviews.numHelpful"]
df1["stars"] = df["reviews.rating"]
df1["date"] = df["reviews.date"]
df1.loc[df1.stars <= 3, 'stars'] = 0
df1.loc[df1.stars > 3, 'stars'] = 1
df1.loc[df1.useful >= 1, 'useful'] = 1

df11 = pd.DataFrame()
df22 = pd.DataFrame()
df11 = df1[df1['date'] == 2017]
df22 = df1[df1['date'] == 2016]
#print(df11.head())
#print(df22.head())
df22 = df22[4:15004]
df11 = df11[4:15004]
df11.to_csv("amazon2017.csv", index = False)
df22.to_csv("amazon2016.csv", index = False)