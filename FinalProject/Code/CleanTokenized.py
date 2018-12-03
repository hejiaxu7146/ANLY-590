import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import numpy as np
import re
stopword = set(stopwords.words('english'))
porter = PorterStemmer()

def tokenize(text):
    letters_only = re.sub("[^a-zA-Z]",  # Search for all non-letters
                          " ",          # Replace all non-letters with spaces
                          str(text))     # Column and row to search
    words = word_tokenize(letters_only) #split words
    words = [w.lower() for w in words if w.isalpha()] #get rid of punctuation
    words =[w for w in words if  not w in stopword]
    stemmed = [porter.stem(w) for w in words]
    stemmed = ' '.join(w for w in stemmed)
    return stemmed


train = pd.read_csv("yelp2014starstrain.csv")
train["text"] = train.text.map(tokenize)
train["text"] = train["text"].astype(str)
train.head()

train.to_csv("simpletest1.csv", index = False)
