from __future__ import print_function

import os
import subprocess
from sklearn.svm import SVC

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


# Load in the testing and training datasets
trainFull = pd.read_csv("data/train.csv", nrows=100000)

# Take subsets of the datasets for training and testing
train = trainFull[:80000].sample(10000)
test_set = trainFull[80000:].sample(10000)

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
svc = SVC(kernel='poly')
svc.fit(X, y)

# Score ability to predict the right hotel clust for a new subset
testX = test_set[features]
testy = test_set["hotel_cluster"]
score = svc.score(testX, testy)

print("Score is " + str(score))