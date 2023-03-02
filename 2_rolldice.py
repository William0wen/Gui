import easygui
import random

easygui.msgbox("Are you ready to roll the dice?", "", "Yes")

for player in range(1, 3):
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)
    easygui.msgbox(f"Player {player}'s rolls were"
                   f"\n{roll_one} and {roll_two}"
                   f"\nTotal: {roll_one + roll_two}", f"Player {player}")
