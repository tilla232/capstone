import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import silhouette_score
from sklearn.cluster import Birch
from sklearn.preprocessing import StandardScaler


# Now we explore clustering using the BIRCH algorithm

stats = pd.read_csv('../data/metrics.csv')
stats.set_index('player',inplace=True)

scaler = StandardScaler()
stats = scaler.fit_transform(stats)

cluster_list = range(10,21)
threshold_list = np.linspace(0.1,0.9,5)
branching_factor_list = np.arange(20,100,20)

model_list = []
for k in cluster_list:
    for t in threshold_list:
        for b in branching_factor_list:
            birch = Birch(threshold=t,branching_factor=b,n_clusters=k)
            birch.fit(stats)
            print "For {} clusters, with a threshold of {} and a branching factor of {}, our silhouette score is {}.".format(k,t,b,silhouette_score(stats,birch.labels_))
            print '---------------------------------------------'
            model_list.append((silhouette_score(stats,birch.labels_),(k,t,b)))
