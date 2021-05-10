import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#reading in the data
movie_df = pd.read_csv('applications.csv')

#let's remove duplicates first
movie_df['dup'] = movie_df.duplicated(subset=None, keep='first')

movie_df = movie_df[movie_df['dup'] == False]

print(movie_df)

del movie_df['dup']

print(movie_df.head())

import re
from nltk.stem import WordNetLemmatizer, PorterStemmer, SnowballStemmer
stop_words_file = 'SmartStoplist.txt'

stop_words = []

with open(stop_words_file, "r") as f:
    for line in f:
        stop_words.extend(line.split()) 
        
stop_words = stop_words  

def preprocess(raw_text):
    
    #regular expression keeping only letters 
    letters_only_text = re.sub("[^a-zA-Z]", " ", raw_text)

    # convert to lower case and split into words -> convert string into list ( 'hello world' -> ['hello', 'world'])
    words = letters_only_text.lower().split()

    cleaned_words = []
    lemmatizer = PorterStemmer() #plug in here any other stemmer or lemmatiser you want to try out
    
    # remove stopwords
    for word in words:
        if word not in stop_words:
            cleaned_words.append(word)
    
    # stemm or lemmatise words
    stemmed_words = []
    for word in cleaned_words:
        word = lemmatizer.stem(word)   #dont forget to change stem to lemmatize if you are using a lemmatizer
        stemmed_words.append(word)
    
    # converting list back to string
    return " ".join(stemmed_words)

movie_df['prep'] = movie_df['reason'].apply(preprocess)

from collections import Counter
Counter(" ".join(movie_df["reason"]).split()).most_common(10)

print(Counter(" ".join(movie_df["reason"]).split()).most_common(10))

#nice library to produce wordclouds
from wordcloud import WordCloud

import matplotlib.pyplot as plt


all_words = '' 

#looping through all incidents and joining them to one text, to extract most common words
for arg in movie_df["reason"]: 

    tokens = arg.split()  
      
    all_words += " ".join(tokens)+" "

wordcloud = WordCloud(width = 700, height = 700, 
                background_color ='white', 
                min_font_size = 10).generate(all_words) 
  
# plot the WordCloud image                        
plt.figure(figsize = (5, 5), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show()
