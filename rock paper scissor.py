import random
choices=['rock','paper','scissors','stone']

computer=random.choice(choices)

player=input("rock,paper, or scissors :")

if player == computer:
    print("computer :",computer)
    print("player :",player)
    print("Tie!")
elif player == "rock":
    if computer =="paper":
        print("computer :", computer)
        print("player :", player)
        print("You lose!")
    if computer == "scissors":
        print("computer :", computer)
        print("player :", player)
        print("You Win!")

elif player =="scissors":
    if computer =="rock":
        print("computer :", computer)
        print("player :", player)
        print("You lose!")
    if computer =="paper":
        print("computer :", computer)
        print("player :", player)
        print("You Win!")
elif player =="paper":
    if computer =="scissors":
        print("computer :", computer)
        print("player :", player)
        print("You lose!")
    if computer =="rock":
        print("computer :", computer)
        print("player :", player)
        print("You Win!")





