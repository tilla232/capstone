import requests
import os
import json
import pandas as pd
import numpy as np

url = 'http://api.probasketballapi.com/advanced/player'
api_key = os.environ['PRO_BASKETBALL_API_KEY']
key_stats = ['pie','ts_pct','dreb_pct','efg_pct','def_rating','treb_pct','usg_pct','oreb_pct','pace','ast_ratio','ast_tov','ast_pct','off_rating']


def ms_to_minutes(t):
    '''
    Params:
    t - A timestamp string of format HH:MM
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

if __name__ == '__main__':
    # read in player/id data to pandas df players
    players = pd.read_csv('../data/player_ids.csv')

    # create empty dataframe to house all advanced stats, along with player
    # name/id's
    advanced_stats = pd.DataFrame()

    # populate player and player_id columns in advanced_stats
    advanced_stats['player'] = players['player']
    advanced_stats['player_id'] = players['id']

    # create empty columns for key stats (found, shockingly, in list key_stats)
    for stat in key_stats:
        advanced_stats[stat] = ''
