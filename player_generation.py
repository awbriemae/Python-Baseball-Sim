# File to generate players

import random
from class_definitions import Player

MIN_STAT = 20
MAX_STAT = 100

available_fnames = []
available_lnames = []

first_name_file = "firstnames.txt"
fnames = open(first_name_file, "r")
for line in fnames:
    line = line.rstrip()
    available_fnames.append(line)
fnames.close

last_name_file = "lastnames.txt"
lnames = open(last_name_file, "r")
for line in lnames:
    line = line.rstrip()
    available_lnames.append(line)
lnames.close

team1 = []

test_team = []

available_positions = ["p","c","1b","2b","ss","3b","lf","cf","rf"]

# 1 - Pitcher (P)
# 2 - Catcher (C)
# 3 - 1st Baseman (1B)
# 4 - 2nd Baseman (2B)
# 5 - Shortstop (SS)
# 6 - 3rd Baseman (3B)
# 7 - Left Field (LF)
# 8 - Center Field (CF)
# 9 - Right Field (RF)

# Loop through available players aznd overwrite their position with the new position

# Randomises the values for a single player

def player_randomiser():
    fname = available_fnames[random.randint(0, len(available_fnames))]
    lname = available_lnames[random.randint(0, len(available_lnames))]
    batting = random.randint(MIN_STAT, MAX_STAT)
    pitching = random.randint(MIN_STAT, MAX_STAT)
    running = random.randint(MIN_STAT, MAX_STAT)
    catching = random.randint(MIN_STAT, MAX_STAT)
    throwing = random.randint(MIN_STAT, MAX_STAT)
    position = Player.position

    return fname, lname, batting, pitching, running, catching, throwing, position

# Creates the player using the class and the inputted variables created above ^
# Changed this for multifunctionality

def player_creation(fname, lname, batting, pitching, running, catching, throwing, position):
    return Player(fname=fname, 
                        lname=lname, 
                        batting=batting, 
                        pitching=pitching, 
                        running=running, 
                        catching=catching, 
                        throwing=throwing,
                        position=position)

    #team.append(Player(fname=fname, 
    #                    lname=lname, 
    #                    batting=batting, 
    #                    pitching=pitching, 
    #                    running=running, 
    #                    catching=catching, 
    #                    throwing=throwing,
    #                    position="bench"))

#highest_pitching = 0

#highest_catching = 0

#highest_throwing = 0

#def position_picker(team):
#    # Pitcher Assignment
#    for item in range(len(team)):
#        if item.pitching() > highest_pitching:
#            highest_pitching = item
#            print(highest_pitching)
#        else:
#            continue

# WHY DID I PUT ALL OF THIS HERE IT SHOULD BE IN TEAM_CREATION.PY
# I look down upon myself.

def savePlayersToFile(users_team):
    f = open("UserPlayerTeam.txt", "w")
    for i in range(len(users_team)):
        f.write(f"{users_team[i].fname},{users_team[i].lname},{users_team[i].batting},{users_team[i].pitching},{users_team[i].running},{users_team[i].catching},{users_team[i].throwing},{users_team[i].position}\n")
    f.close()

# what am i thinking
player_temp_stats1 = []
player_temp_stats2 = []
player_temp_stats3 = []
player_temp_stats4 = []
player_temp_stats5 = []
player_temp_stats6 = []
player_temp_stats7 = []
player_temp_stats8 = []
player_temp_stats9 = []

player_temp_stats_fulllist = []

def loadPlayersFromFile():
    f = open("UserPlayerTeam.txt", "r")
    x = 0
    for i in f:
        playerSplit = i.strip()
        playerSplit = playerSplit.split(",")
        for i in playerSplit:  
            x += 1
            print(x)
            if 1 <= x <= 8:
                player_temp_stats1.append(i)
            elif 9 <= x <= 16:
                player_temp_stats2.append(i)
            elif 17 <= x <= 24:
                player_temp_stats3.append(i)
            elif 25 <= x <= 32:
                player_temp_stats4.append(i)
            elif 33 <= x <= 40:
                player_temp_stats5.append(i)
            elif 41 <= x <= 48:
                player_temp_stats6.append(i)
            elif 49 <= x <= 56:
                player_temp_stats7.append(i)
            elif 57 <= x <= 64:
                player_temp_stats8.append(i)
            else:
                player_temp_stats9.append(i)
            #else:
                #player_temp_stats3.append(i)
    #print(player_temp_stats1)
    #print(player_temp_stats2)
    #print(player_temp_stats3)
    player_temp_stats_fulllist.append(player_temp_stats1)
    player_temp_stats_fulllist.append(player_temp_stats2)
    player_temp_stats_fulllist.append(player_temp_stats3)
    player_temp_stats_fulllist.append(player_temp_stats4)
    player_temp_stats_fulllist.append(player_temp_stats5)
    player_temp_stats_fulllist.append(player_temp_stats6)
    player_temp_stats_fulllist.append(player_temp_stats7)
    player_temp_stats_fulllist.append(player_temp_stats8)
    player_temp_stats_fulllist.append(player_temp_stats9)
    # I've had to repeat "It's not stupid if it works" so many times...
    y = 0
    for y in range(team_amount):
        createdPlayer = player_creation(player_temp_stats_fulllist[y][0], player_temp_stats_fulllist[y][1], player_temp_stats_fulllist[y][2], player_temp_stats_fulllist[y][3], player_temp_stats_fulllist[y][4], player_temp_stats_fulllist[y][5], player_temp_stats_fulllist[y][6], player_temp_stats_fulllist[y][7])
        test_team.append(createdPlayer)
        print(createdPlayer)





