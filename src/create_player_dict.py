import cPickle
import pandas as pd
import goldsberry
import string

bbref = pd.read_csv('../data/bbref_advanced.csv')

# the format of this table, taken directly from basketball-reference.com, is a little annoying: the 'Player' column features a player's name, followed by his abbreviation that the site uses as a URL endpoint.  We don't need this bit, so this line strips it
bbref.Player = bbref.Player.apply(lambda x: x.split('\\',1)[0].translate(None,string.punctuation.replace('-','').replace("'",'')).replace(' Jr','').replace('Jr.','').replace("III",'').strip())

# There are a few (extremely annoying) exceptions to the naming conventions on NBA.com.  bbref is very good about standardizing this, NBA is decidedly not....these next lines fix these exceptions

bbref.Player[99] = 'Nene'
bbref.Player[268] = 'Taurean Prince'
# bbref.Player[118] = 'T.J. McConnell'





players2016 = goldsberry.PlayerList(Season='2016-17')
players2016 = pd.DataFrame(players2016.players())
players2016.DISPLAY_FIRST_LAST = players2016.DISPLAY_FIRST_LAST.apply(lambda x: str(x).split('\\',1)[0].translate(None,string.punctuation.replace('-','').replace("'",'')).replace(' Jr','').replace('Jr.','').replace('III','').strip())

player_dict = pd.Series(players2016.PERSON_ID.values,index=players2016.DISPLAY_FIRST_LAST)


# now we see the reason for reading in the basketball-reference table: that table was built using the basketball-reference season finder, with parameters GP >= 50, and MPG >= 10.  This loop will remove all players from our player_dict that don't meet those criteria.

players_dict = {}
for player in bbref.Player.values:
    players_dict[player] = player_dict[player]

with open('../data/player_dict.txt','r+') as f:
    cPickle.dump(players_dict,f)
