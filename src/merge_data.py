import pandas as pd

stats = pd.read_csv('../data/fornowstats.csv')
shooting = pd.read_csv('../data/players_with_shooting.csv')

shooting.drop('paint_rebounding',axis=1,inplace=True)
shooting.sort_values('player',inplace=True)

stats = stats.merge(shooting,on='player')
stats.drop('Unnamed: 0',axis=1,inplace=True)

stats.to_csv('../data/2016stats.csv')
