# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 01:12:24 2018

@author: hejia
"""

import pandas as pd
from sklearn.model_selection import train_test_split

#df123 = pd.read_csv("amazon2016.csv")
df123 = pd.read_csv("amazon2017.csv")
df = pd.DataFrame()
df["stars"] = df123["stars"]
df["text"] = df123["text"]
#df["useful"] = df123["useful"]
df11 = pd.DataFrame()
df22 = pd.DataFrame()
df11 = df[df['stars'] == 1]
df22 = df[df["stars"] == 0]
print(df11.shape)
print(df22.shape)

df22 = df22[4:904]
df11 = df11[4:904]



train1, test1 = train_test_split(df11, test_size = 0.2)
train0, test0 = train_test_split(df22, test_size = 0.2)

trainfinal =  [train1, train0]
testfinal = [test1, test0]

trainfinal = pd.concat(trainfinal)
testfinal = pd.concat(testfinal)

print(len(trainfinal.stars))
print(len(testfinal.stars))

trainfinal.to_csv("amazon2017starstrain.csv", index = False)
testfinal.to_csv("amazon2017starstest.csv", index = False)