team_name = "The Sligo Sharters"

users_team = []

# This takes in the player that was created and the array + dict
# When the user picks a number it assigns the position to the player and returns the player with the new position.
def positionPicker(createdPlayer, available_positions, tempdict):
    print("What position do you want them to play? ( type the number corresponding to the position thx )")
    for item in available_positions:
        if item in tempdict:
            print(tempdict.get(item))
        else:
            continue

    # Getting user input with validation    
    while True:
        #position1_choice = int(input("--> "))
        try:
            position1_choice = int(input("--> "))
            createdPlayer.position = tempdict.get(position1_choice)
        except ValueError:
            print("Use a number")
            continue
        try: 
            available_positions.remove(position1_choice)
        except ValueError:
            print("Pick an available position")
            continue
        if 1 <= position1_choice <= 9:
            break


    # ngl i feel so smart doing this shit
    #createdPlayer.position = tempdict.get(position1_choice)
    # Actually need to be able ot cathc this error if its not in the list :(
    #while True:
        #if position1_choice in available_positions:
            #available_positions.remove(position1_choice)
            #continue
        #else:
            #print("Pick a position that is still available")
    #except ValueError:
    
    # Adding the player to the team array
    users_team.append(createdPlayer)
    #print(available_positions)
    #print(createdPlayer)
    print(f"{createdPlayer.fname} {createdPlayer.lname} added to {team_name} as a {createdPlayer.position}")
    for i in range(len(users_team)):
        print("-" * 25)
        print(users_team[i])
        print("-" * 25)

    return createdPlayer


#def team_creation(createdPlayer):

    #users_team.append(createdPlayer)

    # Pick the players position on the team
    #position1_choice = int(input("--> "))
    # This causes duplication so i need to change it into a list that gets shorter ( code would also be shorter lol )
    # or a dictionary could work ( never used it so i just kinda wanna learn it lol )
    #match position1_choice:
    #    case 1:
    #        createdPlayer.position = "Pitcher"
    #        print(createdPlayer)
    #    case 2:
    #        createdPlayer.position = "Catcher"
    #        print(createdPlayer)
    #    case 3:
    #        createdPlayer.position = "1st Baseman"
    #        print(createdPlayer)
    #    case 4:
    #        createdPlayer.position = "2nd Baseman"
    #        print(createdPlayer)
    #    case 5:
    #        createdPlayer.position = "Short Stop"
    #        print(createdPlayer)
    #    case 6:
    #        createdPlayer.position = "3rd Baseman"
    #        print(createdPlayer)
    #    case 7:
    #        createdPlayer.position = "Left Field"
    #        print(createdPlayer)
    #    case 8:
    #        createdPlayer.position = "Center Field"
    #        print(createdPlayer)
    #    case 9:
    #        createdPlayer.position = "Right Field"
    #        print(createdPlayer)
    #    case _:
    #        createdPlayer.position = "bench"
    #        print(createdPlayer)

team_amount = 9

# This creates an array with available position using the dictionary.
# Runs the command player creation to create a player 9 times.
# Asks the user if they wanna hire them.
# Then runs positionPicker().
def playerHireProcess():
    available_positions = []
    tempdict = {
        1: "Pitcher",
        2: "Catcher",
        3: "1st Baseman",
        4: "2nd Baseman",
        5: "Short Stop",
        6: "3rd Baseman",
        7: "Left Field",
        8: "Center Field",
        9: "Right Field",
    }
    # I need a way to be able to remove both from the list and the temp dict but not loose the tempdict permanently
    for i in tempdict:
        available_positions.append(i)
        print(i)
        print(available_positions)
    i = 0
    while(i < team_amount):
        fname, lname, batting, pitching, running, catching, throwing, position = player_randomiser()
        createdPlayer = player_creation(fname, lname, batting, pitching, running, catching, throwing, position)
        print(createdPlayer)
        print("Would you like to hire this player?")
        hire_question_response = input("--> ")
        if hire_question_response == "y":
            i += 1
            # If the player wants to hire the player
            positionPicker(createdPlayer, available_positions, tempdict)
        else:
            continue



def createRandomPlayersForEnemyTeam():
    enemyTeam = []
    for i in range(0, 9):
        fname, lname, batting, pitching, running, catching, throwing, position = player_randomiser()
        createdPlayer = player_creation(fname, lname, batting, pitching, running, catching, throwing, position)
        enemyTeam.append(createdPlayer)
        print(createdPlayer)
    print(enemyTeam)
    return enemyTeam

if __name__ == "__main__":
    # Creating a player
    #playerHireProcess()
    #savePlayersToFile(users_team)
    #loadPlayersFromFile()
    createRandomPlayersForEnemyTeam()