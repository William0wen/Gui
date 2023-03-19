import random
import easygui


def roll_dice():
    return [random.randint(1, 6) for _ in range(5)]


def is_winning_combination(dice_roll):
    if len(set(dice_roll)) == 1:
        return "Yahtzee!"
    elif len(set(dice_roll)) == 2 and dice_roll.count(dice_roll[0]) in [1, 4]:
        return "Four of a kind"
    elif len(set(dice_roll)) <= 3 and dice_roll.count(dice_roll[0]) in [1, 2, 3]:
        return "Three of a kind"
    else:
        return "Better luck next time"


def display_roll(dice_roll):
    dice_roll.sort()
    easygui.msgbox(f"You rolled: {dice_roll}")
    choice = easygui.buttonbox("Roll again or stick?", choices=["Roll", "Stick"])
    return choice


def play_game():
    num_of_turns = 0
    play_again = "Yes"
    while play_again == "Yes":
        num_of_turns += 1
        easygui.msgbox(f"Turn {num_of_turns}")
        dice_roll = roll_dice()
        choice = display_roll(dice_roll)
        num_of_rolls = 1

        while choice == "Roll" and num_of_rolls < 3:
            dice_roll = roll_dice()
            choice = display_roll(dice_roll)
            num_of_rolls += 1

        result = is_winning_combination(dice_roll)
        easygui.msgbox(f"Result: {dice_roll}\n{result}")

        play_again = easygui.buttonbox("Do you want to play again?", choices=["Yes", "No"])

    easygui.msgbox("Goodbye")


play_game()


