from __future__ import print_function

import os
import subprocess
from sklearn.metrics import classification_report

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import timeit

# Load in the testing and training datasets
trainFull = pd.read_csv("data/train.csv", nrows=1000000)

start_time = timeit.default_timer()

# Take subsets of the datasets for training and testing
train = trainFull[:800000].sample(100000)
test_set = trainFull[800000:].sample(100000)

# Measure ability to predict the right hotel clust for a new subset
testy = test_set["hotel_cluster"]
randomPrediction = np.random.random_integers(0, 100, len(testy))

report = classification_report(testy, randomPrediction, digits=5)
print(report)

elapsed = timeit.default_timer() - start_time
print(elapsed)
