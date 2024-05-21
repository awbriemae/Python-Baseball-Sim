# File to create the teams also randomised :3

# FOR FUTURE: Have a way of organising the players in stats of best to worst so for example the pitcher is designated as whoever has the best pitching ig

import random

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

    Team2_name = available_teamnames[random.randint(0, number_of_teams)]

    print(Team1_name)
    print(Team2_name)



create_team()