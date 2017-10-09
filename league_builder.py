import csv
import random

# read file
def read_player():
    with open('soccer_players.csv', 'r') as csvfile:
        p_reader = csv.DictReader(csvfile, delimiter=',')
        players = list(p_reader)
        return players
        #print(players)

players_roster = read_player()
#print(players_roster)

def sort_by_exp(players_roster):
    # sort by experience
    exp_yes_roster = []
    exp_no_roster = []
    for player in players_roster:
        if player['Soccer Experience'] == 'YES':
            exp_yes_roster.append(player)
        if player['Soccer Experience'] == 'NO':
            exp_no_roster.append(player)
    return exp_yes_roster, exp_no_roster
    #print(exp_yes_roster)
    #print(exp_no_roster)
experienced_roster, inexperienced_roster = sort_by_exp(players_roster)
# pick teams by experience
def team_roster(experienced_roster, inexperienced_roster):
    # split team randomally
    experienced_roster, inexperienced_roster = sort_by_exp(players_roster)
    while True:
        roster_pick = random.choice(experienced_roster)
        if roster_pick not in Raptors:
            Raptors.append(roster_pick)
            if len(Raptors) == 3:
                break
    while True:
        roster_pick = random.choice(experienced_roster)
        if (roster_pick not in Dragons) and (roster_pick not in Raptors):
            Dragons.append(roster_pick)
            if len(Dragons) == 3:
                break
    while True:
        roster_pick = random.choice(experienced_roster)
        if (roster_pick not in Sharks) and (roster_pick not in Dragons) and (roster_pick not in Raptors):
            Sharks.append(roster_pick)
            if len(Sharks) == 3:
                break
    while True:
        roster_pick = random.choice(inexperienced_roster)
        if roster_pick not in Raptors:
            Raptors.append(roster_pick)
            if len(Raptors) == 6:
                break
    while True:
        roster_pick = random.choice(inexperienced_roster)
        if (roster_pick not in Dragons) and (roster_pick not in Raptors):
            Dragons.append(roster_pick)
            if len(Dragons) == 6:
                break
    while True:
        roster_pick = random.choice(inexperienced_roster)
        if (roster_pick not in Sharks) and (roster_pick not in Dragons) and (roster_pick not in Raptors):
            Sharks.append(roster_pick)
            if len(Sharks) == 6:
                break

    #print(Raptors)
    #print(Dragons)
    #print(Sharks)
    return Raptors, Dragons, Sharks

def write_rosters():
    # write team rosters
    with open('teams.txt', 'a') as file:
        file.write("Raptors\n")
        for player in Raptors:
            roster = player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'] + '\n'
            file.write(roster)
        file.write("Dragons\n")
        for player in Dragons:
            roster = player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'] + '\n'
            file.write(roster)
        file.write("Sharks\n")
        for player in Sharks:
            roster = player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'] + '\n'
            file.write(roster)

def write_letters():
    # write welcome letter to players Guardians
    for player in Raptors:
        filename = player['Name'].replace(' ', '_').lower() + '.txt'
        with open(filename, 'w') as file:
            letter = "Dear " + player['Guardian Name(s)'] + ',' + '\n\n' + "Your child " + player['Name'] + " has made team Raptors. " + '\n' + "The first practice is on Oct 13th 2017 at 5pm. \n\n" + "Sincerely, \n" + "Team Coordinator"
            file.write(letter)

    for player in Dragons:
        filename = player['Name'].replace(' ', '_').lower() + '.txt'
        with open(filename, 'w') as file:
            letter = "Dear " + player['Guardian Name(s)'] + ',' + '\n\n' + "Your child " + player['Name'] + " has made team Dragons. " + '\n' + "The first practice is on Oct 13th 2017 at 5pm. \n\n" + "Sincerely, \n" + "Team Coordinator"
            file.write(letter)

    for player in Sharks:
        filename = player['Name'].replace(' ', '_').lower() + '.txt'
        with open(filename, 'w') as file:
            letter = "Dear " + player['Guardian Name(s)'] + ',' + '\n\n' + "Your child " + player['Name'] + " has made team Sharks. " + '\n' + "The first practice is on Oct 13th 2017 at 5pm. \n\n" + "Sincerely, \n" + "Team Coordinator"
            file.write(letter)




if __name__ == "__main__":

    Raptors = []
    Dragons = []
    Sharks = []

    read_player()
    team_roster(experienced_roster, inexperienced_roster)
    sort_by_exp(players_roster)
    write_rosters()
    write_letters()
