# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 01:43:36 2018

@author: hejia
"""
import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.read_csv("yelp_te.csv")

#df['reviews.date'] = pd.to_datetime(df['reviews.date'], errors='coerce')
#df['reviews.date'] = df['reviews.date'].dt.year
#df1 = pd.DataFrame()
#df1["text"] = df["text"]
#df1["useful"] = df["useful"]
#df1["date"] = df["date"]
#df1["stars"] = df["stars"]


#train, test = train_test_split(df1, test_size = 0.2)

#train.to_csv("yelp_t.csv", index = False)
#test.to_csv("yelp_te.csv", index = False)

print(df["date"].describe())

df.loc[df.stars <= 3, 'stars'] = 0
df.loc[df.stars > 3, 'stars'] = 1
df.loc[df.useful >= 1, 'useful'] = 1


df14 = pd.DataFrame()
df15 = pd.DataFrame()
df16 = pd.DataFrame()
df17 = pd.DataFrame()
df17 = df[df['date'] == 2017]
df16 = df[df['date'] == 2016]
df15 = df[df['date'] == 2015]
df14 = df[df['date'] == 2014]

print(df14.shape)
print(df15.shape)
print(df16.shape)
print(df17.shape)


df14 = df14[10004:30004]
df15 = df15[10004:30004]
df16 = df16[10004:30004]
df17 = df17[10004:30004]


df14.to_csv("yelp2014.csv", index = False)
df15.to_csv("yelp2015.csv", index = False)
df16.to_csv("yelp2016.csv", index = False)
df17.to_csv("yelp2017.csv", index = False)
