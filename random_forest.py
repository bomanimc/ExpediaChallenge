from __future__ import print_function

import os
import subprocess
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


# Load in the testing and training datasets
trainFull = pd.read_csv("data/train.csv", nrows=1000000)

# Take subsets of the datasets for training and testing
train = trainFull[:800000].sample(100000)
test_set = trainFull[800000:].sample(100000)

# Set a list of features to be considered in the tree
features = trainFull.columns.values.tolist()
removelist  =  ["hotel_cluster", "user_id", "date_time", 
"orig_destination_distance", "srch_ci", "srch_co"]
features = [column for column in features if column not in removelist]
print("The features considered are:")
print(features)

# Create and fit a decision tree to the set of data in those features
y = trainFull["hotel_cluster"] 
X = trainFull[features]
rf = RandomForestClassifier(n_estimators=20, n_jobs=-1, max_features=None)
rf.fit(X, y)

# Print the Unique Classes
print("Unique Classes: {}".format(rf.classes_))

# Print feature importances
print(rf.feature_importances_)

# Measure ability to predict the right hotel clust for a new subset
testX = test_set[features]
testy = test_set["hotel_cluster"]
prediction = rf.predict(testX)

report = classification_report(testy, prediction, digits=5)
print(report)

score = rf.score(testX, testy)
print("Score is " + str(score))