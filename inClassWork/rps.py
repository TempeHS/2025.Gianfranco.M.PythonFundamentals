import random

gamesPlayed = 0
gamesWon = 0

while gamesPlayed < 3:
    playerChoice = input("CHOSE YOUR CHARACTER ")

    mylist = ["rock", "paper", "scissors"]
    rand = random.choice(mylist)

    gamesPlayed += 1

    match playerChoice:
        case "rock":
            if rand == "rock":
                print("DRAW")
            if rand == "paper":
                print("YOU LOSE")
            if rand == "scissors":
                print("YOU WIN !")
                gamesWon += 1

        case "paper":
            if rand == "rock":
                print("you win")
                gamesWon += 1
            if rand == "paper":
                print("draw")
            if rand == "scissors":
                print("you lose")

        case "scissors":
            if rand == "rock":
                print("you lose")
            if rand == "paper":
                print("winner !!")
                gamesWon += 1
            if rand == "scissors":
                print("draw")

print(f"gamesWon)
