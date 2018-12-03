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

train = pd.read_csv("yelp2017usefultrain.csv")
test =pd.read_csv("yelp2017usefultest.csv")

trainfinal =  [train, test]

final = pd.concat(trainfinal)


final["text"] = final.text.map(tokenize)
final["text"] = final["text"].astype(str)
final.to_csv("yelp2017useful.csv", index = False)
