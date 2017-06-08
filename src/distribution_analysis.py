import pandas as pd

stats = pd.read_csv('../data/clustered_stats.csv')

# create player-type distribution dataframe!
teams = list(stats['tm'].unique())
team_dists = pd.DataFrame(columns=range(0,13),index=teams)

for team in teams:
    team_dists.loc[team] = stats[stats['tm'] == team]['labels'].value_counts().to_dict()

team_dists.fillna(value=0,inplace=True)
team_dists.drop('TOT',axis=0,inplace=True)
team_dists.sort_index(inplace=True)

# I should've considered this before, but at this point the easiest way to create a target column is to simply do it manually.  Here's season wins for each team,alphabetically:

wins = np.array([43,53,20,41,36,51,33,40,37,67,55,42,51,26,43,41,42,31,34,31,47,29,28,24,41,32,51,49])
