from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
# read in the iris data
iris = load_iris()

# create features and target
X = iris.data
y = iris.target

# train/test split 
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=6)

#Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier
#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)
#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)

#evaluation
print("\nAccuracy:",metrics.accuracy_score(y_test, y_pred))
print("\nClassification Report:\n",metrics.classification_report(y_test, y_pred)) 