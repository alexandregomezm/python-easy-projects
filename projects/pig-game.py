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
        print(f"\nScoreboard: {players_score}")
        print(f"Player {player_index + 1} turn!")

        while True:
            player_decision = input("\nDo you wanna roll the dice? (y/n): ")

            if player_decision.lower() == "n":
                break
            elif player_decision.lower() == "y":
                value = roll()
                if value == 1:
                    print("\nYou rolled a 1! Good luck next round!")
                    players_score[player_index] = players_score[player_index]
                    break
                else:
                    players_score[player_index] += value
                    print(f"\nYou rolled a {value}")
                    print(f"Player {player_index + 1} score now is equal to {players_score[player_index]}")

                    if players_score[player_index] >= 50:
                        break
            else:
                print("Invalid, try again")

    if max(players_score) >= 50:
        print(f"\nPlayer {players_score.index(max(players_score)) + 1} is the winner with a score of {players_score[player_index]}!\n")
        break