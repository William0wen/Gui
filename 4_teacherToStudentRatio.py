import easygui
import math

loop = ""

while loop != "No":
    school = easygui.enterbox("Enter the name of the school").title()
    class_size = easygui.integerbox("What is the maximum number of children allowed per class;"
                                    "\n(Must be a number between 10 and 30)", upperbound=30, lowerbound=10)
    tot_children = easygui.integerbox(f"What is the total number of children at {school}"
                                      "\n(Must be a number between 10 and 1400)", upperbound=1400, lowerbound=10)
    teachers = easygui.integerbox(f"How many teachers are at {school}?"
                                  f"\n(Must be a number between 1 and 120)", lowerbound=1, upperbound=120)

    classes_needed = math.ceil(tot_children / class_size)

    if teachers == classes_needed:
        easygui.msgbox("You have just the right amount of teachers for the classes.")
    elif teachers < classes_needed:
        easygui.msgbox("You don't have enough teachers"
                       f"\nYou could do with {classes_needed -teachers} more teachers")
    elif teachers > classes_needed:
        easygui.msgbox("You have too many teachers"
                       f"\nYou could do with {teachers - classes_needed} less teachers")

    loop = easygui.buttonbox("Do you want to do another calculation", choices=["Yes", "No"])

easygui.msgbox("Goodbye")

