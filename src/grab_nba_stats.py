import cPickle
import pandas as pd
import nba_py.player as nba
from time import sleep
from random import randint

def get_rim_defense(playerID,n):
    num = randint(20,40)
    n += 1
    print num,n

    player_defense = nba.PlayerDefenseTracking(playerID)
    player_defense.json.pop('parameters')
    player_defense.json.pop('resource')

    sleep(num)
    return player_defense.json['resultSets'][0]['rowSet'][3][9]

if __name__ == '__main__':
    with open('../data/player_dict.txt','r+') as f:
        player_dict = cPickle.load(f)

    players = pd.DataFrame(player_dict.items(),columns=['player','id'])


    players['rim_defense'] = players['id'].apply(lambda x: get_rim_defense(x,0))
