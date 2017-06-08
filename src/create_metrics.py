import pandas as pd

stats = pd.read_csv('../data/for_clustering_2016.csv')
stats.set_index('player',inplace=True)

metrics = stats.copy()

stats_to_reg = ['paint_rebounding','3catch_and_shoot','pullupshoot']

for stat in stats_to_reg:
    metrics['{}_norm'.format(stat)] = stats[stat] * stats['MP']
    metrics.drop(stat,axis=1,inplace=True)

metrics.drop('WS/48',axis=1,inplace=True)

metrics.to_csv('../data/metrics.csv')
