#import library
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
# read in the iris data
iris = load_iris()

# create features and target
X = iris.data
y = iris.target

# train/test split 
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=6)

#creating model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

#evaluation
print("\nAccuracy:",metrics.accuracy_score(y_test, y_pred))
print("\nClassification Report:\n",metrics.classification_report(y_test, y_pred))


