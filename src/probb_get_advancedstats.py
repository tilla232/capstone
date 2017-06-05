import requests
import os
import json
import pandas as pd
import numpy as np
from collections import OrderedDict

url = 'http://api.probasketballapi.com/advanced/player'
api_key = os.environ['PRO_BASKETBALL_API_KEY']
key_stats = ['pie','ts_pct','dreb_pct','efg_pct','def_rating','treb_pct','usg_pct','oreb_pct','pace','ast_ratio','ast_tov','ast_pct','off_rating']


def ms_to_minutes(t):
    '''
    Params:
    t - A time string of format HH:MM

    Output:
    A float approximation of t in minutes
    '''
    m, s = [float(i) for i in t.split(':')]
    return m + round(s/60,2)

def request(player_id,season):
    query = {'api_key':api_key,'player_id':player_id,'season':season}
    r = requests.post(url, data=query)
    r = r.json()
    return r

def season_stats(game_dicts,stats,player_id):
    '''
    ProBasketballAPI returns game-by-game stats in a list of dictionaries, as opposed to something more convenient like a list of per-game stats.  This function takes in a player's JSON data, and returns such a list.

    Params:
    games_json - Player's JSON object containing game logs of advanced stats
    stats - The desired stats to return in list form

    Output:
    season_stats - An ordered list of all per-game stats requested
    '''
    season_stats = OrderedDict()
    season_stats['player_id'] = player_id
    for stat in stats:
        stat_list = [float(game[stat]) for game in game_dicts]
        season_stat = (sum(stat_list)/float(len(stat_list)))
        season_stats[stat] = round(season_stat,3)
    return season_stats

if __name__ == '__main__':
    # read in player/id data to pandas df players
    players = pd.read_csv('../data/player_ids.csv')

    # create empty dataframe to house all advanced stats, along with player
    # name/id's
    advanced_stats = pd.DataFrame()

    # populate player and player_id columns in advanced_stats, set players as index
    advanced_stats['player'] = players['player']
    advanced_stats['player_id'] = players['id']
    advanced_stats.set_index('player',inplace=True)

    # create empty columns for key stats (found, shockingly, in list key_stats)
    for stat in key_stats:
        advanced_stats[stat] = ''

    # this is the big one: iteratively utilizes functions request and season_stats to create a dictionary of stats and populate our dataframe with those stats

    # rewrite as function to make more generic for further use on seasons besides 2016!!!
    for player_name,player_id in zip(players['player'].values,players['id'].values):
        logs = request(player_id,2016)
        if not logs:
            continue
        dicts = season_stats(logs,key_stats,player_id)
        advanced_stats.loc[player_name] = pd.Series(dicts)

    advanced_stats.to_csv('../data/probb_advanced_stats.csv')
