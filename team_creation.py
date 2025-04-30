# File to create the teams also randomised :3

# FOR FUTURE: Have a way of organising the players in stats of best to worst so for example the pitcher is designated as whoever has the best pitching ig
# ur dumb u dont know how to do that :{


import random
from player_generation import *
from enemy_team_generation import *
from class_definitions import *


def team_creation(team_name, players, wins, loses):
    return Team(fname=team_name, 
                        players=players, 
                        batting=0, 
                        pitching=0, 
                        )


available_teamnames = []

teamnames_file = "teamnames.txt"
teamnames = open(teamnames_file, "r")
for line in teamnames:
    line = line.rstrip()
    available_teamnames.append(line)
teamnames.close

same_team = True

number_of_teams = len(available_teamnames) - 1


def create_team():
    #print(number_of_teams)
    #print(available_teamnames[random.randint(0, number_of_teams)])

    Team1_name = available_teamnames[random.randint(0, number_of_teams)]
    available_teamnames.remove(Team1_name)
    Team2_name = available_teamnames[random.randint(0, number_of_teams - 1)]


    userPlayers = "null"
    enemyPlayers = createEnemyTeam()

    userTeam = team_creation(Team1_name, userPlayers)
    enemyTeam = team_creation(Team2_name, enemyPlayers)






if __name__ == "__main__":
    create_team()