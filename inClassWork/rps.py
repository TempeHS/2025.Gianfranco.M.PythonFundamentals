import random

playerChoice = input("CHOSE YOUR CHARACTER ")


mylist = ["rock", "paper", "scissors"]
rand = random.choices(mylist)


rand()

match playerChoice:
    case "rock":
        if rand == "rock":
            print("DRAW")
        if rand == "paper":
            print("YOU LOSE")
        if rand == "scissors":
            print("YOU WIN !")

    case "paper":
        if rand == "rock":
            print("you win")
        if rand == "paper":
            print("draw")
        if rand == "scissors":
            print("you lose")

    case "scissors":
        if rand == "rock":
            print("you lose")
        if rand == "paper":
            print("winner !!")
        if rand == "scissors":
            print("draw")
