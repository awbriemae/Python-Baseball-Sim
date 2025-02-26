from player_generation import *

# This generates the "enemy" team

# function that returns random stats

teamName = "Enemy"

def enemyPositionPicker(batting, pitching, running, catching, throwing, position):
    highest_pitch = 0
    if pitching > highest_pitch:
        highest_pitch = pitching
        
    return position

enemyTeamRoster = []
# Generates a random enemy team
def enemyTeamGeneration():
    for i in range(0, 9):
        fname, lname, batting, pitching, running, catching, throwing, position = player_randomiser()
        position = enemyPositionPicker()
        print(fname)
        createdPlayer = player_creation(fname, lname, batting, pitching, running, catching, throwing, position)
        enemyTeamRoster.append(createdPlayer)
        print(enemyTeamRoster[i])
    return enemyTeamRoster

if __name__ == "__main__":
    # Creating a player
    #playerHireProcess()
    #savePlayersToFile(users_team)
    #loadPlayersFromFile()
    enemyTeamGeneration()