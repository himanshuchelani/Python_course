"""Q1. (Create a program that fulfills the following specification.)

Program Specification:
Import breast_cancer.csv file.

This breast cancer database was obtained from the University of Wisconsin

Hospitals, Madison from Dr. William H. Wolberg.

Attribute Information: (class attribute has been moved to last column)

Sample Code Number(id number)                     ----> represented by column A.

Clump Thickness (1 – 10)                                     ----> represented by column B.
Uniformity of Cell Size(1 - 10)                             ----> represented by column C.
Uniformity of Cell Shape (1 - 10)                        ----> represented by column D.
Marginal Adhesion (1 - 10)                                  ----> represented by column E.
Single Epithelial Cell Size (1 - 10)                        ----> represented by column F.
Bare Nuclei (1 - 10)                                               ----> represented by column G.
Bland Chromatin (1 - 10)                                     ----> represented by column H.
Normal Nucleoli (1 - 10)                                      ----> represented by column I.
Mitoses (1 - 10)                                                     ----> represented by column J.
Class: (2 for Benign and 4 for Malignant)         ----> represented by column K. 
A Benign tumor is not a cancerous tumor and Malignant tumor is a cancerous tumor.

                    Impute the missing values with the most frequent values.
                     Perform Classification on the given data-set to predict if the tumor is cancerous or not.
                    Check the accuracy of the model.
                    Predict whether a women has Benign tumor or Malignant tumor, if her Clump thickness is around 6, uniformity of cell size is 2, Uniformity of Cell Shape is 5, Marginal Adhesion is 3, Bland Chromatin is 9, Mitoses is 4, Bare Nuclei is 7, Normal Nuclei is 2 and Single Epithelial Cell Size is 2

(you can neglect the id number column as it doesn't seem  a predictor column)


"""



#import library
import pandas as pd
import numpy as np

#import dataset
df=pd.read_csv("breast_cancer.csv")
df.isnull().any()

# Removing Null Values
df["G"]=df["G"].fillna(method="ffill")


#selecting features and null
labels=df.iloc[: ,-1].values
features=df.iloc[:,1:-1].values

#applying spliting of data

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 0)

#applying model
from sklearn.svm import SVC
classifier = SVC(kernel = 'poly', random_state = 0)
classifier.fit(features_train, labels_train)
labels_pred=classifier.predict(features_test)

#finding score
score_test=classifier.score(features_test,labels_test)
score_train=classifier.score(features_train,labels_train)

#pridictions
labels_pred=classifier.predict(features_test).tolist()
result=[]
for i in labels_pred:
    if i==4:
        result.append("Cancerous")
    else:
        result.append("NonCancerous")
result=np.array(result)
print(result)

x=[6,2,5,3,2,7,9,2,4]
x=np.array(x,ndmin=2)
pred=classifier.predict(x)

if pred==4:
    print("Malignant tumor")
else:
    print("Benign tumor")