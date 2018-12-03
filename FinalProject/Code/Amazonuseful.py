# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 01:27:59 2018

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
df1.loc[df1.useful >= 1, 'useful'] = 1

df11 = pd.DataFrame()
df22 = pd.DataFrame()
df11 = df1[df1['useful'] == 1]
df22 = df1[df1["useful"] == 0]
print(df11.shape)
print(df22.shape)

df22 = df22[4:3004]
df11 = df11[4:3004]



train1, test1 = train_test_split(df11, test_size = 0.2)
train0, test0 = train_test_split(df22, test_size = 0.2)

trainfinal =  [train1, train0]
testfinal = [test1, test0]

trainfinal = pd.concat(trainfinal)
testfinal = pd.concat(testfinal)

trainfinal.to_csv("amazonUSEFULtrain.csv", index = False)
testfinal.to_csv("amazonUSEFULtest.csv", index = False)