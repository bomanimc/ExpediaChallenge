import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

train = pd.read_csv("data/train.csv", parse_dates=['srch_ci', 'srch_co'], nrows=10000)
train.info()