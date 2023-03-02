import easygui
import random

name = easygui.enterbox("What is your name").title()
age = easygui.integerbox("What is your age")
choice = easygui.buttonbox("Do you want to be a communist?", "Question 1", choices=["Yes", "Probably", "Maybe", "Not sure", "No", "What?"])

if choice == "Yes" or choice == "Probably":
    easygui.enterbox("Why are you for communism?", "Question 2")
    easygui.msgbox(f"Thank you, comrade {name}")
elif choice == "No":
    easygui.enterbox("Why are you against communism?", "Question 2")
    easygui.msgbox(f"Thank you, traitor")
else:
    easygui.msgbox(f"Thank you, {name}")


print("### DATA ###")
print(f"Name: {name.title()}")
print(f"Age: {age}")
print(f"Wants to be communist: {choice}")

guess = 0
guesses = 0
number = random.randint(0, 10)

while guess != number:
    guess = easygui.integerbox("Guess the number between 1 and 10", "Number guesser")
    guesses += 1

easygui.msgbox(f"You guessed correctly in {guesses} guesses!", "Good job")
