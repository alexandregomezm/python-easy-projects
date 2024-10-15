# hello! in this project, i saw one of tech with tim videos about easy projects in python and i'll try to replicate the pig game! lets go!
# so, first of all, this is a game played by at least 2 players and we're gonna limit it to 5 players.
# basically, in each one round, the player will choose to roll a dice, and if it equals to one, your score is reset to the initial value at the beginning of the round and you pass.
# the goal is to get more than a target value, such as 50 by example.

import random

def roll():
    roll = random.randint(1,6)
    return roll

while True: #loop to get a valid number of players
    number_players = input("Please, type the number of players: (2-5): ")

    if number_players.isdigit():
        number_players = int(number_players)

        if 2 <= number_players <= 5:
            print(f"Number of players: {number_players}")
            break
        else:
            print("It must be between 2 and 5 players")
    else:
        print("invalid, try again")

players_score = [0 for _ in range(number_players)]

while True: #loop with game logic, it'll be true while no one gets 50 or more points.
    
    for player_index in range(len(players_score)):
        player_decision = input("Do you wanna roll the dice? (y/n): ")

        if player_decision.lower() == "n":
            break
        else:
            value = roll()
            if value == 1:
                print("You rolled a 1! Good luck next round!")
                players_score[player_index] = players_score[player_index] + 0
                break
            else:
                players_score[player_index] += value
                print(f"You rolled a {value}")
                print(f"Player {player_index} score is equal to {players_score[player_index]}")

    if max(players_score) >= 50:
        print(f"Player is the winner!")
        break

# i got stuck at this part! idk why when player 1 rolls the dice, he gets the points and then its players 2 round, its not supposed to do that!