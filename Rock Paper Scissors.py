import random

def play(player, opponent):
    if (
        (player == "P" and opponent == "R")
        or (player == "S" and opponent == "P")
        or (player == "R" and opponent == "S")
    ):
        return True

def rockpaperscissors():
    print("Let's play Rock Paper Scissors")
    Game = ["R", "P", "S"]

    continuegame = None

    while continuegame != "N":

        player = input(
            "Choose your option (R for Rock, P for Paper, S for Scissors): "
        ).upper()
        
        while player not in ["P", "S", "R"]:
            print("Invalid Input!")
            player = input(
                "Choose your option (R for Rock, P for Paper, S for Scissors): "
            ).upper()

        computer = random.choice(Game)
        print("Computer: ", computer)

        if player == computer:
            print("It's a tie")
        elif play(player, computer):
            print("You won!")
        else:
            print("Haha you lose sucker!")

        continuegame = input(
            "Do you wish to continue ('Y' for Yes and 'N' for No): "
        ).upper()

rockpaperscissors()
