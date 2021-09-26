import random

RockPaperScissors = {1: "rock",
                   2: "paper",
                   3: "scissors"}
none = "tie"
def findWinner(player1, player2):
    if player1 == "rock":
        if player2 == "paper":
            winner = player2
        elif player2 == "scissors":
            winner = player1
        else:
            winner = none
    elif player1 == "paper":
        if player2 == "rock":
            winner = player1
        elif player2 == "scissors":
            winner = player2
        else:
            winner = none
    else:
        if player2 == "paper":
            winner = player1
        elif player2 == "rock":
            winner = player2
        else:
            winner = none
    return winner

def oneplayergame():
    botChoice = random.randrange(1, 3)
    player1choice = input("please choose rock, paper, or scissors : ")
    findWinner(player1choice, botChoice)
    return


def twoplayergame():
    player2 = input("player2 please enter your name : ")
    print("Hello " + player1 + " and " + player2)
    player1choice = input(player1 + "'s turn. please choose rock, paper, or scissors : ")
    player2choice = input(player2 + "'s turn. please choose rock, paper, or scissors : ")
    findWinner(player1choice, player2choice)
    return

NumOfPlayer = int(input("Would you like to play with 1 or 2 players? : "))

player1 = input("player1 please enter your name : ")
if NumOfPlayer == 2:
    twoplayergame()
    print(winner)
elif NumOfPlayer == 1:
    oneplayergame()
    print(winner)
else:
    print("nice try guy")



