import random

choices = {
    1: "rock",
    2: "paper",
    3: "scissors"
}

def findwinner(player1, player2):
    print("Player1: " + player1)
    print("Player2: " + player2)
    if player1 == "rock":
        if player2 == "paper":
            winner = player2
        elif player2 == "scissors":
            winner = player1
        elif player2 == "rock":
            winner = 0
    elif player1 == "paper":
        if player2 == "rock":
            winner = player1
        elif player2 == "paper":
            winner = 0
        elif player2 == "scissors":
            winner = player2
    elif player1 == "scissors":
        if player2 == "rock":
            winner = player2
        elif player2 == "paper":
            winner = player1
        elif player2 == "scissors":
            winner = 0
    if winner == player1:
        return "Player 1 wins!"
    elif winner == player2:
        return "Player 2 wins!"
    elif winner == 0:
        return "Tie! You all lose."

def oneplayergame():
    player2 = "bot"
    botchoice = choices[random.randrange(1,3)]
    print(findwinner(player1choice, botchoice))
    return

def twoplayergame():
    player2 = input("please enter player 2's name :")
    print(player1 + " VS " + player2)
    print("Round 1")
    print("FIGHT!!")
    player2choice = input("player 2 choose rock, paper, or scissors : ")
    print(findwinner(player1choice, player2choice))
    return

NumOfPlayers = int(input("Do you want one or two players? : "))
player1 = input("please enter your name : ")

if NumOfPlayers == 1:
    player2 = "bot"
    player1choice = input("player 1 choose rock, paper, or scissors : ")
    oneplayergame()
elif NumOfPlayers == 2:
    player1choice = input("player 1 choose rock, paper, or scissors : ")
    twoplayergame()

