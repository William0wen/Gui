import easygui
import random

card_numbers = ["Two", "Third", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
card_suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
replay = ""


# Main
while replay != "No":
    easygui.msgbox("Are you ready to select a random card from the deck?", "", "Yes")

    player_suit = random.choice(card_suits)
    player_number = random.choice(card_numbers)
    ai_suit = random.choice(card_suits)
    ai_number = random.choice(card_numbers)

    easygui.msgbox(f"You drew the {player_number} of {player_suit}")

    # Scoring
    if card_numbers.index(player_number) > card_numbers.index(ai_number):
        easygui.msgbox(f"Player wins with {player_number} of {player_suit} against"
                       f"\nthe computer's {ai_number} of {ai_suit}", "Player wins")
    elif card_numbers.index(player_number) < card_numbers.index(ai_number):
        easygui.msgbox(f"Computer wins with {ai_number} of {ai_suit} against"
                       f"\nthe Player's {player_number} of {player_suit}", "Computer wins")
    else:
        easygui.msgbox(f"A draw with {player_number} of {player_suit} against"
                       f"\n{ai_number} of {ai_suit}", "Draw")

    replay = easygui.buttonbox("Do you want to replay?", choices=["Yes", "No"])

easygui.msgbox("Ok, bye")
