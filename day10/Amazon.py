"""
Q1. Code Challegene (NLP)
Dataset: amazon_cells_labelled.txt


The Data has sentences from Amazon Reviews

Each line in Data Set is tagged positive or negative

Create a Machine learning model using Natural Language Processing that can predict wheter a given review about the product is positive or negative
"""



#Importig Librarires
import pandas as pd
import numpy as np
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

#Loading Dataset 
df=pd.read_csv("amazon_cells_labelled.txt",delimiter='\t',header=None)
df.columns=["Review","Pred"]

#Appling Noise Removal
corpus = []
for i in range(0,1000):
    review=re.sub('[^a-zA-Z]'," ",df['Review'][i])
    review=review.lower()
    review=review.split()
    review=[word for word in review if word not in set(stopwords.words("english"))]
#Applying stemming
    ps=PorterStemmer()
    review = [ps.stem(word) for word in review]
    review=' '.join(review)
    corpus.append(review)

#bag of plot   
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
labels = df.iloc[:, 1].values

#Spiliting the data
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

#Appliying Model
from sklearn.naive_bayes import GaussianNB,BernoulliNB
classifier = BernoulliNB()
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm_nb = confusion_matrix(labels_test, labels_pred)

#Testing Score
train_score=classifier.score(features_train,labels_train)
test_score=classifier.score(features_test,labels_test)