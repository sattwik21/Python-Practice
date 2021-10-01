import random

choices = ["Rock","Paper","Scissors"]
player = False
cpu_score = 0
player_score = 0

while True:
    player = input("Rock, Paper or  Scissors?").capitalize()
    computer = random.choice(choices)
    # Conditions of Rock,Paper and Scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!",computer,"covers",player)
            cpu_score+=1
        else:
            print("You win!",player,"smashes",computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose!",computer,"cuts",player)
            cpu_score+=1
        else:
            print("You win!",player,"covers",computer)
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You Lose!",computer,"smashes",player)
            cpu_score+=1
        else:
            print("You win!",player,"cuts",computer)
            player_score+=1
    elif player == "End":
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Plaer:{player_score}")
        break