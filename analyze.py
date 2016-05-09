import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt

train = pd.read_csv("data/train.csv", parse_dates=['srch_ci', 'srch_co'], nrows=1000)
train.info()

corrMatrix = train.corr(method='pearson', min_periods=1)
print(corrMatrix)

# # Generate a mask for the upper triangle
# mask = np.zeros_like(corrMatrix, dtype=np.bool)
# mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(20, 15))
plt.xticks(rotation=45)

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corrMatrix, cmap=cmap, vmax=.3,
            square=True, xticklabels=True, yticklabels=True, linewidths=1, ax=ax)

plt.savefig("myfig.png")
