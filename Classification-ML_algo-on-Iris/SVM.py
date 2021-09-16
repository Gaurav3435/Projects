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

# Fitting Naive Bayes Classification to the Training set with linear kernel
from sklearn.svm import SVC
model=SVC()
model.fit(X_train, y_train)
y_pred=model.predict(X_test)

#evaluation
print("\nAccuracy:",metrics.accuracy_score(y_test, y_pred))
print("\nClassification Report:\n",metrics.classification_report(y_test, y_pred))