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

# Creates a single player and adds him to a team
def player_creation():
    fname = available_fnames[random.randint(0, len(available_fnames))]
    lname = available_lnames[random.randint(0, len(available_lnames))]
    batting = random.randint(MIN_STAT, MAX_STAT)
    pitching = random.randint(MIN_STAT, MAX_STAT)
    running = random.randint(MIN_STAT, MAX_STAT)
    catching = random.randint(MIN_STAT, MAX_STAT)
    throwing = random.randint(MIN_STAT, MAX_STAT)
    position = Player.position

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
    position1_choice = int(input("--> "))
    # ngl i feel so smart doing this shit
    createdPlayer.position = tempdict.get(position1_choice)
    # Actually need to be able ot cathc this error if its not in the list :(   
    available_positions.remove(position1_choice)
    print(available_positions)
    print(createdPlayer)

    return createdPlayer


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
    while(i < 9):
        createdPlayer = player_creation()
        print(createdPlayer)
        print("Would you like to hire this player?")
        hire_question_response = input("--> ")
        if hire_question_response == "y":
            i += 1
            # If the player wants to hire the player
            positionPicker(createdPlayer, available_positions, tempdict)




if __name__ == "__main__":
    # Creating a player
    playerHireProcess()
    #print(available_positions)
    #print("Pick a position from the list")
    #position1 = input("--> ")