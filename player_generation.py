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

def player_creation(team):
    fname = available_fnames[random.randint(0, len(available_fnames))]
    lname = available_lnames[random.randint(0, len(available_lnames))]
    batting = random.randint(MIN_STAT, MAX_STAT)
    pitching = random.randint(MIN_STAT, MAX_STAT)
    running = random.randint(MIN_STAT, MAX_STAT)
    catching = random.randint(MIN_STAT, MAX_STAT)
    throwing = random.randint(MIN_STAT, MAX_STAT)


    team.append(Player(fname=fname, 
                        lname=lname, 
                        batting=batting, 
                        pitching=pitching, 
                        running=running, 
                        catching=catching, 
                        throwing=throwing))

if __name__ == "__main__":
    player_creation(team1)
    print(team1[0])
