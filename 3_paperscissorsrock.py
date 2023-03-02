import easygui
import random

weapons = ["paper", "scissors", "rock"]
player_points = 0
ai_points = 0
draws = 0

choice = easygui.buttonbox("Welcome to rock-paper-scissors"
                           "\nDo you want to play?", "WELCOME", choices=["Yes", "No"])

if choice == "Yes":
    for round_ in range(1, 6):
        player_choice = easygui.buttonbox("Choose your weapon", f"Round {round_}/5", choices=["Paper", "scissors", "rock"]).lower()
        ai_choice = random.choice(weapons)

        if player_choice == ai_choice:
            draws += 1
            easygui.msgbox(f"Player chose {player_choice} and computer chose {ai_choice}"
                           f"\nDRAW", f"Round {round_}/5")

        elif player_choice == "rock" and ai_choice == "paper":
            ai_points += 1
            easygui.msgbox(f"Player chose {player_choice} and computer chose {ai_choice}"
                           f"\nCOMPUTER WINS", f"Round {round_}/5")
        elif player_choice == "paper" and ai_choice == "scissors":
            ai_points += 1
            easygui.msgbox(f"Player chose {player_choice} and computer chose {ai_choice}"
                           f"\nCOMPUTER WINS", f"Round {round_}/5")
        elif player_choice == "scissors" and ai_choice == "rock":
            ai_points += 1
            easygui.msgbox(f"Player chose {player_choice} and computer chose {ai_choice}"
                           f"\nCOMPUTER WINS", f"Round {round_}/5")
        else:
            player_points += 1
            easygui.msgbox(f"Player chose {player_choice} and computer chose {ai_choice}"
                           f"\nPLAYER WINS", f"Round {round_}/5")

    easygui.msgbox(f"Draws: {draws}"
                   f"\nPlayer wins: {player_points}"
                   f"\nComputer wins: {ai_points}", "Results")

else:
    easygui.msgbox("Why did you start the program then?????", "bruh", "I don't know")


