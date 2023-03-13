import easygui
import random

card_numbers = ["Two", "Third", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
card_suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
deck = []
draw = []
show_cards = ""

for suit in card_suits:
    for number in card_numbers:
        deck.append([number, suit])

random.shuffle(deck)

for item in range(7):
    draw.append(deck[item])

for card in draw:
    show_cards += f"\n*  Card {draw.index(card)+1}:" \
                  f" {card[0]} of {card[1]}"

easygui.msgbox(f"You have drawn"
               f"\n{show_cards}")
