from __future__ import print_function

import os
import subprocess
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import classification_report

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import timeit


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

start_time = timeit.default_timer()

# Create and fit a decision tree to the set of data in those features
y = trainFull["hotel_cluster"] 
X = trainFull[features]

rf = RandomForestClassifier(n_estimators=20, n_jobs=-1, max_features=None)
kn = KNeighborsClassifier(n_neighbors=25, weights='distance', algorithm='kd_tree', n_jobs=-1)
ovr = OneVsRestClassifier(KNeighborsClassifier(n_neighbors=25, weights='distance', algorithm='kd_tree', n_jobs=-1), n_jobs=-1)

vc = VotingClassifier(estimators=[('kn', kn), ('rf', rf), ('ovr', ovr)], voting='hard')
vc.fit(X, y)

# Measure ability to predict the right hotel clust for a new subset
testX = test_set[features]
testy = test_set["hotel_cluster"]
prediction = vc.predict(testX)

report = classification_report(testy, prediction, digits=5)
print(report)

elapsed = timeit.default_timer() - start_time
print(elapsed)

score = vc.score(testX, testy)
print("Score is " + str(score))