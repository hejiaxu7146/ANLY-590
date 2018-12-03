import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("yelp2014.csv")
print(df.head())
#print(df.head())
df11 = pd.DataFrame()
df22 = pd.DataFrame()
df11 = df[df['stars'] == 1]
df22 = df[df["stars"] == 0]
print(df11.shape)
print(df22.shape)
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

df22 = df22[4:6004]
df11 = df11[4:6004]

train1, test1 = train_test_split(df11, test_size = 0.2)
train0, test0 = train_test_split(df22, test_size = 0.2)

trainfinal =  [train1, train0]
testfinal = [test1, test0]

trainfinal = pd.concat(trainfinal)
testfinal = pd.concat(testfinal)

print(len(trainfinal.useful))
print(len(testfinal.useful))

trainfinal.to_csv("yelp2014starstrain.csv", index = False)
testfinal.to_csv("yelp2014starstest.csv", index = False)
