import csv
def read_csv_dict(filename):
    with open(filename, 'r') as file_handle:
        reader = csv.DictReader(file_handle, delimiter=",")
        csv_list = list(reader)
    return csv_list

class players():
    total_player = dict()
    def __init__(self,playerId):
        self.playerId = playerId
        self.games = []
        self.numberGames = 0
        self.firstName = None
        self.lastName = None
        self.totalQBR = None
    
    def set_team(self,team):
        self.team = team
    def add_games(self,gameId):
        self.games.append(gameId)
        self.numberGames = self.numberGames + 1
    def set_name(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    def get_games(self):
        return self.games
    def get_numberGames(self):
        return self.numberGames
    def get_id(self):
        return self.playerId
    def get_name(self):
        self.fullName = self.firstName + ' ' + self.lastName
        return self.fullName
    def get_team(self):
        return self.team
    def get_QBR(self):
        return self.totalQBR

class games():
    total_games = dict()
    def __init__(self, gameId):
        self.gameId = gameId
        self.player = []
        self.totalQBR = dict()
        self.outcome = dict()
        self.homeAway = dict()
        self.actionPlays = dict()
        
    def set_place(self, place):
        self.place = place
    def add_player(self, player):
        self.player.append(player)
    def set_QBR(self, player_id, QBR):
        self.totalQBR[player_id] = QBR
    def set_outcome(self, player_id, outcome):
        self.outcome[player_id] = outcome
    def set_homeAway(self, player_id, homeAway):
        self.homeAway[player_id] = homeAway
    def set_actionPlays(self, player_id, actionPlays):
        self.actionPlays[player_id] = actionPlays
        
    def get_place(self):
        return self.place
    def get_player(self):
        return self.player
    def get_id(self):
        return self.gameId
    def get_QBR(self, player_id):
        return self.totalQBR[player_id]
    def get_outcome(self, player_id):
        return self.outcome[player_id]
    def get_homeAway(self, player_id):
        return self.homeAway[player_id]
    def get_actionPlays(self, player_id):
        return self.actionPlays[player_id]

temp_year = list(range(2004, 2018))
for i in temp_year:
    temp_name = str(i) + '.csv'
    temp_list = []
    temp_list = read_csv_dict(temp_name)
    for records in temp_list:
        game_id =  records['espn_game_id']
        player_id = records['espn_player_id']

        if game_id in games.total_games:
            pass 
        else:
            games.total_games[game_id] = games(game_id)

        games.total_games[game_id].set_QBR(player_id, records['total_QBR'])
        games.total_games[game_id].set_outcome(player_id, records['won_lost'])
        games.total_games[game_id].add_player(player_id) 
        games.total_games[game_id].set_homeAway(player_id, records['home_away'])
        games.total_games[game_id].set_actionPlays(player_id, records['action_plays'])

        if player_id in players.total_player:
            pass
        else:
            players.total_player[player_id] = players(player_id)

        players.total_player[player_id].set_name(records['first_name'], records['last_name']) 
        players.total_player[player_id].add_games(game_id)

#(7 points) Which player (in which game) had the highest total_QBR in a loss?  What was the value?
player = None
game = None
highest_value = None

for i_game in games.total_games:
    for i_player in games.total_games[i_game].totalQBR.keys():
        if (highest_value == None or \
        highest_value <= games.total_games[i_game].get_QBR(i_player) )and \
        games.total_games[i_game].get_outcome(i_player) == 'L':
            highest_value = games.total_games[i_game].get_QBR(i_player)
            player = i_player
            game = i_game
            
print('highest total_QBR', highest_value)
print('player', players.total_player[player].get_name())
print('game', game)

#(7 points) Which player (in which game) had the lowesttotal_QBR in a win?  What was the value?
player = None
game = None
lowest_value = None

for i_game in games.total_games:
    for i_player in games.total_games[i_game].totalQBR.keys():
        if (lowest_value == None or \
        lowest_value >= games.total_games[i_game].get_QBR(i_player) )\
        and games.total_games[i_game].get_outcome(i_player) == 'W':
            lowest_value = games.total_games[i_game].get_QBR(i_player)
            player = i_player
            game = i_game
print('lowesttotal_QBR', lowest_value)
print('player', players.total_player[player].get_name())
print('game', game)

#(4 points) Which player (in which game) had the highest number of action_plays
player = None
game = None
highest_action_plays = None

for i_game in games.total_games:
    for i_player in games.total_games[i_game].actionPlays.keys():
        if (highest_action_plays == None or \
        highest_action_plays <= games.total_games[i_game].get_actionPlays(i_player) ):
            highest_action_plays = games.total_games[i_game].get_actionPlays(i_player)
            player = i_player
            game = i_game
            
print('highest action_plays', highest_action_plays)
print('player', players.total_player[player].get_name())
print('game', game)

#The player with the highest average total_QBR
player = None
highest_total_QBR = None

for i_player in players.total_player:
    temp_sum = 0.0
    for i_game in players.total_player[i_player].get_games():
        temp_sum = temp_sum + float(games.total_games[i_game].get_QBR(i_player))
    temp_ave = temp_sum / len(players.total_player[i_player].get_games())   
        
    if (highest_total_QBR == None or \
    highest_total_QBR <= temp_ave ):
        highest_total_QBR = temp_ave
        player = i_player

print('highest average total_QBR action_plays', highest_total_QBR)
print('player', players.total_player[player].get_name())

#What are the highest total_QBR values for a player who only started 1 game?
player = None
highest_total_QBR = None

for i_player in players.total_player:
    temp_sum = 0.0
    for i_game in players.total_player[i_player].get_games():
        temp_sum = temp_sum + float(games.total_games[i_game].get_QBR(i_player))
    if len(players.total_player[i_player].get_games()) == 1:   
        temp_ave = temp_sum / len(players.total_player[i_player].get_games())   
        if (highest_total_QBR == None or \
        highest_total_QBR <= temp_ave ):
            highest_total_QBR = temp_ave
            player = i_player
        
    else:
        pass
        
    
print('highest_total_QBR action_plays', highest_total_QBR)
print('player', players.total_player[player].get_name())

#What are the lowest total_QBR values for a player who only started 1 game?  
player = None
lowest_total_QBR = None

for i_player in players.total_player:
    temp_sum = 0.0
    for i_game in players.total_player[i_player].get_games():
        temp_sum = temp_sum + float(games.total_games[i_game].get_QBR(i_player))
    if len(players.total_player[i_player].get_games()) == 1:   
        temp_ave = temp_sum / len(players.total_player[i_player].get_games())   
        if (lowest_total_QBR == None or \
        lowest_total_QBR >= temp_ave ):
            lowest_total_QBR = temp_ave
            player = i_player
        
    else:
        pass
        
    
print('lowest_total_QBR action_plays', lowest_total_QBR)
print('player', players.total_player[player].get_name())



