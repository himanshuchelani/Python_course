"""
Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score"""



import pandas as pd
import numpy as np
df=pd.read_csv("kc_house_data.csv")
df["date"]=df["date"].apply(lambda x: x[0:4])
df["date"]=pd.to_numeric(df["date"])
df=df.drop("id",axis=1)
df.isnull().any()
df["sqft_above"]=df.fillna(df['sqft_above'].mode())
labels=df["price"].values
features = df.drop('price',axis = 1)


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features=sc.fit_transform(features)


from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)



from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features_train,labels_train)
labels_pred=regressor.predict(features_test)
print("printing th e score with test mode:",regressor.score(features_test,labels_test))
print("pritning the score with train model",regressor.score(features_train,labels_train))


from sklearn import metrics
print("mean square value:",np.sqrt(metrics.mean_squared_error(labels_test,labels_pred)))

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet

ls=Lasso()
ri=Ridge()
el=ElasticNet()



ls.fit(features_train,labels_train)
ri.fit(features_train,labels_train)
el.fit(features_train,labels_train)






print ("RSquare Value for Simple Regresssion TEST data is-") 
print (np.round (regressor .score(features_test,labels_test)*100,2))

print ("RSquare Value for Lasso Regresssion TEST data is-")
print (np.round (ls.score(features_test,labels_test)*100,2))

print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (ri.score(features_test,labels_test)*100,2))

print ("RSquare Value for Elastic Net Regresssion TEST data is-")
print (np.round (el.score(features_test,labels_test)*100,2))



predict_test_lasso = ls.predict (features_test) 
predict_test_ridge = ri.predict (features_test)
predict_test_elastic = el.predict(features_test)





print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lasso),2))

print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_ridge),2))

print ("ElasticNet Mean Square Error (MSE) for TEST data is")
print (np.round (metrics .mean_squared_error(labels_test, predict_test_elastic),2))

