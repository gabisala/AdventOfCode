"""
--- Day 2: Rock Paper Scissors ---
The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, 
a giant Rock Paper Scissors tournament is already in progress. Rock Paper Scissors is a game between two players. 
Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. 
Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. 
If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. 
"The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. 
The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y 
for Paper, and Z for Scissors. 
Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. 
Your total score is the sum of your scores for each round. The score for a single round 
is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, 
and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate 
the score you would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?
"""

# Process input data
with open('AdventOfCode/Day_2/input.txt', 'r') as file:
    lines = file.readlines()

games = [line.strip().split() for line in lines]

# First puzzle
# Define rules
value = {"Rock": 1, "Paper": 2, "Scissors": 3}

hand_sign = {"A": "Rock", "X": "Rock", 
           "B": "Paper", "Y": "Paper", 
           "C": "Scissors", "Z": "Scissors"}

opponent_score = 0
my_score = 0

    
for game in games:
    opponent_play = game[0]
    my_play = game[1]
    opponent_hand_sign = hand_sign[opponent_play]
    my_hand_sign = hand_sign[my_play]
    
    print(f'Oponent: {opponent_hand_sign} - Me: {my_hand_sign}')

    if my_hand_sign == opponent_hand_sign:
        print('Draw')
        my_score += (3 + value[my_hand_sign])
        opponent_score += (3 + value[opponent_hand_sign])
    
    elif my_hand_sign == "Rock" and opponent_hand_sign == "Scissors" or opponent_hand_sign == "Scissors" and my_hand_sign == "Rock":
        print('I win')
        my_score += (6 + value[my_hand_sign])
        opponent_score += (0 + value[opponent_hand_sign])
        
    elif my_hand_sign == "Scissors" and opponent_hand_sign == "Paper" or opponent_hand_sign == "Paper" and my_hand_sign == "Scissors":
        print('I win')
        my_score += (6 + value[my_hand_sign])
        opponent_score += (0 + value[opponent_hand_sign])
    
    elif my_hand_sign == "Paper" and opponent_hand_sign == "Rock" or opponent_hand_sign == "Rock" and my_hand_sign == "Paper":
        print('I win')
        my_score += (6 + value[my_hand_sign])
        opponent_score += (0 + value[opponent_hand_sign])
        
    else:
        my_score += (0 + value[my_hand_sign])
        opponent_score += (6 + value[opponent_hand_sign])
        
        
print(f'My score: {my_score}, Opponent score: {opponent_score}')


# Second puzzle
# Define rules
value = {"Rock": 1, "Paper": 2, "Scissors": 3}
hand_sign = {"A": "Rock", "B": "Paper", "C": "Scissors", "Z": "Scissors"}
strategy = {"X": "Lose", "Y": "Draw", "Z": "Win"}

opponent_score = 0
my_score = 0

    
for game in games:
    opponent_play = game[0]
    my_strategy= strategy[game[1]]
    opponent_hand_sign = hand_sign[opponent_play]
    
    if my_strategy == "Draw":
        my_hand_sign = opponent_hand_sign
        
    elif my_strategy == "Win":
        if opponent_hand_sign == "Rock":
            my_hand_sign = "Paper"
        elif opponent_hand_sign == "Paper":
            my_hand_sign = "Scissors"
        elif opponent_hand_sign == "Scissors":
            my_hand_sign = "Rock"
            
    elif my_strategy == "Lose":
        if opponent_hand_sign == "Rock":
            my_hand_sign = "Scissors"
        elif opponent_hand_sign == "Paper":
            my_hand_sign = "Rock"
        elif opponent_hand_sign == "Scissors":
            my_hand_sign = "Paper"
    
    print(f'Oponent: {opponent_hand_sign} - Me: {my_hand_sign}')

    if my_hand_sign == opponent_hand_sign:
        print('Draw')
        my_score += (3 + value[my_hand_sign])
        opponent_score += (3 + value[opponent_hand_sign])
    
    elif my_hand_sign == "Rock" and opponent_hand_sign == "Scissors" or opponent_hand_sign == "Scissors" and my_hand_sign == "Rock":
        print('I win')
        my_score += (6 + value[my_hand_sign])
        opponent_score += (0 + value[opponent_hand_sign])
        
    elif my_hand_sign == "Scissors" and opponent_hand_sign == "Paper" or opponent_hand_sign == "Paper" and my_hand_sign == "Scissors":
        print('I win')
        my_score += (6 + value[my_hand_sign])
        opponent_score += (0 + value[opponent_hand_sign])
    
    elif my_hand_sign == "Paper" and opponent_hand_sign == "Rock" or opponent_hand_sign == "Rock" and my_hand_sign == "Paper":
        print('I win')
        my_score += (6 + value[my_hand_sign])
        opponent_score += (0 + value[opponent_hand_sign])
        
    else:
        my_score += (0 + value[my_hand_sign])
        opponent_score += (6 + value[opponent_hand_sign])
        
        
print(f'My score: {my_score}, Opponent score: {opponent_score}')

