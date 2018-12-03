# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 00:30:15 2018

@author: hejia
"""

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("yelp_test.csv", encoding = "ISO-8859-1")
#print(df.head())
df1 = pd.DataFrame()
df1["text"] = df["text"]
df1["stars"] = df["stars"]
df1 = df1.drop(index = 444090)
df1["stars"] = pd.to_numeric(df1["stars"])
#print(df1.head())
#print(df1[444089:444090])
df1.loc[df1.stars < 4, 'stars'] = 0
df1.loc[df1.stars > 3, 'stars'] = 1
print(df1.head())

df11 = pd.DataFrame()
df22 = pd.DataFrame()
df11 = df1[df1['stars'] == 1]
df22 = df1[df1["stars"] == 0]
print(df11.head())
print(df22.head())
#df1 = pd.DataFrame()
#df1["text"] = df["text"]
#df1["useful"] = df["useful"]
#df1.ix[df.useful > 1, 'useful'] = 0

#train, test = train_test_split(df1, test_size = 0.2)

#train.to_csv("yelp_train.csv", index = False)
#test.to_csv("testhelp.csv", index = False)

#print(len(df.stars))
#import tensorflow as tf
#import keras

df22 = df22[4:20004]
df11 = df11[4:20004]

train1, test1 = train_test_split(df11, test_size = 0.2)
train0, test0 = train_test_split(df22, test_size = 0.2)

trainfinal =  [train1, train0]
testfinal = [test1, test0]

trainfinal = pd.concat(trainfinal)
testfinal = pd.concat(testfinal)

print(len(trainfinal.stars))
print(len(testfinal.stars))

trainfinal.to_csv("yelpstarstrain.csv", index = False)
testfinal.to_csv("yelpstarstest.csv", index = False)