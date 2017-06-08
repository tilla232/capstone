import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

km = KMeans(n_clusters=13,max_iter=500,algorithm='full')

stats = pd.read_csv('../data/metrics.csv')
stats.set_index('player',inplace=True)
# pop team column out for purposes of scaling/analysis
tm = stats.pop('tm')

# standard scale
stats_scaled = StandardScaler().fit_transform(stats)

# fit the model
km.fit(stats_scaled)

# reattach tm column, attach labels
stats['tm'] = tm
stats['labels'] = km.labels_

# calculate means for each stat for each cluster
cluster_nums = {}
for label in range(0,13):
    cluster = stats[stats['labels'] == label]
    cluster.drop('labels',axis=1,inplace=True)
    means_dict = cluster.describe().loc['mean'].to_dict()
    means_dict = {k:round(v,4) for k,v in means_dict.items()}
    cluster_nums[label] = means_dict

# create player-type distribution dataframe!
teams = list(stats['tm'].unique())
team_dists = pd.DataFrame(columns=range(0,13),index=teams)

for team in teams:
    team_dists.loc[team] = stats[stats['tm'] == team]['labels'].value_counts().to_dict()

team_dists.fillna(value=0,inplace=True)
team_dists.drop('TOT',axis=0,inplace=True)
team_dists.sort_index(inplace=True)
