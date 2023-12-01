import random

print("\n")

name = input("Enter your name: ")

while True:
    choices = ["rock", "paper", "scissors"]
    player = None
    computer = random.choice(choices)
    COMP = "computer: "
    PLAYER = "player: "
    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()
    print("\n")

    if player == computer:
        print(COMP, computer)
        print(PLAYER, player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print(COMP, computer)
            print(PLAYER, player)
            print(name + ", you lose...")
        if computer == "scissors":
            print(COMP, computer)
            print(PLAYER, player)
            print(name + ", you win!")
    elif player == "scissors":
        if computer == "rock":
            print(COMP, computer)
            print(PLAYER, player)
            print(name + ", you lose...")
        if computer == "paper":
            print(COMP, computer)
            print(PLAYER, player)
            print(name + ", you win!")
    elif player == "paper":
        if computer == "scissors":
            print(COMP, computer)
            print(PLAYER, player)
            print(name + ", you lose...")
        if computer == "rock":
            print(COMP, computer)
            print(PLAYER, player)
            print(name + ", you win!")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Bye!")