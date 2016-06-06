from __future__ import print_function

import os
import subprocess
from sklearn.tree import DecisionTreeClassifier, export_graphviz

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

def visualize_tree(tree, feature_names):
    """Create tree png using graphviz.

    Args
    ----
    tree -- scikit-learn DecsisionTree.
    feature_names -- list of feature names.
    """
    with open("output/dt.dot", 'w') as f:
        export_graphviz(tree, out_file=f,
                        feature_names=feature_names)

    command = ["dot", "-Tpng", "output/dt.dot", "-o", "output/dt.png"]
    try:
        subprocess.check_call(command)
    except:
        exit("Could not run dot, ie graphviz, to "
             "produce visualization")

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
dt = DecisionTreeClassifier(min_samples_split=20)
dt.fit(X, y)

# Make a visualization of the decision tree
visualize_tree(dt, features)

# Print the Unique Classes
print("Unique Classes: {}".format(dt.classes_))

# Score ability to predict the right hotel clust for a new subset
testX = test_set[features]
testy = test_set["hotel_cluster"]
score = dt.score(testX, testy)

print("Score is " + str(score))
