import requests
import os
import json
import pandas as pd
import numpy as np

url = 'https://probasketballapi.com/players'
api_key = os.environ['PRO_BASKETBALL_API_KEY']

def request():
    query = {'api_key':api_key}
    r = requests.post(url, data=query)
    r = r.json()
    return r

if __name__ == '__main__':
    players = request()
    player_id_dict = {}

    for p in players:
        player_id_dict[p['player_name']] = p['player_id']

    df = pd.DataFrame()
    df['player'] = player_id_dict.keys()
    df['id'] = player_id_dict.values()

    df.to_csv('../data/player_ids.csv')
