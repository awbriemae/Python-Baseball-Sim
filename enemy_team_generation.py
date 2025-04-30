from player_generation import *
import operator
# This generates the "enemy" team

# function that returns random stats

teamName = "Enemy"
no_position = []

enemyTeamRoster = []
# Generates a random enemy team
def enemyTeamGeneration():
    no_position = []
    for i in range(0, 9):
        fname, lname, batting, pitching, running, catching, throwing, position = player_randomiser()
        position = "Bench Warmer"
        createdPlayer = player_creation(fname, lname, batting, pitching, running, catching, throwing, position)
        no_position.append(createdPlayer)
        # print(no_position[i])
    return no_position

# def highest_pitching(no_position):
#     highest_pitching = 0
#     player_pointer = 0
#     for item in no_position:
#         if no_position[item].pitching > highest_pitching:
#             print(no_position[item] + "YES")
#             highest_pitching = no_position[item]
#             player_pointer = item
#             print(highest_pitching)
#         else:
#             print(no_position[item] + "NO")
#             continue
#     no_position.remove(player_pointer)
#     return highest_pitching



# def enemyPositionPicker(no_position):
#     # Pitching first
#     no_position.sort(key=lambda x: x.pitching, reverse=True)
#     print(f"Pitcher chosen is:")
#     print(no_position[0])
#     # Catching Second

def enemyPositionPicker(no_position):
    # My chosen importance = Pitcher, Catcher, SS, 1st, 2nd, 3rd, LF, CF, RF
    skill_list = ["pitching", "catching", "catching", "catching", "throwing", "throwing", "running", "running", "running"]
    position_list = ["Pitching", "Catcher", "Short Stop", "1st Baseman", "2nd Baseman", "3rd Baseman", "Left Field", "Center Field", "Right Field"]
    for i in range(9):
        item = skill_list[i]
        position = position_list[i]
        # print(item)
        no_position.sort(key=operator.attrgetter(item), reverse=True)
        # print(no_position[0])
        no_position[0].position = position
        # print(no_position[0])
        enemyTeamRoster.append(no_position[0])
        no_position.remove(no_position[0])
        # for j in no_position:
        #     print(j.fname)

    # Swapping the short stop to the 4th index cause I like it that way more    
    enemyTeamRoster[2], enemyTeamRoster[3] = enemyTeamRoster[3], enemyTeamRoster[2]
    enemyTeamRoster[3], enemyTeamRoster[4] = enemyTeamRoster[4], enemyTeamRoster[3]
    return enemyTeamRoster
        

def createEnemyTeam():
    no_position = enemyTeamGeneration()
    enemyTeamRoster = enemyPositionPicker(no_position)
    return enemyTeamRoster



if __name__ == "__main__":
    # Creating a player
    #playerHireProcess()
    #savePlayersToFile(users_team)
    #loadPlayersFromFile()
    no_position = enemyTeamGeneration()
    enemyTeamRoster = enemyPositionPicker(no_position)
    for i in range(9):
        print(enemyTeamRoster[i])
    # highest_pitching = highest_pitching(no_position)