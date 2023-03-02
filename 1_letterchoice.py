import easygui
import random

word = easygui.enterbox("What is your word?").upper()
number = easygui.integerbox("How many random letters do you want to get?")

for time in range(1, number + 1):
    rand_letter = random.choice(word)
    easygui.msgbox(f"Your letter is {rand_letter}", f"Random letter {time}")
