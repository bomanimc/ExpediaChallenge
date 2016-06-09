from __future__ import print_function

import os
import subprocess
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


# Load in the testing and training datasets
trainFull = pd.read_csv("data/booking_only.csv")

k = 5
sumscores = 0

for i in range(k):
  interval = 3000000/k
  lowerbound = i * interval
  upperbound = (i + 1) * interval

  # test_set = trainFull[lowerbound: upperbound].sample(1000000)
  test_set = trainFull[lowerbound: upperbound]
  train_set = trainFull[:lowerbound] + trainFull[upperbound:]
  # train = train_set.sample(1000000)
  train = train_set

# Take subsets of the datasets for training and testing
# train = trainFull[:2400000].sample(300000)
# test_set = trainFull[2400000:].sample(300000)

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
  kn = KNeighborsClassifier(n_neighbors=25, weights='distance', algorithm='kd_tree', n_jobs=-1)
  kn.fit(X, y)

  # Measure ability to predict the right hotel clust for a new subset
  testX = test_set[features]
  testy = test_set["hotel_cluster"]
  prediction = kn.predict(testX)

  report = classification_report(testy, prediction, digits=5)
  print(report)

  score = kn.score(testX, testy)
  print("Score is " + str(score))

  sumscores += score

avgscore = sumscores/k
print("Average score is " + str(avgscore))