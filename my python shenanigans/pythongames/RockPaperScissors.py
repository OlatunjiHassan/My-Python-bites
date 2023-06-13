import random
import sys

def pick(play):
    if play == "r":
        return "ROCK"
    elif play == "p":
        return "PAPER"
    elif play == "s":
        return "SCISSORS"
    elif play == "q":
        sys.exit()
def rpsalgo(p1, p2):
    if p1 == 'r':
        if p2 == 'r':
            return "tie"
        if p2 == "p":
            return "loss"
        if p2 == "s":
            return "win"
    if p1 == "s":
        if p2 == "s":
            return "tie"
        if p2 == "r":
            return "loss"
        if p2 == "p":
            return "win"
    if p1 == "p":
        if p2 == "p":
            return "tie"
        if p2 == "s":
            return "loss"
        if p2 == "r":
            return "win"
    else:
        return False



print("ROCK, PAPER, SCISSORS")
wins = 0
losses = 0
ties = 0
plays = ["r", "p", "s"]

while True:
    print(f"{wins} Wins, {losses} Losses, {ties} Ties\nEnter your move: (r)ock (p)aper (s)cissors or (q)uit")
    complay = random.choice(plays) 
    move = input()
    if move == "q":
        sys.exit()
    else:
        print(f"{pick(move)} versus....\n")
        print(f"{pick(complay)}")
        result = rpsalgo(move, complay)
        if result == "tie":
            print("It is a tie!\n")
            ties += 1
        if result == "win":
            print("You win!\n")
            wins += 1
        if result == "loss":
            print("You lost!\n")
            losses += 1
        else:
            continue
    
