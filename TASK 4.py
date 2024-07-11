import random
import time

print("*****************************<WELCOME TO ROCK, PAPER, SCISSORS GAME>************************************")
running=True

while True:
    def get_choices():
        user_choice = input("Enter your choice (Rock, Paper, Scissors): ")
        print("*********************************************************************************************")
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)
        choices = {"user": user_choice.lower(), "computer": computer_choice}
        return choices

    def check_win(user, computer):
        print(f"You chose: {user} :: Computer chose: {computer}")
        print("---------------------------------------------------------------------------------------")
        if user == computer:
            time.sleep(2)
            return (
                "\nThe game is a tie!\n"
                "Thanks for playing...\n"
                "##################################################################################"
            )

        elif user == "rock":
            if computer == "scissors":
                time.sleep(2)
                return (
                    "\nRock beats Scissors!! You Win!!\n"
                    "Thanks for playing....\n"
                    "##########################################################################################"
                )
            else:
                time.sleep(2)
                return (
                    "\nPaper beats Rock!! You Lose..\n"
                    "Thanks for playing....\n"
                    "##########################################################################################"
                )

        elif user == "paper":
            if computer == "rock":
                time.sleep(2)
                return (
                    "\nPaper beats Rock!! You Win!!\n"
                    "Thanks for playing....\n"
                    "##########################################################################################"
                )
            else:
                time.sleep(2)
                return (
                    "\nScissors beats Paper!! You Lose...\n"
                    "Thanks for playing....\n"
                    "##########################################################################################"
                )

        elif user == "scissors":
            if computer == "paper":
                time.sleep(2)
                return (
                    "\nScissors beats Paper!! You Win!!\n"
                    "Thanks for playing....\n"
                    "##########################################################################################"
                )
            else:
                time.sleep(2)
                return (
                    "\nRock beats Scissors!! You Lose...\n"
                    "Thanks for playing....\n"
                    "##########################################################################################"
                )
        else:
            return (
                "\nInvalid input! Please choose Rock, Paper, or Scissors.\n"
                "------------------------------------------------------------------------------------------------"
            )

    choices = get_choices()
    result = check_win(choices["user"], choices["computer"])
    print(result)
