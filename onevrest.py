from __future__ import print_function

import os
import subprocess
from sklearn.multiclass import OneVsRestClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import timeit

# Load in the testing and training datasets
trainFile = pd.read_csv("data/train.csv", nrows=1000000)

# Take subsets of the datasets for training and testing
trainFull = trainFile[:800000]
test_set = trainFile[800000:]

# Set a list of features to be considered in the tree
features = trainFull.columns.values.tolist()
removelist  =  ["hotel_cluster", "user_id", "date_time", 
"orig_destination_distance", "srch_ci", "srch_co"]
features = [column for column in features if column not in removelist]
print("The features considered are:")
print(features)

start_time = timeit.default_timer()

# Create and fit a decision tree to the set of data in those features
y = trainFull["hotel_cluster"] 
X = trainFull[features]
ovr = OneVsRestClassifier(RandomForestClassifier(n_estimators=10, n_jobs=-1, max_features=None, min_samples_split=250), n_jobs=-1)
ovr.fit(X, y)

# Measure ability to predict the right hotel clust for a new subset
testX = test_set[features]
testy = test_set["hotel_cluster"]
prediction = ovr.predict(testX)

report = classification_report(testy, prediction, digits=5)
print(report)

elapsed = timeit.default_timer() - start_time
print(elapsed)

score = ovr.score(testX, testy)
print("Score is " + str(score))